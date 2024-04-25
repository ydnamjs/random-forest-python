features = [
    "User Age", 
    "User Description Length", 
    "User Follower Count", 
    "User Friends Count",
    "User Favorites",
    "User Lists",
    "User Statuses Count",
    "Hashtag Count",
    "Mention Count",
    "URL Count",
    "Text Length",
    "Text Digits",
    "Retweeted Favorites Count",
    "Is Truncated",
    "User Is Default",
    "Number Us"
]

LABELS_PATH = "./data/labeled_tweets.txt"
FEATURE_PATH = "./data/tweet_feature.txt"

LABELS_FILE = open(LABELS_PATH, "r")
FEATURES_FILE = open(FEATURE_PATH, "r")

LABELS_LINES = LABELS_FILE.readlines()
FEATURES_LINES = FEATURES_FILE.readlines()