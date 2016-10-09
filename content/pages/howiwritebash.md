Title: How I write bash
Save_as: howiwritebash.html

This is a short guide to help me write bash scripts since I usually tend to
review my previous code in order to remember how I write Bash.

[TOC]

### Template file

This is what I usually start every bash script with:

    #!/bin/bash

    set -o errexit
    set -o nounset
    set -o pipefail

The shebang subject has been [discussed](https://github.com/LuRsT/hr/commit/61b938bb4f622c42eba3f3aa31e233be870408c1)
about quite a bit.

The others are flags that make errors easier to debug.

### Conditions

#### Arithmetic

    if (( variable <= 0 )); then
        echo "HI"
    fi

#### Strings

Check if string exists

    if [[ -n ${variable} ]]; then
        echo "HI"
    fi


### Loops

    for file in $(ls); do
        echo $file
    done

.

    STRINGS='one two'

    for STRING in $STRINGS; do
        echo $STRING
    done
