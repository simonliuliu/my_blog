AUTHOR = 'Simon Liu'
SITENAME = 'Simon 写字的地方'
SITEURL = ""
SITESUBTITLE = '区块链九年老炮，喜欢研究有趣的区块链项目，✍🏻记录投资学习过程和思考'

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Gitbook", "https://15670662477.gitbook.io/simons-knowledge-hub/"),
    ("Podcast", "https://m.ximalaya.com/selfshare/albumnew/43799385?cId=1005&uid=62974016&shrdv=XIC2EMF-xvMFKdfQmBA0Ksgb1GIpN-Iwdi4&shrh5=iphone&shrid=192b9ef3fce9f78&shrdh=1&shrpid=192b9ef3fce113dc&srcType=6&subType=1010&srcId=43799385&tpName=url&commandShareId=b52e1576355f3958719d00646881c7d4&shareTime=1729696317390&shareLevel=1"),
    ("Mirror", "https://mirror.xyz/0xE5B8988C90Ca60D5f2A913cb3BD35A781aE7F242"),
)
# 设置使用的主题
THEME = 'themes/alchemy'

# （可选）设置网站 logo
SITELOGO = 'images/avatar.jpg'
SITELOGO_SIZE = 128  # 可以调大小

# # Social widget
# SOCIAL = (
#    ('GitHub', 'https://github.com/simonliuliu'),
#     ('Twitter', 'https://x.com/0xsimonliu'),
# )
ICONS = [
    ('twitter', 'https://x.com/0xsimonliu'),
    ('github', 'https://github.com/simonliuliu'),
]
# 显示文章摘要
SUMMARY_MAX_LENGTH = 50

# 开启显示作者
SHOW_ARTICLE_AUTHOR = True

# 开启文章日期
SHOW_DATE_MODIFIED = True

# 页脚信息
SITE_LICENSE = 'Content licensed under CC-BY-SA'

# 如果你想让文章列表首页只显示部分摘要，而不是全文，确保开启：
SUMMARY_MAX_LENGTH = 50

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ['images']

THEME_CSS_OVERRIDES = ['static/css/custom.css']