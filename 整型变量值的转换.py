a = 10
b = 110

print('int before swap a:{},b:{}'.format(a,b))
print('binary before swap a:{},b:{}'.format(bin(a),bin(b)))
a = a ^ b
b = a ^ b
a = a ^ b
print('binary after swap a:{},b:{}'.format(bin(a),bin(b)))
print('int after swap a:{},b:{}'.format(a,b))

#位运算符

a = bin(100)
