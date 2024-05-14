import boto3 
import json

bedrock = boto3.client(service_name='bedrock-runtime')

def list_models():
  """
    List all models that you can fine-tune
  """
  for model in bedrock.list_foundation_models(
      byCustomizationType="FINE_TUNING")["modelSummaries"]:
      for key, value in model.items():
          print(key, ":", value)
      print("-----\n")

prompt="What services do you offer in the institute?"

body = {
    "prompt": prompt,
    "temperature": 0.5,
    "p": 0.9,
    "max_tokens": 512,
}

response = bedrock.invoke_model(
  # use this modelId to test the model before fine-tuning
  modelId="cohere.command-light-text-v14",
  # use this modelId to test the model after fine-tuning and replace the arn of your model
  # modelId="arn:aws:bedrock:us-east-1:XXXXXXXXXXXX:provisioned-model/XXXXXXXXXXXX",
  body=json.dumps(body)
)

response_body = json.loads(response.get("body").read())
outputs = response_body.get('outputs')
print(response_body)