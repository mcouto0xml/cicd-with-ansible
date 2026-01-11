import os
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    # Cor vinda da variável de ambiente
    color = os.getenv("APP_COLOR", "#800808")  # fallback seguro
    version = os.getenv("APP_VERSION", "dev")

    return render_template(
        "index.html",
        background_color=color,
        version=version
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
