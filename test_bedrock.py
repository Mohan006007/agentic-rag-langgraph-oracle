import boto3
import json

client = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)

prompt = """
Explain Retrieval-Augmented Generation (RAG)
simply for beginners in AI.
"""

body = {
    "prompt": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{prompt}\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
    "max_gen_len": 512,
    "temperature": 0.3
}

response = client.invoke_model(
    modelId="meta.llama3-8b-instruct-v1:0",
    body=json.dumps(body)
)

response_body = json.loads(
    response["body"].read()
)

print(response_body["generation"])
