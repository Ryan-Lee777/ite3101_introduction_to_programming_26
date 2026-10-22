def shut_down(s: str) -> str:
    if s == "yes":
        return "Shutting_down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
