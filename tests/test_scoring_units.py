def test_scoring_requires_fractions():
    from src.scoring import compute_icer_score

    preds = {
        "white_pct": 0.12,
        "black_pct": 0.10,
        "asian_pct": 0.05,
        "aian_pct": 0.02,
        "female_pct": 0.55,
        "male_pct": 0.45,
        "age65_pct": 0.30,
    }

    score, _ = compute_icer_score(preds)
    assert score > 0


def test_scoring_uses_complete_reference_override():
    from src.scoring import compute_icer_score

    reference = {
        "white_pct": 0.10,
        "black_pct": 0.20,
        "asian_pct": 0.15,
        "aian_pct": 0.05,
        "female_pct": 0.55,
        "male_pct": 0.45,
        "age65_pct": 0.30,
    }

    score, breakdown = compute_icer_score(reference, reference_override=reference)

    assert score == 21.0
    assert breakdown["population_reference"].tolist() == list(reference.values())
