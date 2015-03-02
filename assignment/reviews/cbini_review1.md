## Peer Review 1

### Strengths of their project (things you particularly like about it)
1. You did a very good job getting and cleaning the dataset.  There is also a good amount of very detailed data dictionaries and explanations. It helped me a lot with the context of this data since I'm not very familiar with the k-12 education system and related terms.

2. You did very well exploring the dataset with various visuals such as scatter matrix, histograms and qqplot. 

3. The code that test the distribution of each feature and the correlation between different features and SGP was very thorough. Not only linear regression was tested but also exponential distribution. And this did explain some of the features very well.

### Comments about things you think could be improved
1. Instead of testing the correlation between each feature and SGP separately with `f_select.f_regression`, you can also write a for loop to get the p-value for each feature and then only focus on the features that are significant.

### Questions about things you don't understand
1.  According to the definition from https://www.k12.wa.us/assessment/SGP/FAQ.aspx#1 looks like a student growth percentile is a number between 1 and 99. So I'm curious that why in this dataset there was 0 and 100 in the 'SGP_MAP_Winter_Math' column. So could this related to why you did not see a normal distribution as you expected?



### Comments about their code
1. The code blocks are very well organized and easy to read.


### Suggestions for next steps
1. Instead of SGP, is there any other metrics we can use to measure student's progress? 
2. Collect more data and repeat this study periodically.
3. Search on web to see if there are other studies conducted about SGP.

