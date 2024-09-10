global_variable = 30

def outer_function():
    outer_variable = 10

    def inner_function():
        #nonlocal outer_variable
        global_variable = 30
        inner_variable = 20
        print("inner_variable: ", inner_variable)
        #print("outer_variable from inner function:", outer_variable)
        print("Global variable from inner function", global_variable)

        #change the outer_variable
        outer_variable = -99
        print("outer_variable from inner function:", outer_variable)

        #change global
        global_variable = 777
        print("Global variable from inner function #2", global_variable)
    inner_function()
    print("outer variable from outer function:", outer_variable)
    #nonlocal global_variable
    print("Global variable from outer function", global_variable)
outer_function()

