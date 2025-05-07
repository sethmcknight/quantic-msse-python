from typing import List, Optional

# This code takes a list of pulse rates and converts them to a new scale.

# example pulse rates
rates = [17, 21, 180, 24]

# Initialize an empty list to store the converted rates using List[Optional[int]] to allow for None values
converted_rates: List[Optional[int]] = []

# Iterate through the pulse rates and convert them
# to a new scale if they are within the specified range``
for rate in rates:
    if rate >= 15 and rate <= 25:
        converted_rates.append(rate * 4)
    else:
        converted_rates.append(None)
    
print(converted_rates)