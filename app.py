import views
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import config
import urls

app = Flask(__name__)


# csrf
csrf = CSRFProtect(app)

# config
app.config.from_object('config.Config')

#######################


# urls
app = urls.add_url(app)


if __name__ == "__main__":
    app.run(debug=True)
