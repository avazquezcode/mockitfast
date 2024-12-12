from fastapi.responses import JSONResponse


def health_check():
    body = {"success": True}
    return JSONResponse(body, 200)
