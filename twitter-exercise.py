# boss at twitter asks you to write a function to show a user's most recent and oldest tweets
# find 1st, find nth

tweets = ['today', 'some tweet', 'random lol', 'my first tweet!']
# assuming the tweets are stored in some array, sorted chronologically, this problem is relatively simple
print(tweets[0], tweets[-1])

# now let's say that each tweet is an object/dictionary with a data key/property, and your boss wants you to write a function that compares all the dates of tweets

tweets = [
    {
        'tweet': 'today',
        'date': 2022
    }, {
        'tweet': 'some tweet',
        'date': 2019
    }, {
        'tweet': 'random lol',
        'date': 2017
    }, {
        'tweet': 'my first tweet!',
        'date': 2012
    }
]

# big O of comparing the dates of all tweets with existing data structure is O(n^2) because we have to compare every item in array of tweets to every other item in array
# given our knowledge of big O, it might make sense for us to store this information in a better format to improve the big O complexity