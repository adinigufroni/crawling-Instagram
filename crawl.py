# get instance
import instaloader
C = instaloader.Instaloader()

# Log in
C.login("adinigfrn", "adngf15")

# get profile data
profile_target = instaloader.Profile.from_username(C.context, "privat.in_id")

# print list of followers
for follower in profile_target.get_followers():
    followers_profile_target = follower.username
    

    profile = instaloader.Profile.from_username(C.context, followers_profile_target)
    #print(type(profile))

#get post's details
    for posts in profile.get_posts():
        post = posts.caption
        #if post is 
        hashtag = posts.caption_hashtags
        likes = posts.likes

        #comment = posts.comments
        #for comment in posts.get_comments():

        if post is not None:
            print("Id : ", followers_profile_target)
            print("CAPTION : ", post.encode('ascii', 'ignore'))  #ignore emoticon
            print("HASHTAG : ", hashtag)
            print("LIKE : ", likes)

            for comment in posts.get_comments():
                print("COMMENT : " , comment.text.encode('ascii', 'ignore'))
            print("\n")
