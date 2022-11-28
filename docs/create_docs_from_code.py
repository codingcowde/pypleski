import pypleski.core
import inspect

def print_class_methods(cl):
    print(cl.__name__)
    print(cl.__doc__)
    for function in dir(cl):
        if "__" not in function:
            word = f"pypleski.core.{cl.__name__}.{function}.__doc__"
            
            doc = ""
            try:
                doc = str(eval(word))
            except Exception as e:
                doc = f"{e}"
            print(f"{cl.__name__}.{function}()")
            print(doc)


###

print_class_methods(pypleski.core.PleskApiClient)
print_class_methods(pypleski.core.PleskApiClientDummy)
print_class_methods(pypleski.core.PleskRequestPacket)
print_class_methods(pypleski.core.PleskResponsePacket)
