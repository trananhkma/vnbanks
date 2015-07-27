# -*- coding: utf-8 -*-


class Bank(object):
    def __init__(self, name, **kwargs):
        self.name = name

    def deposite_rate(self):
        raise NotImplementedError

    def loan_rate(self):
        raise NotImplementedError


class Rate(object):
    def __init__(self, currency, **kwargs):
        self.currency = currency
        self.rates = {}
