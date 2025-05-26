# av-generation
Audio visual translation

🎶 LESS EXELANT PIPELINE (Google Cloud Run)

Trigger Python-based audio/video rendering jobs using a Google Sheet frontend.

Choose a track in Sheets → Click a button → Automatically runs:
- MP3 to WAV conversion
- Spectrogram/image analysis
- Spiral/square/block visual generation
- Final video assembly + logging

Options:
- Run from local or Colab
- Deploy as HTTP service via Cloud Run (this repo)
- Store media in Google Drive or GCS

- less_exelant_pipeline/
├── app.py                  # Flask app for Cloud Run
├── run_pipeline.py         # Your actual logic
├── Dockerfile              # For deployment
├── requirements.txt        # Libraries
└── cloudbuild.yaml         # (optional for CI/CD)
