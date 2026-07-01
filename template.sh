#!/bin/sh

export DOOMTOOLS_PATH="/usr/share/doomtools"
export DOOMTOOLS_JAR="/usr/share/java/doomtools/doomtools.jar"
for arg in "$@"; do
    case "$arg" in
        --update*)
            echo 'DoomTools was installed from dnf, updating in this manner is unsupported.'
            echo 'Update using "dnf upgrade" instead'
            exit 1
            ;;
    esac
done
exec /usr/bin/java -cp "$DOOMTOOLS_JAR" -Xms64M -Xmx4G @MAINCLASS@ "$@"
