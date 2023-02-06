
# push
# pop
# MAXSIZE 10
# TOP = -1


def make_stack():
    st = []
    return st

# empty
def is_empty(st):
    return len(st) == 0
    # return TOP == -1

#push
def push(st, value):
    st.append(value)

#pop
def pop(st):
    if is_empty(st) :
        return "it's already empty"
    
    return st.pop();
    # del st[st.len()-1];
    # return st;


st = make_stack()
push(st, 'S')
push(st, 'T')
push(st, 'A')
push(st, 'C')
push(st, 'K')
print(st)
print(pop(st))
print(pop(st))
print(pop(st))
print(pop(st))
print(pop(st))
print(pop(st))
print(pop(st))