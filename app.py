from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def trigger():
    data = request.json
    track = data.get("track", "unknown")
    mp3_path = data.get("mp3_path")
    
    print(f"📥 Received request for: {track}")

    # Call the actual pipeline
    subprocess.run([
        "python3", "run_pipeline.py",
        "--track", track,
        "--mp3", mp3_path
    ])

    return {"status": "✅ Done", "track": track}
