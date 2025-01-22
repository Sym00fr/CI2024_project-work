# CI2024_project-work
This part of the code creates a dictionary with the names of all numpy functions as keys and the functions themselves as values. The dictionary is then filtered to include only the relevant functions that have a maximum of two input parameters and one output.

##Define node and functions
The population consists of trees, whose nodes can have a numerical value, a variable name, or a numpy operation. In this section, I define the node and all associated functions.

##Generate Tree
We have two types of trees: full trees, where each node has two children, and grow trees, where nodes can have 0 to 2 children at any depth.

##Compute y and Fitness_MSE
These two functions are used to calculate the result of the formula represented by the individual given the input (x), and to calculate the fitness of that function, which is the mean square error.

##Printing y and navigating tree
###Navigate_tree
A test function that explores all nodes of the tree.
###node_list
Returns the list of nodes of that tree.
###get_parent_node
Returns the parent node of the given node, used in mutation and recombination functions.
###print_tree_to_String
Returns the tree as a string.
###is_valid
A function that checks if all problem variables are used in the solution and only once each. Used only in the testing phase, not for the final result.

##Parent selection
###Tournament selection
Returns the best individual based on MSE from a pool of n=5 randomly chosen individuals.
###Uniform selection:
Returns a random individual, used only in the testing phase.

##Mutation
Four types of mutations are defined and used randomly within the algorithm: subtree, point, permutation, and hoist.

##Recombination
Swaps a node from one parent with a node from another parent, used as an alternative to mutations but with a much higher probability.

##Generate population
The generated population consists of grow trees and full trees in a ratio of 3/4 to 1/4 to avoid the bloating phenomenon, as full trees are generally larger than grow trees.

