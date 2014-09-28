import os

for f in os.listdir("."):
    if not f.endswith(".py"):
	    os.rename(f, "MY" + f)
    os.mkdir(f + "_dir")