import dill

with open("functions.bin", "rb") as f:
    functions_binary = dill.load(f)

functions = []

for f in functions_binary:
    func = dill.loads(f)
    functions.append(func)