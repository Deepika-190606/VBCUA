from modules.semantic_similarity import compare_text

def test_similarity():
    score = compare_text(
        "Machine learning is a branch of AI.",
        "Machine learning is a branch of Artificial Intelligence."
    )

    assert 0 <= score <= 1