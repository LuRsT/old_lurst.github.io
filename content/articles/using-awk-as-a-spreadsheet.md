Title: Using awk as a spreadsheet
Date: 2013-11-06
Author: Gil Goncalves

So, apparently we don't need no excel to do some simple calculations on the
console with csv files or text files, so if you like to use the console and
to do a little bit of calculations on simple text files, read on.

So for the example, I'll use a veryyyy simple text file with some letters

    $ cat test.txt
    c
    a
    a
    a
    a
    a
    b
    b
    b
    b
    b
    c
    b
    c
    c

As you can see, the letters aren't even sorted, let's `sort` that out:

    $ cat test.txt | sort
    a
    a
    a
    a
    a
    b
    b
    b
    b
    b
    b
    c
    c
    c
    c

Ok, so now we have all the letters in order, but how many of them do we have?

    $ cat test.txt | sort | uniq -c
      5 a
      6 b
      4 c

As you can see, `uniq -c` counted each of the letters and provided us with the
amount of times that each letter appears by their side.

But this is not enough, we want to know the `SUM()` of all the letters, and
while we could do a simple:

    $ cat test.txt | wc -l
    15

That's not fun at all, and it's only useful if we just wanted the amount of
rows, but this could be the sum of numbers in a text file, so I'll show how
to do the same, with awk:

    $ cat test.txt | sort | uniq -c | awk '{ sum += $1 } END { print sum }'
    15

So, this needs some explanation, what I'm doing in that line is, for every line
I'm suming up the variable `sum` with the first column `$1` of the line (which
are the frequency number that `uniq -c` gives us) and then, with the `END`
instruction, I'm printing the variable `sum` at the end of the processing,
giving us the sum of all the first columns in that text.

But now we lost all the other info from the file that we may or may not care
about, so let's get that again:

    $ cat test.txt | sort | uniq -c | awk '{ sum += $1; print $1 " " $2 } END { print sum }'
    5 a
    6 b
    4 c
    15

This new line has only one new thing, which is the `; print $1 " " $2` appended
to the first set of instructions `{}` which will basically just print the first
column, plus a space and then the second column, but this is horrible, we know
that we have two columns separated by a space, but what if there's more to it?
What if there are 3 columns, or more? Do we print every `$n` there is? No, we
do this:

    $ cat test.txt | sort | uniq -c | awk '{ sum += $1; print $0 } END { print sum }'
          5 a
          6 b
          4 c
    15

Now we're talking, `$0` prints the whole line, and that's exactly what we get.

Play with this to get more elaborate spreadsheet commands and throw your
Excel/Calc to the bin :).
