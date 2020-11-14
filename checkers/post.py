# -*- coding: utf-8 -*-
def post_params_check(content):
    if type(content) is not dict:
        return 'title', False

    title = content.get('title', None)

    if type(title) is not str:
        return 'title', False

    if len(title) < 1 or len(title) > 64:
        return 'title', False

    post_conent = content.get('content', None)

    if type(post_conent) is not str:
        return 'content', False

    if len(post_conent) < 15 or len(post_conent) > 256:
        return 'content', False

    return "ok", True
