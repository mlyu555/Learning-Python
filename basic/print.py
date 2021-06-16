from pprint import pp, saferepr, isrecursive, isreadable

mylist = ["Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.", "Complex is better than complicated."]
print(mylist)
print("---------- pprint -------------")
pp(mylist)
print("---------- pprint缩进(默认1) -------------")
pp(mylist, indent=4)


mydict = {'students': [{'name':'Tom', 'age': 18},{'name':'Jerry', 'age': 19}]}
print(mydict)
print("---------- pprint -------------")
pp(mydict)
print("---------- pprint行宽(默认80，不超长与print等同) -------------")
pp(mydict, width=20)
pp(mydict, width=70)


newlist = [1, [2, [3, [4, [5]]]]]
print("---------- pprint层级(默认全层级) -------------")
pp(newlist, depth=3)


newlist = [1, 2]
newlist.insert(0, newlist)
print(newlist)
pp(newlist)
pp(saferepr(newlist))
pp(isrecursive(newlist))
pp(isreadable(newlist))