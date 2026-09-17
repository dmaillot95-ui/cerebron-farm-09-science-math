import json, os, sys
from pathlib import Path
from gradio_client import Client

role=os.environ['ROLE']; model=os.environ['MODEL']; family=os.environ['FAMILY']
mission=Path('mission/SCIENCE-MATH-MISSION.md').read_text(encoding='utf-8')
prompt=f"""{mission}\n\nROLE: {role}\nMODEL FAMILY: {family}\nPerform your role rigorously. Do not claim theorem status without a complete argument. Distinguish proof, heuristic, experiment and conjecture. Return concise markdown with STATUS and NEXT DECISIVE STEP."""
result={'role':role,'model':model,'family':family,'success':False,'output':'','error':None}
try:
    c=Client(model)
    out=c.predict(message=prompt, api_name='/chat')
    result['success']=True; result['output']=str(out)
except Exception as e:
    result['error']=repr(e)
Path('results').mkdir(exist_ok=True)
Path(f"results/{role}.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'role':role,'success':result['success'],'family':family}))
