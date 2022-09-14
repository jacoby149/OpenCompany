from fastapi import HTTPException, status
import app.settings as settings

LINK = f"https://github.com/{settings.CREATOR}/{settings.REPO}"
NOT_STARRED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"{settings.CREATOR}/{settings.REPO}",
    headers={"WWW-Authenticate": "Basic"},
)