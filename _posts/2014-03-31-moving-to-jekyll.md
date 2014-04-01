---
title: Moving to Jekyll
layout: post
---

How I converted my nicely named markdown files into date preffixed markdown files:

    egrep -o "201[234]-[0-3][0-9]-[0-3][0-9]"  * | tr ':' ' ' | awk '{print mv $1,$2$1}' | xargs -L 1 mv

Macro in vim
