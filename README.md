Please refer to the original repo for more details on their work. Many thanks to the team for sharing their work.

Changes were made in this fork for converting the models to onnx.

I basically added a function convert_to_onnx() in user.py to run the conversion. You will need to modify the function to match your model input size. To keep things simple, I made the function call in a separate script convert_onnx.py. 

You will just need to run convert_onnx.py with the same params as infer.py. The error I had faced was due to the indexing in the backbone which I have commented out. That shouldn't matter for inference since your input will be fixed but you might need it for training.

1. Modify convert_to_onnx() with the correct input sizes for your model
2. Run convert_onnx.py to do the conversion, model.onnx will be created in the same directory
3. Run check_onnx.py to verify the that the ONNX model is valid
