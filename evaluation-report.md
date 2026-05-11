## Three qualitative error examples

### Example 1

- Original sentence: "good, but slow workflow."
- Gold label: positive
- Predicted label: neutral
- Predicted probability for the gold label: 0.3144

Explanation: This review has mixed sentiment. The word "good" is positive, but the phrase "slow workflow" sounds like a complaint. The model may have focused more on the limitation and treated the sentence as neutral instead of positive.

### Example 2

- Original sentence: "nice app to use with friends"
- Gold label: neutral
- Predicted label: positive
- Predicted probability for the gold label: 0.0959

Explanation: The model likely predicted positive because of the word "nice" and the friendly context. Even though the dataset labels it as neutral, the sentence sounds positive to a human too, so this is a somewhat understandable mistake.

### Example 3

- Original sentence: "why can i not delete saved locations? and ive read thtough it many times and dont see anyway at all to delte previously saved locations!!? im going to have to uninstall the app and then reinstall it to reset this location deleting issue u have!?!???"
- Gold label: neutral
- Predicted label: negative
- Predicted probability for the gold label: 0.1230

Explanation: This sentence contains many negative cues, such as not being able to delete saved locations, uninstalling the app, and repeated punctuation. The model predicted negative because the review sounds frustrated, even though the gold label is neutral.

## Hugging Face Hub model URL

https://huggingface.co/AwwadR/m7-app-review-sentiment