from statistics import mean


def mean_absolute_error(actual: list[float], predicted: list[float]) -> float:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("Lists must have equal non-zero length")
    return mean(abs(a - p) for a, p in zip(actual, predicted))


def baseline_predict(training_targets: list[float], test_count: int) -> list[float]:
    if not training_targets or test_count < 0:
        raise ValueError("Training targets required and test_count non-negative")
    return [mean(training_targets)] * test_count


if __name__ == "__main__":
    training, actual = [10.0, 12.0, 11.0, 13.0], [10.5, 12.5]
    predicted = baseline_predict(training, len(actual))
    print("Predictions:", predicted, "MAE:", mean_absolute_error(actual, predicted))
