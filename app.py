import time
import hashlib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="DermaScan API",
    description="API d'Inférence Dermatologique - Mastère 1 Data Engineer",
    version="1.2.0"
)

# Sel applicatif pour la pseudonymisation RGPD (Art. 32)
APP_SALT = "DermAScaN_M1_2026_SecUreSaLt"

class InferenceRequest(BaseModel):
    patient_id: str
    image_base64: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DermaScan API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "dermascan-api"}

@app.post("/predict")
def predict(payload: InferenceRequest):
    start_time = time.time()
    
    # Hachage SHA-256 salé de l'identifiant patient
    patient_hash = hashlib.sha256((payload.patient_id + APP_SALT).encode('utf-8')).hexdigest()
    
    # Simulation du temps d'inférence d'un modèle de Deep Learning
    time.sleep(0.04) 
    latency_ms = round((time.time() - start_time) * 1000, 2)
    
    return {
        "status": 200,
        "patient_hash_sha256": patient_hash,
        "prediction": "benign",
        "confidence": 0.94,
        "inference_latency_ms": latency_ms,
        "model_version": "v1.2.0"
    }