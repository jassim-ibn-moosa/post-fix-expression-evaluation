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
