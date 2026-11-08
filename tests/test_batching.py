from pipeline.batching import batch_orders


def test_batches_have_at_most_the_requested_size():
    assert [len(batch) for batch in batch_orders(list(range(7)), 3)] == [3, 3, 1]


def test_empty_input_gives_no_batches():
    assert batch_orders([], 3) == []
