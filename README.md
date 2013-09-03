<h1>Twitter sentiment analysis</h1>
====================================

I made these exercises during the Introduction to Data Science course offered by Coursera at: https://www.coursera.org/course/datasci

The code is mine, but the following instructions are extracted from the course.


<h2>Twitter account configuration</h2>
---------------------------------------------------

The steps below will help you set up your twitter account to be able to access the live 1% stream.
 
●      Create a twitter account if you do not already have one.
●      Go to https://dev.twitter.com/apps and log in with your twitter credentials.
●      Click "create an application"
●      Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
●      On the next page, scroll down and click "Create my access token"
●      Copy your "Consumer key" and your "Consumer secret" into twitterstream.py
●      Click "Create my access token." You can Read more about Oauth authorization.
●      Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret.
 
access_token_key = "<Enter your access token key here>"
access_token_secret = "<Enter your access token secret here>"
 
consumer_key = "<Enter consumer key>"
consumer_secret = "<Enter consumer secret>"
 
●      Run the following and make sure you see data flowing and that no errors occur.  Stop the program with Ctrl-C once you are satisfied.
 
$ python twitterstream.py
 
You can pipe the output to a file, wait a few minutes, then terminate the program to generate a sample.  Use the following command:
 
$ python twitterstream.py > output.txt


<h2>Derive the sentiment of each tweet</h2>
---------------------------------------------

You need to create with the above example a file with twitter data, let's say output.txt

Run: $ python tweet_sentiment.py <sentiment_file> output.txt

where <sentiment_file> is AFINN-111.txt or other file with sentiment rated words


<h2>Derive the sentiment of new terms</h2>
-------------------------------------------

Again, we need twitter data extracted from the stream.

Run: $ python term_sentiment.py <sentiment_file> output.txt
 
The script prints to stdout each term-sentiment pair, one pair per line, in the following format:        
         
<term:string> <sentiment:float>


<h2>Compute Term Frequency</h2>
-----------------------------------

Given a file of tweets as an input proceed in the following way:
 
Run: $ python frequency.py <tweet_file>
  
The script prints to stdout each term-frequency pair, one pair per line, in the following format:
         
<term:string> <frequency:float>


<h2>Getting the happiest State</h2>
---------------------------------

Run: $ python happiest_state.py <sentiment_file> output.txt

The script prints the two letter state abbreviation to stdout of the happiest USA State.


<h2>Top ten hash tags</h2>
----------------------------------

Computes the ten most frequently occurring hash tags from the data in output.txt
  
Run: $ python top_ten.py <tweet_file>

The script prints to stdout each hashtag-count pair, one per line, in the following format:
         
<hashtag:string> <count:float>
