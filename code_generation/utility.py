def camelCaseSplit(string):
	return re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', string)).split()

def toSnakeCase(lst):
	return "_".join(lst).lower()

def argnameByType(typename):
	return toSnakeCase(camelCaseSplit(typename))