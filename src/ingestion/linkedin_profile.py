import json
from pathlib import Path

from src.core.exceptions import SourceParsingError
from src.core.logger import get_logger
from src.ingestion.base import BaseSourceParser
from src.models.source import SourceMetadata, SourcePayload


logger = get_logger(__name__)


class LinkedInProfileParser(BaseSourceParser):
    """
    Parser for LinkedIn profile exports.
    """

    source_name = "linkedin_profile"

    def parse(
        self,
        file_path: str
    ) -> SourcePayload:

        path = Path(file_path)

        if not path.exists():
            raise SourceParsingError(
                f"LinkedIn profile file not found: {file_path}"
            )

        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            metadata = SourceMetadata(
                source_name=self.source_name,
                file_path=file_path,
                record_count=1
            )

            logger.info(
                "LinkedIn profile parsed successfully."
            )

            return SourcePayload(
                metadata=metadata,
                raw_data=data
            )

        except Exception as exc:
            raise SourceParsingError(
                f"Failed to parse LinkedIn profile: {exc}"
            ) from exc
