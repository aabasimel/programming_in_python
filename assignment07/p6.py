# CTMS-14
# a7 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university


def key_with_min_value(d):
    if not d:  # handle empty dictionary
        return None
    return min(d, key=d.get)

sampleDict = {
    'Physics': 82,
    'Math': 85,
    'History': 75,
    'Management': 70,
    'Chemistry': 72
}

min_key = key_with_min_value(sampleDict)
print(f"The subject with the minimum score is: {min_key}")
