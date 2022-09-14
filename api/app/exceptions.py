from fastapi import HTTPException, status
import app.settings as settings
NOT_STARRED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"in order to login, you must star {settings.CREATOR}/{settings.REPO}",
    headers={"WWW-Authenticate": "Basic"},
)