# Comparing Protocol Buffers, SQL, MongoDB in Twitter data

The goal is to experiment with working with data in various degrees of structure.  

Work with a dataset of Tweets encoded in multiple ways to compute some summary information and reflect on the pros and cons of each approach.

`twitter.json` contains a JSON-encoded tweet on each line.      

In the following steps, I use three systems to perform data
analysis: Protocol Buffers, relational database SQLite, and
MongoDB.  Using each of the three systems, I'm going to answer the
following three questions:

1. Find the number of deleted messages in the dataset.
2. Find the number of tweets that are replies to another tweet.
3. Find the five user IDs (field name: `uid`) that have tweeted the most.     
