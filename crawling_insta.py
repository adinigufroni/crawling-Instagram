import instaloader
import json

C = instaloader.Instaloader(max_connection_attempts=0)

#log in
C.login('adinigfrn', 'adngf156')

#get profile target
profile_target = instaloader.Profile.from_username(C.context, 'cobanihpake')

#json file
jsfile1 = open('crawling_data1.json', 'w+')
jsfile2 = open('crawling_data2.json', 'w+')

#get crawling data1
data_ring1 = []
get_followers = profile_target.get_followers()

for follower in get_followers:
    followers_profile_target = follower.username
    profile = instaloader.Profile.from_username(C.context, followers_profile_target)
    profile_post = 1
    
    for post in profile.get_posts():
        if post.caption == None:
            profile_post += 1
            continue
        else:
            profile_post += 1
            caption = post.caption.encode('ascii', 'ignore').decode('ascii')
            location = post.location
            hashtag = post.caption_hashtags 
            likes = post.likes
            comments = post.get_comments()
            full_comments = []
            
            for comment in comments:  
                list_comment = comment.text.encode('ascii', 'ignore').decode('ascii')
                full_comments.append(list_comment)
                
            hasil_crawl = {
                'ID':followers_profile_target,
                'CAPTION':caption,
                'LOCATION':location,
                'HASHTAG':hashtag,
                'LIKES':str(likes),
                'COMMENTS':full_comments}

            print(
                "ID : @", followers_profile_target, "\n",
                "CAPTION : ", caption, "\n",
                "LOCATION : ", location, "\n",
                "HASHTAG : ", hashtag, "\n",
                "LIKES : ", likes, "\n",
                "COMMENTS : ", full_comments, "\n",
                "\n")
            
            data_ring1.append(hasil_crawl)

#get crawling data2
data_ring2 = []

for follower in get_followers:
    followers_profile_target = follower.username
    profile = instaloader.Profile.from_username(C.context, followers_profile_target)
    profile_post = 1

    get_followers2 = get_followers(followers_profile_target)
    
    for follower2 in get_followers2:
        followers2_profile_target = follower2.username
        profile2 = instaloader.Profile.from_username(C.context, followers2_profile_target)
        profile_post = 1
        
        for post in profile2.get_posts():
            if post.caption == None:
                profile_post += 1
                continue
            else:
                profile_post += 1
                caption = post.caption.encode('ascii', 'ignore').decode('ascii')
                location = post.location
                hashtag = post.caption_hashtags 
                likes = post.likes
                comments = post.get_comments()
                full_comments = []
                
                for comment in comments:  
                    list_comment = comment.text.encode('ascii', 'ignore').decode('ascii')
                    full_comments.append(list_comment)
                    
                hasil_crawl = {
                    'ID':followers_profile_target,
                    'CAPTION':caption,
                    'LOCATION':location,
                    'HASHTAG':hashtag,
                    'LIKES':str(likes),
                    'COMMENTS':full_comments}

                print(
                    "ID : @", followers_profile_target, "\n",
                    "CAPTION : ", caption, "\n",
                    "LOCATION : ", location, "\n",
                    "HASHTAG : ", hashtag, "\n",
                    "LIKES : ", likes, "\n",
                    "COMMENTS : ", full_comments, "\n",
                    "\n")
                
                data_ring2.append(hasil_crawl)
            
J = json.dumps(data_ring1)
jsfile1.write(J)
jsfile1.close()

J2 = json.dumps(data_ring2)
jsfile2.write(J2)
jsfile2.close()
