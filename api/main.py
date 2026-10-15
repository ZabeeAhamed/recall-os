
from fastapi import FastAPI, HTTPException

from api.db import get_db_connection

app = FastAPI(title="recall-os")


@app.get("/health")
def health_check():
    try:
        with get_db_connection() as conn:
            conn.execute("SELECT 1")

        return {"status": "ok"}

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        ) from exc
