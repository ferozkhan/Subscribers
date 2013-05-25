# -*- encoding: utf-8 -*-

from module.validator import email
from nose.tools import raises, assert_true, assert_false


def test_pass_email_validation():
    ''' validation test for email: xyz@mail.com, assert True '''
    assert_true(email('xyz@mail.com'))


def test_fail_email_validation_1():
    ''' validation test for email: xyz, assert False '''
    assert_false(email('xyz'))


def test_fail_email_validation_2():
    ''' validation test for email: xyz@d.s.s.s, assert False '''
    assert_false(email('xyz@d.s.s.s'))


def test_fail_email_validation_3():
    ''' validation test for email: xyz@d, assert False '''
    assert_false(email('xyz@d'))


def test_fail_email_validation_4():
    ''' validation test for email: mail.com, assert False '''
    assert_false(email('mail.com'))


@raises(TypeError)
def test_raise_typeerr_if_email_is_not_stirng():
    ''' validation test for email: 123:integer, raises TypeError '''
    email(123)


@raises(ValueError)
def test_raise_valueerr_if_email_empty():
    ''' validation test for email: None, raises ValueError '''
    email('')
