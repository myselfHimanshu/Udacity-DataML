# Analyzing the NYC Subway Dataset

<i>by Himanshu Panwar ,Udacity Intro to Data Science , Project 1 </i>

<b>Section 1: Statistical Test</b>

<b>1.1 Which statistical test did you use to analyze the NYC subway data? Did you use a one-tail or a two-tail P value? What is the null hypothesis? What is your p-critical value?</b>

I used Mann-Whitney u-test to analyze the dataset. The two-tailed test was appropriate.

Null hypothesis is that the two population are the same. There is no relationship between two measured phenomena, or no difference among groups. The p-critical value used was 0.05 or 5%.

<b>1.2 Why is this statistical test applicable to the dataset? In particular, consider the assumptions that the test is making about the distribution of ridership in the two samples.</b>

As per the histogram , neither the ‘rain’ nor ‘ no-rain’ was normally distributed, so the non-parametric test Mann-Whitney U-test was a good fit to dataset.

To confirm neither datasets were normally distributed , Shapiro-wilk could be applied.

 <b>1.3 What results did you get from this statistical test? These should include the following numerical values: p-values, as well as the means for each of the two samples under test. </b>

![pvalue.png](https://github.com/myselfHimanshu/Udacity-DataML/blob/master/Intro-To-Data-Science/NYCSubway/images/image01.png)

<b>1.4 What is the significance and interpretation of these results?</b>

p-value satisfies the p-critical value.

Conclusion 95% confidence that null hypothesis is false , ridership is different with or without rain.

<b>Section 2: Linear Regression</b>

<b>2.1 What approach did you use to compute the coefficients theta and produce prediction for ENTRIESn_hourly in your regression model:

OLS using Statsmodels or Scikit Learn

Gradient descent using Scikit Learn

Or something different?</b>

I used Gradient Descent  to train the model with default learning rate(alpha) and iterations.

I also used OLS using Statsmodels to predict EXITSn_hourly using ENTRIESn_hourly.

<b>2.2 What features (input variables) did you use in your model? Did you use any dummy variables as part of your features?</b>

features used : [rain,precipitation,hour,mean Temperature]

Dummy Variable include : UNIT (turnstile location) this variable made wide variation between different stops.

<b>2.3 Why did you select these features in your model? We are looking for specific reasons that lead you to believe that the selected features will contribute to the predictive power of your model.

              Your reasons might be based on intuition. For example, response for fog might be: “I decided to use fog because I

              thought that when it is very foggy outside people might decide to use the subway more often.”

              Your reasons might also be based on data exploration and experimentation, for example: “I used feature X  

              because as soon as I included it in my model, it drastically improved my R2 value.” </b>

I included [rain,precipitation,hour,mean Temperature] because these are the features that can affect the ridership.

Hypothesis can be : “people prefer subway more often when it’s raining or when there is bad weather outside”.

<b>2.4 What are the parameters (also known as "coefficients" or "weights") of the non-dummy features in your linear regression model?</b>

[-4.24736210e+00, 8.60518981e+00, 4.64832083e+01, 4.64163466e+02, -3.19114921e+01, 1.08898857e+02]

<b>2.5 What is your model’s R2 (coefficients of determination) value?</b>

R^2 value is (0.458044314039)

<b>2.6 What does this R2 value mean for the goodness of fit for your regression model? Do you think this linear model to predict ridership is appropriate for this dataset, given this R2  value?</b>

R^2 : Coefficient of Determination . How our model fits.

It only tells about 45.8% variation.

<b>Section 3: Visualization</b>

<b>3.1 One visualization should contain two histograms: one of  ENTRIESn_hourly for rainy days and one of ENTRIESn_hourly for non-rainy days.</b>
You can combine the two histograms in a single plot or you can use two separate plots.If you decide to use to two separate plots for the two histograms, please ensure that the x-axis limits for both of the plots are identical. It is much easier to compare the two in that case.
For the histograms, you should have intervals representing the volume of ridership (value of ENTRIESn_hourly) on the x-axis and the frequency of occurrence on the y-axis.
For example, each interval (along the x-axis), the height of the bar for this interval will represent the number of records (rows in our data) that have ENTRIESn_hourly that falls in this interval.Remember to increase the number of bins in the histogram (by having larger number of bars). The default bin width is not sufficient to capture the variability in the two samples.

![rain vs no-rain](https://github.com/myselfHimanshu/Udacity-DataML/blob/master/Intro-To-Data-Science/NYCSubway/images/image03.png)

Plotting overlaid histogram , not normally distributed , less rainy days than no  rainy days.

<b>3.2 One visualization can be more freeform. You should feel free to implement something that we discussed in class (e.g., scatter plots, line plots) or attempt to implement something more advanced if you'd like. Some suggestions are:</b>

                 Ridership by time-of-day

                 Ridership by day-of-week

![By day of week](https://github.com/myselfHimanshu/Udacity-DataML/blob/master/Intro-To-Data-Science/NYCSubway/images/image02.png)

The most subway entries: Wednesday and Friday

Sunday and Saturday least entries.

![By time of the day](https://github.com/myselfHimanshu/Udacity-DataML/blob/master/Intro-To-Data-Science/NYCSubway/images/image00.png)

How ridership varies based on Subway station (UNIT)

![plotting the average number of subway entries at each hour.](https://github.com/myselfHimanshu/Udacity-DataML/blob/master/Intro-To-Data-Science/NYCSubway/images/image04.png)

 plotting the average number of subway entries at each hour.

There are several peaks throughout the day, with the most prominent ones being at noon and 8pm.

Are more people going out at (12pm) and  (8pm).

<b>Section 4: Conclusion</b>

<b>4.1 From your analysis and interpretation of the data, do more people ride the NYC subway when it is raining or when it is not raining?</b>

By the result of U-test p-value: 0.025, we can interpret with high level of certainty that people ride subway when it is raining.

<b>4.2 What analyses lead you to this conclusion? You should use results from both your statistical tests and your linear regression to support your analysis.</b>

The positive coefficient for the rain  indicates the presence of rain contributes to increased ridership.

The means of both data sets are not that different from each other, the Mann-Whitney U test did indicate that there was a statistically significant change in ridership for rain vs. no-rain.

So we can claim that rain increases subway ridership.


