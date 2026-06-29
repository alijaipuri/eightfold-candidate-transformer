from datetime import datetime
from typing import Dict

from src.core.logger import get_logger
from src.core.pipeline_context import PipelineContext
from src.core.pipeline_result import PipelineResult

from src.ingestion.ats_json import ATSJSONParser
from src.ingestion.github_profile import GitHubProfileParser
from src.ingestion.linkedin_profile import LinkedInProfileParser
from src.ingestion.recruiter_csv import RecruiterCSVParser
from src.ingestion.recruiter_notes import RecruiterNotesParser
from src.ingestion.resume_parser import ResumeParser

from src.merge.canonical_builder import CanonicalCandidateBuilder
from src.merge.provenance_generator import ProvenanceGenerator


logger = get_logger(__name__)


class CandidateTransformationPipeline:
    """
    Main orchestration layer for the candidate transformation system.

    Responsibilities:
        1. Ingest all candidate sources
        2. Parse heterogeneous data formats
        3. Build canonical candidate profile
        4. Generate provenance metadata
        5. Return structured pipeline result
    """

    def __init__(self):

        self.parsers = {
            "recruiter_csv": RecruiterCSVParser(),
            "ats_json": ATSJSONParser(),
            "github_profile": GitHubProfileParser(),
            "linkedin_profile": LinkedInProfileParser(),
            "resume": ResumeParser(),
            "recruiter_notes": RecruiterNotesParser(),
        }

        self.canonical_builder = (
            CanonicalCandidateBuilder()
        )

        self.provenance_generator = (
            ProvenanceGenerator()
        )

    def ingest_sources(
        self,
        context: PipelineContext
    ) -> Dict:
        """
        Parse and ingest all provided candidate sources.
        """

        parsed_sources = {}

        source_mapping = {
            "recruiter_csv": context.recruiter_csv,
            "ats_json": context.ats_json,
            "github_profile": context.github_profile,
            "linkedin_profile": context.linkedin_profile,
            "resume": context.resume_file,
            "recruiter_notes": context.recruiter_notes,
        }

        logger.info(
            "Beginning source ingestion phase."
        )

        for source_name, path in source_mapping.items():

            if path is None:
                logger.warning(
                    f"Skipping missing source: {source_name}"
                )
                continue

            logger.info(
                f"Processing source: {source_name}"
            )

            parser = self.parsers[source_name]

            parsed_payload = parser.parse(
                str(path)
            )

            parsed_sources[source_name] = (
                parsed_payload
            )

            logger.info(
                f"Successfully ingested "
                f"{source_name}"
            )

        logger.info(
            f"Completed ingestion of "
            f"{len(parsed_sources)} sources."
        )

        return parsed_sources

    def build_canonical_profile(
        self,
        parsed_sources: Dict
    ):
        """
        Construct unified candidate representation.
        """

        logger.info(
            "Starting canonical profile generation."
        )

        canonical_candidate = (
            self.canonical_builder.build(
                parsed_sources
            )
        )

        logger.info(
            "Canonical profile generation completed."
        )

        return canonical_candidate

    def generate_provenance(
        self,
        canonical_candidate
    ) -> Dict:
        """
        Generate provenance metadata for
        all resolved candidate fields.
        """

        logger.info(
            "Generating provenance metadata."
        )

        provenance = (
            self.provenance_generator.generate(
                canonical_candidate
            )
        )

        logger.info(
            "Provenance generation completed."
        )

        return provenance

    def run(
        self,
        context: PipelineContext
    ) -> PipelineResult:
        """
        Execute end-to-end transformation pipeline.
        """

        logger.info(
            "Starting candidate transformation pipeline."
        )

        parsed_sources = self.ingest_sources(
            context
        )

        canonical_candidate = (
            self.build_canonical_profile(
                parsed_sources
            )
        )

        provenance = (
            self.generate_provenance(
                canonical_candidate
            )
        )

        logger.info(
            "Pipeline execution completed successfully."
        )

        return PipelineResult(
            success=True,
            execution_timestamp=datetime.utcnow(),
            processed_sources=list(
                parsed_sources.keys()
            ),
            warnings=[],
            canonical_profile=(
                canonical_candidate.model_dump()
            ),
            provenance=provenance
        )
