import flask
import bergflix


@bergflix.app.route('/api/v1/', methods=['GET'])
def get_index():
    """Return list of available services. Authentication not required."""
    context = {
        "posts": "/api/v1/posts/",
        "comments": "/api/v1/comments/",
        "url": "/api/v1/"
    }

    return flask.jsonify(**context)
