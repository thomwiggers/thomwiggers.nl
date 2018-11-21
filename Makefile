SERVER=clearlyreta.rded.nl:/var/www/thomwiggers.nl

.PHONY: all
all: site


static/.well-known/thomwiggers.asc:
	gpg --batch --output "$@" --armor --export 915D4ED34871E82F

static/.well-known/openpgpgey/hu/sse5gyx9eaexk3pndqafyju99sru31bh:
	./generate-openpgpkey-hu.py --exist-ok --output-dir static/.well-known/openpgpkey/hu/ --mail-domain thomwiggers.nl

.PHONY: .well-known
.well-known: static/.well-known/thomwiggers.asc static/.well-known/openpgpgey/hu/sse5gyx9eaexk3pndqafyju99sru31bh

.PHONY: site
site: .well-known
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
