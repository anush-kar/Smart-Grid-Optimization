# Energy Scheduling Optimization in Smart Grids

This project provides a Python-based solution for optimizing energy scheduling in electrical smart grids using dynamic programming. The goal is to minimize the cost of meeting energy demand over time by balancing the use of renewable sources, grid power, and stored energy while respecting capacity and efficiency constraints.

## Project Overview
Energy scheduling in smart grids is a critical aspect of efficient power management. This program models the energy demand and supply over a series of time periods, enabling optimal energy source selection (renewables, grid, or storage) to minimize costs. The solution is designed to adapt to varying demand, supply, cost configurations, and storage limitations, making it flexible for real-world applications.

## Features
- **Dynamic Programming Optimization**: Efficiently calculates the minimum cost for energy scheduling.
- **Flexible Energy Source Selection**: Balances renewable energy, grid power, and storage use to minimize costs.
- **Configurable Inputs**: Customize demand, costs, storage capacity, and supply constraints for different scenarios.
- **Scalable**: Handles input instances of varying time periods and storage levels.

## Requirements
- **Python 3.6+**
- **NumPy** library for handling multi-dimensional arrays.

Install NumPy:
```bash
pip install numpy
```
## Usage
To run the program, configure your parameters in the main script and call the optimize_energy_schedule() function.

## Results
- **Minimum Cost**: Display the total minimum cost for meeting demand across all periods.
- **Optimal Schedule**: An output showing which energy source to use and how much energy to allocate per time slot to achieve minimal cost.
