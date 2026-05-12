# Calibration Analysis

## Reliability diagram interpretation

The saved reliability diagram (`figures/reliability-diagram.png`) shows that the model is mostly over-confident in the middle and high confidence buckets. A perfectly calibrated model would follow the diagonal line, where predicted confidence matches empirical accuracy.

In the 0.6–0.7 confidence bucket, the model had accuracy of 0.542 with 343 examples. Since the bucket confidence is around 0.65 but the real accuracy is only about 0.54, the model is over-confident in this range.

The 0.7–0.8 confidence bucket also shows over-confidence. It had accuracy of 0.582 with 342 examples, which is lower than the expected confidence level for that bucket.

The 0.8–0.9 bucket had accuracy of 0.746 with 370 examples. This is closer to the diagonal line, but it is still slightly over-confident because the empirical accuracy is below the bucket confidence.

The 0.9–1.0 bucket had accuracy of 0.869 with 383 examples. This shows the model is more reliable when it is very confident, but it is still a little over-confident because the accuracy is lower than the confidence range.

The first three buckets had zero examples, so I did not interpret them. The 0.3–0.4 bucket had only 3 examples, so it is too small to draw a strong conclusion from.

## Expected Calibration Error

The Expected Calibration Error was:

**ECE = 0.0956**

This means that, on average, the model's predicted confidence differs from its actual accuracy by about 9.56 percentage points.

For production use, this means the model's probability scores should be treated carefully. The model can still be useful for classification, but its confidence values are not perfectly trustworthy. For example, when the model gives confidence around 0.75, the real accuracy may be closer to 0.58 based on the reliability diagram.

## A specific calibration pattern

One clear calibration pattern is over-confidence in the middle confidence buckets, especially from 0.6 to 0.8. In the 0.6–0.7 bucket, the accuracy was 0.542 with 343 examples. In the 0.7–0.8 bucket, the accuracy was 0.582 with 342 examples. Both buckets have empirical accuracy below their predicted confidence range.

This pattern may have happened because the model was fine-tuned on a limited dataset. The classifier learned useful sentiment patterns, but its probability estimates are not perfectly calibrated. Since this is a 3-class sentiment task, some examples may be close to class boundaries. For example, a review may contain mixed wording, or the review text may not perfectly match the rating label. These harder examples can make the model confident even when the prediction is not correct.

## A proposed engineering action

Based on these findings, I would use threshold-based abstention in production. For example, if the model's confidence is below 0.80, the system should avoid making a fully automatic decision and instead flag the prediction for human review.

I would also use temperature scaling on a validation set to reduce over-confidence without retraining the full DistilBERT model. Finally, I would collect more labeled examples from the confusing middle-confidence range, especially examples where the model gives confidence between 0.6 and 0.8 but predicts incorrectly.