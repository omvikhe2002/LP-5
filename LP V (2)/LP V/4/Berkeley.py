# 4. Implement Berkeley algorithm for clock synchronization.

import time
import random

# Function to calculate the clock offset
def calculate_offset(remotes):
    local_time = time.time()
    offsets = [remote - local_time for remote in remotes]
    return sum(offsets) / len(offsets)

# Function to synchronize clocks using the Berkeley algorithm
def synchronize_clocks():
    num_peers = int(input("Enter the number of peers: "))
    local_time = time.time()
    
    # Simulate remote clocks with random offsets
    remote_times = [local_time + random.uniform(-1, 1) for _ in range(num_peers)]
    print("Local time:", local_time)
    print("Remote times:", remote_times)
    
    # Calculate the clock offset
    offset = calculate_offset(remote_times)
    
    # Adjust local clock
    adjusted_time = local_time + offset
    print("Adjusted local time:", adjusted_time)

# Execute the clock synchronization
synchronize_clocks()
