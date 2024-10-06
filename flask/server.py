import flask

from flask import jsonify, request
from flask.views import MethodView
from models import Advertisement, Session

app = flask.Flask("advertisements")


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(http_response: flask.Response):
    request.session.close()

    return http_response


class AdvertisementView(MethodView):
    def get(self, advtg_id: int):
        advtg = request.session.get(Advertisement, advtg_id)

        return jsonify(advtg.json)

    def post(self):
        json_data = request.json
        advtg = Advertisement(**json_data)

        # Create advertisement
        request.session.add(advtg)
        request.session.commit()

        return jsonify({"id": advtg.id})

    def patch(self, advtg_id: int):
        advtg = request.session.get(Advertisement, advtg_id)
        json_data = request.json

        for field, value in json_data.items():
            setattr(advtg, field, value)

        request.session.add(advtg)
        request.session.commit()

        return jsonify(advtg.json)

    def delete(self, advtg_id: int):
        advtg = request.session.get(Advertisement, advtg_id)

        request.session.delete(advtg)
        request.session.commit()

        return jsonify({"status": "deleted"})


advertisement_view = AdvertisementView.as_view('advertisement')

app.add_url_rule("/", view_func=advertisement_view, methods=["POST"])
app.add_url_rule("/<int:advtg_id>", view_func=advertisement_view, methods=["GET", "PATCH", "DELETE"])

app.run()
