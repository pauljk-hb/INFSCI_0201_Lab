from flask import Flask, render_template, request
import segno
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    message = ""

    if request.method == "POST":
        message = request.form["data"]
        qr = segno.make(message)
        
        buffer = io.BytesIO()
        qr.save(buffer, kind="png", scale=4)
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        qr_code = f"data:image/png;base64,{img_str}"

    return render_template("index.html", qr_code=qr_code, message=message)

if __name__ == "__main__":
    app.run(debug=True)
