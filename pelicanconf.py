# Pelican development config for echenique.com migration
AUTHOR = "Carlos Echenique"
SITENAME = "echenique dot com"
SITESUBTITLE = "Thoughts, stories and ideas."
SITEURL = ""

PATH = "content"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# Content layout (migrated from Ghost)
ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images", "extra"]

ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"
ARCHIVES_SAVE_AS = "archives/index.html"

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Feeds (disabled in dev)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme: Flex (cloned to ../Flex, kept alongside other repos in the GitHub folder)
THEME = "../Flex"
THEME_COLOR = "dark"
PYGMENTS_STYLE = "tokyonight-day"
PYGMENTS_STYLE_DARK = "tokyonight-storm"

# Plugins (installed via requirements.txt)
PLUGINS = ["photos", "thumbnailer"]

# Thumbnails for the article index (see Flex templates/index.html).
# Covers (article `Cover` metadata, content/images/...) get a small
# derivative at output/thumbs/<slug>/<file>_index.<ext>.
IMAGE_PATH = "images"
THUMBNAIL_DIR = "thumbs"
THUMBNAIL_SIZES = {"index": "150x?"}

# Markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": True},
    },
    "output_format": "html5",
}

# Favicon served from site root, plus CNAME for the www.echenique.com
# custom domain on GitHub Pages.
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}
FAVICON = "/favicon.ico"

RELATIVE_URLS = True
