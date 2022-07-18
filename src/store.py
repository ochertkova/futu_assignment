deps = [{"name" : "testideppi",
         "deps" : ["toinendeppi", "ulkoinen_deppi"]},   
        {"name" : "toinendeppi",
         "deps" : ["toinendeppi", "ulkoinen_deppi"]}]      

def find_dep(dep_name):
    for dep in deps:
        if dep["name"] == dep_name:
            return dep
 