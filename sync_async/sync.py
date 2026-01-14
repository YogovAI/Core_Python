# import time

# def task():
#     time.sleep(10)   # blocks everything

# task()
# print("done")



import time

def job(name):
    print("start", name)
    time.sleep(5)
    print("end", name)

job("A")
job("B")
job("C")
