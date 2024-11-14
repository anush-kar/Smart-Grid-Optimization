import numpy as np

class SmartGrid:
    def __init__(self, num_states, num_actions, discount_factor):
        self.num_states = num_states
        self.num_actions = num_actions
        self.discount_factor = discount_factor
        self.value_function = np.zeros(num_states)

    def transition_probability(self, state, action):
        # Simplified example with probabilities for different actions
        if action == 0:
            return 0.8
        elif action == 1:
            return 0.2
        else:
            return 1.0 / self.num_states

    def reward(self, state, action):
        if action == 0:
            return 10  # High reward for stabilizing
        elif action == 1:
            return -10  # Penalty for destabilizing
        else:
            return 0  # Neutral reward

    def value_iteration(self, max_iterations=100, threshold=0.001, max_value=1000):
        for _ in range(max_iterations):
            delta = 0
            for state in range(self.num_states):
                old_value = self.value_function[state]
                
                # Compute the new value, with clamping to avoid overflow
                new_value = max(
                    sum(
                        self.transition_probability(state, action) *
                        (self.reward(state, action) + self.discount_factor * self.value_function[next_state])
                        for next_state in range(self.num_states)
                    )
                    for action in range(self.num_actions)
                )

                # Clamp the new value to avoid overflow issues
                new_value = np.clip(new_value, -max_value, max_value)

                # Update the value function and calculate the difference (delta)
                self.value_function[state] = new_value
                delta = max(delta, abs(old_value - new_value))

            # If the change (delta) is below the threshold, we consider it converged
            if delta < threshold:
                break

    def get_optimal_policy(self):
        policy = np.zeros(self.num_states, dtype=int)
        for state in range(self.num_states):
            policy[state] = max(
                range(self.num_actions),
                key=lambda action: sum(
                    self.transition_probability(state, action) *
                    (self.reward(state, action) + self.discount_factor * self.value_function[next_state])
                    for next_state in range(self.num_states)
                )
            )
        return policy

if __name__ == '__main__':
    # Example grid with 10 states, 3 actions, and a discount factor of 0.9
    grid = SmartGrid(num_states=10, num_actions=3, discount_factor=0.9)
    # Perform value iteration to calculate the optimal value function
    grid.value_iteration()
    # Retrieve the optimal policy for the grid
    optimal_policy = grid.get_optimal_policy()
    # Print the optimal policy
    print("Optimal Policy:", optimal_policy)
    # Print the value function
    print("Value function:", grid.value_function)