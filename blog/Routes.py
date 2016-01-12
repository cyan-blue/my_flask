#HERE YOU CAN EDIT THE ROUTES (the urls) for the app. 
#With this config you can only have 1 route per view.
#To avoid this you can manually edit the file blog.py.


index = "/"

show_page = "/page/<int:page>/"    #<int:page> required in the url
#show_page = "/<int:page>/" for example

view_post_only_id = "/post/<int:post_id>/" #<int:post_id> required in the url
view_post = "/post/<int:post_id>/<post_url>/"  #<int:post_id> & <post_url> are required in the url
view_tag = "/tag/<tag>"


admin_login = "/admin/login"
admin_logout = "/admin/logout"
admin_panel = "/admin/"
admin_add_post = "/admin/add/"
admin_edit_post = "/admin/edit/<int:post_id>"
admin_delete_post = "/admin/delete/<int:post_id>/" #<int:post_id> required in the url


#API

api_get_page = "/api/page/<int:page>"
api_get_post = "/api/post/<int:post_id>"
api_get_post_with_tag = "/api/tag/<tag>"