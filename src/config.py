"""Config loader."""

import os

DEBUG = os.getenv("DEBUG", "false") == "true"
PORT = int(os.getenv("PORT", "8080"))
