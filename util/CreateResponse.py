from flask import Response
from bson.json_util import dumps

def create_response(data, status_code):
    if status_code >= 200 and status_code <= 299:
        return Response(
            response=dumps(data),
            status=status_code,
            mimetype="application/json"
        )
    if status_code >= 400:
        if len(data) == 1:
            data = {
                "error": data[0]
            }
            return Response(
                response=dumps(data),
                status=status_code,
                mimetype="application/json"
            )
        else:
            data = {
                "errors": data
            }
            return Response(
                response=dumps(data),
                status=status_code,
                mimetype="application/json"
            )