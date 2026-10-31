def print_hello_n_times(n):
    for _ in range(n):
        print("hello world")

num_times = int(input("How many times to print hello world? "))
print_hello_n_times(num_times)