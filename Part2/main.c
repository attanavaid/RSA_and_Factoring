#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <gmp.h>

// Helpful Links: https://gmplib.org/manual/Integer-Functions

void P_RHO(const mpz_t n) {
    mpz_t i, curr, curr2, curr3, y, k, next, dif, d;
    mpz_init(i);
    mpz_init(curr);
    mpz_init(curr2);
    mpz_init(curr3);
    mpz_init(y);
    mpz_init(k);
    mpz_init(next);
    mpz_init(dif);
    mpz_init(d);

    mpz_set_ui(k, 2U);
    if (mpz_divisible_p(n, k)) {
        gmp_printf("Pollard's Rho determined that one of the divisors for test80 is 2.\n");
        mpz_clear(i);
        mpz_clear(curr);
        mpz_clear(curr2);
        mpz_clear(curr3);
        mpz_clear(y);
        mpz_clear(k);
        mpz_clear(next);
        mpz_clear(dif);
        mpz_clear(d);
    }

    gmp_randstate_t state;
    gmp_randinit_mt(state);
    gmp_randseed_ui(state, 1U);
    mpz_urandomm(curr, state, n);
    mpz_set(y, curr);
    mpz_set_ui(i, 1U);

    while (1) {
        mpz_add_ui(i, i, 1);
        mpz_pow_ui(curr2, curr, 2);
        mpz_sub_ui(curr3, curr2, 1);
        mpz_mod(next, curr3, n);
        mpz_sub(dif, y, next);
        mpz_gcd(d, dif, n);

        if ((mpz_cmp_si(d, 1) != 0) && (mpz_cmp(d, n) != 0)) {
            gmp_printf("Pollard's Rho determined that one of the divisors for test80 is %Zd\n", d);
            gmp_randclear(state);
            mpz_clear(i);
            mpz_clear(curr);
            mpz_clear(curr2);
            mpz_clear(curr3);
            mpz_clear(y);
            mpz_clear(k);
            mpz_clear(next);
            mpz_clear(dif);
            mpz_clear(d);
        }

        if (mpz_cmp(i, k) == 0) {
            mpz_set(y, next);
            mpz_mul_ui(k, k, 2);
        }

        mpz_set(curr, next);
    }
        
    gmp_printf("There are no divisors for test80.\n");
    gmp_randclear(state);
    mpz_clear(i);
    mpz_clear(curr);
    mpz_clear(curr2);
    mpz_clear(curr3);
    mpz_clear(y);
    mpz_clear(k);
    mpz_clear(next);
    mpz_clear(dif);
    mpz_clear(d);
}

int main() {
    mpz_t n;
    mpz_init(n);
    mpz_set_str(n, "98834976202698839303077", 10);
    P_RHO(n);
    return 0;
}