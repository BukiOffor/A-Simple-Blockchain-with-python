import csv

class Transaction:

    transactions = []
   
    def __init__(self,transaction_id, input, output, sender, receiver):
        self.transaction_id = transaction_id
        self.input = input
        self.output = output
        self.sender = sender
        self.receiver = receiver
                   
    def transaction_block(self):
        self.transaction_list = {"transaction_ID":self.transaction_id,"input":self.input, "output":self.output, "sender":self.sender,"receiver":self.receiver}
        Transaction.transactions.append(self.transaction_list)
       
    
    @classmethod
    def transaction_pool(cls):
        with open("mining_pool.csv", 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['transaction_ID', 'input', "output",'sender','receiver'])
            for transactions in Transaction.transactions:
                writer.writerow(transactions)
                
    
tt = Transaction(1, 200, 180, "ghicdfgh125","lpiuhyh909")
ll = Transaction(2, 300, 265, "loicdkjj125","lpiklyh909")
jj = Transaction(3, 300, 269, "loicdkjj125","lpiklyh909")
tt.transaction_block()
ll.transaction_block()
jj.transaction_block()
Transaction.transaction_pool()


