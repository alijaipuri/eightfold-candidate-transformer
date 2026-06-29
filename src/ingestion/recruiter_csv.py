import csv
from pathlib import Path

from src.core.exceptions import SourceParsingError
from src.core.logger import get_logger
from src.ingestion.base import BaseSourceParser
from src.models.source import SourceMetadata, SourcePayload


logger = get_logger(__name__)


class RecruiterCSVParser(BaseSourceParser):
    """
    Parser for recruiter supplied CSV candidate exports.
    """

    source_name = "recruiter_csv"

    def parse(
        self,
        file_path: str
    ) -> SourcePayload:

        path = Path(file_path)

        if not path.exists():
            raise SourceParsingError(
                f"Recruiter CSV file not found: {file_path}"
            )

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                rows = list(reader)

            logger.info(
                "Parsed recruiter CSV successfully."
            )

            metadata = SourceMetadata(
                source_name=self.source_name,
                file_path=file_path,
                record_count=len(rows)
            )

            return SourcePayload(
                metadata=metadata,
                raw_data=rows
            )

        except Exception as exc:
            raise SourceParsingError(
                f"Failed to parse recruiter CSV: {exc}"
            ) from exc
