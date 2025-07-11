from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('SJ-Ray/Re-Punctuate')
model = TFT5ForConditionalGeneration.from_pretrained('SJ-Ray/Re-Punctuate')

input_text = 'the story of this brave brilliant athlete whose very being was questioned so publicly is one that still captures the imagination'
inputs = tokenizer.encode("punctuate: " + input_text, return_tensors="tf")
result = model.generate(inputs)

decoded_output = tokenizer.decode(result[0], skip_special_tokens=True)
print(decoded_output)
