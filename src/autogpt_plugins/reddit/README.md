# desojo/autogpt-twitter 🐣

A plugin adding reddit posting into Auto GPT

## Features

- make a reddit post by using the `reddit_post(post_title, post_text, subreddit)` command

## Installation

1. Clone this repo as instructed in the main repository
2. Add this chunk of code along with your reddit API information to the `.env` file within AutoGPT:

```
################################################################################
### REDDIT API
################################################################################

# REDDIT_USERNAME=
# REDDIT_PASSWORD=
# REDDIT_CLIENT_ID=
# REDDIT_CLIENT_SECRET=
# REDDIT_USER_AGENT=
```

## Reddit API Setup

1. Create a reddit account
2. Go to [Reddit preferences/apps] https://www.reddit.com/prefs/apps
3. Create a an app
4. Choose a name for your project
5. Select Script; "Script for personal use. Will only have access to the developers accounts" and write a description
6. Grab the keys: "Personal use script" this will be your REDDIT_CLIENT_ID and "secret" this will be your REDDIT_CLIENT_SECRET
7. REDDIT_USER_AGENT example 'projectname by /u/redditusername"