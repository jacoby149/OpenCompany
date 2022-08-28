from fastapi import HTTPException, status

# LOGIN = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="incorrect username or password",
#     headers={"WWW-Authenticate": "Basic"},
# )