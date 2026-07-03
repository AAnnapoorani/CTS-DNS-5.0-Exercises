from flask import jsonify

from . import courses_bp


@courses_bp.route(
    "/test"
)

def test():

    return jsonify({
        "message":
        "Hands On 5 Working"
    })