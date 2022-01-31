from . import v1_bp


@v1_bp.route("analytics", methods=["GET"])
def show_analytics():
    pass
