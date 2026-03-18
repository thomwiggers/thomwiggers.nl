#!/usr/bin/env bash
set -euo pipefail

# ── Hugo (extended) ───────────────────────────────────────────────────────────
HUGO_VERSION=$(grep hugo_version /workspace/hugoblox.yaml | awk '{print $2}' | tr -d "'")
ARCH=$(dpkg --print-architecture)
echo "==> Installing Hugo extended v${HUGO_VERSION} (${ARCH})"
curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${ARCH}.deb" \
    -o /tmp/hugo.deb
sudo dpkg -i /tmp/hugo.deb
rm /tmp/hugo.deb
echo "==> Hugo $(hugo version)"

# ── Node + pnpm ───────────────────────────────────────────────────────────────
PNPM_VERSION=$(grep '"packageManager"' /workspace/package.json | grep -oP 'pnpm@\K[^"]+')
echo "==> Installing Node 20 and pnpm v${PNPM_VERSION}"
curl -fsSL https://fnm.vercel.app/install | sudo bash -s -- --install-dir /usr/local/bin --skip-shell
fnm install 20
fnm default 20
eval "$(fnm env)"
npm install -g "pnpm@${PNPM_VERSION}"
echo "==> pnpm $(pnpm --version)"
