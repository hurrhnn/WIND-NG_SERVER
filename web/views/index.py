from flask import Blueprint

callname = __name__.rsplit(".", 1)[-1]

bp = Blueprint(
    name=callname,
    import_name=__name__,
    url_prefix="/"
)


@bp.route('/')
def test():
    return "This is a test Index Page!"