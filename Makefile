SERVER=clearlyreta.rded.nl:/var/www/thomwiggers.nl

.PHONY: all
all: site


static/.well-known/thomwiggers.asc:
	--batch --output "$@" --armor --export 915D4ED34871E82F

static/.well-known/openpgpgey/hu/sse5gyx9eaexk3pndqafyju99sru31bh:
	./generate-openpgpkey-hu.py --exist-ok --output-dir static/.well-known/openpgpkey --mail-domain thomwiggers.nl

.PHONY: .well-known
.well-known: static/.well-known/thomwiggers.asc static/.well-known/openpgpgey/hu/sse5gyx9eaexk3pndqafyju99sru31bh

.PHONY: site
site: .well-known
	~/go/bin/hugo --enableGitInfo --minify

.PHONY: serve
serve:
	~/go/bin/hugo server --buildDrafts --buildFuture

.PHONY: rsync
rsync: site
	rsync public/ -ave ssh --delete "${SERVER}"

.PHONY: rsync
rsync-dry: site
	rsync public/ -ave ssh --dry-run --delete "${SERVER}"

# vim : ft=make noet :
