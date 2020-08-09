def calculator(operation,a,b):
    if(operation == '+'):
        return a+b;
    elif(operation == '-'):
        return a-b;
    elif operation == '*':
        return a*b;
    elif operation == '/':
        if b > 0:
            return a/b;
        else: 
            return "b should not zero";
    else:
        return "Operation not found!!"

a = 4;
b = 5;
print("sum of {} + {} = {} ".format(a,b,calculator('+',a,b)));
# print("sum of %d + %d = %f",%a,%b,%calculator('+',a,b));
print(calculator('-',a,b));
print(calculator('*',a,b));
print(calculator('/',a,b));
print(calculator('/',a,b));