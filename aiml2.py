def reflex_vacuum_agent(location,status):
    if status =="Dirty":
        return "Suck"
    elif location =="A":
        return "right"
    elif location=="B":
        return "left"
    
location ="A"
status= "Dirty"

#location =["A","B"]


action = reflex_vacuum_agent(location,status)
print(f"location :{location},Status:{status},Action :{action}")

