#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
    if n == 0:#when there is no cookies to eat, one way is finish eating
        return 1
    if n < 0:#Do not add negative iterations
        return 0
    if n not in cache:#Cache works better for large numbers as saves iteratively
      #Cache is defaulted to empty dictionary, minimum needed to generate a permutation is (n-1) + (n-2) + (n-3) for cookies with more than 4
      #Each time function recursively calls itself, it updates cache by checking first if that n exists and iteratively adds to cache
        cache[n] = eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)

    return cache[n]
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')