/*
 *  Filename:  fact.c
 *   Created:  11/01/2015 07:13:56 PM
 *    Author:  Rafael Gozlan <rafael.gozlan@epita.fr>
 */

#include <stdio.h>

long long fact(int n)
{
    return (n > 0) ? fact(n - 1) * n : 1;
}
