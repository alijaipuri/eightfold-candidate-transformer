from pathlib import Path

from src.core.exceptions import SourceParsingError
from src.core.logger import get_logger
from src.ingestion.base import BaseSourceParser
from src.models.source import SourceMetadata, SourcePayload


logger = get_logger(__name__)


class ResumeParser(BaseSourceParser):
    """
    Parser for unstructured resume text.
    """

    source_name = "resume"

    def parse(
        self,
        file_path: str
    ) -> SourcePayload:

        path = Path(file_path)

        if not path.exists():
            raise SourceParsingError(
                f"Resume file not found: {file_path}"
            )

        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                text = file.read()

            metadata = SourceMetadata(
                source_name=self.source_name,
                file_path=file_path,
                record_count=1
            )

            logger.info(
                "Resume parsed successfully."
            )

            return SourcePayload(
                metadata=metadata,
                raw_data={
                    "raw_text": text
                }
            )

        except Exception as exc:
            raise SourceParsingError(
                f"Failed to parse resume: {exc}"
            ) from exc
