import itertools

def gen1():
    for i in range(5):
        yield i 

def gen2():
    for i in range(3):
        yield i + 5


geno=gen1()
gent=gen2()

for a in itertools.zip_longest(geno,gent):
    print(a)

                

# def gen1():
#     for i in range(5):
#         yield i 

# def gen2():
#     for i in range(3):
#         yield i + 5


# geno=gen1()
# gent=gen2()

# for a in zip(geno,gent):
#     print(a)

                