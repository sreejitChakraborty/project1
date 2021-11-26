import views

# config your urls here


def add_url(app):
    app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])
    app.add_url_rule('/page2', view_func=views.page2, methods=['GET', 'POST'])

    return app
