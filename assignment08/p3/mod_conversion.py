# CTMS-14
# a8 p3.py
# Ahmed Abasimel
# aabasimel@constructor.university

def in2cm_table(start: float, end: float, step: float) -> None:
    length = start
    while length <= end:
        cm = length * 2.54
        print(f"{length:<10.1f}{cm:<10.1f}")
        length += step
