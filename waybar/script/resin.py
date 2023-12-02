import genshin
import asyncio
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["resin", "commission"], help="Pick which function to run")
args = parser.parse_args()

data = {}

def getResin(current_resin):
    data['text'] = current_resin
    if current_resin >= 150:
        data['class'] = "resinfull"
    print(json.dumps(data), flush=True)

def getCompletedCommission(completed_commissions):
    if not completed_commissions:
        data['text'] = "Do Daily Commission!"
        data['class'] = "nodaily"
    else:
        data['text'] = "Commission is done"
        data['class'] = "yesdaily"
        
    print(data, flush=True)

async def main():
    cookie = {"ltuid_v2": , "ltoken_v2": ""}
    while True:
        client = genshin.Client(cookie)
        notes = await client.get_genshin_notes(801401037)
        
        match args.type:
            case "resin":
                getResin(notes.current_resin)
            case "commission":
                getCompletedCommission(notes.completed_commissions)
        
        await asyncio.sleep(480)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(main())
    loop.run_forever()
except KeyboardInterrupt:
    pass
    loop.close()
