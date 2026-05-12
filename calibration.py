"""
Stretch Tuesday — Calibration Analysis.

Reliability diagram + Expected Calibration Error (ECE).
"""

import numpy as np


def reliability_diagram(probs: np.ndarray, y_true: np.ndarray, n_bins: int = 10):
    """
    Bin predictions by max predicted probability; compute empirical accuracy per bin.

    Returns (bucket_centers, bucket_accuracies, bucket_counts), all length n_bins.
    """
    probs = np.asarray(probs)
    y_true = np.asarray(y_true)

    confidences = np.max(probs, axis=1)
    predictions = np.argmax(probs, axis=1)
    correct = predictions == y_true

    edges = np.linspace(0, 1, n_bins + 1)
    bucket_centers = (edges[:-1] + edges[1:]) / 2

    bucket_accuracies = np.zeros(n_bins)
    bucket_counts = np.zeros(n_bins, dtype=int)

    for i in range(n_bins):
        left = edges[i]
        right = edges[i + 1]

        if i == n_bins - 1:
            in_bucket = (confidences >= left) & (confidences <= right)
        else:
            in_bucket = (confidences >= left) & (confidences < right)

        bucket_counts[i] = np.sum(in_bucket)

        if bucket_counts[i] > 0:
            bucket_accuracies[i] = np.mean(correct[in_bucket])
        else:
            bucket_accuracies[i] = 0.0

    return bucket_centers, bucket_accuracies, bucket_counts


def expected_calibration_error(probs: np.ndarray, y_true: np.ndarray, n_bins: int = 10) -> float:
    """
    ECE = sum over bins of (bucket_count / N) * |bucket_accuracy - bucket_confidence|.

    A perfectly calibrated model has ECE = 0.
    """
    probs = np.asarray(probs)
    y_true = np.asarray(y_true)

    confidences = np.max(probs, axis=1)
    predictions = np.argmax(probs, axis=1)
    correct = predictions == y_true

    edges = np.linspace(0, 1, n_bins + 1)

    n = len(y_true)
    ece = 0.0

    for i in range(n_bins):
        left = edges[i]
        right = edges[i + 1]

        if i == n_bins - 1:
            in_bucket = (confidences >= left) & (confidences <= right)
        else:
            in_bucket = (confidences >= left) & (confidences < right)

        bucket_count = np.sum(in_bucket)

        if bucket_count > 0:
            bucket_accuracy = np.mean(correct[in_bucket])
            bucket_confidence = np.mean(confidences[in_bucket])

            ece += (bucket_count / n) * abs(bucket_accuracy - bucket_confidence)
    
    return float(ece)


def plot_reliability(centers: np.ndarray, accs: np.ndarray, counts: np.ndarray, output_path: str) -> None:
    """Save a reliability diagram. Provided helper — do not modify."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 5))
    width = 1.0 / max(len(centers), 1)
    ax.bar(centers, accs, width=width * 0.9, edgecolor="black", alpha=0.8, label="Empirical accuracy")
    ax.plot([0, 1], [0, 1], "--", color="grey", label="Perfect calibration")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Predicted probability (bucket center)")
    ax.set_ylabel("Empirical accuracy")
    ax.set_title("Reliability diagram")
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
