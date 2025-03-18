AUTHOR = 'TRI'
SITENAME = 'TRI-Blog'
SITEURL = ""

SITESUBTITLE = '一関高専総合技研部 公式ブログ'

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = 'themes/aboutwilson'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Builded html file name

SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'


# Blogroll
LINKS = (
    ("X(Twitter)", "https://x.com/NITIC_Giken"),
    ("Instagram", "https://www.instagram.com/nitic_giken/"),
    ("YouTube", "https://youtube.com/channel/UCWzD5T_rBI4QKLPVGZo2Q8A?si=aSBOSZR3XGf4Xw8O")
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
