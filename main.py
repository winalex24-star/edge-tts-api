from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import edge_tts
import uuid

app = FastAPI()

class TTSRequest(BaseModel):
    texto: str
    voz: str = "es-US-AlonsoNeural"

@app.post("/tts")
async def tts(req: TTSRequest):

    archivo = f"{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        req.texto,
        req.voz
    )

    await communicate.save(archivo)

    return FileResponse(
        archivo,
        media_type="audio/mpeg",
        filename="audio.mp3"
    )
