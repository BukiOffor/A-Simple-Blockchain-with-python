import hashlib
import datetime
import csv

hashlist = []
Blockchain = []
def main():
    mining()

def mining():
    try:
        counter = 0
        with open("mining_pool.csv") as file:
            reader = csv.reader(file)
            for lines in reader:
                transaction = repr(lines).encode()
                hash = hashlib.sha256(transaction).hexdigest()
                hashlist.append(hash)
                blocks = { "prev_block":"0"*64, "block_header":hash, "difficulty":0, "time":datetime.datetime.now(), "transactions":{"transaction_ID":lines[0],"input":lines[1], "output":lines[2], "sender":lines[3],"receiver":lines[4]}}
                if not counter == 0:
                    blocks['prev_block'] = hashlist[counter-1]
                Blockchain.append(blocks)
                counter += 1
        

        with open("BlockChainLedger.csv", 'a')as file:
            writer = csv.DictWriter(file, fieldnames=[ 'prev_block','block_header', "difficulty",'time','transactions'])
            writer.writeheader()
            for blocks in Blockchain:
                writer.writerow(blocks)
    except FileNotFoundError:
        print('******Be sure to generate transactions by running transactions.py first******')

if __name__ == "__main__":
    main()




