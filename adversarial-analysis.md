# Adversarial Evaluation Analysis

## Per-hypothesis accuracy

| Hypothesis category | Correct | Total | Accuracy |
|---|---:|---:|---:|
| domain_shift | 4 | 7 | 0.57 |
| length_extreme | 6 | 6 | 1.00 |
| lexical_trigger | 3 | 7 | 0.43 |
| negation | 3 | 6 | 0.50 |
| sarcasm | 1 | 6 | 0.17 |

Overall accuracy: 17 / 32 = 0.53

## Confirmed hypotheses

The sarcasm hypothesis was strongly confirmed. The model struggled when the sentence used positive surface words sarcastically. For example, row 27 was expected to be negative, but the model predicted positive with high confidence because of the word “Amazing.” Row 28 had the same pattern: the sentence was negative because restarting the app every five minutes is a complaint, but the model predicted positive. Row 30 was also expected negative, but the model predicted positive, likely because it focused on the phrase “I just love” instead of the complaint about waiting forever.

The negation hypothesis was partly confirmed. In row 6, the sentence “I cannot say this app is bad after the latest fix” was expected positive because it negates the negative cue “bad,” but the model predicted negative. In row 8, the sentence says there are no serious complaints, so the expected label was positive, but the model predicted neutral. This suggests the model sometimes reacts to negative cue words like “bad” and “complaints” without fully handling the negation.

The lexical trigger hypothesis was also confirmed. In row 9, the sentence included the positive cue “beautiful,” but the full sentence was negative because the app crashes. The model predicted neutral instead of negative. Rows 12, 13, and 14 also show that when positive words like “friendly,” “fast,” or “reliable” appear in a negative context, the model does not always identify the final sentiment correctly.

## Refuted hypotheses

The length_extreme hypothesis was mostly refuted. I expected the model to struggle with very short or very long reviews, but it correctly classified all six examples in this category. It correctly handled short examples like “Works great,” “Crashes constantly,” and “It is okay.” It also handled long mixed sentences in rows 24 and 25, where the final sentiment depended on several details across the sentence.

The domain_shift hypothesis was partly refuted. I expected the model to fail more often on sentences outside the app-review domain, but it correctly labeled four out of seven domain-shift examples as neutral. For example, it correctly predicted neutral for the recipe sentence, the sports sentence about a player scoring, the weather sentence, and the laptop specification sentence. However, it still failed on some domain-shift examples, such as row 3 and row 16, which shows that the model is not fully robust outside app-review style language.

## What the results reveal about the decision boundary

The adversarial results suggest that the model’s decision boundary relies heavily on surface sentiment cues. It often treats words like “Amazing,” “Perfect,” “love,” “beautiful,” “friendly,” and “reliable” as strong positive signals, even when the full sentence uses them sarcastically or flips the meaning with a complaint. This is most visible in the sarcasm examples, where the model predicted positive for negative sentences with high confidence.

The model also shows weaker handling of negation. It can handle some simple negation examples, such as “did not improve,” but it struggles when the negation changes the meaning of a negative cue, such as “cannot say this app is bad” or “do not have any serious complaints.” This suggests that the model sometimes focuses on individual cue words instead of fully modeling the sentence logic.

At the same time, the model handled length extremes better than expected. It classified both short and long examples correctly, which suggests that sentence length alone is not the main weakness. The bigger weakness is semantic complexity, especially sarcasm, negation, and mixed sentiment where the surface cue conflicts with the actual intended meaning.