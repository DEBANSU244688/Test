from app.services.market_data_ingestion import JobPostRecord, ingest_job_posts


def test_ingest_job_posts_aggregates_skill_frequency() -> None:
    posts = [
        JobPostRecord(
            role="Backend Engineer",
            description="Must have Python, SQL, and Docker. AWS is preferred.",
        ),
        JobPostRecord(
            role="ML Engineer",
            description="Python and Machine Learning required. Docker plus Kubernetes experience.",
        ),
        JobPostRecord(
            role="Full Stack Engineer",
            description="React, TypeScript, SQL, and AWS experience.",
        ),
    ]

    result = ingest_job_posts(posts)

    assert result["python"] == 2
    assert result["sql"] == 2
    assert result["docker"] == 2
    assert result["aws"] == 2
    assert result["machine learning"] == 1
