from pathlib import Path

import yaml
from plumbum.cmd import copier as copier_cmd

from copier.cli import CopierApp

SIMPLE_DEMO_PATH = Path(__file__).parent / "demo_simple"


def test_good_cli_run(dst):
    run_result = CopierApp.run(
        ["--quiet", "-a", "altered-answers.yml", str(SIMPLE_DEMO_PATH), str(dst)],
        exit=False,
    )
    a_txt = dst / "a.txt"
    assert run_result[1] == 0
    assert a_txt.exists()
    assert a_txt.is_file()
    assert a_txt.read_text().strip() == "EXAMPLE_CONTENT"
    answers = yaml.safe_load((dst / "altered-answers.yml").read_text())
    assert answers["_src_path"] == str(SIMPLE_DEMO_PATH)


def test_help():
    copier_cmd("--help-all")
