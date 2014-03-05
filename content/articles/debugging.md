Title: Debugging
Date: 2014-04-04
Author: Gil Goncalves

**This is more of a wiki page to help me than a normal blog post**

> Debugging is twice as hard as writing the code in the first place. Therefore,
> if you write the code as cleverly as possible, you are, by definition, not
> smart enough to debug it.
--_Brian Kernighan_

## Getting the most out of a bug

When you find a bug, you have an oportunity to learn more about:

* The program you are working on
* The type of mistakes that you make
* How to solve problems
* How to fix bugs

Always assume that the bug is your fault, that will help you identify the bug
faster, also a lot less embarrassment from your peers once they find out that
the error that you said was the compiler/colleague/luck/weather's fault was
actually just you forgetting a `;` in the end of a line.

## Finding the bug

* Try to reproduce the the bug using different ways and tringulating them, so
that you can get a good understand of where it is and what it affects
* Use a debugger
* The old print statements to know what parts are being executing and with what
values is always good is you don't have a good debugger
* Talk to someone about it, AKA Rubber duck debugging

## Fixing the bug

* Understand the problem
* Understand the problem within the program
* Confirm the diagnosis
* Fix the problem, not the symptom
* Before you change a piece of code, think about why you're going to change,
don\'t do Voodoo Programming
* Make 1(one) change at a time
* Add a new test for the bug
* Is possible that the bug is somewhere else?

## Other notes

* Set your compiler (or `lint` if your using a dynamic language) to the be the
pickiest possible.
* Warnings should be treated as errors.

