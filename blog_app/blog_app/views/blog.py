from pyramid.view import view_config


@view_config(route_name='blog',
             renderer='blog_app:templates/view_blog.jinja2')
def blog_view(request):
    return {}


@view_config(route_name='blog_action', match_param='action=create',
             renderer='blog_app:templates/edit_blog.jinja2')
def blog_create(request):
    return {}


@view_config(route_name='blog_action', match_param='action=edit',
             renderer='blog_app:templates/edit_blog.jinja2')
def blog_update(request):
    return {}