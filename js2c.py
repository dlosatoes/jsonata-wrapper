#!/usr/bin/python3
import json
with open("jsonata-es5.min.js") as infil:
    indata = infil.read()
    with open("jsonata-es5.h","w") as outfil:
        outfil.write("#include <string>\n")
        outfil.write("const std::string JAVASCRIP_JSONATA_LIB =\n")
        chunklen = 80
        chunks = [indata[i:i+chunklen] for i in range(0, len(indata), chunklen)]
        escaped = [json.dumps(x) for x in chunks]
        for chunk in escaped:
            outfil.write("    " + chunk + "\n") 
        outfil.write("    \"\";\n")

