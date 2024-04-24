'''3. Develop a distributed system, to find sum of N elements in an array
by distributing N/n elements to n number of processors MPI or
OpenMP. Demonstrate by displaying the intermediate sums calculated
at different processors.'''
# download msmpi from chrom
# pip install mpi
# pip install mpi4py
# python (filename).py

from mpi4py import MPI

def distribute_array(arr, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()
    chunk_size = len(arr) // size
    start = rank * chunk_size
    end = start + chunk_size if rank < size - 1 else len(arr)
    return arr[start:end]

def compute_sum(arr):
    return sum(arr)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Define the array to be summed (Assuming same array on all processors)
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Distribute the array among processors
    local_array = distribute_array(array, comm)

    # Compute local sum
    local_sum = compute_sum(local_array)

    # Gather all local sums on root process (rank 0)
    all_sums = comm.gather(local_sum, root=0)

    # Display intermediate sums calculated at different processors
    print("Processor", rank, "computed local sum:", local_sum)

    # Root process combines sums to get the final result
    if rank == 0:
        final_sum = sum(all_sums)
        print("Final Sum:", final_sum)

if __name__ == "__main__":
    main()



'''explanation of the provided Python code:

Import MPI:

We import the MPI module from the mpi4py library. 
This module provides the necessary functions and objects for MPI programming.
Define Helper Functions:

distribute_array(arr, comm): 
This function divides the input array arr into smaller chunks and distributes these chunks among MPI processes using the communicator comm.

compute_sum(arr): 
This function computes the sum of elements in the input array arr.

Main Function (main()):

Initialize MPI communicator, get the rank of the current process (rank), 
and the total number of processes (size).

Define the Array:
We define the array to be summed. In this example, we assume the same array is used by all MPI processes. This array can be any list of numbers.

Distribute the Array:
We distribute the array among MPI processes using the distribute_array() function. Each process receives a portion of the array based on its rank.

Compute Local Sum:
Each MPI process computes the sum of its local portion of the array using the compute_sum() function. This results in each process having its local sum.

Gather Local Sums:
We gather all local sums from each MPI process onto the root process (rank 0) using the comm.gather() function. This collects all local sums into a list called all_sums on the root process.

Display Intermediate Sums:
Each MPI process prints out its rank and the local sum it computed. This displays the intermediate sums calculated at different processors.

Combine Sums (Root Process):
On the root process (rank 0), we sum up all the local sums from all_sums to compute the final sum of all elements in the array.
Print Final Sum (Root Process):

Finally, the root process prints out the final sum of all elements in the array.'''