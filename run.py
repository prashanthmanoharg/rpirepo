import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PI_PORT"))  # Retrieve PI_PORT from environment variables
    app.run(host="0.0.0.0", port=port, debug=True)