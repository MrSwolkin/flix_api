from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.method)
        print()
        model = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label
        print(model)
        print(app_label)

        # lógica da permissão
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return request.user.has_perm("genres.view_genre")

        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")

        if request.method in ["PATCH", "PUT"]:
            return request.user.has_perm("genres.change_genre")

        if request.method == "DELETE":
            return request.user.has_perm("genres.delete_genre")

        return False
