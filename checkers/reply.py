# -*- coding: utf-8 -*-
def reply_post_params_check(content):
    if type(content) is not dict:
        return 'content', False

    reply_content = content.get('content', None)

    if type(reply_content) is not str:
        return 'content', False

    if len(reply_content) < 15 or len(reply_content) > 256:
        return 'content', False

    reply_id = content.get('replyId', 0)

    if type(reply_id) is not int:
        return 'replyId', False

    if reply_id < 0:
        return 'replyId', False

    return "ok", True
