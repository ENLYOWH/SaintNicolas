import math

G = 6.67 * 10**-11

m1_input = input("m1: ")
m2_input = input("m2: ")
r_input = input("d: ")

try:
  r = float(r_input.replace('^', 'e').replace('**', '**'))
except ValueError:
  r = eval(r_input.replace('^', 'e').replace('**', '**'))

try:
  m1 = float(m1_input.replace('^', 'e').replace('**', '**'))
except ValueError:
  m1 = eval(m1_input.replace('^', 'e').replace('**', '**'))

try:
  m2 = float(m2_input.replace('^', 'e').replace('**', '**'))
except ValueError:
  m2 = eval(m2_input.replace('^', 'e').replace('**', '**'))

force = G * m1 * m2 / r**2

print("Fg = {:.6e} N".format(force))
