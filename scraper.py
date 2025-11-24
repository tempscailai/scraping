from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route("/")
def scrape_botlfarm():
    url = request.args.get("scrape")

    if not url:
        return jsonify({"error": "Missing URL parameter. Use ?scrape=https://example.com"}), 400

    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 500

    if response.status_code != 200:
        return jsonify({"error": f"Failed to fetch page, status {response.status_code}"}), 500

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string if soup.title else "No title found"

    return jsonify({"title": title})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
