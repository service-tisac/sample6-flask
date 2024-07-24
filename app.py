from flask import Flask, request, jsonify
import torch
import torch.nn as nn
from typing import List

# Define the Neural Network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load model from checkpoint
def load_model(checkpoint_path):
    model = SimpleNN()
    model.load_state_dict(torch.load(checkpoint_path))
    model.eval()
    return model

# Create Flask app
app = Flask(__name__)

# Load the model checkpoint
model = load_model('simple_nn_checkpoint.pth')

@app.route('/')
def hello():
    print("Hello sample 6")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'input' not in data or len(data['input']) != 10:
        return jsonify({"error": "Input must be a list of 10 floats."}), 400
    
    input_tensor = torch.tensor(data['input']).float().unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(input_tensor)
    
    return jsonify({"output": output.squeeze().item()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
