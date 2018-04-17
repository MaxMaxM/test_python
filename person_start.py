#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person():
    """docstring for Person"""
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.pay = pay
        self.age = age
        self.job = job

if __name__ == '__main__':
    bob = Person('Bob Smith', 43, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.lastName())
    sue.giveRaise(.10)
    print(sue.pay)


