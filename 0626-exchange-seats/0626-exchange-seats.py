import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat["student"] = seat["student"].where(
        (seat["id"] % 2 == 0) | (seat["id"] == len(seat)),
        seat["student"].shift(-1)
    ).where(
        (seat["id"] % 2 == 1),
        seat["student"].shift(1)
    )

    return seat