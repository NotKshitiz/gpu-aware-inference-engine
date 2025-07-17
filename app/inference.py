from transformers import AutoTokenizer
import onnxruntime as ort
import numpy as np

# Load tokenizer and ONNX session
tokenizer = AutoTokenizer.from_pretrained("onnx/gpt2")
session = ort.InferenceSession(r"C:\Users\kshit\OneDrive\Documents\Desktop\Transformers\onnx-gpt2\model.onnx", providers=["DmlExecutionProvider"])


text = "Hey guys i wanna learn onnx"
max_tokens = 50

for _ in range(max_tokens):
    inputs = tokenizer(text, return_tensors="np")
    input_ids = inputs["input_ids"]

    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    logits = session.run([output_name], {input_name: input_ids})[0]

    next_token_logits = logits[0, -1]
    next_token_id = int(np.argmax(next_token_logits))
    next_token = tokenizer.decode([next_token_id])

    text += next_token

print(" Final Generated Text:\n", text)
