## **Data explaination**

(use crawl.py)
First we logged in to one of our team's account then we choose privat.in_id as our profile/account target. From each privat.in_id's followers, we can get metadata such as:
1. username/id : 
    when an account doesn't have any posts, then the program move to the next followers
2. caption : 
    in every caption, we ignore the emoticons but still print hashtags
3. hashtag : 
    hashtags that already shown in caption
4. likes : 
    it shows how many likes of the post
5. comments : 
    it shows every comments of the post (without emoticon)
