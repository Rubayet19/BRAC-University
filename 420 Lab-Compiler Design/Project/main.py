def infix_to_postfix(infix):
    operators = {"|": 1, ".": 2, "*": 3, "(": 4, ")": 4}
    tokens = []
    i = 0
    while i < len(infix):
        if infix[i].isdigit() or infix[i].isalpha():

            j = i + 1
            while j < len(infix) and (infix[j].isdigit() or infix[j].isalpha()):
                j += 1
            tokens.append(infix[i:j])
            i = j
        else:

            tokens.append(infix[i])
            i += 1

    output = ""
    opstack = []
    for token in tokens:
        if token.isdigit() or token.isalpha() or token == '#':

            output += token
        elif token == "(":

            opstack.append(token)
        elif token == ")":

            while opstack and opstack[-1] != "(":
                output += opstack.pop()
            if opstack and opstack[-1] == "(":
                opstack.pop()
        else:
            while opstack and opstack[-1] != "(" and operators[token] <= operators[opstack[-1]]:
                output += opstack.pop()
            opstack.append(token)

    while opstack:
        output += opstack.pop()

    return output

regex = "(a|b)*.a.b.b"
regex = regex + ".#"

#"ab|*ac.*|#."
postfix = infix_to_postfix(regex)



class Node:
    def __init__(self, value, left=None, right=None, parent = None, num=None):
        self.value = value
        self.left = left
        self.right = right
        self.first_pos = set()
        self.last_pos = set()
        self.nullable = False
        self.parent = parent
        self.num = num

def position(regex):
    stack = []
    output = []
    leaf = []
    count = 1
    for i in regex:
        if i.isalpha() or i == '#':
            node1 = Node(value=i, num=count)
            node1.first_pos.add(count)
            node1.last_pos.add(count)
            leaf.append(node1)
            stack.append(node1)
            count += 1
        elif i == '|' or i == '.':
            newNode = Node(value=i)
            a = stack.pop()
            b = stack.pop()
            if i == "|":
                newNode.nullable = False
                if a.nullable or b.nullable:
                    newNode.nullable = True
                newNode.first_pos = a.first_pos|b.first_pos
                newNode.last_pos  = a.last_pos|b.last_pos
            else:
                if b.nullable and a.nullable:
                    newNode.nullable = True
                if b.nullable == True:
                    newNode.first_pos = a.first_pos|b.first_pos
                    newNode.last_pos = a.last_pos
                if b.nullable!= True:
                    newNode.first_pos = b.first_pos
                    newNode.last_pos = a.last_pos

            newNode.right = a
            newNode.left = b
            stack.append(newNode)
            output.append(newNode)
        elif i == '*':
            a = stack.pop()
            newNode = Node(value = i, left=a)
            newNode.nullable = True
            newNode.first_pos = a.first_pos
            newNode.last_pos = a.last_pos
            stack.append(newNode)
            output.append(newNode)
        else:
            output.append(Node(value = i))
    return output, leaf

val = position(postfix)

def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    if node.num:
        print(f"{'  ' }Num: {node.num}")
        print(f"{'  ' }Value: {node.value}")
    else:
        print(f"{'  '}Parent Value: {node.value}")
    print(f"{'  ' }First Pos: {node.first_pos}")
    print(f"{'  ' }Last Pos: {node.last_pos}")
    print_tree(node.right)



root_node = val[0][-1]
print_tree(root_node)


