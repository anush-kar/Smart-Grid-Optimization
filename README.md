# Smart-Grid-Optimization
This code is an implementation of a dynamic programming algorithm for finding the optimal policy in a simplified smart grid environment. The code uses value iteration, a dynamic programming technique, to calculate the optimal value function and determine the best policy for each state.

### 1. Class and Initialization (SmartGrid):

The SmartGrid class is initialized with parameters: num_states, num_actions, and discount_factor.
num_states represents the number of possible states in the environment, while num_actions represents the possible actions.
discount_factor helps balance immediate vs. future rewards.
The class initializes value_function as a zero array representing the expected long-term reward of each state.

### 2. Transition Probability Function (transition_probability):

This function returns the probability of reaching a particular next state given a current state and action.
The probabilities vary based on actions, reflecting the likelihood of reaching different states depending on the action taken.

### 3. Reward Function (reward):

Returns the immediate reward associated with taking an action in a state.
For instance, action 0 gives a high reward (10), possibly indicating a desirable action like "stabilizing" the grid, while action 1 imposes a penalty (-10).

### 4. Value Iteration (value_iteration):

Goal: 
Use dynamic programming to compute the value function, which represents the maximum expected reward achievable from each state by following the best possible actions.
Steps:
For each state, calculate the new value as the maximum expected return of taking each possible action, considering the transition probability, reward, and discounted future value.
Update the value_function if the difference between the old and new values exceeds a small threshold, indicating convergence.

### 5. Optimal Policy Calculation (get_optimal_policy):

After finding the value function, the get_optimal_policy method calculates the best action (policy) for each state.
For each state, it selects the action with the highest expected reward based on the computed value function.

## Dynamic Programming and Value Iteration
In this code, dynamic programming is applied through value iteration to solve a Markov Decision Process (MDP). Value iteration is a method that:

Iteratively improves the value of each state by considering all possible actions.
Combines rewards with future discounted rewards, capturing long-term benefits over merely immediate rewards.
Uses previously computed values for each state (stored in value_function) to optimize current state values without redundant recalculations, characteristic of dynamic programming.

## Sample output
for an example grid with 10 states, 3 actions, and a discount factor of 0.9
![image](https://github.com/user-attachments/assets/69127a66-ce20-4b69-b6bd-c48ecaf86192)
