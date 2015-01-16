/* Copyright (c) 2001-2014, Live365, Inc. All rights reserved.
 * 950 Tower Lane, #1550, Foster City, CA 94404. USA 
 */
/*
 * DESCRIPTION
 *  
 *
 * PRIVATE CLASSES
 *  <list of private classes defined - with one-line descriptions>
 * 
 * NOTES
 *
 *
 * MODIFIED    (YYYY/MM/DD)    
 *  fchen     2015/01/16 - Creation
 */
package main;

import java.util.LinkedList;
import java.lang.Math;

/**
 * Created by jcfrank7 on 15/1/16.
 */
public class Entry {
    public static void main(String[] args) {
        if (args.length < 1) {
            println("Give me a number.");
            return;
        }
        long num = Long.valueOf(args[0]);
        println("number is " + num + ", now get primes.");
        Entry me = new Entry(num);
        for (long prime : me.getPrimes()) {
            println(String.valueOf(prime));
        }
    }

    private long number = 0L;
    public Entry(long num) {
        this.number = num;
    }

    private Long[] getPrimes() {
        LinkedList<Long> primes = new LinkedList<>();
        primes.add(2L);  //initial value
        long counter = 3L;
        while (counter <= number) {
            boolean isPrime = true;
            double sqrt = Math.sqrt(counter);
            // divide with primes, if any one of the results is zero, it's not a prime.
            for (long prime : primes) {
                // we only need to try prime numbers smaller than sqrt.
                if (prime > sqrt) {
                    continue;
                }
                if (Long.compare(counter % prime, 0) == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(counter);
            }
            counter++;
        }
        return primes.toArray(new Long[primes.size()]);
    }

    private static void println(String msg) {
        System.out.println(msg);
    }
}
