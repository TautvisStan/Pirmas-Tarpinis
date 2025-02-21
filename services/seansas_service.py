from datetime import datetime
def patikrinti_persidengima(seansas1, seansas2):
    latest_start = max(seansas1.pradzia, seansas2.pradzia)
    earliest_end = min(seansas1.pabaiga, seansas2.pabaiga)

    skritumas = (earliest_end - latest_start).total_seconds()
    overlap = max(0, skritumas)
    return overlap == 0


# >>> Range = namedtuple('Range', ['start', 'end'])

# >>> r1 = Range(start=datetime(2012, 1, 15), end=datetime(2012, 5, 10))
# >>> r2 = Range(start=datetime(2012, 3, 20), end=datetime(2012, 9, 15))
# >>> latest_start = max(r1.start, r2.start)
# >>> earliest_end = min(r1.end, r2.end)
# >>> delta = (earliest_end - latest_start).days + 1
# >>> overlap = max(0, delta)
# >>> overlap