#!/bin/sh

set -eu

SKILLS="immerse xray reconcile driftcheck curate"

if [ "$#" -ne 0 ]; then
  printf 'Usage: %s\n' "$0" >&2
  exit 64
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPOSITORY_ROOT=$(dirname -- "$SCRIPT_DIR")

: "${HOME:?HOME must be set}"
DESTINATION_ROOT=${CURSOR_SKILLS_DIR:-"$HOME/.cursor/skills"}

for skill in $SKILLS; do
  source_path="$REPOSITORY_ROOT/skills/$skill"
  if [ ! -f "$source_path/SKILL.md" ]; then
    printf 'Missing source skill: %s\n' "$source_path/SKILL.md" >&2
    exit 1
  fi
done

collisions=""
for skill in $SKILLS; do
  destination_path="$DESTINATION_ROOT/$skill"
  if [ -e "$destination_path" ] || [ -L "$destination_path" ]; then
    collisions="${collisions}
  $destination_path"
  fi
done

if [ -n "$collisions" ]; then
  printf 'Installation aborted; these destinations already exist:%s\n' \
    "$collisions" >&2
  printf 'Inspect them and remove or rename them explicitly before retrying.\n' \
    >&2
  exit 1
fi

mkdir -p "$DESTINATION_ROOT"
stage=$(mktemp -d "$DESTINATION_ROOT/.vibelib-install.XXXXXX")
trap 'rm -rf "$stage"' EXIT HUP INT TERM

for skill in $SKILLS; do
  cp -R "$REPOSITORY_ROOT/skills/$skill" "$stage/$skill"
done

for skill in $SKILLS; do
  mv "$stage/$skill" "$DESTINATION_ROOT/$skill"
done

rmdir "$stage"
trap - EXIT HUP INT TERM

printf 'Installed VibeLib skills in %s:\n' "$DESTINATION_ROOT"
for skill in $SKILLS; do
  printf '  /%s\n' "$skill"
done
printf 'Reload Cursor if the skills are not visible immediately.\n'
