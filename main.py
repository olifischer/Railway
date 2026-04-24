from flask import Flask
import os

app = Flask(__name__)

#test

@app.route('/')
def hello():
    return "Hallo! Diese Seite läuft auf Railway."

if __name__ == "__main__":
    # Railway gibt den Port über eine Umgebungsvariable vor
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)