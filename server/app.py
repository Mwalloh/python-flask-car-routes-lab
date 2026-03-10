from flask import Flask
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Flatiron Cars</h1>"

@app.route('/<model>')
def car(model):
    if model in existing_models:
        return f"<h2>Flatiron {model} is in our fleet!</h2>"
    else:
        return f"<h2>No models called {model} exists in our catalog</h2>"
    
if __name__ == "__main__":
    app.run(port=5555, debug=True)