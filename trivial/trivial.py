env = {
        'x': 3,
        'y': 4,
        '+': lambda v, e: sum(v),
        '-': lambda v, e: v[0] - v[1],
        '*': lambda v, e: v[0] * v[1],
        '/': lambda v, e: v[0] / v[1],
        'print': lambda v, e: print(v),
    }

# Try implementing the following:
# ['begin', [...], e]
# ['if', [BOOL_EXP], ['begin', [...], e], e]

def begin(v, e):
    if type(v) is list:
        if len(v) == 0:
            return None
        
        for i in v[:]:
            evaluate(v[i:], e)
    if type(v) is str:
        return resolve(v, e)
    return v

def If(b, v, e):
    

    return

def resolve_Bool(v, e):


    return


def resolve(s, e):
    #return e.get(s, None)
    if s in e:
        return e[s]
    else:
        return None

def set_statement(v, e):
    assert len(v) == 3
    assert v[0] == "set"
    assert type(v[1]) is str
    e[v[1]] = evaluate(v[2], e)
    return None

def evaluate(v, e):
    if type(v) is list:
        if len(v) == 0:
            return None
        assert type(v[0]) is str
        if v[0] == "set":
            return set_statement(v, e)
        # if v[0] == "set":
        #     return set_statement(v, e)
        
        f = resolve(v[0], e)
        assert callable(f)
        values = [evaluate(value, e) for value in v[1:]]
        # Expression called a "Comprehension" ^^^
        return f(values, e)
    if type(v) is str:
        return resolve(v, e)
    return v

def test_evaluate():
    print("test_evaluate")
    assert evaluate(1, env) == 1
    assert evaluate(1.2, env) == 1.2
    assert evaluate('x', env) == 3
    assert evaluate(['+', 11, 22], env) == 33
    assert evaluate(['+', ['+', 11, 22], 22], env) == 55
    assert evaluate(['-', 33, 22], env) == 11
    assert evaluate(['*', 10, 22], env) == 220
    assert evaluate(['/', 220, 10], env) == 22
    assert evaluate(['set', 'q', 7], env) == None
    assert env['q'] == 7
    assert evaluate(['set', 'q', 77], env) == None
    assert env['q'] == 77
    assert evaluate(['set', 'q', ['+', 5, 6]], env) == None
    assert env['q'] == 11
    evaluate(['print', 2, 3, 4], env)
    begin(['print', ['set', 'x', ['+', 10, 15]], env], ], env)

def test_resolve():
    print("test_resolve")
    assert resolve('x', env) == 3
    assert resolve('y', env) == 4

if __name__ == "__main__":
    test_evaluate()
    test_resolve()
    print("Done")
