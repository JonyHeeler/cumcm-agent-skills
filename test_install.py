"""Run with python test_install.py; uses temporary directories only."""
import tempfile
from pathlib import Path
from install import install

with tempfile.TemporaryDirectory() as temporary:
    destination = Path(temporary) / "installed"
    install(destination)
    source = Path(__file__).parent / "skills"
    assert len(list(destination.glob("*/SKILL.md"))) == 10
    for item in source.rglob("*"):
        if item.is_file():
            assert item.read_bytes() == (destination / item.relative_to(source)).read_bytes()
    try:
        install(destination)
    except SystemExit as error:
        assert "Already exists" in str(error)
    else:
        raise AssertionError("Existing files must not be overwritten")
    blocked = Path(temporary) / "blocked"
    blocked.mkdir()
    (blocked / "cumcm-writing-style").write_text("keep", encoding="utf-8")
    try:
        install(blocked)
    except SystemExit:
        assert list(blocked.iterdir()) == [blocked / "cumcm-writing-style"]
        assert (blocked / "cumcm-writing-style").read_text() == "keep"
    else:
        raise AssertionError("Collision preflight failed")
print("PASS: complete copy, byte equality, repeat and collision protection")
