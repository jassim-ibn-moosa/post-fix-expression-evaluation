def get_post_expr():
    print "Enter the post fix expression"
    post_expr = raw_input()
    return post_expr

def scan_expression(post_expr,operator,operand,i):
    if post_expr[i] in operator:
        operator = post_expr[i]
        return operator
    else:
        operand = post_expr[i]
        return operand

def push(operand,stk):
    stk.append(operand)
    return stk

def pop(stk):
    return stk.pop()

def evaluate(operator,operand1,operand2,stk):
    if operator == '+':
        res = operand1 + operand2
    elif operator == '-':
        res = operand1 - operand2
    elif operator == '*':
        res = operand1 * operand2
    elif operator == '/':
        res = operand1 / operand2
    return res

def main():
    stk = []
    post_expr = get_post_expr()
    operators = ['+','-','*','/']
    operand = [1,2,3,4,5,6,7,8,9,0]
    for i in range(len(post_expr)):
        scan_expr = scan_expression(post_expr,operators,operand,i)
        stk = map(int, stk)
        if scan_expr in operators:
            operator = scan_expr
            operand2 = pop(stk)
            operand1 = pop(stk)
            res = evaluate(operator,operand1,operand2,stk)
            push(res,stk)
        else:
            stk = push(scan_expr,stk)
    print 'Result = {}'.format(stk)
        
if __name__ == '__main__':
    main()
