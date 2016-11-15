from flask import Flask
app = Flask(__name__)

import application.views.search
import application.views.details
import application.views.download
