from sourcemap_trace import trace
import json
m={'version':3,'sources':['demo.js'],'names':[],'mappings':'AAAA,KACE'};r=trace(m,1,6);assert r['line']==2 and r['column']==2;print(json.dumps(r))
