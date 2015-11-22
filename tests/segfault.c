/*
 *  Filename:  segfault.c
 *   Created:  11/22/2015 07:05:16 PM
 *    Author:  Rafael Gozlan <rafael.gozlan@epita.fr>
 */

int segv(int n)
{
    return n * segv(n-1);
}
