# Topological Properties
This code aims to explore the topological properties of Quantum Spin Hall Efect. The graphs generated help visualize and analyze the system's band structure and Berry phase, which are crucial for understanding its topological characteristics.

# The Code
The code is organized into two files: 'qsh.py' and 'main.py'. 

- 'qsh.py' contains essential functions and calculations used in the main code ('main.py'). This file includes the implementation of the Hamiltonian and other relevant mathematical operations, like functions to plot graphs.

- 'main.py' is the main script that interacts with the user and generates the graphs. To execute the code and obtain results, you can run 'main.py' using Python 3.


It is important to note that that the Hamiltonian has been implemented directly in the code but can be easily changed by the user if desired. Additionally, it emphasizes that for this version, the Hamiltonian needs to be a 2x2 matrix.

# Output
To use the code, run main.py and follow the on-screen instructions to input the hopping term and topological mass. The code will generate five graphs (examples can be seen at output-examples directory) that will be better discussed below:

- bands.png: A band structure plot from the Hamiltonian, fixing ky=0 and varying Kx.

- berry.png: A graph showing all possibilities of Berry phase from combinations of kx and ky. The color intensity corresponds to the Berry phase intensity.

- kx_fixed.png: Shows how the Berry phase changes with a fixed kx, representing a kind of phase transition.

- ky_fixed.png: Similar to kx_fixed.png, but now fixing ky.

- proj.png: This graph is plotted by projecting the band structure on a spin basis using the Pauli matrix Z (sigma_z).

# Contact
If you have any questions or need further assistance, feel free to reach out to me via email at viniciusggarcia1@hotmail.com.