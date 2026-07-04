import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    lim = (len(seat) // 2) * 2

    for i in range(0, lim, 2):
        temp = seat.at[i, "student"]
        seat.at[i, "student"] = seat.at[i+1, "student"]
        seat.at[i+1, "student"] = temp
    
    return seat