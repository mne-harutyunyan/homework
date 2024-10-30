# You are working with a large dataset stored in multiple CSV files. Each file contains transaction data from
#  different regions. Your task is to process these files concurrently and aggregate the data into a summary 
# report that includes the total number of transactions and the sum of transaction amounts for each file.
# Use the multiprocessing library to create separate processes for each CSV file.
# Each process should read its assigned file, sum the transaction amounts, and count the number of transactions.
# Aggregate the results from all processes and print the final summary.

import multiprocessing
import csv

def process_file(file_path, queue):
    transaction_amounts = 0.0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction_amounts += float(row['Amount'])
            total_transactions = int(row['Transaction ID'])

    queue.put((total_transactions, transaction_amounts))

def aggregate_results(file_path):
    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=process_file, args=(file1,queue))
    process2 = multiprocessing.Process(target=process_file, args=(file2,queue))
    process3 = multiprocessing.Process(target=process_file, args=(file3,queue))



    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    total_transactions = 0
    total_amount = 0.0
    while not queue.empty():
        transactions, amount = queue.get()
        total_transactions += transactions
        total_amount += amount

    return total_transactions, total_amount

file1 = 'transactions_region1.csv'
file2 = 'transactions_region2.csv'
file3 = 'transactions_region3.csv'

if __name__ == '__main__':
    file_paths = [file1, file2, file3]
    total_transactions, total_amount = aggregate_results(file_paths)

    print(f"Total Transactions: {total_transactions}")
    print(f"Total Amount: ${total_amount:.2f}")
