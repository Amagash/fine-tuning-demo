# Customize LLMs Through Fine-Tuning demo

This code is only for educational purposes on fine tuning LLMs and has been explained on the [Deep Dive into LLMs S1E3 episode](https://www.twitch.tv/videos/2144922963). As we saw in the episode, fine-tuning allows to customize your LLM. There are different way you can customize an LLM. Here we showcase Fine-tuning and Continued pre-training.

|     | Fine-tuning | Continued pre-training |
| -------- | ------- | ------- |
| Purpose  | Adapt the pre-trained model to perform well on specific downstream tasks. **Specialize the model for tasks** such as sentiment analysis, question answering, text classification, etc.   | **Enhance the model's general language understanding and capabilities**. Improve the model by exposing it to more data, which may include more diverse, updated, or domain-specific texts.
| Data | Involves **smaller**, **labeled** datasets that are specific to the task at hand.     | Typically involves **large**, diverse, and possibly **unsupervised** datasets similar to the original pre-training data.
| Parameters    | Typically involves **updating all the model's parameters**, but can also use techniques that modify a **subset of parameters** (e.g., parameter-efficient fine-tuning).    | A**ll the model's parameters** (weights) are usually updated.
| Outcome    | A specialized model that performs well on specific tasks but may not retain the same level of general language understanding as before. | A more generally knowledgeable and capable model that can better understand and generate language across a wide range of contexts.

