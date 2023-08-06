from flask import Flask, render_template, request
import diffusion_inference

# make our Flask api...
app = Flask(__name__, template_folder="template")


# form urls/...
@app.route("/")
def home():
    return render_template("rm.html")


# Accepting form data
@app.route("/prediction", methods=["POST"])
def prediction():
    e = request.form["fikira"]
    print(e)
    e = diffusion_inference.sw_en(e)
    print(e)
    prompt = "{}, 512px x 512px, high resolution ".format(e)
    diffusion_inference.generate_image(prompt)

    return render_template("rm1.html")


# Run this file as the main file...
if __name__ == "__main__":
    app.run(debug=True)
