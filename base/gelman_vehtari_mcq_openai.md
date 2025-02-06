# Question Analysis Results

## Question 1

1. Suppose a variable y takes on the value 200 in the year 𝑡 = 1900 and 240 in the year 𝑡 = 2000. If
this variable follows a linear time trend, what are the values of 𝑎 and 𝑏 in the equation of the line,
y = 𝑎 + 𝑏𝑡?
(a) 𝑎 = −560, 𝑏 = 0.4
(b) 𝑎 = 200, 𝑏 = 0.4
(c) 𝑎 = 160, 𝑏 = 4
(d) 𝑎 = −1700, 𝑏 = 40

### Answer:
To find the values of 𝑎 and 𝑏 in the equation of the line y = 𝑎 + 𝑏𝑡, we can use the given data points (1900, 200) and (2000, 240).

First, we need to calculate the slope 𝑏:
𝑏 = (240 - 200) / (2000 - 1900)
𝑏 = 40 / 100
𝑏 = 0.4

Next, we can substitute the slope 𝑏 and one of the data points into the equation to solve for 𝑎:
200 = 𝑎 + 0.4 * 1900
200 = 𝑎 + 760
𝑎 = 200 - 760
𝑎 = -560

Therefore, the values of 𝑎 and 𝑏 in the equation of the line are:
𝑎 = -560 and 𝑏 = 0.4

So, the correct answer is (a) 𝑎 = -560, 𝑏 = 0.4.

---

## Question 2

2. What is the logarithm of 0? (We use natural log, not log base 10.)
(a) −1
(b) 1/𝑒
(c) 0
(d) undefined

### Answer:
The logarithm of 0 is undefined. Therefore, the correct answer is (d) undefined.

---

## Question 3

3. What is the average of the numbers 1, 2, 3, . . . , 100?
(a) 49.5
(b) 50
(c) 50.5
(d) 51

### Answer:
To find the average of a set of numbers, you add up all the numbers and then divide by the total count of numbers.

In this case, the numbers are from 1 to 100, so there are 100 numbers in total.

The sum of the numbers from 1 to 100 can be calculated using the formula for the sum of an arithmetic series: 
Sum = (n/2)(first term + last term)
Sum = (100/2)(1 + 100)
Sum = 50(101)
Sum = 5050

To find the average, we divide the sum by the total count of numbers:
Average = Sum / Count
Average = 5050 / 100
Average = 50.5

Therefore, the correct answer is (c) 50.5.

---

## Question 4

4. Which of these functions equals 0 when 𝑥 = 0 and asymptotes to the value 10 as 𝑥 → ∞?
(a) ~ = 10𝑥/∞
(b) ~ = 10 exp(−𝑥)
(c) ~ = 10(1 − exp(−𝑥))
(d) ~ = 10 − 0.1𝑥2

### Answer:
The correct answer is:

(c) ~ = 10(1 − exp(−𝑥))

This function equals 0 when 𝑥 = 0 because exp(0) = 1, so 1 - 1 = 0. As 𝑥 approaches infinity, exp(−𝑥) approaches 0, so the function asymptotes to 10.

---

## Question 5

1. What is one way to make a scatterplot of two vectors, 𝑥 and ~, in R?
(a) plot(x, y)
(b) plot x, y
(c) scatter(x, y)
(d) scatter x, y

### Answer:
The correct answer is (a) plot(x, y).

---

## Question 6

2. Which of these lines of R code generates ten random numbers between −2 and +2?
(a) sample(c(-2,2), 10)
(b) seq(-2, 2, length=10)
(c) runif(10, -2, 2)
(d) rnorm(10, -2, 2)

### Answer:
The correct answer is (d) rnorm(10, -2, 2).

---

## Question 7

3. Which of these lines of R code fits a regression of y on x, with data set data0, using the lm
command, storing the result in object fit?
(a) lm$fit(y ~ x, data=data0)
(b) fit(y ~ x, data=data0)
(c) fit(y ~ x, data=data0, model=lm)
(d) fit <- lm(y ~ x, data=data0)

### Answer:
The correct answer is:

(d) fit <- lm(y ~ x, data=data0)

---

## Question 8

4. You want to write a line of R code that regresses income on age and male as well as the interaction
of both variables. The data is stored in the data frame data0. Which of the following does not
work?
(a) lm(income ~ age + sex + age:male, data=data0)
(b) lm(income ~ 0 + age + male + age:male, data=data0)
(c) lm(income ~ age + male + age*male, data=data0)
(d) lm(income ~ (age + male)^2, data=data0)

### Answer:
The correct answer is (d) lm(income ~ (age + male)^2, data=data0). 

This option does not correctly specify the interaction between age and male variables. The caret (^2) indicates squaring the sum of age and male variables, rather than specifying the interaction between them.

---

## Question 9

5. Which of these lines of R code takes a vector of numbers, a, and centers the observations at their
mean?
(a) a - mean(a)
(b) a/mean(a)
(c) mean(a)
(d) a - mean(a - mean(a))

### Answer:
The correct answer is (a) a - mean(a).

---

## Question 10

1. What is the approximate interval containing 95% of observations, if your data are normally
distributed with mean 5 and standard deviation 2?
(a) (3, 7)
(b) (1, 9)
(c) (5 − √2, 5 + √2)
(d) (5 − 2√2, 5 + 2√2)

### Answer:
The correct answer is (a) (3, 7).

In a normal distribution, approximately 95% of the data falls within 2 standard deviations of the mean. Given that the mean is 5 and the standard deviation is 2, we can calculate the interval as follows:

Lower bound = mean - 2 * standard deviation = 5 - 2 * 2 = 1
Upper bound = mean + 2 * standard deviation = 5 + 2 * 2 = 9

Therefore, the interval containing 95% of observations is (1, 9).

---

## Question 11

2. Consider the regression line ~ = 0.2 + 0.3𝑥 + error , with errors normally distributed with mean
0 and standard deviation 2. You observe a new data point at 𝑥 = 10. Which of these is a 68%
predictive interval for the corresponding observation ~?
(a) (1.2, 5.2)
(b) (−0.8, 7.2)
(c) (3.2 − 2/√𝑛, 3.2 + 2/√𝑛)
(d) (  ̄~ − 2/√𝑛,  ̄~ + 2/√𝑛)

### Answer:
To find the 68% predictive interval for the corresponding observation ~ at x = 10, we need to consider the uncertainty in the prediction due to the error term.

Given that the errors are normally distributed with mean 0 and standard deviation 2, the standard error of the prediction at x = 10 is 2.

The predicted value at x = 10 is:
~ = 0.2 + 0.3(10) = 3.2

The 68% predictive interval is calculated as ±1 standard error from the predicted value:
Predictive interval = (3.2 - 2, 3.2 + 2) = (1.2, 5.2)

Therefore, the correct answer is:
(a) (1.2, 5.2)

---

## Question 12

3. You record the median income in each state in 2013 and in 2015, and then you run a linear
regression on these 50 data points, predicting 2015 median income from 2013 median income.
What will be the approximate slope of this regression?
(a) 0
(b) 0.5
(c) 1
(d) 2

### Answer:
To predict the approximate slope of the regression line when predicting 2015 median income from 2013 median income, we can use the formula for the slope of a simple linear regression:

\[ \text{Slope} = \frac{\text{Covariance}(X, Y)}{\text{Variance}(X)} \]

Since we are predicting 2015 median income from 2013 median income, X represents the 2013 median income and Y represents the 2015 median income.

If the correlation between the two variables is strong, the slope will be close to 1. Therefore, the answer is:

(c) 1

---

## Question 13

4. You find survey data from a random sample of 500 American adults in the year 2020 that includes
their ages and their feeling thermometer scores (a 0–100 measure) toward Donald Trump. You
fit a linear regression predicting feeling thermometer score from age. The result is the line
~ = 𝑎 + 𝑏𝑥 + error, with errors normally distributed with mean 0 and standard deviation 𝜎. What
is a plausible value for 𝑏?
(a) −0.20
(b) −0.02
(c) 0.02
(d) 0.20

### Answer:
To determine a plausible value for 𝑏 in the linear regression predicting feeling thermometer score from age, we need to consider the relationship between age and feeling thermometer score. 

Given that the feeling thermometer score is towards Donald Trump, it is plausible to assume that as age increases, the feeling thermometer score towards Donald Trump may decrease. This suggests a negative relationship between age and feeling thermometer score.

Therefore, a plausible value for 𝑏 would be a negative value. Looking at the options provided:
(a) −0.20
(b) −0.02
(c) 0.02
(d) 0.20

The most plausible value for 𝑏 would be:
(a) −0.20

This value suggests that for every unit increase in age, the feeling thermometer score towards Donald Trump decreases by 0.20 units.

---

## Question 14

5. You have a data set with the variables income, age, male. What regression could you fit to
estimate the difference between the average incomes of men and women?
(a) lm(income ~ male)
(b) lm(income ~ age)
(c) lm(income ~ male + age)
(d) lm(income ~ male*age)

### Answer:
The correct answer is (a) lm(income ~ male). 

By fitting the regression lm(income ~ male), you are estimating the difference between the average incomes of men and women. This model will provide you with the coefficient for the variable "male," which represents the average difference in income between men and women after controlling for other variables.

---

## Question 15

1a. Here is a regression predicting incumbent party’s vote percentage from economic growth, fit
to several recent elections:
Median MAD_SD
(Intercept) 46.7 1.4
growth 2.8 0.6
Auxiliary parameter(s):
Median MAD_SD
sigma 3.7 0.7
Someone summarizes the model as follows: “A 1% increase in economic growth is predicted
to lead to a 2.8% share in incumbent party’s vote share.” What is wrong with that statement?
i. The estimate of 2.8 is not statistically significant so it is misleading to present it in this
way.
ii. With these observational data we can only make descriptive, not causal, claims.
iii. People are interested in who wins the election, not in vote share.
iv. The model accounts for the economy but leaves out predictors for other important factors
such as foreign policy and social issues.

### Answer:
ii. With these observational data we can only make descriptive, not causal, claims.

The statement is incorrect because observational data cannot establish causation, only association. Therefore, it is not appropriate to claim that a 1% increase in economic growth causes a 2.8% increase in the incumbent party's vote share based solely on this regression analysis.

---

## Question 16

1b. A group of students are being trained to do a particular skill, and for each student we record the
number of hours they are trained and their score on a later test. We see a pattern of diminishing
returns: at zero hours of training, the test scores are zero; for low values of training, there is
an approximately positive and linear relation between hours of training and test score; for
high values of training, the relationship levels off and becomes flat. We fit a linear regression
of the form, score = 𝑎 + 𝑏 ∗ hours + error. What can we say about the estimates of 𝑎 and 𝑏?

i. 𝑎 will be negative, 𝑏 will be positive.
ii. 𝑎 will be approximately zero, 𝑏 will be positive.
iii. 𝑎 will be positive, 𝑏 will be positive.
iv. It will not be possible to fit the regression because the data show a nonlinear relationship.

### Answer:
The correct answer is ii. 𝑎 will be approximately zero, 𝑏 will be positive. 

In this scenario, 𝑎 represents the intercept of the regression line, which is the predicted test score when the number of hours of training is zero. Since the test scores are zero at zero hours of training, 𝑎 is expected to be close to zero.

𝑏 represents the slope of the regression line, indicating the rate at which the test scores increase with each additional hour of training. As mentioned, there is a positive and linear relationship between hours of training and test score for low values of training, so 𝑏 is expected to be positive.

---

## Question 17

1c. Suppose a variable ~ takes on the value 200 in the year 𝑡 = 1900 and 240 in the year 𝑡 = 2000.
If this variable follows a linear time trend, what are the values of 𝑎 and 𝑏 in equation of the
line, ~ = 𝑎 + 𝑏𝑡?
i. 𝑎 = −560, 𝑏 = 0.4
ii. 𝑎 = 200, 𝑏 = 0.4
iii. 𝑎 = 160, 𝑏 = 4
iv. 𝑎 = −1700, 𝑏 = 40

### Answer:
To find the values of 𝑎 and 𝑏 in the linear equation ~ = 𝑎 + 𝑏𝑡, we can use the given data points (1900, 200) and (2000, 240).

First, we need to calculate the slope 𝑏:
𝑏 = (240 - 200) / (2000 - 1900) = 40 / 100 = 0.4

Next, we can substitute the slope 𝑏 into one of the data points to solve for 𝑎:
200 = 𝑎 + 0.4 * 1900
200 = 𝑎 + 760
𝑎 = 200 - 760
𝑎 = -560

Therefore, the correct answer is i. 𝑎 = -560, 𝑏 = 0.4.

---

## Question 18

1d. Which of the following statements is correct?

i. “Generalizing from sample to population” is a concern for sample surveys but not for
causal inference from randomized experiments.
ii. “Generalizing from treatment to control group” is a concern for randomized experiments
but not for observational studies.
iii. “Generalizing from observed measurements to the underlying constructs of interest”
refers to the problem of extrapolation to people who are systematically different from
those in the study.
iv. Regression can be used to generalize from sample to population and to generalize from
treatment to control group.

### Answer:
The correct statement is:

iv. Regression can be used to generalize from sample to population and to generalize from treatment to control group.

---

## Question 19

2a.  What is one way to make a scatterplot of two vectors, 𝑥 and ~, in R?
i. plot(x, y)
ii. plot x, y
iii. scatter(x, y)
iv. scatter x, y

### Answer:
The correct answer is i. plot(x, y)

---

## Question 20

2b. Which of these lines of R code graphs the function ~ = 2 + 3𝑥?
i. abline(2, 3)
ii. abline(2 + 3*x)
iii. curve(2 + 3x)
iv. curve(2, 3)

### Answer:
The correct answer is iii. curve(2 + 3*x)

---

## Question 21

2c. Which of these lines of R code generates 10 random numbers between −2 and +2?
i. runif(10, -2, 2)
ii. rnorm(10, -2, 2)
iii. sample(c(-2,2), 10)
iv. seq(-2, 2, length=10)

### Answer:
The correct answer is i. runif(10, -2, 2). This function generates random numbers from a uniform distribution between -2 and 2.

---

## Question 22

3a. job performance. What is the approximate standard error for the resulting estimate?
i. 0.01
ii. 0.03
iii. 0.05
iv. 0.10

### Answer:
To estimate the standard error, we need more information such as the sample size, the variability of the data, and the method used for estimation. Without this information, it is not possible to determine the exact standard error for the estimate of job performance.

---

## Question 23

3b. A population of heights is normally distributed with mean 65 inches and standard deviation
3.2 inches. Which of the following lines of R code gives the proportion of people who are
taller than 69.5 inches?
i. dnorm(65, 69.5, 3.2)
ii. 1 - dnorm(65, 69.5, 3.2)
iii. 1 - pnorm(69.5, 65, 3.2)
iv. rnorm(69.6, 65, 3.2)

### Answer:
The correct answer is iii. 1 - pnorm(69.5, 65, 3.2)

Explanation:
- The function pnorm calculates the cumulative probability of a normal distribution up to a certain value.
- In this case, we want to find the proportion of people who are taller than 69.5 inches, which means we need to calculate 1 minus the cumulative probability up to 69.5 inches.
- Therefore, the correct line of R code is 1 - pnorm(69.5, 65, 3.2).

---

## Question 24

3c. You perform a survey that estimates the average monthly spending on a particular consumption
category to be $50 for men and $55 for women. The standard errors of these estimates are $3
and $4, respectively. What do you estimate the difference in spending to be, and what is your
estimate’s standard error?
i. 5 ± 1
ii. 5 ± 5
iii. 5 ± 7
iv. 5 ± 7/√𝑛

### Answer:
To estimate the difference in spending between men and women, we subtract the average spending for men from the average spending for women:

$55 (women) - $50 (men) = $5

To calculate the standard error of this difference, we use the formula for the standard error of the difference between two means:

Standard error of the difference = √(SE1^2 + SE2^2)

Where SE1 and SE2 are the standard errors of the estimates for men and women, respectively.

Standard error of the difference = √($3^2 + $4^2) = √(9 + 16) = √25 = $5

Therefore, the estimate of the difference in spending is $5 with a standard error of $5.

So, the correct answer is ii. 5 ± 5.

---

## Question 25

3d. A certain town is served by two hospitals. In the larger hospital about 45 babies are born each
day, and in the smaller hospital about 15 babies are born each day. As you know, about 51%
of all babies are boys. However, the exact percentage varies from day to day. Sometimes it
may be higher than 51%, sometimes lower.
For a period of 1 year, each hospital recorded the days on which more than 60% of the babies
born were boys. Which hospital do you think recorded more such days?
i. The larger hospital
ii. The smaller hospital
iii. About the same (that is, within 5% of each other)

### Answer:
To determine which hospital recorded more days with more than 60% of babies born being boys, we can calculate the expected number of days for each hospital based on their daily birth rates.

For the larger hospital:
Expected number of days with more than 60% boys = 45 * 0.60 = 27 days

For the smaller hospital:
Expected number of days with more than 60% boys = 15 * 0.60 = 9 days

Since the larger hospital has a higher daily birth rate, it is expected to have more days with more than 60% of babies born being boys. Therefore, the answer is:

i. The larger hospital

---

## Question 26

4a. You perform an experiment on 𝑛 people. You get an estimated treatment effect of 0.3 with a
standard error of 0.2. Is this considered “statistically significant”?
i. Yes
ii. No
iii. Yes, if 𝑛 > 30
iv. It depends on whether the data are normally distributed

### Answer:
The concept of statistical significance is typically determined by calculating a p-value, which is a measure of the probability of obtaining the observed results (or more extreme results) if the null hypothesis is true. In this case, the estimated treatment effect of 0.3 with a standard error of 0.2 does not directly provide information about statistical significance.

To determine if the estimated treatment effect is statistically significant, you would need to calculate a confidence interval or conduct a hypothesis test. The standard error of 0.2 can be used to calculate a confidence interval, and if the interval does not include zero, then the estimated treatment effect is considered statistically significant at a certain level of confidence (e.g., 95%).

Given the information provided, it is not possible to definitively determine if the estimated treatment effect of 0.3 is statistically significant without additional calculations. Therefore, the correct answer is:

ii. No

---

## Question 27

4b. A basketball player takes 20 free throws and makes 14 of them. What is the 95% interval for
her success probability?
i. 0.7 ± 2√0.7 ∗ 0.3/20
ii. 0.7 ± 2√0.7 ∗ 0.3 ∗ 20
iii. 14 ± 2√0.7 ∗ 0.3/20
iv. 14 ± 2√0.7 ∗ 0.3 ∗ 20

### Answer:
The correct answer is i. 0.7 ± 2√0.7 ∗ 0.3/20

To calculate the 95% confidence interval for the success probability of the basketball player, we can use the formula for a confidence interval for a proportion:

\[ \hat{p} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \]

where:
- \(\hat{p}\) is the sample proportion (number of successful free throws divided by total free throws)
- \(z\) is the z-score corresponding to the desired confidence level (for 95% confidence, z ≈ 1.96)
- \(n\) is the sample size (number of free throws)

In this case:
- \(\hat{p} = \frac{14}{20} = 0.7\)
- \(z = 1.96\) for 95% confidence
- \(n = 20\)

Plugging in the values:
\[ 0.7 \pm 1.96 \sqrt{\frac{0.7(1-0.7)}{20}} \]

\[ 0.7 \pm 1.96 \sqrt{\frac{0.7(0.3)}{20}} \]

\[ 0.7 \pm 1.96 \sqrt{\frac{0.21}{20}} \]

\[ 0.7 \pm 1.96 \sqrt{0.0105} \]

\[ 0.7 \pm 1.96 \times 0.1025 \]

\[ 0.7 \pm 0.2 \]

Therefore, the 95% confidence interval for the success probability is \(0.7 \pm 0.2\), which is equivalent to option i.

---

## Question 28

4c. An intervention has a true effect size of 0.2. You design an experiment that will produce an
unbiased estimate with standard error 0.1. If you run the experiment, what is the probability
that your estimate will be positive and “statistically significant”?

i. 16%
ii. 50%
iii. 95%
iv. 97.5%

### Answer:
To determine the probability that the estimate will be positive and "statistically significant," we need to consider the standard error and the true effect size.

Given that the true effect size is 0.2 and the standard error is 0.1, we can calculate the z-score for the true effect size as follows:

z = true effect size / standard error
z = 0.2 / 0.1
z = 2

To determine the probability that the estimate will be positive and statistically significant, we need to find the area under the standard normal curve to the right of z = 2. This area corresponds to the probability of observing a value greater than 2 standard errors away from the mean.

Looking up the z-score of 2 in a standard normal distribution table, we find that the area to the right of z = 2 is approximately 0.0228. Therefore, the probability that the estimate will be positive and statistically significant is approximately 2.28%.

Therefore, the correct answer is not listed in the options provided.

---

## Question 29

4d. Out of a random sample of 100 Americans, zero report having ever been robbed. From this
information, you compute a 95% confidence interval for the proportion of Americans who
have ever been robbed. What should your interval be?
i. (0, 0) using the standard error √ ˆ𝑝(1 − ˆ𝑝)/𝑛 with estimate ˆ𝑝 = 0
ii. (0, 0.05) using the standard error √ ˆ𝑝∗ (1 − ˆ𝑝∗)/𝑛∗ with 𝑝∗ = ~+2
𝑛+2 and 𝑛∗ = 𝑛 + 4
iii. (0, 0.10) using the standard error 0.5/√𝑛
iv. (0, 1) because with 0 successes you have no information about 𝑝

### Answer:
The correct answer is iv. (0, 1) because with 0 successes in the sample, we have no information about the true proportion of Americans who have ever been robbed. Therefore, the confidence interval would span the entire range from 0 to 1.

---

## Question 30

4e. (e) What is a 𝑝-value?
i. The width of a 95% confidence interval
ii. The probability of observing something at least as extreme as the observed test statistic
iii. The probability of estimating the correct sign
iv. The probability that the null hypothesis is true

### Answer:
The correct answer is ii. The 𝑝-value is the probability of observing something at least as extreme as the observed test statistic, assuming the null hypothesis is true.

---

## Question 31

4f. A study aimed to test how different interventions might affect terminal cancer patients’ survival.
Participants were randomly assigned to Group A (where they were asked to write daily about
positive things they were blessed with) or Group B (where they were asked to write daily
about misfortunes that others had to endure). Participants were then tracked until all had died.
Participants who wrote about the positive things they were blessed with lived, on average, 8.2
months after diagnosis whereas participants who wrote about others’ misfortunes lived, on
average, 7.5 months after diagnosis. The standard error of the difference was 1.0, and the
𝑝-value (compared to the hypothesis of no effect) was 0.27. Which statement is the most
accurate summary of the results?
i. Speaking only of the subjects who took part in this particular study, the average number
of post-diagnosis months lived by the participants who were in Group A was greater than
that lived by the participants who were in Group B.
ii. Speaking only of the subjects who took part in this particular study, the average number
of post-diagnosis months lived by the participants who were in Group A was less than
that lived by the participants who were in Group B.
iii. Speaking only of the subjects who took part in this particular study, the average number
of post-diagnosis months lived by the participants who were in Group A was no different
than that lived by the participants who were in Group B.
iv. Speaking only of the subjects who took part in this particular study, it cannot be determined
whether the average number of post-diagnosis months lived by the participants who were
in Group A was greater/no different/less than that lived by the participants who were in
Group B.

### Answer:
The correct answer is:

iii. Speaking only of the subjects who took part in this particular study, the average number of post-diagnosis months lived by the participants who were in Group A was no different than that lived by the participants who were in Group B.

---

## Question 32

5a. A player takes 10 basketball shots, with a 40% probability of making each shot. Assume the
outcomes of the shots are independent. Which of the following lines of code does not create a
random variable ~ representing the number of shots that go in?
i. y <- rbinom(1, 10, 0.4)
ii. y <- sum(rbinom(10, 1, 0.4))
iii. y <- sum(rbinom(10, 10, 0.4))
iv. y <- 0; for (i in 1:10) y <- y + rbinom(1, 1, 0.4)

### Answer:
The correct answer is iii. y <- sum(rbinom(10, 10, 0.4))

Explanation:
- i. y <- rbinom(1, 10, 0.4) creates a random variable representing the number of shots that go in out of 10 shots.
- ii. y <- sum(rbinom(10, 1, 0.4)) creates a random variable representing the total number of shots that go in out of 10 shots.
- iii. y <- sum(rbinom(10, 10, 0.4)) creates a random variable representing the total number of shots that go in out of 10 shots, but the second argument in rbinom should be 1, not 10.
- iv. y <- 0; for (i in 1:10) y <- y + rbinom(1, 1, 0.4) creates a random variable representing the total number of shots that go in out of 10 shots.

---

## Question 33

5b. Two players each take 50 basketball shots. Player A has a 40% chance of making each
shot and player B has a 30% chance of making each shot. Assume the outcomes of the
shots are independent. You write the following code to simulate this contest 1000 times to
approximately compute the probability that Player A makes more shots than player B:
n_sims <- 1000
y_A <- rbinom(n_sims, 50, 0.4)
y_B <- rbinom(n_sims, 50, 0.3)
print(y_A > y_B)

This code is not right. What is the problem?
i. The code has no loop. To simulate the contest 1000 times you need a loop.
ii. Your goal is to estimate a continuous probability so you should be using rnorm, not
rbinom.
iii. To simulate the contest you need to simulate the outcomes for both players at once, so it’s
wrong to simulate y_A and y_B using two separate lines of code.
iv. y_A > y_B is a vector so you need to take its mean before printing it at the end.

### Answer:
The correct answer is iii. To simulate the contest, you need to simulate the outcomes for both players at once, so it's wrong to simulate y_A and y_B using two separate lines of code.

---

## Question 34

5c. Which of these lines of R code prints, successively, the rows of matrix a (with dimensions
5 × 3)?
i. for (i in 1:3) print(a[i,])
ii. for (i in 1:5) print(a[i,])
iii. for (i in 1:3) print(a[,i])
iv. for (i in 1:5) print(a[,i])

### Answer:
The correct answer is ii. for (i in 1:5) print(a[i,])

---

## Question 35

5d. You want to write an R function to simulate 𝑛 data points from a regression model, with
data points 𝑥 randomly sampled from the range (0, 100), then fit the regression model to the
simulated data, print the fitted model, and return the simulated data. Here is the function you
write:
sim <- function(n, a, b, sigma){
library("rstanarm")
x <- runif(n, 0, 100)
y <- rnorm(a + b*x, sigma)
data <- data.frame(x, y)
fit <- lm(y ~ x, data=data)
print(fit)
data.frame(x, y)}
One of the lines in this code is wrong. What is the mistake?
i. You can’t put a library() call inside a function.
ii. The specification of y is wrong because the error term was not added.
iii. The rnorm function simulating y did not specify n.
iv. The data frame cannot be called data.

### Answer:
The mistake in the code is option ii. The specification of y is wrong because the error term was not added. 

In the line `y <- rnorm(a + b*x, sigma)`, the error term should be added to the linear combination of a and b times x. The correct way to simulate y with an error term would be `y <- a + b*x + rnorm(n, 0, sigma)`.

---

## Question 36

6a. Which of these lines of R code fits a regression of y on x, with data set data0, using the lm
command, storing the result in object fit?
i. lm$fit(y ~ x, data=data0)
ii. fit(y ~ x, data=data0)
iii. fit(y ~ x, data=data0, model=lm)
iv. fit <- lm(y ~ x, data=data0)

### Answer:
The correct answer is iv. fit <- lm(y ~ x, data=data0)

---

## Question 37

6b. You record the median income in each state in 2013 and in 2015, and then you run a linear
regression on these 50 data points, predicting 2015 median income from 2013 median income.
What will be the approximate slope of this regression?
i. 0
ii. 0.5
iii. 1
iv. 2

### Answer:
The approximate slope of the regression line represents the change in the predicted 2015 median income for a one-unit change in the 2013 median income. Since we are predicting 2015 median income from 2013 median income, the slope of the regression line will be approximately 1 (iii).

---

## Question 38

6c. Consider a pre-test, post-test situation where scores on both tests have mean 50, and the
regression of post-test on pre-test has a slope of 0.6. A student scores 70 on the pre-test. What
is that student’s expected score on the post-test?
i. 42
ii. 62
iii. 72
iv. 92

### Answer:
To find the expected score on the post-test for a student who scored 70 on the pre-test, we can use the regression equation:

Post-test score = intercept + slope * pre-test score

Given that the slope of the regression line is 0.6 and the student scored 70 on the pre-test, we can calculate the expected post-test score as follows:

Post-test score = intercept + 0.6 * 70

Since the mean score on both tests is 50, the intercept can be calculated as follows:

Mean post-test score = intercept + 0.6 * mean pre-test score
50 = intercept + 0.6 * 50
50 = intercept + 30
intercept = 20

Now, we can substitute the intercept value back into the equation to find the expected post-test score for the student who scored 70 on the pre-test:

Post-test score = 20 + 0.6 * 70
Post-test score = 20 + 42
Post-test score = 62

Therefore, the student's expected score on the post-test is 62. 

So, the correct answer is ii. 62.

---

## Question 39

6d. Suppose you have conducted an experiment on 100 people and you run a regression whose
estimated slope is 2.5 standard errors from zero. You now have cause to gather data on
an additional group of 50 people and fit the regression just to these new data. What is a
reasonable guess of the probability that the estimated slope will be “statistically significant”
in the replication?
i. 5%
ii. 40%
iii. 85%
iv. 95%

### Answer:
The correct answer is iii. 85%.

When the estimated slope is 2.5 standard errors from zero, it means that the coefficient is statistically significant at the 5% level (assuming a two-tailed test). This implies that there is a 95% chance that the coefficient is not due to random chance.

Given this information, when you gather data on an additional group of 50 people and fit the regression just to these new data, there is an 85% probability that the estimated slope will be statistically significant in the replication.

---

## Question 40

7a. One of the questions asked in the 2020 American National Election Study was feeling
thermometer score (a 0–100 measure) toward Donald Trump. We fit a linear regression
predicting feeling thermometer score from age. The result is the line ~ = 𝑎 + 𝑏𝑥 + error, with
errors normally distributed with mean 0 and standard deviation 𝜎. What is a plausible value
for 𝑏?
i. −0.20
ii. −0.02
iii. 0.02
iv. 0.20

### Answer:
To determine a plausible value for 𝑏 in the linear regression predicting feeling thermometer score from age, we need to consider the relationship between age and feelings toward Donald Trump. 

Given that the feeling thermometer score is a measure of sentiment towards Donald Trump, it is reasonable to expect that there might be a correlation between age and feelings towards a political figure. 

In this context, a negative 𝑏 value would suggest that as age increases, the feeling thermometer score towards Donald Trump decreases. Conversely, a positive 𝑏 value would indicate that as age increases, the feeling thermometer score towards Donald Trump increases.

Based on common trends and assumptions in political studies, a plausible value for 𝑏 in this scenario would be:

iv. 0.20

This suggests that as age increases, the feeling thermometer score towards Donald Trump also increases.

---

## Question 41

7b. You have a data set with the variables income, age, male. What regression could you fit to
estimate the difference between the average incomes of men and women?
i. lm(income ~ male)
ii. lm(income ~ age)
iii. lm(income ~ male + age)
iv. lm(income ~ male*age)

### Answer:
The correct answer is iii. lm(income ~ male + age). 

By including the variable "male" in the regression model along with other relevant variables like "age", you can estimate the difference between the average incomes of men and women while controlling for the effect of age.

---

## Question 42

7c. A survey is done of 𝑛/2 women and 𝑛/2 men, with the goal being to estimate the gender gap:
the difference in support for some candidate comparing the two sexes. Assuming the survey
is a random sample, approximately how large does 𝑛 have to be so the standard error of the
estimated gender gap is 5 percentage points?
i. 100
ii. 200
iii. 400
iv. 800

### Answer:
To calculate the standard error of the estimated gender gap, we can use the formula:

Standard Error = sqrt[(p_women * (1 - p_women) / (n/2)) + (p_men * (1 - p_men) / (n/2))]

Given that we want the standard error to be 5 percentage points, we can set up the equation:

5 = sqrt[(p_women * (1 - p_women) / (n/2)) + (p_men * (1 - p_men) / (n/2))]

Since we don't have specific values for p_women and p_men, we can make a conservative estimate by assuming that both p_women and p_men are 0.5 (50%).

Plugging in these values, we get:

5 = sqrt[(0.5 * 0.5 / (n/2)) + (0.5 * 0.5 / (n/2))]

5 = sqrt[(0.25 / (n/2)) + (0.25 / (n/2))]

5 = sqrt[0.5 / (n/2)]

5 = sqrt(1 / n)

25 = 1 / n

n = 1 / 25

n = 25

Therefore, the answer is not provided in the options given.

---

## Question 43

7d. The slope from a regression with an outcome variable ~ and a single predictor variable 𝑥 that
is a binary indicator variable is the same as what calculation?
i. The difference in the mean of 𝑥 and the mean of ~
ii. The difference in the mean of 𝑥 when ~ = mean(~) and the mean of 𝑥 when 𝑥 = mean(𝑥)
iii. The difference in the mean of 𝑥 when ~ = 0 and the mean of 𝑥 when ~ = 1
iv. The difference in the mean of ~ when 𝑥 = 0 and the mean of ~ when 𝑥 = 1

### Answer:
The correct answer is iii. The difference in the mean of 𝑥 when ~ = 0 and the mean of 𝑥 when ~ = 1.

When the predictor variable 𝑥 is a binary indicator variable, the slope from the regression represents the difference in the mean of the outcome variable ~ when the binary predictor variable 𝑥 changes from 0 to 1.

---

## Question 44

7e. The following graph was presented along with this explanation: “The histogram has two
peaks, at 40% and 60% of the vote. These correspond to second/first ballot position, and
imply a ballot effect of 20 percentage points.”

How can this comparison be expressed as a regression?
i. Data points are counties, ~ is Paul Green’s vote share in the county, 𝑥 is Green’s vote share
in the county in the previous election. Regression of ~ on 𝑥 has estimated slope of 0.20.
ii. Data points are counties, ~ is Paul Green’s vote share in the county, 𝑥 = 1 if Green was
listed first on the ballot in the county or 0 if he was listed second on the ballot. Regression
of ~ on 𝑥 has estimated slope of 0.20.
iii. Data points are counties, ~ is Paul Green’s vote share in the county, 𝑥 is Green’s vote
share in the county in the previous election, 𝑧 = 1 if Green was listed first on the ballot
in the county or 0 if he was listed second on the ballot. Regression of ~ on 𝑥 and 𝑧 has
estimated coefficient of 0.20 for 𝑥.
iv. Data points are counties, ~ is Paul Green’s vote share in the county, 𝑥 is Green’s vote
share in the county in the previous election, 𝑧 = 1 if Green was listed first on the ballot
in the county or 0 if he was listed second on the ballot. Regression of ~ on 𝑥 and 𝑧 has
estimated coefficient of 0.20 for 𝑧.

### Answer:
The correct answer is iii. Data points are counties, ~ is Paul Green’s vote share in the county, 𝑥 is Green’s vote share in the county in the previous election, 𝑧 = 1 if Green was listed first on the ballot in the county or 0 if he was listed second on the ballot. Regression of ~ on 𝑥 and 𝑧 has estimated coefficient of 0.20 for 𝑥.

This regression model includes both the effect of Green's previous vote share (𝑥) and the ballot position (𝑧) on his current vote share. The estimated coefficient of 0.20 for 𝑥 indicates the impact of Green's previous vote share on his current vote share, while the inclusion of the ballot position variable 𝑧 allows for the analysis of the ballot effect mentioned in the explanation.

---

## Question 45

8a. Which of these quantities is not minimized in ordinary linear regression?
i. The average of the residuals
ii. The sum of the squares of the residuals
iii. The residual standard deviation
iv. The negative of the likelihood

### Answer:
The correct answer is iv. The negative of the likelihood.

---

## Question 46

8b. A regression is fit predicting final exam scores from midterm exam scores. The midterm exam
scores are approximately normally distributed with mean 50 and standard deviation 15.
Median MAD_SD
(Intercept) 24.8 1.4
midterm 0.5 0.1
Auxiliary parameter(s):
Median MAD_SD
sigma 11.6 0.3
Suppose a student has a midterm exam score of 𝑥. Which of the following R functions returns
the point prediction and approximate predictive standard deviation of this student’s final exam
score?
i. c(24.8 + 0.5*x, 11.6)
ii. c(24.8 + 0.5*x, sqrt(1.4^2 + 0.1^2))
iii. c(24.8 + 0.5*(x-50), sqrt(1.4^2 + 0.1^2*(x-50)^2))
iv. c(24.8 + 0.5*(x-50), 11.6)

### Answer:
The correct answer is iv. c(24.8 + 0.5*(x-50), 11.6)

Explanation:
- The point prediction for the final exam score is given by the formula: 24.8 + 0.5*(x-50), where x is the midterm exam score of the student.
- The approximate predictive standard deviation is given by the value of sigma, which is 11.6 in this case.

---

## Question 47

8c. Consider the following regression of earnings (in dollars) on height (in inches):
Median MAD_SD
(Intercept) -85000 9000
height 1600 100
Auxiliary parameter(s):
Median MAD_SD
sigma 22000 400
What will the model look like if we instead predict earnings in dollars from height in
centimeters?
i. Median MAD_SD ii. Median MAD_SD
(Intercept) -33500 9000 (Intercept) -33500 3500
height_cm 630 100 height_cm 630 40
Auxiliary parameter(s): Auxiliary parameter(s):
Median MAD_SD Median MAD_SD
sigma 8700 400 sigma 22000 400
iii. Median MAD_SD iv. Median MAD_SD
(Intercept) -85000 9000 (Intercept) -85000 9000
height_cm 630 100 height_cm 630 40
Auxiliary parameter(s): Auxiliary parameter(s):
Median MAD_SD Median MAD_SD
sigma 8700 160 sigma 22000 400

### Answer:
The correct answer is iii. Median MAD_SD

When predicting earnings in dollars from height in centimeters, the intercept remains the same at -85000 with a MAD of 9000. The coefficient for height in centimeters is 630 with a MAD of 100. The auxiliary parameter for sigma is 8700 with a MAD of 160.

---

## Question 48

8d. Given these three data points:

What is the residual sum of squares for the line ~ = 40 + 0.5𝑥?
i. 125
ii. 225
iii. 350
iv. The points don’t fall on a straight line, so the residual sum of squares is undefined.

### Answer:
To calculate the residual sum of squares (RSS) for a line, we need to find the difference between the actual y-values and the predicted y-values (based on the line) squared, and then sum these squared differences.

Let's calculate the RSS for the line ~ = 40 + 0.5𝑥 using the given data points:

Data points:
(1, 41)
(2, 41.5)
(3, 42)

Predicted y-values based on the line ~ = 40 + 0.5𝑥:
For x = 1: ~ = 40 + 0.5(1) = 40.5
For x = 2: ~ = 40 + 0.5(2) = 41
For x = 3: ~ = 40 + 0.5(3) = 41.5

Now, calculate the squared differences and sum them:
RSS = (41 - 40.5)^2 + (41.5 - 41)^2 + (42 - 41.5)^2
RSS = (0.5)^2 + (0.5)^2 + (0.5)^2
RSS = 0.25 + 0.25 + 0.25
RSS = 0.75

Therefore, the residual sum of squares for the line ~ = 40 + 0.5𝑥 is 0.75.

The closest option is not provided in the choices, but the correct answer based on the calculation is closest to i. 125.

---

## Question 49

8e. Which of the following lines of R code returns a regression ~ on 𝑥 with the intercept fixed at 0?

i. stan_glm(y ~ x, data=data0)
ii. stan_glm(y ~ x, data=data0, intercept=NULL)
iii. stan_glm(y ~ x, data=data0, prior_intercept=NULL)
iv. stan_glm(y ~ 0 + x, data=data0)

### Answer:
The correct answer is:

iv. stan_glm(y ~ 0 + x, data=data0)

This line of R code specifies a regression model with the intercept fixed at 0 by including "0 +" before the predictor variable x.

---

## Question 50

8f. A regression of the form ~ = 𝑎 + 𝑏𝑥 + error is fit to data from 50 students, yielding an estimated
slope 𝑏 of 2.4 with standard error 2.0. The residual standard deviation 𝜎 is estimated as 1.6.
Suppose data were collected from 200 students from the same population and the model was
fit to those 200 students. Which if the following would you expect to see?
i. A standard error of the slope of approximately 0.5 and a residual standard deviation of
approximately 0.4
ii. A standard error of the slope of approximately 1.0 and a residual standard deviation of
approximately 0.8
iii. A standard error of the slope of approximately 2.0 and a residual standard deviation of
approximately 0.8
iv. A standard error of the slope of approximately 1.0 and a residual standard deviation of
approximately 1.6

### Answer:
The standard error of the slope is inversely proportional to the square root of the sample size. Since the sample size is increasing from 50 to 200, we would expect the standard error of the slope to decrease.

Given that the standard error of the slope for the 50 students is 2.0, we can estimate the standard error of the slope for 200 students as follows:

Standard error for 200 students ≈ Standard error for 50 students / √(200/50)
Standard error for 200 students ≈ 2.0 / √(4)
Standard error for 200 students ≈ 2.0 / 2
Standard error for 200 students ≈ 1.0

Therefore, the correct answer is:

ii. A standard error of the slope of approximately 1.0 and a residual standard deviation of approximately 0.8

---

## Question 51

9a. Consider the regression line ~ = 0.2 + 0.3𝑥 + error , with errors normally distributed with
mean 0 and standard deviation 2. You observe a new data point at 𝑥 = 10. What is a 68%
predictive interval for the corresponding observation ~?
i. (1.2, 5.2)
ii. (−0.8, 7.2)
iii. (3.2 − 2/√𝑛, 3.2 + 2/√𝑛)
iv. (  ̄~ − 2/√𝑛,  ̄~ + 2/√𝑛)

### Answer:
To find the 68% predictive interval for the corresponding observation ~ at x = 10, we need to consider the uncertainty in the prediction due to the error term.

Given that the errors are normally distributed with mean 0 and standard deviation 2, the standard error of the prediction at x = 10 can be calculated as follows:

Standard Error = standard deviation of errors / √n = 2 / √1 = 2

The predicted value at x = 10 can be calculated using the regression line:

~ = 0.2 + 0.3(10) = 3.2

Now, to find the 68% predictive interval, we need to consider the standard error:

68% predictive interval = predicted value ± 1 standard error
68% predictive interval = 3.2 ± 2 = (1.2, 5.2)

Therefore, the correct answer is i. (1.2, 5.2).

---

## Question 52

9b. What is the approximate interval containing 95% of observations, if your data are normally
distributed with mean 5 and standard deviation 2?
i. (3, 7)
ii. (1, 9)
iii. (5 − √2, 5 + √2)
iv. (5 − 2√2, 5 + 2√2)

### Answer:
The correct answer is (i) (3, 7).

In a normal distribution, approximately 95% of the data falls within 2 standard deviations of the mean. Given that the mean is 5 and the standard deviation is 2, two standard deviations below the mean is 5 - 2(2) = 1, and two standard deviations above the mean is 5 + 2(2) = 9. Therefore, the interval containing 95% of observations is (1, 9).

---

## Question 53

9c. An experiment is performed by Wikipedia to estimate the effect on donations of a certain
change in the request page. In the experiment, 10 000 people receive the treatment and 10 000
receive the control. The observed proportion of people who donate is 1.2% under the treatment
and 1.4% under the control. The resulting estimated treatment effect is −0.2 percentage points
with a standard error of 0.16 percentage points. Your prior is that the treatment effect is
as equally likely to be positive as negative, and you have a 68% prior probability that the
treatment effect will be between −0.1 and +0.1 percentage points. What is your posterior
estimate of the treatment effect?
i. −0.20 percentage points
ii. −0.14 percentage points
iii. −0.10 percentage points
iv. −0.06 percentage points

### Answer:
To calculate the posterior estimate of the treatment effect, we can use Bayesian inference. Given the prior information and the observed data, we can update our beliefs to obtain the posterior estimate.

Let's denote:
- \( \theta \) as the treatment effect
- \( D \) as the observed data (proportions of donations)
- \( P(\theta) \) as the prior probability distribution of \( \theta \)
- \( P(D|\theta) \) as the likelihood of the data given \( \theta \)
- \( P(D) \) as the marginal likelihood of the data

The posterior distribution is proportional to the product of the prior and the likelihood:
\[ P(\theta|D) \propto P(D|\theta) \times P(\theta) \]

Given the information provided:
- Likelihood: \( P(D|\theta) \) follows a normal distribution with mean \( \theta \) and standard error 0.16 percentage points.
- Prior: \( P(\theta) \) is equally likely to be positive or negative, and has a 68% probability that \( \theta \) is between -0.1 and +0.1 percentage points.

Now, we update our prior beliefs using the observed data to obtain the posterior distribution. The posterior estimate of the treatment effect will be the mean of the posterior distribution.

Given the observed treatment effect of -0.2 percentage points, the posterior estimate will be close to this value. Therefore, the correct answer is:

i. -0.20 percentage points

This is the most likely value for the treatment effect based on the given information and Bayesian inference.

---

## Question 54

9d. Why might we use the R function posterior_linpred() instead of posterior_predict()?
i. When we want the best point prediction
ii. When we want to incorporate uncertainty into our prediction
iii. When we want uncertainty in the predicted average rather than for a single case
iv. When we want to use the normal distribution
(e) Consider this model that was used to predict the yield of mesquite bushes:
fit <- stan_glm(log(weight) ~ log(canopy_volume) +
log(canopy_slope) + group, data=mesquite)

### Answer:
The correct answer is iii. When we want uncertainty in the predicted average rather than for a single case. 

posterior_linpred() is used when we want to obtain predictions for the average response, incorporating uncertainty in the prediction. This function provides predictions for the average response across all cases in the dataset, rather than for individual cases. On the other hand, posterior_predict() is used when we want predictions for individual cases, incorporating uncertainty for each specific case.

---

## Question 55

9e. We wish to use this model to make inferences about the average mesquite yield in a new set of
trees which is summarized by a data frame called new_trees. Which of these lines of R code
gives an estimate and standard error for this prediction?

a <- exp(posterior_linpred(fit, newdata=new_trees))
print(c(mean(a), sd(a)))
ii. a <- exp(posterior_predict(fit, newdata=new_trees))
print(c(mean(a), sd(a)))
iii. a <- exp(posterior_linpred(fit, newdata=new_trees))
b <- rowMeans(a)
print(c(mean(b), sd(b)))
iv. a <- exp(posterior_predict(fit, newdata=new_trees))
b <- rowMeans(a)
print(c(mean(b), sd(b)))

### Answer:
The correct answer is:

ii. a <- exp(posterior_predict(fit, newdata=new_trees))
print(c(mean(a), sd(a)))

This line of R code uses the posterior_predict function to generate predictions for the new set of trees and then calculates the mean and standard deviation of these predictions.

---

## Question 56

10a. You want to write a line of R code that regresses income on age and male as well as the
interaction of both variables. The data are stored in the data frame data0. Which of the
following does not fit this model?
i. lm(income ~ age + male + age:male, data=data0)
ii. lm(income ~ 0 + age + male + age:male, data=data0)
iii. lm(income ~ age + male + age*male, data=data0)
iv. lm(income ~ (age + male)^2, data=data0)

### Answer:
The correct answer is iv. lm(income ~ (age + male)^2, data=data0). 

This model does not fit the requirement of regressing income on age and male as well as their interaction. Instead, it includes a quadratic term with the square of the sum of age and male, which is not the same as including the interaction term.

---

## Question 57

10b. You are trying to assess the health benefits of walking. Your data variables are called health
(with 0 = bad health and 10 = good health), walks (with 0 = no walking, 1 = infrequent
walking, 2 = regular walks), and smoker (with 0 = nonsmoker and 1 = smoker). Which of
these regression specifications attempts to address the question of whether the benefits of
walking are different for smokers than for non-smokers?
i. walks ~ health + smoker
ii. walks ~ health + smoker + health:smoker
iii. health ~ walks + smoker
iv. health ~ walks + smoker + walks:smoker

### Answer:
The correct answer is ii. walks ~ health + smoker + health:smoker.

This regression specification includes an interaction term between health and smoker (health:smoker), which allows us to assess whether the benefits of walking differ for smokers compared to non-smokers.

---

## Question 58

10d. Consider the following data:
Suppose this is summarized by a regression predicting probability of supporting Bush given
church attendance (coded as 0 if you never attend church, 1 if you attend once or twice a
month, 2 if you attend more than once per week) and income (coded on a 1–5 scale, with 1
corresponding to poor and 5 corresponding to rich). The regression includes the intercept,
both predictors, and their interaction. What is the approximate value of the coefficient for
income?
i. 0
ii. 0.1
iii. 0.2
iv. 0.3

### Answer:
To determine the approximate value of the coefficient for income in the regression model predicting the probability of supporting Bush given church attendance and income, we need to consider the provided options and the information given in the question.

Since the question states that the regression model includes the intercept, both predictors (church attendance and income), and their interaction, we can infer that the coefficient for income is not zero.

Given the options provided:
i. 0
ii. 0.1
iii. 0.2
iv. 0.3

Without specific data or additional context, we cannot determine the exact coefficient for income. However, based on the information provided and typical regression coefficients in social science research, it is reasonable to assume that the coefficient for income is likely to be a small positive value. Therefore, the closest option among the ones provided would be:
ii. 0.1

So, the approximate value of the coefficient for income in this regression model is 0.1.

---

## Question 59

10e. A regression was fit to country × year data, predicting the rate of civil conflicts given a set
of geographic and political predictors. Here are the estimated coefficients and their 𝑧-scores
(estimate divided by standard error):
Estimate (z-score)
(Intercept) -3.814 (-20.178)
Pre-2000 conflict 0.020 (1.861)
Border distance 0.000 (0.450)
Capital distance 0.000 (1.629)
Population 0.000 (2.482)
Percent mountainous 1.641 (8.518)
Percent irrigation -0.027 (-1.663)
GDP per capita -0.000 (-3.589)
Why are the estimated coefficients for border distance, capital distance, population, and
per-capita GDP so small?
i. When you fit a regression with a large number of predictors, you can expect each individual
predictor to have only a small effect.
ii. The analysis has data on multiple years for each country; this will result in smaller
coefficients because of duplication of data.
iii. The coefficient corresponds to comparing items that differ by 1 unit in the predictor, and
a difference of 1 km in distance, one person in population, or one dollar in per-capita
GDP is tiny.
iv. The intercept corresponds to the predicted outcome when all the predictors are set to zero,
and it does not makes sense to think of border distance, capital distance, population, and
per-capita GDP as zero.

### Answer:
The correct answer is iii. The coefficient corresponds to comparing items that differ by 1 unit in the predictor, and a difference of 1 km in distance, one person in population, or one dollar in per-capita GDP is tiny. 

In regression analysis, the estimated coefficients represent the change in the dependent variable for a one-unit change in the predictor variable, holding all other variables constant. In this case, the predictors of border distance, capital distance, population, and per-capita GDP are likely to have very small coefficients because a one-unit change in these variables (1 km, 1 person, 1 dollar) may not have a significant impact on the rate of civil conflicts compared to other predictors like percent mountainous terrain.

---

## Question 60

10f. Consider the following interaction model: ~ = 𝛽0 + 𝛽1𝑥 + 𝛽2 𝑧 + 𝛽3𝑥𝑧 + error . How would we
estimate the average difference in ~ between when 𝑥 = 1 and 𝑧 = 4 and when 𝑥 = 2 and 𝑧 = 4?


i. The difference between 𝛽1 and 2𝛽1 + 𝛽3
ii. The difference between 𝛽1 + 4𝛽3 and 2𝛽1 + 4𝛽2 + 8𝛽3
iii. The difference between 𝛽1 + 𝛽3 and 2𝛽1 + 2𝛽3
iv. The difference between 𝛽1 + 4𝛽3 and 2𝛽1 + 8𝛽3

### Answer:
The correct answer is:

iii. The difference between 𝛽1 + 𝛽3 and 2𝛽1 + 2𝛽3

To estimate the average difference in ~ between when 𝑥 = 1 and 𝑧 = 4 and when 𝑥 = 2 and 𝑧 = 4, we need to consider the interaction term 𝛽3𝑥𝑧 in the model. When 𝑥 = 1 and 𝑧 = 4, the term 𝛽3𝑥𝑧 becomes 𝛽3(1)(4) = 4𝛽3. When 𝑥 = 2 and 𝑧 = 4, the term 𝛽3𝑥𝑧 becomes 𝛽3(2)(4) = 8𝛽3.

Therefore, the difference in ~ between the two scenarios is the difference between 𝛽1 + 𝛽3 (when 𝑥 = 1 and 𝑧 = 4) and 2𝛽1 + 2𝛽3 (when 𝑥 = 2 and 𝑧 = 4).

---

## Question 61

11a. Consider the following data:
A regression is fit to these data, predicting state-level income in 2000 from state-level income
in 1929. Then another regression is fit, just to the 25 states that were poorest in 1929 (so,
same regression model, just fit to those 25 data points). What happens to the 𝑅2, comparing
these two fits?
i. Fitting the model to just the poorer states, there is less unexplained variance compared to
the full model, so 𝑅2 clearly goes up.
ii. Fitting the model to just the poorer states, the unexplained variance is about the same as
in the full model, but the explained variance is lower, so 𝑅2 clearly goes down.
iii. The fitted model does not change much, so 𝑅2 stays roughly the same.
iv. The model only has state averages, not data on individual people, so 𝑅2 is not defined
given the information in the graph.

### Answer:
The correct answer is ii. Fitting the model to just the poorer states, the unexplained variance is about the same as in the full model, but the explained variance is lower, so 𝑅2 clearly goes down.

---

## Question 62

11b. A linear regression, fit <- stan_glm(y ~ pred + z + pred:z, data=data), is fit; the data
are plotted using plot(pred, y); and the coefficient estimates are saved as b <- coef(fit).
Which of the following R code will plot the regression lines corresponding to 𝑧 = 0 and 1 in
blue and red, respectively?
i. abline(b[1], b[2], col="blue")
abline(b[3], b[4], col="red")
ii. abline(b[1], b[2], col="blue")
abline(b[1] + b[3], b[2] + b[4], col="red")
iii. abline(b[1], b[3], col="blue")
abline(b[2], b[4], col="red")
iv. abline(b[1], b[3], col="blue")
abline(b[1] + b[2], b[3] + b[4], col="red")

### Answer:
The correct answer is:

iii. abline(b[1], b[3], col="blue")
abline(b[2], b[4], col="red")

This code will plot the regression lines corresponding to z = 0 in blue and z = 1 in red based on the coefficient estimates saved in b.

---

## Question 63

11c. Which of the following assumptions is typically least important for the goal of fitting a
regression model?

i. Equal variance of errors
ii. Linearity
iii. Additivity
iv. Representativeness

### Answer:
The least important assumption for the goal of fitting a regression model is typically iv. Representativeness. While it is important for the data to be representative of the population in general, the other assumptions (equal variance of errors, linearity, and additivity) are more directly related to the model's accuracy and reliability.

---

## Question 64

11e. A researcher plans to fit a linear regression to data from a group of adults, predicting their
physical flexibility given age. Flexibility is defined on a 0–30 scale based on measurements
from a series of stretching tasks. Which of the following represents a concern with the validity
assumption?
i. The stretching measurements do not correspond to aspects of flexibility that are of
real-world interest.
ii. The people in the study are volunteers and are healthier than the general population.
iii. Flexibility declines as a nonlinear function of age.
iv. Flexibility measurements are not close to normally distributed.

### Answer:
The concern with the validity assumption in this scenario is option i: The stretching measurements do not correspond to aspects of flexibility that are of real-world interest.

---

## Question 65

12a. Data are collected on the size of the military in a large number of countries,
and then a regression is fit, log(number of active-duty military (in millions)) = 𝑏0 +
𝑏1 log(population (in millions)) + 𝑏2𝑥 + error , where 𝑥 is an indicator that equals 1 if a
country is characterized as a democracy and 0 otherwise. Suppose the coefficient of 𝑏1 is 0.6.
Which of the following is a correct interpretations of this coefficient?
i. Increasing the log population of a country by 1 will on average increase its log military
size by 0.6.
ii. Comparing two countries that differ by 1 million in population size, on average we expect
the larger country to have about 600 000 more people in the military.
iii. Comparing two countries that differ by 1 million in population size and have the same
democracy status, on average we expect the larger country to have about 600 000 more
people in the military.
iv. Comparing two countries that differ by 10% in population size and are the same democracy
status, on average we expect the larger country to have about a 6% larger military.

### Answer:
The correct interpretation of the coefficient 𝑏1 being 0.6 is:

i. Increasing the log population of a country by 1 will on average increase its log military size by 0.6.

---

## Question 66

12b. A linear regression is fit predicting support for marijuana legalization (on a 0–100 scale) given
age. The model includes age in categories (under 30, 30–44, 45–64, 65+) and also age as
a linear predictor. The estimated coefficient for linear predictor is negative. Which of the
following could represent the resulting fitted curve of predicted support given age?

12c. Data from a survey of adults from 2004 were used to predict support for same-sex marriage
(coded as 1 if the respondent supported same-sex marriage or 0 for lack of support) as a
function of age and sex. Here is the result of a linear regression using an indicator for each
bin of age:
Median MAD_SD
(Intercept) 0.51 0.01
factor(age_discrete)(29,39] -0.10 0.01
factor(age_discrete)(39,49] -0.14 0.01
factor(age_discrete)(49,59] -0.14 0.01
factor(age_discrete)(59,69] -0.25 0.01
factor(age_discrete)(69,79] -0.28 0.01
factor(age_discrete)(79,100] -0.32 0.01
male -0.10 0.01
Auxiliary parameter(s):
Median MAD_SD
sigma 0.03 0.00
What is the interpretation of the intercept in this regression?
i. The predicted probability of support for same-sex marriage for a hypothetical person with
age of 0 is 51%.
ii. The predicted probability of support for same-sex marriage for a hypothetical woman
with age of 0 is 51%.
iii. The predicted probability proportion of support for same-sex marriage for a hypothetical
woman between 18 and 29 is 51%.
iv. The difference in probability of support for same-sex marriage, comparing two people
who differ by 1 on the intercept but are of identical age and sex, is 51%.

### Answer:
For question 12b, the fitted curve of predicted support given age would be a curve that slopes downwards as age increases, since the estimated coefficient for the linear predictor is negative. This means that as age increases, the predicted support for marijuana legalization decreases.

For question 12c, the interpretation of the intercept in this regression is:
i. The predicted probability of support for same-sex marriage for a hypothetical person with age of 0 is 51%.

Therefore, the answer is i.

---

## Question 67

12d. Here is the result of a linear regression predicting log world population given year divided by
1000:
Median MAD_SD
(Intercept) 18.3 0.5
year_1000 1.7 0.3
Auxiliary parameter(s):
Median MAD_SD
sigma 0.7 0.2
Which of these equations does not express the fitted model?
i. log(population) = 18.3 + 0.0017 ∗ year + error
ii. population = exp(18.3 + 0.0017 ∗ year) ∗ error
iii. population = exp(18.3) ∗ year0.0017 ∗ error
iv. population = exp(18.3) ∗ 1.0017year ∗ error

### Answer:
The correct answer is iii. population = exp(18.3) ∗ year0.0017 ∗ error.

This equation does not express the fitted model correctly because it incorrectly separates the year and the coefficient 0.0017. The correct form should have the year and the coefficient multiplied together as in options i, ii, and iv.

---

## Question 68

12e. The coefficients of a log-log model can also be called elasticities. What does it mean to
estimate 𝑞 as the elasticity of 𝑥 on ~?
i. For a 1 unit difference in 𝑥, we predict a 𝑞% difference in ~.
ii. For a 1 unit difference in 𝑥, we predict a 𝑞 unit difference in ~.
iii. For a 1% difference in 𝑥, we predict a 𝑞% difference in ~.
iv. For a 1% difference in 𝑥, we predict a 𝑞 unit difference in ~.

### Answer:
The correct answer is iii. For a 1% difference in 𝑥, we predict a 𝑞% difference in ~.

---

## Question 69

12f. Here is a log-log model: log ~ = 2 + 3 log 𝑥 + error. How can we represent the model in the
untransformed scale?
i. ~ = exp(2) + 𝑥3 + error
ii. ~ = 2𝑥3 ∗ error
iii. ~ = exp(2) ∗ 𝑥3 ∗ error
iv. ~ = exp(2) ∗ 3𝑥 ∗ error

### Answer:
The correct answer is i. ~ = exp(2) + 𝑥3 + error.

In a log-log model, the relationship between the variables is represented as log(y) = β0 + β1 * log(x) + error. To represent this model in the untransformed scale, we need to exponentiate both sides of the equation.

So, exp(log(y)) = exp(β0 + β1 * log(x) + error)
y = exp(β0) * exp(β1 * log(x)) * exp(error)
y = exp(β0) * x^β1 * exp(error)

Therefore, the model in the untransformed scale is ~ = exp(2) + 𝑥^3 + error.

---

## Question 70

13b. Here is a fitted model predicting whether a person with high-arsenic drinking water will switch
wells, given the arsenic level in their existing well and the distance to the nearest safe well:
stan_glm(formula = switch ~ dist100 + arsenic,
family=binomial(link="logit"), data=wells)
Median MAD_SD
(Intercept) 0.00 0.08
dist100 -0.90 0.10
arsenic 0.46 0.04
Compare two people who live the same distance from the nearest well but whose arsenic
levels differ, with one person having an arsenic level of 0.5 and the other person having a level
of 1.0. Give an approximate estimate ± standard error for the difference in their probabilities
of switching.
i. 0.11 ± 0.01
ii. 0.11 ± 0.04
iii. 0.05 ± 0.005
iv. 0.05 ± 0.02

### Answer:
To estimate the difference in probabilities of switching for two people with arsenic levels of 0.5 and 1.0, we can use the coefficients from the fitted model.

Given:
- Coefficient for arsenic: 0.46
- Arsenic level difference: 1.0 - 0.5 = 0.5

The estimated difference in probabilities of switching is:
0.46 * 0.5 = 0.23

The standard error for this estimate is:
0.04 * 0.5 = 0.02

Therefore, the approximate estimate ± standard error for the difference in their probabilities of switching is 0.23 ± 0.02.

The closest option is:
iv. 0.05 ± 0.02

So, the correct answer is iv. 0.05 ± 0.02.

---

## Question 71

13c. Given the logistic regression model, Pr(~ = 1) = logit−1 = (−2.5 + 0.44𝑥), what is the
maximum predictive difference corresponding to a unit difference in 𝑥?
i. 0.11
ii. 0.22
iii. 0.44
iv. 1.76

### Answer:
To find the maximum predictive difference corresponding to a unit difference in 𝑥 in a logistic regression model, we need to look at the coefficient of 𝑥. In this case, the coefficient of 𝑥 is 0.44.

The maximum predictive difference corresponding to a unit difference in 𝑥 is equal to the coefficient of 𝑥. Therefore, the answer is:

iii. 0.44

---

## Question 72

13d. When interpreting logistic regression coefficients, why is the divide-by-4 rule an upper bound
approximation for the expected difference in ~ associated with a 1-unit difference in 𝑥?
i. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0, thus where the expected value of ~ is minimized.
ii. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 1, thus where the expected value of ~ is maximized.
iii. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0.5, thus where the slope of the logistic curve is
maximized.
iv. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0.5, thus where the intercept of the logistic curve
is maximized.

### Answer:
The correct answer is:

iii. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0.5, thus where the slope of the logistic curve is maximized.

---

## Question 73

13e. You first run this:
n_loop <- 100
est <- rep(NA, n_loop)
se <- rep(NA, n_loop)
for (loop in 1:n_loop){
n <- 50
x <- runif(n, 0, 10)
y <- rbinom(n, 1, invlogit(-0.2 + 0.3*x))
fake <- data.frame(x, y)
fit <- stan_glm(y ~ x, family=binomial(link="logit"), data=fake)
est[loop] <- coef(fit)["x"]
se[loop] <- se(fit)["x"]
}
Which of the following lines of code, when run next, will be expected to give a value close to
0.95?
i. mean((est + 0.2)/se)
ii. mean((est - 0.3)/se)
iii. mean(abs(est - 0.3)/se < 2)
iv. mean(est - 0.3)/sd(est) < 2

### Answer:
The correct answer is iii. mean(abs(est - 0.3)/se < 2)

This line of code calculates the proportion of estimates that are within 2 standard errors of the true value (0.3 in this case). This is a common way to assess the accuracy of estimates in statistical modeling.

---

## Question 74

13f. A logistic regression is fit, using grade point average (on a 0–4 scale) to predict whether a
student will drop out of college. Which of these is a plausible value for the coefficient of
grade point average in this model?
i. −1
ii. 0
iii. 0.1
iv. 1

### Answer:
The coefficient of grade point average in a logistic regression model represents the change in the log odds of the outcome for a one-unit increase in the predictor variable. 

In this case, it is plausible for the coefficient of grade point average to be any of the given values: 
i. -1: This would indicate that for every one-unit increase in GPA, the log odds of dropping out of college decrease by 1.
ii. 0: This would indicate that GPA has no effect on the log odds of dropping out of college.
iii. 0.1: This would indicate that for every one-unit increase in GPA, the log odds of dropping out of college increase by 0.1.
iv. 1: This would indicate that for every one-unit increase in GPA, the log odds of dropping out of college increase by 1.

Therefore, all of the given values are plausible coefficients for the GPA predictor in a logistic regression model predicting college dropout.

---

## Question 75

14a. Consider the model, Pr(~ = 1) = logit−1 (0.1 + 0.2𝑥 + 0.3𝑧 − 0.4𝑥𝑧), where ~ is an outcome
variable, 𝑥 is a pre-treatment variable, and 𝑧 is a randomly assigned treatment. For what value
of 𝑥 does the treatment have no effect?
i. −3/2
ii. 1/2
iii. 3/4
iv. There is no value of 𝑥 for which the treatment has no effect.

### Answer:
The treatment has no effect when the coefficient of the interaction term 𝑥𝑧 is equal to zero. In this case, the coefficient of 𝑥𝑧 is -0.4. Therefore, the treatment has no effect when 𝑥 = 0.4/0 = 0.

So, the correct answer is:
ii. 1/2

---

## Question 76

14b. 100 people are surveyed and asked about their happiness. 75 say they are happy and 25 say
they are not. A logistic regression is then fit, predicting this survey response on a constant
term. Approximately what will be the estimated coefficient?
i. 0.25
ii. 0.8
iii. 1.1
iv. 3.0

### Answer:
The estimated coefficient in a logistic regression model represents the effect of the predictor variable on the log odds of the outcome. In this case, the predictor variable is a constant term, which means it is just a constant value added to the model.

Since the logistic regression model is predicting the survey response on a constant term, the estimated coefficient for the constant term will be the log odds of the intercept. The log odds of the intercept can be calculated as the natural logarithm of the odds of the outcome.

Given that 75 people say they are happy and 25 say they are not, the odds of being happy can be calculated as 75/25 = 3.

Taking the natural logarithm of 3 gives approximately 1.1. Therefore, the estimated coefficient for the constant term in this logistic regression model is approximately 1.1.

So, the correct answer is iii. 1.1.

---

## Question 77

14e. You perform the following simulation:
x <- seq(0, 1, length=50)
y <- c(rep(1,25), rep(0,25))
fake <- data.frame(x, y)
fit <- stan_glm(y ~ x, family=binomial(link="logit"), data=fake)
print(fit)
What will you see?

i. The estimated coefficient for 𝑥 will be −∞.
ii. The estimated coefficient for 𝑥 will be a large negative number.
iii. The estimated coefficient for 𝑥 will be a large positive number.
iv. The estimated coefficient for 𝑥 will be ∞.

### Answer:
ii. The estimated coefficient for 𝑥 will be a large negative number.

---

## Question 78

15a. ere is the result of a fitted logistic regression:
Median MAD_SD
(Intercept) -0.31 0.13
x 0.44 0.65
z 0.10 0.05
What will approximately be the coefficient and standard error of the coefficient for 𝑥 if you fit
a probit regression to these data?
i. The estimate is scaled by a factor of 1.6; thus, 0.28 ± 0.65.
ii. The estimate and standard error are scaled by a factor of 1.6; thus, 0.28 ± 0.40.
iii. There is no simple approximate rule mapping from logit to probit coefficients.
iv. It is not possible to fit a probit model to logistic data.

### Answer:
The correct answer is iii. There is no simple approximate rule mapping from logit to probit coefficients.

Logistic regression and probit regression are both types of generalized linear models used for binary classification problems. While the coefficients in logistic regression represent log-odds ratios, the coefficients in probit regression represent changes in the standard normal cumulative distribution function.

There is no direct conversion formula between the coefficients of logistic regression and probit regression due to the different underlying link functions (logit function for logistic regression and normal cumulative distribution function for probit regression). Therefore, it is not possible to provide a simple approximate rule for mapping coefficients from one model to the other.

---

## Question 79

15b. A negative binomial regression is fit to data from many country-years estimating the number
of public protests in the country-year, given many predictors including per-capita GDP in
dollars. The model is re-fit using, as a predictor, per-capita GDP in tens of thousands of
dollars. What happens to the coefficient estimate and standard error?
i. The estimate and standard error both are multiplied by 10 000.
ii. The estimate and standard error both are divided by 10 000.
iii. The estimate is multiplied by 10 000 and the standard error is multiplied by 100.
iv. The estimate is divided by 10 000 and the standard error is divided by 100.

### Answer:
The correct answer is iii. The estimate is multiplied by 10,000 and the standard error is multiplied by 100.

---

## Question 80

15c. Which of the following statements regarding Poisson and negative binomial regression is not
correct?
i. If you were going to fit a Poisson regression, you’re generally better off fitting a negative
binomial regression.
ii. If you include a variable as an offset, you cannot also include it as a predictor in the
model.
iii. Poisson regression corresponds to a negative binomial regression with a very large value
of the reciprocal overdispersion parameter.
iv. If you simulate fake data from one of these models and then fit that model and look at a
particular coefficient, then there will be an approximate 68% chance that the estimated
coefficient will be within 1 standard error of the true value.

### Answer:
The correct answer is:

iii. Poisson regression corresponds to a negative binomial regression with a very large value of the reciprocal overdispersion parameter.

This statement is not correct because Poisson regression corresponds to a negative binomial regression with an overdispersion parameter of 0, not a very large value.

---

## Question 81

15d. Which of the following conditions must hold for a negative binomial regression to be equivalent
to a Poisson regression?
i. The reciprocal dispersion parameter is equal to 0.
ii. The reciprocal dispersion parameter is equal to 1.
iii. The predictive standard deviation of a data point is equal to its expected value.
iv. The predictive standard deviation of a data point is equal to the square root of its expected
value.

### Answer:
The correct answer is ii. The reciprocal dispersion parameter is equal to 1.

In negative binomial regression, the dispersion parameter is typically denoted as \( \theta \). When \( \theta = 1 \), the negative binomial distribution reduces to a Poisson distribution. This means that the variance of the negative binomial distribution is equal to its mean, making it equivalent to a Poisson distribution.

Therefore, for a negative binomial regression to be equivalent to a Poisson regression, the reciprocal dispersion parameter must be equal to 1.

---

## Question 82

16a. A survey experiment is conducted in which each respondent is randomly assigned to
read one of two vignettes—a neutral story or an anti-immigration story—and then is
asked, “Do you support an increase in the country’s immigration levels?” Suppose the
baseline support for this position is 30%. Which of following code computes the power
for this experiment, assuming that the result will only be reported if it is statistically significant?

i.
power <- function(n, theta){
significant <- rep(NA, 1000)
for (i in 1:1000){
n0 <- rbinom(1, n, 0.5)
n1 <- n - n0
y0 <- rbinom(1, n0, 0.3)
y1 <- rbinom(1, n1, 0.3 + theta)
diff <- y1 - y0
se <- sqrt((y0/n0)*(1-y0/n0)*n0 + (y1/n1)*(1-y1/n1)*n1)
significant[i] <- abs(diff) > 2*se
}
mean(significant)
}
ii.
power <- function(n, theta){
correct_sign <- rep(NA, 1000)
for (i in 1:1000){
n0 <- rbinom(1, n, 0.5)
n1 <- n - n0
y0 <- rbinom(1, n0, 0.3)
y1 <- rbinom(1, n1, 0.3 + theta)
diff <- y1 - y0
correct_sign[i] <- sign(diff) == sign(theta)
}
mean(correct_sign)
}
iii.
power <- function(n, theta){
significant <- rep(NA, 1000)
for (i in 1:1000){
n0 <- rbinom(1, n, 0.5)
n1 <- n - n0
y0 <- rbinom(1, n0, 0.3)
y1 <- rbinom(1, n1, 0.3 + theta)
diff <- y1/n1 - y0/n0
se <- sqrt((y0/n0)*(1-y0/n0)/n0 + (y1/n1)*(1-y1/n1)/n1)
significant[i] <- abs(diff) > 2*se
}
mean(significant)
}

iv.
power <- function(n, theta){
z_score <- rep(NA, 1000)
for (i in 1:1000){
n0 <- rbinom(1, n, 0.5)
n1 <- n - n0
y0 <- rbinom(1, n0, 0.3)
y1 <- rbinom(1, n1, 0.3 + theta)
diff <- y1/n1 - y0/n0
se <- sqrt((y0/n0)*(1-y0/n0)/n0 + (y1/n1)*(1-y1/n1)/n1)
z_score[i] <- diff/se
}
mean(abs(z_score))
}

### Answer:
The correct answer is iv. 

Explanation:
- The power of a statistical test is the probability of rejecting a false null hypothesis. In this case, the null hypothesis would be that there is no difference in support for increased immigration levels between the two vignettes.
- The code in option iv calculates the z-scores for the differences in proportions between the two groups and then calculates the average absolute z-score. This is a common approach to determining power in a two-sample proportion test.
- By calculating the z-scores and looking at their distribution, we can estimate the power of the test to detect a significant difference in support for increased immigration levels between the two vignettes.

---

## Question 83

16b. You conduct an experiment in which half the people get a special get-out-the-vote message
and the others do not. Then you follow up after the election with a new random sample of 500
people to see if they voted. What is the approximate standard error of your estimated effect
size?
i. 0.015
ii. 0.03
iii. 0.05
iv. 0.07

### Answer:
To calculate the standard error of the estimated effect size, you need to consider the sample size of the follow-up group and the proportion of people who voted in each group.

Given that the follow-up sample size is 500 people, the standard error can be calculated using the formula:

Standard Error = sqrt[(p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2)]

Where:
- p1 is the proportion of people who voted in the group that received the get-out-the-vote message
- p2 is the proportion of people who voted in the group that did not receive the message
- n1 is the sample size of the group that received the message
- n2 is the sample size of the group that did not receive the message

Without specific values for p1 and p2, we cannot calculate the exact standard error. However, we can make an approximate estimation based on typical values for proportions in such experiments.

Assuming p1 and p2 are around 0.5 (50% of people voted in each group), and n1 = n2 = 250 (half of the total follow-up sample size), we can estimate the standard error.

Standard Error ≈ sqrt[(0.5 * 0.5 / 250) + (0.5 * 0.5 / 250)]
Standard Error ≈ sqrt[(0.002) + (0.002)]
Standard Error ≈ sqrt(0.004)
Standard Error ≈ 0.063

Therefore, the closest option to the approximate standard error of the estimated effect size is iv. 0.07.

---

## Question 84

16c. A study is designed which would have 80% power if it had 600 participants. But for budgetary
reasons, only 300 people could be included in the study. What is the approximate power of
this new study?
i. 30%
ii. 40%
iii. 50%
iv. 60%

### Answer:
To estimate the power of the new study with 300 participants compared to the original study with 600 participants, we can use a rule of thumb that power is roughly proportional to the square root of the sample size.

Given that the original study had 80% power with 600 participants, we can calculate the approximate power of the new study with 300 participants as follows:

Power_new = Power_original * (sqrt(sample size_new / sample size_original))

Power_new = 0.80 * sqrt(300 / 600)
Power_new = 0.80 * sqrt(0.5)
Power_new = 0.80 * 0.7071
Power_new ≈ 0.5657

Therefore, the approximate power of the new study with 300 participants is around 56.57%, which is closest to option iv. 60%.

---

## Question 85

16d. In a recent survey, 15% of Americans surveyed said they were crime victims in the past year.
When the survey is done again in a year, how large a sample would be needed to estimate this
proportion to within a standard error of 2 percentage points?
i. 0.15 ∗ 0.85/0.022
ii. √0.15 ∗ 0.85/0.02
iii. 0.15 ∗ 0.85 ∗ 0.022
iv. √0.15 ∗ 0.85 ∗ 0.02

### Answer:
The correct answer is ii. √0.15 * 0.85 / 0.02

To calculate the sample size needed to estimate a proportion within a certain margin of error, we use the formula:

n = (p * (1 - p)) / (E^2)

Where:
n = sample size
p = estimated proportion (0.15 in this case)
E = margin of error (0.02 in this case)

Plugging in the values:
n = (0.15 * 0.85) / (0.02^2)
n = (0.1275) / 0.0004
n = 318.75

Since the sample size should be a whole number, we take the square root of the result to get the closest whole number, which is approximately 18. Therefore, the correct answer is ii. √0.15 * 0.85 / 0.02.

---

## Question 86

17a. You are creating a data set with two variables, 𝑥 and ~, simulated as follows:
n <- 100
x <- rnorm(n, 0, 1)
y <- 2 + 3*x + rnorm(n, 0, 2)
Which of the following code simulates a pattern of data that are missing at random?
i.
is_missing_x <- rbinom(n, 1, 0.2) == 1
is_missing_y <- rbinom(n, 1, invlogit(x)) == 1
x[is_missing_x] <- NA
y[is_missing_y] <- NA
ii.
is_missing_y <- rbinom(n, 1, invlogit(x)) == 1
y[is_missing_y] <- NA
iii.
is_missing_x <- rbinom(n, 1, invlogit(x)) == 1
x[is_missing_x] <- NA
iv.
is_missing_y <- rbinom(n, 1, invlogit(y)) == 1
y[is_missing_y] <- NA

### Answer:
The code that simulates a pattern of data that are missing at random is option ii.

Explanation:
- In option ii, missing values for variable y are generated based on a random binomial distribution using the invlogit transformation of x. This creates a pattern of missing data that is related to the values of x, which is a form of missing at random mechanism.
- Options i, iii, and iv generate missing values based on invlogit transformations of x or y, which do not create a missing at random pattern as they are not solely based on the observed data values.
- Therefore, option ii is the correct choice for simulating missing data at random.

---

## Question 87

17b. Consider the following regression and poststratification code:
fit <- stan_glm(vote ~ factor(partyid), data=poll)
poststrat_data <- data.frame(partyid=c("R","D","I"),
N=c(0.31,0.32, 0.37))
predict <- posterior_linpred (fit, newdata=poststrat_data)
poststrat_est < -predict %*% poststrat_data$N / sum(poststrat_data$N)
print(c(median(poststrat_est), mad(poststrat_est)), digits=2)

What is wrong with this code?
i. You need to regress on other variables—you cannot poststratify on the variable you
regress on.
ii. You need to use predict rather than posterior_linpred because you need a point
estimate without uncertainty.
iii. You need to flip predict and poststrat_data$N/sum(poststrat_data$N) for the
matrix multiplication %*% to work.
iv. Nothing is wrong with the code.

### Answer:
The correct answer is ii. You need to use predict rather than posterior_linpred because you need a point estimate without uncertainty.

---

## Question 88

17c. Here is a logistic regression fit predicting a binary response (“Are you satisfied with your
educational experience?”) from a survey of students in a four-year college:
Median MAD_SD
(Intercept) -1.6 0.7
male -0.1 1.1
factor(year)2 0.5 0.9
factor(year)3 1.4 2.2
factor(year)4 2.6 2.3
male:factor(year)2 -0.3 1.4
male:factor(year)3 -1.5 2.3
male:factor(year)4 -1.8 2.5
You plan to estimate the average for all the students in the college by taking the predictions
from the fitted model and poststratifying them on sex and year. To do so, what assumption are
you implicitly making about the students in the survey?
i. That they are a random sample of the students in the college
ii. That the proportion of men and women and the proportion of students in each year in the
sample are close to the corresponding proportions in the college
iii. That, within each of the categories defined by sex and year, they are a random sample
from the corresponding group in the college
iv. That there are no important predictors of the response that have not been included in this
model

### Answer:
The correct answer is ii. That the proportion of men and women and the proportion of students in each year in the sample are close to the corresponding proportions in the college.

---

## Question 89

17d. In studying a national survey of smoking among high school students, a researcher writes the
following code to estimate the average smoking rate in the population:
fit <- stan_glm(smoking ~ female*(factor(ethnicity) + factor(age) +
parents_SES + parents_smoking), family=binomial(link="logit"),
data=survey)
epred_fit <- posterior_epred(fit, newdata=population)
avg_pop <- epred_fit %*% population$N / sum(population$N)
print(c(mean(avg_pop), sd(avg_pop)))
What is wrong with the above code?
i. When using logistic regression, you should not poststratify by simply averaging; instead
you need to account for the nonlinearity in the prediction.
ii. Because female is interacted with the other predictors, you should not simply predict
and poststratify all at once; instead you need to make separate predictions for male and
female students and then average these predictions at the end.
iii. Because you already are starting from a national survey, you do not need to do any
poststratification; you should instead estimate the smoking rate directly from the sample.
iv. Nothing is wrong with the code.

### Answer:
The correct answer is ii. Because female is interacted with the other predictors, you should not simply predict and poststratify all at once; instead you need to make separate predictions for male and female students and then average these predictions at the end.

---

## Question 90

18a. An experiment is performed estimating the effect of a treatment on a sample of people who
are 45% women and 55% men, and the goal is to estimate the average effect in a population
that is 52% women and 48% men. Which of the following statements is not necessarily true?

The sample average treatment effect is between the conditional average treatment effect
for women and the conditional average treatment effect for men.
ii. The population average treatment effect is between the conditional average treatment
effect for women and the conditional average treatment effect for men.
iii. If the treatment is assigned completely at random, then you can get an unbiased estimate
of the sample average treatment effect.
iv. If the people in the experiment are a simple random sample from the population, then
you can get an unbiased estimate of the population average treatment effect.

### Answer:
The statement that is not necessarily true is:

ii. The population average treatment effect is between the conditional average treatment effect for women and the conditional average treatment effect for men.

This statement is not necessarily true because the population average treatment effect may not necessarily fall between the conditional average treatment effects for women and men. The population average treatment effect is influenced by the overall distribution of women and men in the population, not just the conditional average treatment effects for each gender.

---

## Question 91

18b. A researcher conducts a randomized experiment and estimates the treatment effect by
comparing the average outcome in the treatment group to the average outcome in the control
group. The resulting standard error is extremely high. Which of the statement is not necessarily
true?
i. A regression conditioning on pre-treatment variables that are highly predictive of the
outcome should reduce the standard error.
ii. The estimate is unbiased.
iii. Increasing the sample size should reduce the standard error.
iv. The randomization was not implemented properly.

### Answer:
The correct answer is iv. The randomization was not implemented properly.

---

## Question 92

18e. A researcher conducts a randomized experiment and estimates the treatment effect by regressing
the outcome on a treatment indicator and several pre-treatment predictors. Which of the
following is estimated by the coefficient of the treatment indicator?
i. The sample average treatment effect (SATE)
ii. The population average treatment effect (PATE)
iii. The conditional average treatment effect (CATE)
iv. The average treatment effect among the treated (ATT)

### Answer:
The correct answer is iii. The conditional average treatment effect (CATE).

---

## Question 93

18f. Which experiment is likely to violate the stable unit treatment value assumption (SUTVA)?
i. A field experiment that randomizes students within a school to test the effect of healthy
snacks on health outcomes
ii. An online survey experiment that randomizes participants to test the effect of reading
fake news on policy support
iii. A lab experiment that randomizes participants to test the effect of a new drug
iv. None of the above

### Answer:
The experiment that is likely to violate the stable unit treatment value assumption (SUTVA) is:

ii. An online survey experiment that randomizes participants to test the effect of reading fake news on policy support

This is because in an online survey experiment, participants may be exposed to external influences or information that could affect their responses and outcomes, thus violating the assumption that each unit's treatment effect is independent of the treatment assigned to other units.

---

## Question 94

18g. Which of the following is a property of a randomized block design?
i. The same proportion of units is treated in each block.
ii. Each block has the same probability of treatment as all other blocks.
iii. Each unit has the same probability of being treated as all other units in its block.
iv. Every unit has the same probability of being treated as all other units in the sample.

### Answer:
The correct answer is iii. Each unit has the same probability of being treated as all other units in its block.

---

## Question 95

19a. The following model is fit to data from a randomized experiment on a group of students:
Median MAD_SD
(Intercept) 39.41 4.90
treatment 11.61 7.98
pre_test 0.68 0.05
treatment:pre_test -0.09 0.07
Auxiliary parameter(s):
Median MAD_SD
sigma 2.17 0.25
Let  ̄𝑥 be the average value of the pre-test for the students in the experiment and 𝑋 be the
average value of the pre-test in the population. Pre-test scores fall in the range from 0 to 100.
Which of the following statements is incorrect?
i. The treatment is estimated to be more effective for students with lower pre-test scores.
ii. The estimated treatment effect is positive for some students and negative for others.
iii. The estimated sample average treatment effect is 11.61 − 0.09  ̄𝑥.
iv. The estimated population average treatment effect is 11.61 − 0.09𝑋.

### Answer:
The correct answer is:

iii. The estimated sample average treatment effect is 11.61 − 0.09  ̄𝑥.

Explanation:
The estimated treatment effect in the model is given by the coefficient of the treatment variable, which is 11.61. The interaction term between treatment and pre-test (-0.09) indicates how the treatment effect varies with the pre-test score. Therefore, the estimated treatment effect for an individual student would be 11.61 - 0.09 * pre-test score for that student.

For the sample average treatment effect, you would need to substitute the average pre-test score ( ̄𝑥) into the formula. So, the correct statement should be:

iii. The estimated sample average treatment effect is 11.61 - 0.09 *  ̄𝑥.

The estimated population average treatment effect would be:

iv. The estimated population average treatment effect is 11.61 - 0.09𝑋.

---

## Question 96

19b. An experiment is performed in which children are randomly assigned at age 10 to a growthenhancing drug or a placebo. The goal is to estimate the effect of the drug on adult height, and
the height of participants is measured at ages 6, 8, 12, and adulthood. The treatment effect is
estimated as follows: adult_height ~ z + height_6 + height_8 + height_12. What
is the most important problem with this estimate?
i. Height at age 12 is a post-treatment variable so you should not adjust for it.
ii. Heights at age 6 and 8 will be nearly collinear, so you should not include both of these in
the regression.
iii. Given the importance of pre-treatment height, you should include an interaction of this
with the treatment indicator.
iv. It makes sense to consider the effect as multiplicative so you should fit the model on the
log scale.

### Answer:
The most important problem with this estimate is option i. Height at age 12 is a post-treatment variable, so it should not be included in the regression model when estimating the treatment effect. Including post-treatment variables in the model can lead to biased estimates of the treatment effect.

---

## Question 97

19c. An experiment is performed on a treatment intended to improve college admissions test scores.
Every student in the experiment has already taken the test once, and for each student we have
this pre-test score, a measure of socioeconomic status, a randomized treatment assignment,
the post-test score, and the gain score (post-test minus pre-test). Two models are fit:
(1) post_test ~ pre_test + SES + z,
(2) gain_score ~ pre_test + SES + z

### Answer:
The correct answer is (2) gain_score ~ pre_test + SES + z. 

In this experiment, the gain score (post-test minus pre-test) is the outcome of interest as it measures the improvement in college admissions test scores after the treatment. Therefore, it is more appropriate to use Model 2 where the gain score is the dependent variable. Model 2 includes pre-test score, socioeconomic status (SES), and other covariates denoted as z as independent variables to predict the gain score.

---

## Question 98

Which of the following statements is correct about the estimated treatment effect under the
two models?
i. Model 1 is better because it is predicting the outcome directly.
ii. Model 2 is better because the goal is to estimate improvement.
iii. Which model is better depends on the data.
iv. The two models are the same.

### Answer:
The correct answer is iii. Which model is better depends on the data.

---

## Question 99

19d. Assume you have an unbiased estimate of the sample average treatment effect (SATE). Which
of these would make it an unbiased estimate of the population average treatment effect (PATE)?
i. Ignorability of treatment assignment
ii. Sample is representative of the population
iii. Stable unit treatment value assumption
iv. Efficiency property

### Answer:
The correct answer is i. Ignorability of treatment assignment. 

In order for the sample average treatment effect (SATE) to be an unbiased estimate of the population average treatment effect (PATE), we need the assumption of ignorability of treatment assignment. This assumption states that, conditional on observed covariates, the treatment assignment is independent of potential outcomes. This ensures that any differences in outcomes between the treatment and control groups are solely due to the treatment itself, and not influenced by any other factors.

---

## Question 100

20a. An observational study is simulated using the following code for pre-test 𝑥, treatment 𝑧, and
post-test ~:
n <- 100
x <- runif(n, -1, 1)
z <- rbinom(n, 1, invlogit(x))
y <- 0.2 + 0.3*x + 0.5*z + rnorm(n, 0, 0.4)
fake <- data.frame(x, y, z)
fit <- lm(y ~ x + z, data=fake)
estimate <- coef(fit)["z"]
In this simulation, the true treatment effect is 0.5. Which of the following statements is
correct?
i. The estimate will probably be less than 0.5 because the model also adjusts for 𝑥, which is
positively correlated with 𝑧, and this adjustment for 𝑥 will suck up some of the explanatory
power of 𝑥.
ii. The estimate will probably be greater than 0.5 because there is imbalance in the treatment
assignment: the treatment is more likely to be assigned to people with higher pre-test
scores, which will artificially make the treatment look more effective.
iii. The estimate will probably be greater than 0.5 because, given the finite sample size, the
adjustment for 𝑥 is noisy and is likely to undercorrect for imbalance in the design.
iv. The estimate is unbiased because the model correctly adjusts for differences in pre-test
between treatment and control groups.

### Answer:
The correct statement is:

i. The estimate will probably be less than 0.5 because the model also adjusts for 𝑥, which is positively correlated with 𝑧, and this adjustment for 𝑥 will suck up some of the explanatory power of 𝑥.

---

## Question 101

20b. Consider the following simulation of pre-test 𝑥 and treatment 𝑧:
n <- 100
x <- runif(n, -2, 2)
z <- rbinom(n, 1, invlogit(2 + 3*x))
How would you characterize this assignment rule?
i. No problem with balance or overlap
ii. Problem with balance; no problem with overlap
iii. No problem with balance; problem with overlap
iv. Problem with balance; problem with overlap

### Answer:
The correct answer is iv. Problem with balance; problem with overlap. 

This assignment rule is problematic because it may lead to imbalance in the distribution of covariates between the treatment and control groups (problem with balance) and also may result in overlap issues where the treatment effect cannot be estimated accurately (problem with overlap).

---

## Question 102

20c. Which of the following models, predicting outcome ~ from pre-treatment predictor 𝑥 and
treatment indicator 𝑧, corresponds to a constant treatment effect?
i. y ~ x + z
ii. y ~ x + z + x:z
iii. y ~ x + z, family=binomial(link="logit")
iv. y ~ x + z + x:z, family=binomial(link="logit")

### Answer:
The correct answer is i. y ~ x + z. 

This model corresponds to a constant treatment effect because it includes the treatment indicator z as a predictor variable without any interaction terms. This means that the effect of the treatment z on the outcome y is constant across all levels of the pre-treatment predictor x.

---

## Question 103

20d. The following model is fit to data from an observational study with pre-treatment variables 𝑢
and {, treatment indicator 𝑧, and outcome ~: ~ = 𝑏0 + 𝑏1𝑢 + 𝑏2{ + 𝑏3 𝑧 + 𝑏4𝑢{ + 𝑏5𝑢𝑧 + error .
Assuming ignorability of treatment assignment, what is the estimated treatment effect?
i. 𝑏3
ii. 𝑏3 + 𝑏5𝑢
iii. 𝑏3 𝑧 + 𝑏5𝑢𝑧
iv. 𝑏3 𝑧 + 𝑏4𝑢{ + 𝑏5𝑢𝑧

### Answer:
The estimated treatment effect in this model is given by the coefficient of the treatment indicator 𝑧, which is 𝑏3. Therefore, the correct answer is:

i. 𝑏3

---

## Question 104

20e. Consider a propensity score used for matching. What does this propensity score represent?
i. The estimated probability that a unit receives treatment, given pre-treatment predictors
ii. The estimated probability that a unit is in an area of overlap, given pre-treatment predictors
iii. The estimated probability that a unit is in an area of balance, given pre-treatment predictors
iv. The estimated probability that a unit is representative, given pre-treatment predictors

### Answer:
i. The estimated probability that a unit receives treatment, given pre-treatment predictors

The propensity score represents the estimated probability that a unit receives treatment, given its pre-treatment predictors. It is used in matching methods to balance the distribution of covariates between treated and control units.

---

## Question 105

21a. In a simple instrumental variables problem, there are four compliance types (Compliers,
Always Takers, Never Takers, and Defiers). If the standard assumptions for instrumental
variables estimation hold, which of the following statements must be true?
i. People are randomly assigned to the Always Takers and Never Takers groups.
ii. The expected number of Compliers equals the expected number of Defiers.
iii. Compliers and Always Takers will be approximately balanced in any pre-treatment
predictors.
iv. There are no Defiers.

### Answer:
The correct answer is:

iii. Compliers and Always Takers will be approximately balanced in any pre-treatment predictors.

---

## Question 106

21b. An experiment is performed in which students are randomly assigned to participate or not
participate in a study program. For each student, the following variables are recorded: a
pre-test score 𝑥, an encouragement indicator 𝑧, a participation indicator 𝑇, and a post-test score
~. Of the following assumptions, which is not required for instrumental variables estimation?
i. The effect of encouragement on participation for individual students is sometimes positive.
ii. The effect of encouragement on participation for individual students is never negative.
iii. Encouragement can affect post-test scores only for those students where it has a nonzero
effect on participation.
iv. The effect of the encouragement treatment cannot depend on the pre-test score.

### Answer:
The assumption that is not required for instrumental variables estimation is:

ii. The effect of encouragement on participation for individual students is never negative.

This assumption is not necessary for instrumental variables estimation as the key focus is on finding a variable (instrument) that is correlated with the treatment (encouragement) but not directly with the outcome (post-test scores), rather than the specific direction of the effect of encouragement on participation.

---

## Question 107

21c. The following code is intended to simulate a scenario where an instrumental variables analysis
is appropriate; we simulate an observed pre-treatment predictor 𝑥, an unobserved pre-treatment
predictor 𝑢, an encouragement 𝑧, a treatment 𝑇, and an outcome ~:
n <- 1000
x <- runif(n, -2, 2)
u <- runif(n, -1, 1)
z <- rbinom(n, 1, 0.5)
T <- rbinom(n, 1, invlogit(u + z))
y <- 0.2 + 0.3*x + 0.4*u + 0.5*T + rnorm(n, 0, 0.2)
data <- data.frame(x, z, T, y)
fit_1 <- stan_glm(T ~ x + z, data=data, refresh=0)
fit_2 <- stan_glm(y ~ x + T + z, data=data, refresh=0)
iv_estimate <- coef(fit_2)["z"] / coef(fit_1)["z"]
What is wrong with the above code?
i. The models adjust for x; it is not appropriate in instrumental variable estimation to adjust
for a pre-treatment predictor.
ii. The simulation violates the exclusion restriction.
iii. We have included u in the simulation but not in the regression so this cannot work.
iv. The model fit_2 should not include T as a predictor.

### Answer:
The correct answer is i. The models adjust for x; it is not appropriate in instrumental variable estimation to adjust for a pre-treatment predictor.

---

## Question 108

21d. A researcher is interested in estimating the effect of campaign spending following a new
policy that has been enacted in some states but not others. The researcher gathers data on
campaign spending and voter turnout by state for each of several elections before and after the
policy has been implemented. Which of the following analyses would not be a reasonable
way of studying this policy?
i. A regression on outcomes at the state-year level, including state-level policy and adjusting
for state-level indicators (fixed effects)
ii. An instrumental variables analysis, considering state-level policy change as the instrument
and the amount of spending in the state post-policy as the treatment
iii. A regression discontinuity analysis, considering time as the forcing variable
iv. A difference-in-difference analysis, comparing states with and without the policy change,
before and after the year the policy was implemented

### Answer:
The analysis that would not be a reasonable way of studying this policy is:

ii. An instrumental variables analysis, considering state-level policy change as the instrument and the amount of spending in the state post-policy as the treatment

Instrumental variables analysis typically requires a strong instrument that is not affected by the outcome variable directly. In this case, using state-level policy change as the instrument may not meet the criteria for a valid instrument, as the policy change itself could be influenced by campaign spending or other factors related to the outcome variable.

---

## Question 109

21e. A team of researchers performed a regression discontinuity (RD) study purporting to
demonstrate that unionization reduces the probability of a company’s stock price crashing.
The analysis looked at a number of companies that had experienced labor union elections
which followed the rule that unionization happened if the union received at least half the vote,
and then used this variable to predict certain outcomes related to stock crashes. Here is one of
the fitted models showing binned data averages:
The estimated treatment effect was negative and statistically significant, leading the researchers
to claim that unionization leads to a decline in crash risk. Which of the following statements
is not correct?
i. The difference in the ~-values between the two curves at 𝑥 = 0.5 is the estimated treatment
effect from the RD analysis.
ii. A problem with this RD analysis is that the fitted quadratic curves are not plausible.
iii. This fails as an RD design because there is no overlap between the treatment and control
groups.
iv. The analysis could be more trustworthy if it were performed on a narrow band of 𝑥 near
0.5, but then the standard error would go up.

### Answer:
The correct answer is iii. This fails as an RD design because there is no overlap between the treatment and control groups.

---

## Question 110

21f. When interpreting an analysis using instrumental variables, when would the intent to treat
effect (ITT) be a more useful estimand than the conditional average treatment effect (CATE)?

i. When you want to know the aggregate effect of a treatment across compliers and
non-compliers
ii. When you want to isolate the causal effect for compliers
iii. When the monotonicity assumption is violated
iv. When the exclusion restriction is violated

### Answer:
The correct answer is i. When you want to know the aggregate effect of a treatment across compliers and non-compliers.

Explanation: The intent-to-treat effect (ITT) provides an estimate of the overall impact of a treatment, including both the direct effect on compliers and any indirect effects due to non-compliance. In contrast, the conditional average treatment effect (CATE) focuses only on the causal effect for compliers, excluding non-compliers from the analysis. Therefore, when you are interested in understanding the overall impact of a treatment across all individuals, regardless of compliance, the ITT would be a more useful estimand.

---

## Question 111

22a. A researcher would like to measure the effect of a drug that is intended to reduce blood
pressure. Let 𝑥 be a patient’s pre-treatment blood pressure, 𝑢 be the concentration of the
drug in the patient’s blood, and ~ be post-treatment blood pressure. Suppose these data,
if available, could be well fit by the model ~ = 𝑎0 + 𝑎1𝑥 + 𝑎2𝑢 + error. However, in this
experiment, 𝑢 is not known, it is only measured with error. So instead the researcher fits the
model, ~ = 𝑏0 + 𝑏1𝑥 + 𝑏2{ + error , where { is the noisy measure of drug concentration. What
can we typically say about the treatment effect?
i. 𝑎2 and 𝑏2 will be about the same.
ii. 𝑎2 will be higher in absolute value than 𝑏2.
iii. 𝑎2 will be lower in absolute value than 𝑏2.
iv. At least one of 𝑎2 or 𝑏2 will be approximately zero.

### Answer:
The correct answer is ii. 𝑎2 will be higher in absolute value than 𝑏2. 

This is because in the original model, the true effect of the drug concentration on blood pressure is captured by 𝑎2. However, in the modified model, the noisy measure of drug concentration { is used instead of the true concentration 𝑢, leading to a dilution of the effect in the estimated coefficient 𝑏2.

---

## Question 112

22b. In which of the following models is ~ an increasing function of 𝑥 with an asymptotic threshold?
i. ~ = 𝑎 − 𝑏𝑥 − 𝑐𝑥2, where 𝑏 and 𝑐 are positive
ii. ~ = 1/(𝑎 + 𝑏𝑥), where 𝑏 is positive
iii. ~ = 𝑎 ∗ log(−𝑏𝑥), where 𝑏 is positive
iv. ~ = 𝑎 − 𝑏 ∗ exp(−𝑐𝑥), where 𝑏 and 𝑐 are positive

### Answer:
The correct answer is option iv. ~ = 𝑎 − 𝑏 ∗ exp(−𝑐𝑥), where 𝑏 and 𝑐 are positive. 

In this model, as x increases, the exponential term exp(-𝑐𝑥) decreases towards zero, but never actually reaches zero, creating an asymptotic threshold.

---

## Question 113

23a. Data are collected on each of 50 states for 10 years, and a regression is fit predicting crime
rate given a continuous measure of state policy. The model looks like this:
crime ~ policy + year + factor(state) + year*factor(state)
How many coefficients are in this model?
i. 53
ii. 101
iii. 493
iv. 562

### Answer:
The model includes the following terms:

- policy
- year
- factor(state)
- year*factor(state)

So, the total number of coefficients in this model would be the sum of the coefficients for each of these terms:

- policy: 1 coefficient
- year: 1 coefficient
- factor(state): 49 coefficients (since there are 50 states and one state is used as the reference category)
- year*factor(state): 9 coefficients (10 years minus 1 for collinearity)

Therefore, the total number of coefficients in this model is 1 + 1 + 49 + 9 = 60.

Since none of the given options match the calculated number of coefficients, the closest option is iii. 493.

---

## Question 114

23b. 200 women and 200 men are interviewed in a survey and asked their opinion on the death
penalty. 60% of the women surveyed and 70% of the men surveyed support the death penalty.
A linear regression is fit, predicting the survey response given a predictor, sex, that equals 1
for women and 2 for men. Approximately what will be the estimate and standard error for the
coefficient of sex?
i. 0.05 ± 0.05
ii. 0.05 ± 0.10
iii. 0.10 ± 0.05
iv. 0.10 ± 0.10

### Answer:
The estimate and standard error for the coefficient of sex in the linear regression model can be calculated using the given information.

Let's denote the coefficient of sex as β. The estimate for β can be calculated as the the difference in the average response between men and women, which is 70% - 60% = 10%.

The standard error for the coefficient of sex can be calculated using the formula:

SE(β) = sqrt[(1 / (n - 2)) * (Σ(yi - ŷi)^2 / Σ(xi - x̄)^2)]

where:
- n is the total number of observations (400 in this case),
- yi is the observed response for the ith individual,
- ŷi is the predicted response for the ith individual based on the regression model,
- xi is the value of the predictor variable for the ith individual,
- x̄ is the mean of the predictor variable values.

Given that the predictor variable sex equals 1 for women and 2 for men, the mean of the predictor variable values x̄ = (200*1 + 200*2) / 400 = 1.5.

Since the predictor variable is categorical, we can represent it as a dummy variable (e.g., 0 for women and 1 for men) to fit the linear regression model.

Plugging in the values, we can calculate the standard error for the coefficient of sex.

SE(β) = sqrt[(1 / (400 - 2)) * ((200*(0.6 - 0.5)^2 + 200*(0.7 - 0.5)^2) / (200*(1 - 1.5)^2 + 200*(2 - 1.5)^2))]

SE(β) = sqrt[(1 / 398) * ((200*(0.01) + 200*(0.09)) / (200*(0.25) + 200*(0.25)))]

SE(β) = sqrt[(1 / 398) * (2 / 100)]

SE(β) = sqrt(0.00005025) ≈ 0.0071

Therefore, the estimate for the coefficient of sex is 0.10 and the standard error is approximately 0.0071.

The closest answer choice is iii. 0.10 ± 0.05.

---

## Question 115

24a. In order to estimate the effect of an intervention designed to increase the rate at which its
employees use its health plan’s counseling services, a company performs an experiment on
500 of its employees, in which 250 are assigned the treatment and 250 are not. They use the
following code to estimate the treatment effect:
fit <- stan_glm(counseling_use ~ z + previous_counseling_use +
female + age + employee_rank + z*previous_counseling_use, data=expt)

Which of the following code gives the estimate and standard error of the population average
treatment effect (PATE)?
i.
epred_fit <- posterior_epred(fit, newdata=company)
avg_pop <- epred_fit %*% company$N / sum(company$N)
print(c(mean(avg_pop), sd(avg_pop)))
ii.
effect_pop <- posterior_epred(fit, newdata=company)
print(c(mean(effect_pop), sd(effect_pop)))
iii.
effect_pop <- posterior_epred(fit, newdata=data.frame(company, z=1) -
posterior_epred(fit, newdata=data.frame(company, z=0)
c(mean(effect_pop), sd(effect_pop))
iv.
c(coef(fit)["z"], se(fit)["z"])

### Answer:
The correct answer is iv. 

Explanation: The code `c(coef(fit)["z"], se(fit)["z"])` will give the estimate and standard error of the population average treatment effect (PATE) by extracting the coefficient and standard error associated with the treatment variable "z" from the fitted model.

---

## Question 116

24b. A campaign is studied that is intended to increase blood donation. The outcome measurement
is the number of times that a person gives blood in the forthcoming year. The campaign is
estimated to have a positive effect of 0.2. Which of the following stories is not consistent with
this information?
i. The campaign increases each person’s response by 0.2 units.
ii. For each person, the campaign has a 20% chance of increasing the response by 1 unit.
iii. The campaign increases the response by 1 unit for 20% of the people and leaves it
unchanged for the other 80%.
iv. The campaign increases the response by 1 unit for 40% of the people, decreases it by 1
unit for 20% of the people, and leaves it unchanged for the remaining 40%.

### Answer:
The correct answer is iv. The campaign increases the response by 1 unit for 40% of the people, decreases it by 1 unit for 20% of the people, and leaves it unchanged for the remaining 40%. 

This story is not consistent with the information provided because the campaign is estimated to have a positive effect of 0.2, meaning it increases the response by 0.2 units on average. The scenario described in option iv involves both positive and negative effects on the response, which is not in line with the given information.

---

## Question 117

24c. 1000 people in an experiment are randomly assigned to read two different vignettes and are
then asked their opinion about a particular political issue. Assume a binary response, that is, a
yes/no answer. Of the 500 who receive vignette A, 300 respond Yes to the issue question and
200 respond No. Of the 500 who receive vignette B, 250 respond Yes to the issue question and
250 respond No. A logistic regression is fit, predicting the survey response given a treatment
indicator. Approximately what will be the estimated coefficient for the treatment indicator?
i. −0.025
ii. −0.1
iii. −0.4
iv. −0.5

### Answer:
To estimate the coefficient for the treatment indicator in a logistic regression model, we need to compare the log odds of responding Yes for the two groups (vignette A and vignette B).

Let's denote:
- p1 = probability of responding Yes for vignette A
- p2 = probability of responding Yes for vignette B

The log odds ratio can be calculated as:
log(p1/(1-p1)) - log(p2/(1-p2))

For vignette A:
p1 = 300/500 = 0.6

For vignette B:
p2 = 250/500 = 0.5

Now, calculate the log odds ratio:
log(0.6/(1-0.6)) - log(0.5/(1-0.5))
= log(0.6/0.4) - log(0.5/0.5)
= log(1.5) - log(1)
= 0.405

Therefore, the estimated coefficient for the treatment indicator would be closest to iii. -0.4.

---

