import csv
from pathlib import Path
p=Path(__file__).parent
with (p/'tasks.csv').open() as f: tasks=list(csv.DictReader(f))
early={}; late={}
for t in tasks:
    deps=t['dependencies'].split(';') if t['dependencies'] else []
    s=max((early[d][1] for d in deps),default=0)
    early[t['id']]=(s,s+int(t['duration']))
finish=max(e for s,e in early.values())
for t in reversed(tasks):
    successors=[u['id'] for u in tasks if t['id'] in u['dependencies'].split(';')]
    late[t['id']]=min((late[u] for u in successors),default=finish)-int(t['duration'])
    assert late[t['id']]-early[t['id']][0]==int(t['float'])
bac=sum(float(t['budget']) for t in tasks)
pv=sum(float(t['budget'])*max(0,min(1,(12-early[t['id']][0])/int(t['duration']))) for t in tasks)
ev=sum(float(t['budget'])*float(t['progress']) for t in tasks)
ac=sum(float(t['actual']) for t in tasks)
cpi=ev/ac; spi=ev/pv; eac=bac/cpi
assert finish==24 and bac==2000000
for label,value in [('Duration',finish),('BAC',bac),('PV',pv),('EV',ev),('AC',ac),('CV',ev-ac),('SV',ev-pv),('CPI',cpi),('SPI',spi),('EAC',eac),('VAC',bac-eac)]: print(f'{label}: {value:,.3f}')
print('Critical activities:', ', '.join(t['id'] for t in tasks if late[t['id']]==early[t['id']][0]))
