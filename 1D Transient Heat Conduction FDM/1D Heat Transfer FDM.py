import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting
from tqdm import tqdm  # For progress bar

# Heat equation parameters
L = 1.0  # Length of the rod
alpha = 0.01  # Thermal diffusivity (alpha = k / (rho * Cp))
Nx = 100  # Number of spatial grid points
dx = L / (Nx - 1)  # Spatial step size
T_final = 10  # Total simulation time
dt = 0.001  # Time step size
Nt = int(T_final / dt)  # Number of time steps

# Spatial grid
x = np.linspace(0, L, Nx)
time = np.linspace(0, T_final, Nt)

# Function to get the initial condition from the user
def get_initial_condition():
    print("Choose an initial condition for temperature:")
    print("1. sin(pi * x)")
    print("2. sin(2pi * x)")
    print("3. x*np.sin(np.pi * x) + x*np.sin(2 * np.pi * x)")
    choice = int(input("Enter 1, 2, or 3: "))
    
    if choice == 1:
        return np.sin(np.pi * x)
    elif choice == 2:
        return np.sin(2*np.pi * x)
    elif choice == 3:
        return x*np.sin(np.pi * x) + x*np.sin(2 * np.pi * x)
    else:
        print("Invalid choice. Defaulting to sin(pi * x).")
        return np.sin(np.pi * x)

# Initialize temperature array
T = np.zeros((Nt, Nx))  # 2D matrix to store temperature [time, space]

# Set the initial condition at t=0
T[0, :] = get_initial_condition()

# Apply boundary conditions: T(0,t) = T(L,t) = 0 (fixed at both ends)
T[:, 0] = 0.0
T[:, -1] = 0.0

# Time-stepping loop with progress bar
for n in tqdm(range(1, Nt), desc="Solving 1D Heat Conduction"):
    for i in range(1, Nx - 1):
        T[n, i] = T[n-1, i] + alpha * dt / dx**2 * (T[n-1, i+1] - 2*T[n-1, i] + T[n-1, i-1])

# Create the figure with subplots for the three plots
fig = plt.figure(figsize=(18, 6))

# First subplot: 2D line plot
ax1 = fig.add_subplot(1, 3, 1)
for n in range(0, Nt, Nt // 5):  # Plot for 5 different time steps
    ax1.plot(x, T[n, :], label=f'Time = {n * dt:.4f}s')

ax1.set_title('1D Heat Conduction (2D Line Plot)')
ax1.set_xlabel('Position (x)')
ax1.set_ylabel('Temperature (T)')
ax1.legend()
ax1.grid(True)

# Second subplot: Heatmap of temperature evolution
ax2 = fig.add_subplot(1, 3, 2)
heatmap = ax2.imshow(T, aspect='auto', cmap='hot', extent=[0, L, 0, T_final])
ax2.set_title('Temperature Evolution (Heatmap)')
ax2.set_xlabel('Position (x)')
ax2.set_ylabel('Time (t)')
fig.colorbar(heatmap, ax=ax2, label='Temperature (T)')

# Third subplot: 3D Surface Plot
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
X, Y = np.meshgrid(x, time)  # Create meshgrid for space and time
ax3.plot_surface(X, Y, T, cmap='viridis')

ax3.set_title('3D Surface Plot of Temperature Evolution')
ax3.set_xlabel('Position (x)')
ax3.set_ylabel('Time (t)')
ax3.set_zlabel('Temperature (T)')

# Adjust layout and display all plots in one window
plt.tight_layout()
plt.show()
