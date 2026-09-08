"""Copy the bundled skills without replacing existing installations (Python 3.9+)."""
import argparse
import shutil
from pathlib import Path


def install(destination):
    sources = sorted((Path(__file__).parent / "skills").glob("*/SKILL.md"))
    if not sources:
        raise SystemExit("No bundled skills found.")
    pending = []
    for entry in sources:
        source = entry.parent
        target = destination / source.name
        if target.exists() or target.is_symlink():
            raise SystemExit(f"Already exists; no skills copied: {target}")
        pending.append((source, target))
    destination.mkdir(parents=True, exist_ok=True)
    for source, target in pending:
        shutil.copytree(source, target)
    print(f"Installed {len(pending)} skills in {destination.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Destination skills directory; default: ~/.agents/skills")
    install(parser.parse_args().dest.expanduser())
