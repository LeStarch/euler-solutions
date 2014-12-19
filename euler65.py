#Generates the the ad infinium repitions of the continued fraction of e
def egen():
    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k = k + 1

print(egen()[0:9])

