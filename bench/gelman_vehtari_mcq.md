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

-----------------------------------

1c. Suppose a variable ~ takes on the value 200 in the year 𝑡 = 1900 and 240 in the year 𝑡 = 2000.
If this variable follows a linear time trend, what are the values of 𝑎 and 𝑏 in equation of the
line, ~ = 𝑎 + 𝑏𝑡?
i. 𝑎 = −560, 𝑏 = 0.4
ii. 𝑎 = 200, 𝑏 = 0.4
iii. 𝑎 = 160, 𝑏 = 4
iv. 𝑎 = −1700, 𝑏 = 40

-----------------------------------

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

-----------------------------------

2a.  What is one way to make a scatterplot of two vectors, 𝑥 and ~, in R?
i. plot(x, y)
ii. plot x, y
iii. scatter(x, y)
iv. scatter x, y

-----------------------------------

2b. Which of these lines of R code graphs the function ~ = 2 + 3𝑥?
i. abline(2, 3)
ii. abline(2 + 3*x)
iii. curve(2 + 3x)
iv. curve(2, 3)

-----------------------------------


2c. Which of these lines of R code generates 10 random numbers between −2 and +2?
i. runif(10, -2, 2)
ii. rnorm(10, -2, 2)
iii. sample(c(-2,2), 10)
iv. seq(-2, 2, length=10)

-----------------------------------


3a. job performance. What is the approximate standard error for the resulting estimate?
i. 0.01
ii. 0.03
iii. 0.05
iv. 0.10

-----------------------------------

3b. A population of heights is normally distributed with mean 65 inches and standard deviation
3.2 inches. Which of the following lines of R code gives the proportion of people who are
taller than 69.5 inches?
i. dnorm(65, 69.5, 3.2)
ii. 1 - dnorm(65, 69.5, 3.2)
iii. 1 - pnorm(69.5, 65, 3.2)
iv. rnorm(69.6, 65, 3.2)

-----------------------------------

3c. You perform a survey that estimates the average monthly spending on a particular consumption
category to be $50 for men and $55 for women. The standard errors of these estimates are $3
and $4, respectively. What do you estimate the difference in spending to be, and what is your
estimate’s standard error?
i. 5 ± 1
ii. 5 ± 5
iii. 5 ± 7
iv. 5 ± 7/√𝑛

-----------------------------------

3d. A certain town is served by two hospitals. In the larger hospital about 45 babies are born each
day, and in the smaller hospital about 15 babies are born each day. As you know, about 51%
of all babies are boys. However, the exact percentage varies from day to day. Sometimes it
may be higher than 51%, sometimes lower.
For a period of 1 year, each hospital recorded the days on which more than 60% of the babies
born were boys. Which hospital do you think recorded more such days?
i. The larger hospital
ii. The smaller hospital
iii. About the same (that is, within 5% of each other)

-----------------------------------

4a. You perform an experiment on 𝑛 people. You get an estimated treatment effect of 0.3 with a
standard error of 0.2. Is this considered “statistically significant”?
i. Yes
ii. No
iii. Yes, if 𝑛 > 30
iv. It depends on whether the data are normally distributed

-----------------------------------

4b. A basketball player takes 20 free throws and makes 14 of them. What is the 95% interval for
her success probability?
i. 0.7 ± 2√0.7 ∗ 0.3/20
ii. 0.7 ± 2√0.7 ∗ 0.3 ∗ 20
iii. 14 ± 2√0.7 ∗ 0.3/20
iv. 14 ± 2√0.7 ∗ 0.3 ∗ 20

-----------------------------------

4c. An intervention has a true effect size of 0.2. You design an experiment that will produce an
unbiased estimate with standard error 0.1. If you run the experiment, what is the probability
that your estimate will be positive and “statistically significant”?

i. 16%
ii. 50%
iii. 95%
iv. 97.5%

-----------------------------------

4d. Out of a random sample of 100 Americans, zero report having ever been robbed. From this
information, you compute a 95% confidence interval for the proportion of Americans who
have ever been robbed. What should your interval be?
i. (0, 0) using the standard error √ ˆ𝑝(1 − ˆ𝑝)/𝑛 with estimate ˆ𝑝 = 0
ii. (0, 0.05) using the standard error √ ˆ𝑝∗ (1 − ˆ𝑝∗)/𝑛∗ with 𝑝∗ = ~+2
𝑛+2 and 𝑛∗ = 𝑛 + 4
iii. (0, 0.10) using the standard error 0.5/√𝑛
iv. (0, 1) because with 0 successes you have no information about 𝑝

-----------------------------------

4e. (e) What is a 𝑝-value?
i. The width of a 95% confidence interval
ii. The probability of observing something at least as extreme as the observed test statistic
iii. The probability of estimating the correct sign
iv. The probability that the null hypothesis is true

-----------------------------------

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

-----------------------------------

5a. A player takes 10 basketball shots, with a 40% probability of making each shot. Assume the
outcomes of the shots are independent. Which of the following lines of code does not create a
random variable ~ representing the number of shots that go in?
i. y <- rbinom(1, 10, 0.4)
ii. y <- sum(rbinom(10, 1, 0.4))
iii. y <- sum(rbinom(10, 10, 0.4))
iv. y <- 0; for (i in 1:10) y <- y + rbinom(1, 1, 0.4)

-----------------------------------

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

-----------------------------------

5c. Which of these lines of R code prints, successively, the rows of matrix a (with dimensions
5 × 3)?
i. for (i in 1:3) print(a[i,])
ii. for (i in 1:5) print(a[i,])
iii. for (i in 1:3) print(a[,i])
iv. for (i in 1:5) print(a[,i])

-----------------------------------

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


-----------------------------------

6a. Which of these lines of R code fits a regression of y on x, with data set data0, using the lm
command, storing the result in object fit?
i. lm$fit(y ~ x, data=data0)
ii. fit(y ~ x, data=data0)
iii. fit(y ~ x, data=data0, model=lm)
iv. fit <- lm(y ~ x, data=data0)

-----------------------------------

6b. You record the median income in each state in 2013 and in 2015, and then you run a linear
regression on these 50 data points, predicting 2015 median income from 2013 median income.
What will be the approximate slope of this regression?
i. 0
ii. 0.5
iii. 1
iv. 2

-----------------------------------

6c. Consider a pre-test, post-test situation where scores on both tests have mean 50, and the
regression of post-test on pre-test has a slope of 0.6. A student scores 70 on the pre-test. What
is that student’s expected score on the post-test?
i. 42
ii. 62
iii. 72
iv. 92

-----------------------------------

6d. Suppose you have conducted an experiment on 100 people and you run a regression whose
estimated slope is 2.5 standard errors from zero. You now have cause to gather data on
an additional group of 50 people and fit the regression just to these new data. What is a
reasonable guess of the probability that the estimated slope will be “statistically significant”
in the replication?
i. 5%
ii. 40%
iii. 85%
iv. 95%

-----------------------------------


7a. One of the questions asked in the 2020 American National Election Study was feeling
thermometer score (a 0–100 measure) toward Donald Trump. We fit a linear regression
predicting feeling thermometer score from age. The result is the line ~ = 𝑎 + 𝑏𝑥 + error, with
errors normally distributed with mean 0 and standard deviation 𝜎. What is a plausible value
for 𝑏?
i. −0.20
ii. −0.02
iii. 0.02
iv. 0.20

-----------------------------------

7b. You have a data set with the variables income, age, male. What regression could you fit to
estimate the difference between the average incomes of men and women?
i. lm(income ~ male)
ii. lm(income ~ age)
iii. lm(income ~ male + age)
iv. lm(income ~ male*age)

-----------------------------------

7c. A survey is done of 𝑛/2 women and 𝑛/2 men, with the goal being to estimate the gender gap:
the difference in support for some candidate comparing the two sexes. Assuming the survey
is a random sample, approximately how large does 𝑛 have to be so the standard error of the
estimated gender gap is 5 percentage points?
i. 100
ii. 200
iii. 400
iv. 800

-----------------------------------

7d. The slope from a regression with an outcome variable ~ and a single predictor variable 𝑥 that
is a binary indicator variable is the same as what calculation?
i. The difference in the mean of 𝑥 and the mean of ~
ii. The difference in the mean of 𝑥 when ~ = mean(~) and the mean of 𝑥 when 𝑥 = mean(𝑥)
iii. The difference in the mean of 𝑥 when ~ = 0 and the mean of 𝑥 when ~ = 1
iv. The difference in the mean of ~ when 𝑥 = 0 and the mean of ~ when 𝑥 = 1

-----------------------------------

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

-----------------------------------

8a. Which of these quantities is not minimized in ordinary linear regression?
i. The average of the residuals
ii. The sum of the squares of the residuals
iii. The residual standard deviation
iv. The negative of the likelihood

-----------------------------------

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

-----------------------------------

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

-----------------------------------

8d. Given these three data points:

What is the residual sum of squares for the line ~ = 40 + 0.5𝑥?
i. 125
ii. 225
iii. 350
iv. The points don’t fall on a straight line, so the residual sum of squares is undefined.

-----------------------------------

8e. Which of the following lines of R code returns a regression ~ on 𝑥 with the intercept fixed at 0?

i. stan_glm(y ~ x, data=data0)
ii. stan_glm(y ~ x, data=data0, intercept=NULL)
iii. stan_glm(y ~ x, data=data0, prior_intercept=NULL)
iv. stan_glm(y ~ 0 + x, data=data0)

-----------------------------------

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

-----------------------------------

9a. Consider the regression line ~ = 0.2 + 0.3𝑥 + error , with errors normally distributed with
mean 0 and standard deviation 2. You observe a new data point at 𝑥 = 10. What is a 68%
predictive interval for the corresponding observation ~?
i. (1.2, 5.2)
ii. (−0.8, 7.2)
iii. (3.2 − 2/√𝑛, 3.2 + 2/√𝑛)
iv. (  ̄~ − 2/√𝑛,  ̄~ + 2/√𝑛)

-----------------------------------

9b. What is the approximate interval containing 95% of observations, if your data are normally
distributed with mean 5 and standard deviation 2?
i. (3, 7)
ii. (1, 9)
iii. (5 − √2, 5 + √2)
iv. (5 − 2√2, 5 + 2√2)

-----------------------------------

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

-----------------------------------

9d. Why might we use the R function posterior_linpred() instead of posterior_predict()?
i. When we want the best point prediction
ii. When we want to incorporate uncertainty into our prediction
iii. When we want uncertainty in the predicted average rather than for a single case
iv. When we want to use the normal distribution
(e) Consider this model that was used to predict the yield of mesquite bushes:
fit <- stan_glm(log(weight) ~ log(canopy_volume) +
log(canopy_slope) + group, data=mesquite)

-----------------------------------

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

-----------------------------------

10a. You want to write a line of R code that regresses income on age and male as well as the
interaction of both variables. The data are stored in the data frame data0. Which of the
following does not fit this model?
i. lm(income ~ age + male + age:male, data=data0)
ii. lm(income ~ 0 + age + male + age:male, data=data0)
iii. lm(income ~ age + male + age*male, data=data0)
iv. lm(income ~ (age + male)^2, data=data0)


-----------------------------------

10b. You are trying to assess the health benefits of walking. Your data variables are called health
(with 0 = bad health and 10 = good health), walks (with 0 = no walking, 1 = infrequent
walking, 2 = regular walks), and smoker (with 0 = nonsmoker and 1 = smoker). Which of
these regression specifications attempts to address the question of whether the benefits of
walking are different for smokers than for non-smokers?
i. walks ~ health + smoker
ii. walks ~ health + smoker + health:smoker
iii. health ~ walks + smoker
iv. health ~ walks + smoker + walks:smoker

-----------------------------------

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

-----------------------------------


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

-----------------------------------

10f. Consider the following interaction model: ~ = 𝛽0 + 𝛽1𝑥 + 𝛽2 𝑧 + 𝛽3𝑥𝑧 + error . How would we
estimate the average difference in ~ between when 𝑥 = 1 and 𝑧 = 4 and when 𝑥 = 2 and 𝑧 = 4?


i. The difference between 𝛽1 and 2𝛽1 + 𝛽3
ii. The difference between 𝛽1 + 4𝛽3 and 2𝛽1 + 4𝛽2 + 8𝛽3
iii. The difference between 𝛽1 + 𝛽3 and 2𝛽1 + 2𝛽3
iv. The difference between 𝛽1 + 4𝛽3 and 2𝛽1 + 8𝛽3

-----------------------------------

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

-----------------------------------

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

-----------------------------------

11c. Which of the following assumptions is typically least important for the goal of fitting a
regression model?

i. Equal variance of errors
ii. Linearity
iii. Additivity
iv. Representativeness

-----------------------------------

11e. A researcher plans to fit a linear regression to data from a group of adults, predicting their
physical flexibility given age. Flexibility is defined on a 0–30 scale based on measurements
from a series of stretching tasks. Which of the following represents a concern with the validity
assumption?
i. The stretching measurements do not correspond to aspects of flexibility that are of
real-world interest.
ii. The people in the study are volunteers and are healthier than the general population.
iii. Flexibility declines as a nonlinear function of age.
iv. Flexibility measurements are not close to normally distributed.

-----------------------------------

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

-----------------------------------

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

-----------------------------------

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

-----------------------------------

12e. The coefficients of a log-log model can also be called elasticities. What does it mean to
estimate 𝑞 as the elasticity of 𝑥 on ~?
i. For a 1 unit difference in 𝑥, we predict a 𝑞% difference in ~.
ii. For a 1 unit difference in 𝑥, we predict a 𝑞 unit difference in ~.
iii. For a 1% difference in 𝑥, we predict a 𝑞% difference in ~.
iv. For a 1% difference in 𝑥, we predict a 𝑞 unit difference in ~.

-----------------------------------

12f. Here is a log-log model: log ~ = 2 + 3 log 𝑥 + error. How can we represent the model in the
untransformed scale?
i. ~ = exp(2) + 𝑥3 + error
ii. ~ = 2𝑥3 ∗ error
iii. ~ = exp(2) ∗ 𝑥3 ∗ error
iv. ~ = exp(2) ∗ 3𝑥 ∗ error

-----------------------------------

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

-----------------------------------

13c. Given the logistic regression model, Pr(~ = 1) = logit−1 = (−2.5 + 0.44𝑥), what is the
maximum predictive difference corresponding to a unit difference in 𝑥?
i. 0.11
ii. 0.22
iii. 0.44
iv. 1.76

-----------------------------------

13d. When interpreting logistic regression coefficients, why is the divide-by-4 rule an upper bound
approximation for the expected difference in ~ associated with a 1-unit difference in 𝑥?
i. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0, thus where the expected value of ~ is minimized.
ii. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 1, thus where the expected value of ~ is maximized.
iii. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0.5, thus where the slope of the logistic curve is
maximized.
iv. It is accurate where logit−1 (𝑎 + 𝑏𝑥) = 0.5, thus where the intercept of the logistic curve
is maximized.

-----------------------------------

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

-----------------------------------

13f. A logistic regression is fit, using grade point average (on a 0–4 scale) to predict whether a
student will drop out of college. Which of these is a plausible value for the coefficient of
grade point average in this model?
i. −1
ii. 0
iii. 0.1
iv. 1

-----------------------------------

14a. Consider the model, Pr(~ = 1) = logit−1 (0.1 + 0.2𝑥 + 0.3𝑧 − 0.4𝑥𝑧), where ~ is an outcome
variable, 𝑥 is a pre-treatment variable, and 𝑧 is a randomly assigned treatment. For what value
of 𝑥 does the treatment have no effect?
i. −3/2
ii. 1/2
iii. 3/4
iv. There is no value of 𝑥 for which the treatment has no effect.

-----------------------------------

14b. 100 people are surveyed and asked about their happiness. 75 say they are happy and 25 say
they are not. A logistic regression is then fit, predicting this survey response on a constant
term. Approximately what will be the estimated coefficient?
i. 0.25
ii. 0.8
iii. 1.1
iv. 3.0

-----------------------------------

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

-----------------------------------

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

-----------------------------------

15b. A negative binomial regression is fit to data from many country-years estimating the number
of public protests in the country-year, given many predictors including per-capita GDP in
dollars. The model is re-fit using, as a predictor, per-capita GDP in tens of thousands of
dollars. What happens to the coefficient estimate and standard error?
i. The estimate and standard error both are multiplied by 10 000.
ii. The estimate and standard error both are divided by 10 000.
iii. The estimate is multiplied by 10 000 and the standard error is multiplied by 100.
iv. The estimate is divided by 10 000 and the standard error is divided by 100.

-----------------------------------

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

-----------------------------------

15d. Which of the following conditions must hold for a negative binomial regression to be equivalent
to a Poisson regression?
i. The reciprocal dispersion parameter is equal to 0.
ii. The reciprocal dispersion parameter is equal to 1.
iii. The predictive standard deviation of a data point is equal to its expected value.
iv. The predictive standard deviation of a data point is equal to the square root of its expected
value.

-----------------------------------

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

-----------------------------------

16b. You conduct an experiment in which half the people get a special get-out-the-vote message
and the others do not. Then you follow up after the election with a new random sample of 500
people to see if they voted. What is the approximate standard error of your estimated effect
size?
i. 0.015
ii. 0.03
iii. 0.05
iv. 0.07

-----------------------------------

16c. A study is designed which would have 80% power if it had 600 participants. But for budgetary
reasons, only 300 people could be included in the study. What is the approximate power of
this new study?
i. 30%
ii. 40%
iii. 50%
iv. 60%

-----------------------------------

16d. In a recent survey, 15% of Americans surveyed said they were crime victims in the past year.
When the survey is done again in a year, how large a sample would be needed to estimate this
proportion to within a standard error of 2 percentage points?
i. 0.15 ∗ 0.85/0.022
ii. √0.15 ∗ 0.85/0.02
iii. 0.15 ∗ 0.85 ∗ 0.022
iv. √0.15 ∗ 0.85 ∗ 0.02

-----------------------------------

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

-----------------------------------

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


-----------------------------------

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

-----------------------------------

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


-----------------------------------

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

-----------------------------------

18b. A researcher conducts a randomized experiment and estimates the treatment effect by
comparing the average outcome in the treatment group to the average outcome in the control
group. The resulting standard error is extremely high. Which of the statement is not necessarily
true?
i. A regression conditioning on pre-treatment variables that are highly predictive of the
outcome should reduce the standard error.
ii. The estimate is unbiased.
iii. Increasing the sample size should reduce the standard error.
iv. The randomization was not implemented properly.

-----------------------------------

18e. A researcher conducts a randomized experiment and estimates the treatment effect by regressing
the outcome on a treatment indicator and several pre-treatment predictors. Which of the
following is estimated by the coefficient of the treatment indicator?
i. The sample average treatment effect (SATE)
ii. The population average treatment effect (PATE)
iii. The conditional average treatment effect (CATE)
iv. The average treatment effect among the treated (ATT)

-----------------------------------

18f. Which experiment is likely to violate the stable unit treatment value assumption (SUTVA)?
i. A field experiment that randomizes students within a school to test the effect of healthy
snacks on health outcomes
ii. An online survey experiment that randomizes participants to test the effect of reading
fake news on policy support
iii. A lab experiment that randomizes participants to test the effect of a new drug
iv. None of the above

-----------------------------------

18g. Which of the following is a property of a randomized block design?
i. The same proportion of units is treated in each block.
ii. Each block has the same probability of treatment as all other blocks.
iii. Each unit has the same probability of being treated as all other units in its block.
iv. Every unit has the same probability of being treated as all other units in the sample.

-----------------------------------

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

-----------------------------------

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

-----------------------------------

19c. An experiment is performed on a treatment intended to improve college admissions test scores.
Every student in the experiment has already taken the test once, and for each student we have
this pre-test score, a measure of socioeconomic status, a randomized treatment assignment,
the post-test score, and the gain score (post-test minus pre-test). Two models are fit:
(1) post_test ~ pre_test + SES + z,
(2) gain_score ~ pre_test + SES + z

-----------------------------------

Which of the following statements is correct about the estimated treatment effect under the
two models?
i. Model 1 is better because it is predicting the outcome directly.
ii. Model 2 is better because the goal is to estimate improvement.
iii. Which model is better depends on the data.
iv. The two models are the same.

-----------------------------------

19d. Assume you have an unbiased estimate of the sample average treatment effect (SATE). Which
of these would make it an unbiased estimate of the population average treatment effect (PATE)?
i. Ignorability of treatment assignment
ii. Sample is representative of the population
iii. Stable unit treatment value assumption
iv. Efficiency property

-----------------------------------

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

-----------------------------------

20b. Consider the following simulation of pre-test 𝑥 and treatment 𝑧:
n <- 100
x <- runif(n, -2, 2)
z <- rbinom(n, 1, invlogit(2 + 3*x))
How would you characterize this assignment rule?
i. No problem with balance or overlap
ii. Problem with balance; no problem with overlap
iii. No problem with balance; problem with overlap
iv. Problem with balance; problem with overlap

-----------------------------------

20c. Which of the following models, predicting outcome ~ from pre-treatment predictor 𝑥 and
treatment indicator 𝑧, corresponds to a constant treatment effect?
i. y ~ x + z
ii. y ~ x + z + x:z
iii. y ~ x + z, family=binomial(link="logit")
iv. y ~ x + z + x:z, family=binomial(link="logit")

-----------------------------------

20d. The following model is fit to data from an observational study with pre-treatment variables 𝑢
and {, treatment indicator 𝑧, and outcome ~: ~ = 𝑏0 + 𝑏1𝑢 + 𝑏2{ + 𝑏3 𝑧 + 𝑏4𝑢{ + 𝑏5𝑢𝑧 + error .
Assuming ignorability of treatment assignment, what is the estimated treatment effect?
i. 𝑏3
ii. 𝑏3 + 𝑏5𝑢
iii. 𝑏3 𝑧 + 𝑏5𝑢𝑧
iv. 𝑏3 𝑧 + 𝑏4𝑢{ + 𝑏5𝑢𝑧

-----------------------------------

20e. Consider a propensity score used for matching. What does this propensity score represent?
i. The estimated probability that a unit receives treatment, given pre-treatment predictors
ii. The estimated probability that a unit is in an area of overlap, given pre-treatment predictors
iii. The estimated probability that a unit is in an area of balance, given pre-treatment predictors
iv. The estimated probability that a unit is representative, given pre-treatment predictors

-----------------------------------

21a. In a simple instrumental variables problem, there are four compliance types (Compliers,
Always Takers, Never Takers, and Defiers). If the standard assumptions for instrumental
variables estimation hold, which of the following statements must be true?
i. People are randomly assigned to the Always Takers and Never Takers groups.
ii. The expected number of Compliers equals the expected number of Defiers.
iii. Compliers and Always Takers will be approximately balanced in any pre-treatment
predictors.
iv. There are no Defiers.

-----------------------------------

21b. An experiment is performed in which students are randomly assigned to participate or not
participate in a study program. For each student, the following variables are recorded: a
pre-test score 𝑥, an encouragement indicator 𝑧, a participation indicator 𝑇, and a post-test score
~. Of the following assumptions, which is not required for instrumental variables estimation?
i. The effect of encouragement on participation for individual students is sometimes positive.
ii. The effect of encouragement on participation for individual students is never negative.
iii. Encouragement can affect post-test scores only for those students where it has a nonzero
effect on participation.
iv. The effect of the encouragement treatment cannot depend on the pre-test score.

-----------------------------------

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

-----------------------------------


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

-----------------------------------

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

-----------------------------------

21f. When interpreting an analysis using instrumental variables, when would the intent to treat
effect (ITT) be a more useful estimand than the conditional average treatment effect (CATE)?

i. When you want to know the aggregate effect of a treatment across compliers and
non-compliers
ii. When you want to isolate the causal effect for compliers
iii. When the monotonicity assumption is violated
iv. When the exclusion restriction is violated

-----------------------------------

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

-----------------------------------

22b. In which of the following models is ~ an increasing function of 𝑥 with an asymptotic threshold?
i. ~ = 𝑎 − 𝑏𝑥 − 𝑐𝑥2, where 𝑏 and 𝑐 are positive
ii. ~ = 1/(𝑎 + 𝑏𝑥), where 𝑏 is positive
iii. ~ = 𝑎 ∗ log(−𝑏𝑥), where 𝑏 is positive
iv. ~ = 𝑎 − 𝑏 ∗ exp(−𝑐𝑥), where 𝑏 and 𝑐 are positive

-----------------------------------

23a. Data are collected on each of 50 states for 10 years, and a regression is fit predicting crime
rate given a continuous measure of state policy. The model looks like this:
crime ~ policy + year + factor(state) + year*factor(state)
How many coefficients are in this model?
i. 53
ii. 101
iii. 493
iv. 562

-----------------------------------

23b. 200 women and 200 men are interviewed in a survey and asked their opinion on the death
penalty. 60% of the women surveyed and 70% of the men surveyed support the death penalty.
A linear regression is fit, predicting the survey response given a predictor, sex, that equals 1
for women and 2 for men. Approximately what will be the estimate and standard error for the
coefficient of sex?
i. 0.05 ± 0.05
ii. 0.05 ± 0.10
iii. 0.10 ± 0.05
iv. 0.10 ± 0.10

-----------------------------------


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

-----------------------------------

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

-----------------------------------

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




