"""A normal local virtual environment must not trip the source-path gate."""
from pathlib import Path
import subprocess


def test_guard_skips_dependencies_but_rejects_project_paths(tmp_path):
    guard = Path(__file__).resolve().parents[1] / "tools/check_paths.sh"
    dependency = tmp_path / ".venv-audit/lib/package.py"
    dependency.parent.mkdir(parents=True)
    machine_path = "/" + "Users/example/private-data"
    dependency.write_text(f"DATA = {machine_path!r}\n")
    run = lambda: subprocess.run(["bash", str(guard), str(tmp_path)], capture_output=True, text=True)
    assert run().returncode == 0
    (tmp_path / "analysis.py").write_text(f"DATA = {machine_path!r}\n")
    assert run().returncode == 1
