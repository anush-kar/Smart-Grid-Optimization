import numpy as np

def optimize_energy_schedule(demand, costs, max_storage, efficiency, max_supply, T):
    """
    Optimizes the energy schedule over a given time horizon.
    
    Parameters:
    - demand: List of energy demands at each time period
    - costs: Dictionary containing the cost per unit of each source (e.g., 'renewable', 'grid', 'storage')
    - max_storage: Maximum storage capacity (in energy units)
    - efficiency: Efficiency factor for charging/discharging storage (0 < efficiency <= 1)
    - max_supply: Maximum supply that can be purchased or generated per source
    - T: Number of time periods
    
    Returns:
    - min_cost: The minimum achievable cost to satisfy demand over all periods
    - schedule: The optimal schedule showing usage from each source per time period
    """

    # Initialize DP table: dp[t][s] is the minimum cost at time t with storage level s
    dp = np.full((T+1, max_storage+1), float('inf'))
    dp[0][0] = 0  # No cost at time 0 with zero storage

    # Backtrack table to trace the schedule
    schedule = [[None] * (max_storage + 1) for _ in range(T+1)]

    # Populate the DP table
    for t in range(1, T+1):
        for s in range(max_storage+1):  # s is the storage level at the beginning of time t
            # Calculate demand to fulfill
            current_demand = demand[t-1]

            # Option 1: Use renewable source if within supply limits
            if current_demand <= max_supply['renewable']:
                renewable_cost = current_demand * costs['renewable']
                if dp[t-1][s] + renewable_cost < dp[t][s]:
                    dp[t][s] = dp[t-1][s] + renewable_cost
                    schedule[t][s] = ('renewable', current_demand)

            # Option 2: Use grid power if within supply limits
            if current_demand <= max_supply['grid']:
                grid_cost = current_demand * costs['grid']
                if dp[t-1][s] + grid_cost < dp[t][s]:
                    dp[t][s] = dp[t-1][s] + grid_cost
                    schedule[t][s] = ('grid', current_demand)

            # Option 3: Use storage if enough is stored
            if s >= current_demand:
                storage_cost = current_demand * costs['storage']
                if dp[t-1][s - int(current_demand / efficiency)] + storage_cost < dp[t][s]:
                    dp[t][s] = dp[t-1][s - int(current_demand / efficiency)] + storage_cost
                    schedule[t][s] = ('storage', current_demand)

            # Option 4: Charge storage with excess renewable or grid power (if storage has capacity)
            if s < max_storage:
                charge_amount = min(max_storage - s, max_supply['renewable'])
                charge_cost = charge_amount * costs['renewable']
                if dp[t-1][s] + charge_cost < dp[t][s + int(charge_amount * efficiency)]:
                    dp[t][s + int(charge_amount * efficiency)] = dp[t-1][s] + charge_cost
                    schedule[t][s + int(charge_amount * efficiency)] = ('charge_renewable', charge_amount)

    # Find the optimal cost and retrieve schedule
    min_cost = min(dp[T])
    best_storage_level = np.argmin(dp[T])
    final_schedule = []

    for t in range(T, 0, -1):
        if schedule[t][best_storage_level] is None:
            # If no action was assigned for this state, skip (or use default)
            continue
        action, amount = schedule[t][best_storage_level]
        final_schedule.append((t, action, amount))
        if action == 'storage':
            best_storage_level += int(amount / efficiency)  # Update storage based on use

    final_schedule.reverse()  # Order schedule by time

    return min_cost, final_schedule

# Example usage:
demand = [30, 20, 25, 35, 45, 20, 10, 40, 30, 25, 15, 35]  # Demand per time slot
costs = {
    'renewable': 0.05,  # Cost per unit from renewable
    'grid': 0.10,       # Cost per unit from grid
    'storage': 0.02     # Cost per unit from storage
}
max_storage = 100  # Maximum storage capacity
efficiency = 0.9   # Efficiency of storage
max_supply = {
    'renewable': 50,    # Max renewable supply per slot
    'grid': 50          # Max grid supply per slot
}
T = len(demand)        # Time periods (length of demand array)

# Compute optimal schedule
min_cost, optimal_schedule = optimize_energy_schedule(demand, costs, max_storage, efficiency, max_supply, T)

print(f"Minimum cost: {min_cost}")
print("Optimal schedule:")
for time, action, amount in optimal_schedule:
    print(f"Time {time}: Use {action} for {amount} units")
