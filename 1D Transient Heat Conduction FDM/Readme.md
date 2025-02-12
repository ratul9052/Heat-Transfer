# 1D Heat Conduction Simulation using Finite Difference Method (FDM)

This project simulates the 1D transient heat conduction in a rod using the explicit Finite Difference Method (FDM). The code is implemented in Python and visualizes the temperature distribution over space and time using three different plots: a 2D line plot, a heatmap, and a 3D surface plot. The user can choose an initial condition for the temperature distribution, and the boundary conditions are fixed at zero for both ends of the rod.

![Plot](image.svg)

## Problem Description

The 1D heat conduction problem is governed by the following partial differential equation (PDE):

    ∂T/∂t = α ∂²T/∂x²

Where:
- **T(x, t)** is the temperature as a function of position **x** and time **t**.
- **α (alpha)** is the thermal diffusivity of the material.

The goal is to solve for **T(x, t)** over time, given some initial and boundary conditions.

### Parameter Values
- **Length of the rod** (L): 1.0 meter
- **Thermal diffusivity** (α): 0.01 m²/s
- **Number of spatial grid points** (Nx): 100
- **Time step size** (Δt): 0.001 seconds
- **Final simulation time** (T_final): 10 seconds

## Boundary Conditions (BC)

The boundary conditions applied in this simulation are **Dirichlet boundary conditions**, meaning that the temperature at both ends of the rod is fixed at zero throughout the simulation.

- T(0, t) = 0 for all t
- T(L, t) = 0 for all t

Where **L** is the length of the rod.

## Initial Conditions (IC)

The initial temperature distribution along the rod is chosen by the user. The following options are available for the initial condition:

1. T(x, 0) = sin(πx)
2. T(x, 0) = sin(2πx)
3. T(x, 0) = x * sin(πx) + x * sin(2πx)

The user can select one of these options when running the simulation.

## Finite Difference Method (FDM)

The explicit finite difference method is used to numerically solve the PDE. The spatial domain is discretized into a grid with **Nx** points, and the time is discretized into **Nt** time steps. The forward-time, centered-space (FTCS) scheme is used to compute the temperature at each point in the rod at every time step.

The update equation is given by:

    Tᵢⁿ⁺¹ = Tᵢⁿ + α (Δt / Δx²) * (Tᵢ₊₁ⁿ - 2Tᵢⁿ + Tᵢ₋₁ⁿ)

Where:
- **Tᵢⁿ** is the temperature at position **i** and time step **n**.
- **Δt** is the time step size.
- **Δx** is the spatial step size.

## Visualization

Three types of visualizations are provided in this project:
1. **2D Line Plot**: Temperature profile at various time steps.
2. **Heatmap**: A 2D heatmap showing temperature evolution over space and time.
3. **3D Surface Plot**: A 3D plot showing temperature as a function of space and time.

## Dependencies

This project requires the following Python libraries:
- `numpy` for numerical computations
- `matplotlib` for plotting
- `tqdm` for progress bars

To install the necessary packages, run:

```bash
pip install numpy matplotlib tqdm
