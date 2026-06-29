from pathlib import Path
from typing import Optional

import typer

from src.core.pipeline import CandidateTransformationPipeline
from src.core.pipeline_context import PipelineContext


app = typer.Typer(
    help="Multi-source candidate data transformation pipeline."
)


@app.command("run")
def run_pipeline(
    recruiter: Optional[Path] = typer.Option(
        None,
        help="Path to recruiter CSV file."
    ),
    ats: Optional[Path] = typer.Option(
        None,
        help="Path to ATS JSON export."
    ),
    github: Optional[Path] = typer.Option(
        None,
        help="Path to GitHub profile JSON."
    ),
    linkedin: Optional[Path] = typer.Option(
        None,
        help="Path to LinkedIn profile JSON."
    ),
    resume: Optional[Path] = typer.Option(
        None,
        help="Path to resume text file."
    ),
    notes: Optional[Path] = typer.Option(
        None,
        help="Path to recruiter notes."
    ),
) -> None:
    """
    Execute the candidate transformation pipeline.
    """

    context = PipelineContext(
        recruiter_csv=recruiter,
        ats_json=ats,
        github_profile=github,
        linkedin_profile=linkedin,
        resume_file=resume,
        recruiter_notes=notes,
    )

    pipeline = CandidateTransformationPipeline()

    result = pipeline.run(context)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
