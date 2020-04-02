class ArgList:
	def __init__(self, *args):
		assert len(args) % 2 == 0
		self.params = args

	def __str__(self):
		return ", ".join([" ".join(var) for var in self.params])

	@staticmethod
	def anonymous(*types):
		argnames = []
		for typename in types:
			argnames.append(argnameByType(typename))

		return ArgList(*zip(types, argnames))

	@staticmethod
	def fromDict(**kwargs):
		params = []
		for argname, typename in kwargs:
			params.append((typename, argname))

		return ArgList(*params)

class Signature:
	def __init__(self, ret_type, arglist):
		self.ret_type = ret_type
		self.arglist = arglist

	def __str__(self):
		return "{} {{}}({})".format(self.ret_type, str(self.arglist))

	@staticmethod
	def main():
		return Signature("void", ArgList(("int", "argc"), ("char**", "argv")))

class Method:
	def __init__(self, name, signature):
		self.name = name
		self.signature = signature

	def __str__(self):
		return str(self.signature).format(self.name)

class ClassMethod:
	def __init__(self, prot, name, signature):
		self.prot = prot
		self.method = Method(name, signature)

	def __str__(self):
		return str(self.method)