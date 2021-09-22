# %%
import pandas
import itertools

from psaw import PushshiftAPI

api = PushshiftAPI()

cols = [
    "id",
    "author",
    "url",
    "title",
    "selftext",
    "domain",
]

if __name__ == "__main__":
    gen = api.search_submissions(subreddit='dataengineering')
    df = pandas.DataFrame([thing.d_ for thing in itertools.islice(gen, 500)])
    df.selftext = df.selftext.str.replace('\\n', ' ')
    df[cols].to_csv("sample_keyword_project/data/posts.csv")

# all_awardings
# allow_live_comments
# author
# author_flair_css_class
# author_flair_richtext
# author_flair_text
# author_flair_type
# author_fullname
# author_is_blocked
# author_patreon_flair
# author_premium
# awarders
# can_mod_post
# contest_mode
# created_utc
# domain
# full_link
# gildings
# id
# is_created_from_ads_ui
# is_crosspostable
# is_meta
# is_original_content
# is_reddit_media_domain
# is_robot_indexable
# is_self
# is_video
# link_flair_background_color
# link_flair_richtext
# link_flair_template_id
# link_flair_text
# link_flair_text_color
# link_flair_type
# locked
# media_only
# no_follow
# num_comments
# num_crossposts
# over_18
# parent_whitelist_status
# permalink
# pinned
# pwls
# retrieved_on
# score
# selftext
# send_replies
# spoiler
# stickied
# subreddit
# subreddit_id
# subreddit_subscribers
# subreddit_type
# thumbnail
# title
# total_awards_received
# treatment_tags
# upvote_ratio
# url
# whitelist_status
# wls
# created
# post_hint
# preview
# thumbnail_height
# thumbnail_width
# url_overridden_by_dest
# removed_by_category
