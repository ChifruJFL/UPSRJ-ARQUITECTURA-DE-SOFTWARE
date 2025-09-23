from flask import Blueprint, jsonify, request, render_template
from service.user_service import UserService
from service.group_service import GroupService
from py_utils.logger import plog, INFO, DEBUG

bp = Blueprint("routes", __name__)
user_service = UserService()
group_service = GroupService()

@bp.route("/users")
def api_users():
    plog("GET /users", INFO)
    users = user_service.get_all()
    return jsonify(users)

@bp.route("/groups")
def api_groups():
    plog("GET /groups", INFO)
    groups = group_service.get_all()
    return jsonify(groups)

@bp.route("/search", methods=["GET", "POST"])
def search():
    plog("Called /search", DEBUG)
    # Determinar si buscamos usuarios o grupos
    entity_type = request.args.get("type") or request.form.get("type") or "user"
    keyword = request.args.get("keyword") or request.form.get("keyword") or ""
    id_str = request.args.get("id") or request.form.get("id") or ""

    if not keyword and not id_str:
        return render_template("search.html", type_selected=entity_type)

    results = []
    if id_str:
        try:
            idv = int(id_str)
        except ValueError:
            return render_template("error.html", message="Invalid ID format")
        if entity_type == "user":
            item = user_service.get_by_id(idv)
            if not item:
                return render_template("error.html", message="User not found")
            # obtener grupos del usuario
            groups = [g for g in group_service.get_all() if idv in g.get("members",[])]
            return render_template("result.html", kind="user", user=item, groups=groups)
        else:
            grp = group_service.get_by_id(idv)
            if not grp:
                return render_template("error.html", message="Group not found")
            return render_template("result.html", kind="group", group=grp)

    if keyword:
        if entity_type == "user":
            users = user_service.get_by_keyword(keyword)
            if not users:
                return render_template("error.html", message="User not found")
            # para cada usuario, obtener grupos
            users_with_groups = []
            all_groups = group_service.get_all()
            for u in users:
                u_groups = [g for g in all_groups if u["id"] in g.get("members",[])]
                users_with_groups.append({"user": u, "groups": u_groups})
            return render_template("result.html", kind="user_list", users=users_with_groups)
        else:
            groups = group_service.get_by_keyword(keyword)
            if not groups:
                return render_template("error.html", message="Group not found")
            return render_template("result.html", kind="group_list", groups=groups)

    return render_template("error.html", message="No search criteria provided")
