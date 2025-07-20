import dill

from langchain_core.tools import StructuredTool

with open("functions.bin", "rb") as f:
    functions = dill.load(f)

tools = []

for f in functions:
    func = dill.loads(f)
    tool = StructuredTool.from_function(func = func)
    tools.append(tool)