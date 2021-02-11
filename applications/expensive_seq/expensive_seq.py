# Your code here


def expensive_seq(x, y, z):
    # Your code here


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
# Your code here

cache = {}


def expensive_seq(x, y, z):
    # Your code here

    # set base case for recursion
    if x <= 0:
        return y + z

    # create a unique key for our cache for x,y,z values
    key = f"x{x}y{y}z{z}"

    # check if the answer to this particular calculation is already memoized in the cache
    if key not in cache:
        # if not, then save it to the cache
        cache[key] = expensive_seq(
            x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    # return the cached answer
    return cache[key]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
