import math, time
from sympy.interactive import init_printing
import sympy as sp
import numpy as np


def function_parser(s):						# Converting input to differentiable and integrable form
	s=s.replace('sqrt','sp.sqrt').replace('e^','exp')
	s=s.replace('sin','sp.sin').replace('asp.sin','sp.asin')
	s=s.replace('csc','sp.csc').replace('asp.csc','sp.acsc')
	s=s.replace('cos','sp.cos').replace('asp.cos','sp.cos')
	s=s.replace('sec','sp.sec').replace('asp.sec','sp.sec')
	s=s.replace('tan','sp.tan').replace('asp.tan','sp.atan')
	s=s.replace('cot','sp.cot').replace('asp.cot','sp.acot')
	s=s.replace('log', 'sp.log').replace('abs', 'sp.Abs').replace('^','**')

	return eval(s)

def mathematical_parser(s,output=None):
	s=s.replace('d', '*(pi)/180')
	s=s.replace('pi', 'math.pi').replace('e','math.e').replace('^','**')
	s=s.replace('sqrt','math.sqrt').replace('pow', 'math.pow')
	s=s.replace('sin','math.sin').replace('amath.sin','math.asin')
	s=s.replace('cos','math.cos').replace('amath.cos','math.cos')
	s=s.replace('tan','math.tan').replace('amath.tan','math.atan')
	s=s.replace('log', 'math.log').replace('abs', 'math.abs')
	s=s.replace('C', 'math.comb').replace('P','math.perm')
	s=s.replace('ans', '{}'.format(output))
	
	return s

def parser_value(s,output=None):
	return eval(mathematical_parser(s,output))

def soln_parser(s):
	s=s.replace('\/`','√').replace('*',' × ')
	s=s.replace('e^', '𝓮^').replace('x','𝓍').replace('y','𝓎').replace('z','𝔃').replace('f','𝓯').replace('g','𝓰')

	return s

def anti_parser(s):
	s=s.replace(',',' =').replace('sqrt','\/`').replace('**','^')
	s=s.replace('exp', 'e^') 

	return s

def graph_function_parser(s):						# Converting input to differentiable and integrable form
	s=s.replace('sqrt','np.sqrt').replace('e^','(np.e)**').replace("pi","np.pi")
	s=s.replace('sin','np.sin').replace('anp.sin','np.asin')
	s=s.replace('csc','1/np.sin').replace('a1/np.sin','1/np.asin')
	s=s.replace('cos','np.cos').replace('anp.cos','np.cos')
	s=s.replace('sec','1/np.cos').replace('a1/np.cos','1/np.acos')
	s=s.replace('tan','np.tan').replace('anp.tan','np.atan')
	s=s.replace('cot','1/np.tan').replace('a1/np.tan','1/np.atan')
	s=s.replace('log', 'np.log').replace('abs', 'np.abs').replace('^','**')

	return (s)

def cursive():
    cursive='c𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩 𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃 𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵 𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏 '
    return cursive

s=input()
print(mathematical_parser(s))
print(parser_value(s))
print(anti_parser(s))
