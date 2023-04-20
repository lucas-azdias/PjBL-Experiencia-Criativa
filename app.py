from controllers.app_controller import createApp
from utils.create_db import create_db


if __name__ == "__main__":
    app = createApp()
    create_db(app)
    app.run(debug=True)
