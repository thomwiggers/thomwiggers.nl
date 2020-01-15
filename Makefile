SERVER=archeron.wg.rded.nl:/var/www/thomwiggers.nl

.PHONY: all
all: site

.PHONY: site
site:
	#pipenv run academic import --assets
	hugo --enableGitInfo --minify

.PHONY: serve
serve:
	hugo server --buildDrafts --buildFuture

.PHONY: rsync
rsync: site
	rsync public/ -ave ssh --delete "${SERVER}"

.PHONY: rsync
rsync-dry: site
	rsync public/ -ave ssh --dry-run --delete "${SERVER}"

# vim : set ft=make noet :
