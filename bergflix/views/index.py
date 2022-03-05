import flask
import bergflix


@bergflix.app.route('/', methods=['GET'])
def get_index():
    context = {
        
    }

    return flask.jsonify(**context)
