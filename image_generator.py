from flask import Flask, request, jsonify, render_template
import requests
import random

app = Flask(__name__)

def generate_pollinations_image(prompt, width=768, height=768, seed=None, nologo=True):
    # Build the URL
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width={width}&height={height}"
    if seed:
        url += f"&seed={seed}"
    if nologo:
        url += "&nologo"

    return url

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["GET"])
def generate():
    prompt = request.args.get("prompt", "a beautiful painting")
    width = int(request.args.get("width", 768))
    height = int(request.args.get("height", 768))
    seed = request.args.get("seed", "")
    nologo = request.args.get("nologo", "true").lower() == "true"

    tries = 3
    url = None

    for attempt in range(tries):
        # Generate image URL
        url = generate_pollinations_image(prompt, width, height, seed if seed else random.randint(1, 99999), nologo)

        # Try fetching the image to validate it
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200 and res.content[:10] != b"\x00\x00\x00\x00\x00\x00\x00\x00":
                # ✅ Looks like a valid image
                return jsonify({"success": True, "image_url": url})
        except Exception:
            pass

        # 🔄 If failed, try with smaller size
        width = max(512, width - 256)
        height = max(512, height - 256)

    # ❌ If all attempts fail
    return jsonify({"success": False, "error": "Could not generate a valid image. Please try again."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008, debug=True)
