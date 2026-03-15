from flask import Flask, Request

from ifsApprover import config
from ifsApprover.web.helper import requires_auth

app = Flask(__name__)

# use the already existing config
for key in config:
    app.config[key] = config[key]

Request.max_form_memory_size = 20 * 1024 * 1024

from ifsApprover.web.views import images, mails, web_ui

app.register_blueprint(images.images, url_prefix="/images")
# app.register_blueprint(previews.previews, url_prefix="/previews")
app.register_blueprint(mails.mails, url_prefix="/mails")
if app.config["SERVE_STATIC_FRONTEND"]:
    app.register_blueprint(web_ui.web_ui, url_prefix="/")
