# Topological Properties
This code aims to explore the topological properties of Quantum Spin Hall. The graphs generated help visualize and analyze the system's band structure and Berry phase, which are crucial for understanding its topological characteristics.

# The Code
The code is organized in two files: qsh.py and main.py. The qsh.py contains functions that are used in the main code (main.py). In order to get some results you can execute de main.py using python3, for example, and you'll have to enter the hopping term and the topological mass. The Hamiltonian was implemented directly in the code, however can be easily changed. In this version the Hamiltonian has to be 2x2.

# Output
To use the code, run main.py and follow the on-screen instructions to input the hopping term and topological mass. The code will generate five graphs that will be better discussed below:

- bands.png: A band structure plot from the Hamiltonian, fixing ky=0 and varying Kx.

- berry.png: A graph showing all possibilities of Berry phase from combinations of kx and ky. The color intensity corresponds to the Berry phase intensity.

- kx_fixed.png: Shows how the Berry phase changes with a fixed kx, representing a kind of phase transition.

- ky_fixed.png: Similar to kx_fixed.png, but now fixing ky.

- proj.png: This graph is plotted by projecting the band structure on a spin basis using the Pauli matrix Z (sigma_z).

# Contact
If you have any questions or need further assistance, feel free to reach out to me via email at viniciusggarcia1@hotmail.com.