import onnx
onnx_model = onnx.load('model.onnx')
onnx.checker.check_model(onnx_model)
print(onnx.helper.printable_graph(onnx_model.graph))
print("Check complete!")