from transformers import (AutoTokenizer,AutoModelForCausalLM)
# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b")
model = AutoModelForCausalLM.from_pretrained("THUDM/chatglm3-6b")

# Prepare text input
input_text = "中金公司交易员月薪八万五是如何做到的？"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate a response
output = model.generate(input_ids, max_length=100)

# Decode and print the output
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
print(decoded_output)
