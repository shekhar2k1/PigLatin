from flask import request, jsonify, Blueprint


from .. import piglatin


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    response = """
        Usage: "{}translate?text=Piglatintext."
    """.format(request.url)
    return response


@main.route('/translate', methods=['GET'])
def translate():
    text = request.args.get('text')
    if not text:
        message = 'Invalid input text={}'.format(text)
        return jsonify(error=500, text=str(message)), 500

    response = {'text': piglatin.translate(text)}
    return jsonify(response)
