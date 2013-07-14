# -*- encoding: utf-8 -*-

import re
EMAIL_REGX = '^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$'


def is_email_valid(email=None):
    ''' email validator '''
    if email is None and not isinstance(email, basestring):
        return False
    else:
        return bool(re.match(EMAIL_REGX, email))
