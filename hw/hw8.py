#!/usr/bin/env python3

def recuts(x):
    slovar={'one':1,'One':1,'ONE':1,'two':2,'Two':2,'TWO':2,'three':'3','Three':'3','THREE':'3','four':'4','Four':'4','FOUR':'4','five':'5','Five':'5','FIVE':'5','six':'6','Six':'6','SIX':'6','seven':'7','Seven':'7','SEVEN':'7','eight':'8','Eight':'8','EIGHT':'8','nine':'9','Nine':'9','NINE':'9','ten':'10','Ten':'10','TEN':'10'}
    while True:
        try:
            if x=='cancel':
                print("Bye!")
                exit()
            if x=='one':
                print((int((slovar.get('one'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='One':
                print((int((slovar.get('One'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='ONE':
                print((int((slovar.get('ONE'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='two':
                print((int((slovar.get('two'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='Two':
                print((int((slovar.get('Two'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='TWO':
                print((int((slovar.get('TWO'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='three':
                print((int((slovar.get('three'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='Three':
                print((int((slovar.get('Three'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='THREE':
                print((int((slovar.get('THREE'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='four':
                print((int((slovar.get('four'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='Four':
                print((int((slovar.get('Four'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='FOUR':
                print((int((slovar.get('FOUR'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='five':
                print((int((slovar.get('five'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='Five':
                print((int((slovar.get('Five'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='FIVE':
                print((int((slovar.get('FIVE'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='six':
                print((int((slovar.get('six'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='Six':
                print((int((slovar.get('Six'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='SIX':
                print((int((slovar.get('SIX'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='seven':
                print((int((slovar.get('seven'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='Seven':
                print((int((slovar.get('Seven'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='SEVEN':
                print((int((slovar.get('SEVEN'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='eight':
                print((int((slovar.get('eight'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='Eight':
                print((int((slovar.get('Eight'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='EIGHT':
                print((int((slovar.get('EIGHT'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='nine':
                print((int((slovar.get('nine'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='Nine':
                print((int((slovar.get('Nine'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='NINE':
                print((int((slovar.get('NINE'))))*3+1)
                recuts(x=input("Enter you value: "))
            if x=='ten':
                print((int((slovar.get('ten'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='Ten':
                print((int((slovar.get('Ten'))))/2)
                recuts(x=input("Enter you value: "))
            if x=='TEN':
                print((int((slovar.get('TEN'))))/2)
                recuts(x=input("Enter you value: "))
            elif int(x)%2==0:
                print((int(x))/2)
                recuts(x=input("Enter your value: "))
            else:
                print((int(x)*3)+1)
                recuts(x=input("Enter your value: "))
        except ValueError:
            print("We can't convert this word to number")
            recuts(x=input("Enter you value: "))
recuts(x=input("Enter your value: "))
