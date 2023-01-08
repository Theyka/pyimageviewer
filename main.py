# Webserver imports
from quart import Quart, request, app, url_for, render_template
from hypercorn.config import Config
from hypercorn.asyncio import serve

# User imports
import asyncio
import datetime
import os

# WebServer Application
app = Quart(__name__, static_folder='static')

@app.route("/")
async def index():
    try:
        if request.args.get('id'):
            if os.path.exists(f"./static/image/{request.args.get('id')}"):
                return f"""
                        <html lang="en">
                            <head>
                                <script src="https://code.jquery.com/jquery-3.6.0.min.js"
                                    integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
                                    crossorigin="anonymous">
                                </script>
                                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"
                                    integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns"
                                    crossorigin="anonymous">
                                </script>
                                <style>
                                    .form-control {{
                                        background-color: #202020 !important;
                                        border-color: #484848 !important;
                                        color: white !important;
                                    }}
    
                                    .form-control::placeholder {{
                                        transition: 0.2s;
                                    }}
    
                                    .form-control:focus::placeholder {{
                                        color: white !important;
                                        transition: 0.2s;
                                    }}
    
                                    .input-group-text {{
                                        background-color: #202020 !important;
                                        border-color: #484848 !important;
                                    }}
    
                                    .input-group-prepend .input-group-text {{
                                        border-right: none;
                                    }}
    
                                    .input-group-append .input-group-text {{
                                        border-left: none;
                                    }}
                                </style>
                                <meta name="robots" content="noindex">
                                <link rel="stylesheet" href="{url_for('static', filename='css/argon.css')}">
                                <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.15.3/css/all.css">
                                <title>Theyka.net - {request.args.get('id')}</title>
                                <meta name="twitter:card" content="summary_large_image">
                                <meta name="twitter:image" content="{request.url_root}{url_for('static', filename='image/'+request.args.get("id"))}">
                                <meta name="twitter:image:src" content="{request.url_root}{url_for('static', filename='image/'+request.args.get("id"))}">
                                <meta property="og:image" content="{request.url_root}{url_for('static', filename='image/'+request.args.get("id"))}">
                                <meta name="theme-color" content="#e69e0a">
                                <meta property="og:title" content="Theyka.net" />
                                <meta property="og:site_name" content="{request.args.get('id')}">
                                <meta name="twitter:site" content="{request.args.get('id')}">
                            </head>
                            <body>
                                <div class="row mt-5 no-gutters">
                                    <div class="col-md-3"></div>
                                    <div class="col-md-6 mx-2">
                                        <div class="card card-stats text-center card-shadow bg-darker mb-4">
                                            <div class="card-body">
                                                <h3 class="card-title mb-0">
                                                    {request.args.get("id")}
                                                </h3>
                                                <br>
                                                <img src="{url_for('static', filename='image/'+request.args.get("id"))}" alt="image" style="max-height: 75vh; width: auto; max-width: 100%; border-radius: 0.25rem" />
                                                <br>
                                                <a href="{url_for('static', filename='image/'+request.args.get("id"))}" download target="_blank" class="btn btn-success" style="margin-top: 2%;">
                                                    <span class="btn-inner--icon">
                                                        <i class="fas fa-cloud-download mr-2"></i>
                                                    </span>
                                                    Download
                                                </a>
                                            
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-3"></div>
                                </div>
                        </body>
                        </html>
                        """
            else:
                return await render_template("not_found.html")
        else:
            return await render_template("not_found.html")
    except Exception as error:
        return f'{{"error": "{error}", "time": "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"}}'


if __name__ == "__main__":
    # Hypercorn configuration
    config = Config()
    config.bind = "0.0.0.0:25997"
    # Start Server
    asyncio.run(serve(app, config=config))
