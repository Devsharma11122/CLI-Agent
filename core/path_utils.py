from pathlib import Path

WORKSPACE = Path("workspace").resolve()


def safe_path(relative_path: str) -> Path:
    """
    Resolve a user-provided path and ensure it stays
    inside the workspace directory.
    """

    target = (WORKSPACE / relative_path).resolve()

    try:
        target.relative_to(WORKSPACE)
    except ValueError:
        raise ValueError(
            "Access denied. Path is outside the workspace."
        )

    return target