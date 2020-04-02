#!/usr/bin/python3

import re
from enum import Enum
import json

from classes import *
from utility import *

base_visitor = 'Visitor'

rule_header_template = """#pragma once
#include "{base_class}.h"

class {class_name} : public {base_class} {{
 public:
  {class_name}();
  int eval() const override;
  void Accept(Visitor* visitor) override;

private:

}}
"""

rule_impl_template = """#include "{class_name}.h"

{class_name}::{class_name}() {{
}}
  
}}

int {class_name}::eval() const {{
  
}}

void {class_name}::Accept(Visitor* visitor) {{
    visitor->Visit(this);
}}
"""

visitor_header_template = """#pragma once
#include "{base_class}.h"

class {class_name} : public {base_class} {{
 public:
  {class_name}();

{visit_decl}
 private:
  
}};
"""

visitor_impl_template = """#include "{class_name}.h"

{class_name}::{class_name}() {{
  
}}

{visit_def}

"""

visit_method_decl_template = "  void Visit({} {}) override;\n"

visit_method_def_template = """void {}::Visit({} {}) {{
  
}}

"""

def VisitorHeader(base_class, class_name, rules):
	return visitor_header_template.format(base_class = base_visitor, 
									  	  class_name = class_name, 
									  	  visit_decl = DeclareVisits(EachRule(rules)))

def VisitorSource(base_class, class_name, rules):
	return visitor_impl_template.format(class_name = class_name, 
										visit_def = DefineVisits(EachRule(rules), class_name))

def EachRule(rules):
	return [(Pointer(argtype), "that") for argtype in rules]

def Pointer(argtype):
	return argtype + "*"

def DeclareVisits(params):
	output = ""

	for argtype, argname in params:
		output += visit_method_decl_template.format(argtype, argname)

	return output

def DefineVisits(params, class_name):
	output = ""
	for argtype, argname in params:
		output += visit_method_def_template.format(class_name, argtype, argname)
	return output

def Write(text, filepath):
	with open(filepath, "w+") as file:
		file.write(text)

def GetClassPaths(directory, class_name):
	return "{}/{}.h".format(directory, class_name), "{}/{}.cpp".format(directory, class_name)

def MakeVisitor(class_name, directory, rules):
	base_class = base_visitor
	header_path, source_path = GetClassPaths(directory, class_name)

	header = VisitorHeader(base_class, class_name, rules)
	source = VisitorSource(base_class, class_name, rules)
	Write(header, header_path)
	Write(source, source_path)

def MakeRule(class_name, directory, )

class ClassData:
	def __init__(self, path):
		self.data = self.read_data(path)

	def read_data(self, path):
		parsed = None
		with open(path, "r") as file:
			parsed = json.loads(file.read())
		return parsed

	def __getitem__(self, key):
		return self.data[key]

class Generator:
	def __init__(self, class_data):
		self.class_data = class_data
		self.rules = class_data["Rules"]
		self.visitors = class_data["Visitors"]

	def spawn_visitors(self, dir):
		for visitor in self.visitors:
			MakeVisitor(visitor, dir, self.rules)

	def spawn_rules(self, dir):
		for rule in self.rules:









