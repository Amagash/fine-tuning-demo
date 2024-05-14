# Customize LLMs Through Fine-Tuning demo

This code is only for educational purposes on fine tuning LLMs and has been explained on the [Deep Dive into LLMs S1E3 episode](https://www.twitch.tv/videos/2144922963). As we saw in the episode, fine-tuning allows to customize your LLM. There are different way you can customize an LLM. Here we showcase Fine-tuning and Continued pre-training.

|     | Fine-tuning | Continued pre-training |
| -------- | ------- | ------- |
| Purpose  | Adapt the pre-trained model to perform well on specific downstream tasks. **Specialize the model for tasks** such as sentiment analysis, question answering, text classification, etc.   | **Enhance the model's general language understanding and capabilities**. Improve the model by exposing it to more data, which may include more diverse, updated, or domain-specific texts.
| Data | Involves **smaller**, **labeled** datasets that are specific to the task at hand.     | Typically involves **large**, diverse, and possibly **unsupervised** datasets similar to the original pre-training data.
| Parameters    | Typically involves **updating all the model's parameters**, but can also use techniques that modify a **subset of parameters** (e.g., parameter-efficient fine-tuning).    | A**ll the model's parameters** (weights) are usually updated.
| Outcome    | A specialized model that performs well on specific tasks but may not retain the same level of general language understanding as before. | A more generally knowledgeable and capable model that can better understand and generate language across a wide range of contexts.

## Quickstart

1. In your terminal :

```
pip install requirements.txt
```

2. Go to your [AWS](https://us-east-1.console.aws.amazon.com/) account 
3. Upload the datasets from the data folder in a S3 bucket
4. Search Bedrock and click on get started
5. Click on Custom models
6. Click on Customize model
7. Create a Fine-tuning job
8. Select the model you want to fine-tune, set a name, a job name, the location of your S3 bucket, the output location (can be the same S3 bucket)
9. Choose a role or create a new one.
10. Click on create Fine-tuning job
11. Once it's created and deployed you can replace the modelId in the main.py file with the arn of your custom model.
12. To send a query change the prompt in the main.py file and run the file

```
python path/to/main.py
```