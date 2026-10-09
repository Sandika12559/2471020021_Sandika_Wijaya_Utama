x = "global" 
def tes(): 
    x = "lokal"     # hanya di dalam tes()
    print(x)        # lokal
tes() 
print(x)            ## global