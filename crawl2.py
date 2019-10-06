# Get instance
import instaloader
import json
L = instaloader.Instaloader()

# Login or load session
L.login("mauraputri", "instagrammm")

# Obtain profile metadata
profile_target = instaloader.Profile.from_username(L.context, "privat.in_id")

# Print list of followeers
for follower in profile_target.get_followers():
    followers_target = follower.username

profile = instaloader.Profile.from_username(L.context, followers_target)


for posts in profile.get_posts():
    
    hashtag = posts.caption_hashtags
    likes = posts.likes
    username = followers_target
    post = posts.caption
          
    if post is not None:
        post = post.encode('ascii', 'ignore')
           
for comment in posts.get_comments():
    comment = comment.text.encode('ascii', 'ignore')
            
       
    to_json_file = {
        'username: ': username,
        'caption: ': post,
        'hashtag: ': hashtag,
        'like: ': likes,
        'comment: ': comment}
    
    with open ('crawl_data.json' , 'w') as json_file:
        json.dump(to_json_file, json_file)

#the result of this program could end in json file,
        #but when we check the file, its still empty
        #we still try to fix these codes
