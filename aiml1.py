
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Initial environment
location = "A"
status = "Dirty"

# Simulate agent actions for 5 iterations
for _ in range(5):
    action = reflex_vacuum_agent(location, status)
    print(f"Location: {location}, Status: {status}, Action: {action}")
    
    # Update environment based on action
    if action == "Suck":
        status = "Clean"
    elif action == "Right":
        location = "B"
        # assume new location B status (you can change)
        status = "Dirty"  # or "Clean" depending on scenario
    elif action == "Left":
        location = "A"
        status = "Dirty"  # or "Clean" depending on scenario