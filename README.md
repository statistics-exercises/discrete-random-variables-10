# Plotting Negative Binomial Random variables

As a final exercise lets make a scatter plot of the negative binomial random variables you have just learned to generated.  In particular, you are going to generate 100 negative binomial random variables and then draw a graph showing the values of all these random variables. To complete this exercise you will need to:  

- Write a function called `negative_binomial` that takes `k` (the number of successes that must be generated) and  `p` (the probability of success) as parameters using what you learned in the previous exercise.

- Use this function and what you know about loops and lists  to generate a list called `random_variables` that contains 100 negative binomial random variables all of which have the p parameter set to the global variable `prob` and the k parameter set to the global variable `kval`.

I have included code in the cell on the left that will plot your list of random variables.  To get this code to work, however, you will need to write a second list called `indices` that contains a numerical index for each of these random variables.  The first of these indices should be equal to one, the second should be equal to two, the third should be three and so on.   
