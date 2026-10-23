"""Cache isolation and the deposited offline example contract; no API access."""
import json
from pathlib import Path

import pytest

from consilience import cli


def test_gene_and_tissue_changes_refetch(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(cli.lenses, "resolve_ids", lambda genes: {})
    def fetch(genes, ids, hpa_field):
        calls.append((tuple(genes), hpa_field))
        return {(genes[0], genes[1]): len(calls) / 10}, {}
    monkeypatch.setattr(cli.lenses, "expression_sim", fetch)
    args = (str(tmp_path), "same-name")
    first = cli._lens_cached("expression", ["A", "B"], "brain", *args)
    assert cli._lens_cached("expression", ["B", "A"], "brain", *args) == first
    assert cli._lens_cached("expression", ["C", "D"], "brain", *args) == {("C", "D"): .2}
    assert cli._lens_cached("expression", ["A", "B"], "blood", *args) == {("A", "B"): .3}
    assert len(calls) == 3


def test_refresh_preserves_deposited_snapshot(tmp_path, monkeypatch):
    inputs = cli._cache_inputs("structure", ["A", "B"], "unused")
    snapshot = tmp_path / "example__structure.json"
    cli._save_sim(snapshot, {("A", "B"): .9}, inputs)
    original = snapshot.read_bytes()
    monkeypatch.setitem(cli.lenses.LENSES, "structure", lambda genes: {("A", "B"): .1})
    assert cli._lens_cached("structure", ["A", "B"], "unused", tmp_path, "example", refresh=True) == {("A", "B"): .1}
    assert snapshot.read_bytes() == original
    assert cli._lens_cached("structure", ["A", "B"], "unused", tmp_path, "example") == {("A", "B"): .9}


def test_unlabelled_legacy_cache_is_not_trusted(tmp_path, monkeypatch):
    (tmp_path / "example__structure.json").write_text('{"A|B":0.9}')
    monkeypatch.setitem(cli.lenses.LENSES, "structure", lambda genes: {("A", "B"): .2})
    assert cli._lens_cached("structure", ["A", "B"], "unused", tmp_path, "example") == {("A", "B"): .2}


def test_example_snapshots_are_self_describing_and_offline(monkeypatch):
    root = Path(__file__).resolve().parents[1] / "examples"
    def network_forbidden(*args, **kwargs):
        raise AssertionError("A shipped example tried to fetch live data")
    monkeypatch.setattr(cli.lenses, "resolve_ids", network_forbidden)
    monkeypatch.setattr(cli.lenses, "expression_sim", network_forbidden)
    for lens in cli.lenses.LENSES:
        monkeypatch.setitem(cli.lenses.LENSES, lens, network_forbidden)
    for name in ("cardiac", "immune"):
        cfg = json.loads((root / f"{name}.json").read_text())
        genes = sorted({g for values in cfg["components"].values() for g in values})
        for lens in cli.PROVIDERS:
            path = root / ".consilience_cache" / f"{name}__{lens}.json"
            original = path.read_bytes()
            sim = cli._lens_cached(lens, genes, cfg["expression_field"], path.parent, name)
            assert sim
            assert path.read_bytes() == original


def test_unsupported_species_fails_before_fetch(tmp_path):
    with pytest.raises(ValueError, match="human"):
        cli._lens_cached("structure", ["A", "B"], "unused", tmp_path, "mouse", species=10090)
