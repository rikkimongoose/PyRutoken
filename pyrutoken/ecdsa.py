import gmpy2, random, sys

GMP_ROUND_ZERO = 0
MAX_RANDOM = sys.maxint
MAX_RANDOM_GMP = 33554432

class GmpMethods:
    def gmp_mod2(number, divider):
        result = c_mod(number, divider)
        if result > 0: result = add(divider, result)
        return result

    def gmp_random(number):
        random = mpz_random(42, MAX_RANDOM_GMP);
        small_rand = random.rand(0, MAX_RANDOM);
        while random > number:
            random = c_div(random, small_rand)
        return random

    def gmp_hexdec(hexval):
        return mpz(hexval)__format__('Z')

    def gmp_dechex(decval):
        return mpz(decval)__format__('a')

