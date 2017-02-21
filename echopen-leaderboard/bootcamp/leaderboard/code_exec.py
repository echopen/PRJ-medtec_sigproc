import ast
import pip 

def execute_user_script(file_list):
    f = open("uploaded_custom.py", "r")
    data = f.read()

    tree = ast.parse(data)
    # tree.body[0] contains FunctionDef for fun1, tree.body[1] for fun2

    str_func = ""
    run_func = ""
    for function in tree.body:
        if isinstance(function,ast.FunctionDef):
            # Just in case if there are loops in the definition
            lastBody = function.body[-1]
            while isinstance (lastBody,(ast.For,ast.While,ast.If)):
                lastBody = lastBody.Body[-1]
            lastLine = lastBody.lineno
            if function.name == 'install_packages' :
                st = data.split("\n")
                for i , line in enumerate(st,1):
                    if i in range(function.lineno,lastLine+1):
                        str_func = str_func +'\n'+ line
                print str_func


            elif function.name == 'run':
                st = data.split("\n")
                for i , line in enumerate(st,1):
                    if i in range(function.lineno,lastLine+1):
                        run_func = run_func +'\n'+ line
                print run_func



    exec str_func
    exec run_func
    import time

    install_packages()
    start = time.clock()
    for i in file_list :
        run(i)
    end = time.clock()
    return (end - start)
