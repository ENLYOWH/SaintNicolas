import math

k = 8.99 * 10**9
e = 1.6 * 10**-19

n1 = int(input("q1 : "))
n2 = int(input("q2 : "))
r_input = input("d: ")

try:
  r = float(r_input.replace('^', 'e').replace('**', '**'))
except ValueError:
  r = eval(r_input.replace('^', 'e').replace('**', '**'))

q1 = n1 * e
q2 = n2 * e
force = k * q1 * q2 / r**2

print("Fe = {:.6e} N".format(force))
