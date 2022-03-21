def div(a,b):
	if a<b:
		a,b = b,a
	print(a/b)

div(4,2)
#want extra condition always greater divide by lesser
#dont want to change div code
#add extra feature using decorator.

def smart_div(func):
	def inner(a,b):
		if a <b:
			a,b = b,a
		return func(a,b)
	return inner

div = smart_div(div)