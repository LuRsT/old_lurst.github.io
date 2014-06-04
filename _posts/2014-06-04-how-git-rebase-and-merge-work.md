---
title: How does git rebase and merge work
layout: post
---

Today I was tasked with rebasing our project's git repo, and since there was
some confusion wether we should keep rebasing or merging, here is a very simple
example of how they look like in the tree:

![These where the instructions](http://i.imgur.com/zW2Xax9.png)

I created a test repo and did the following steps:

{% highlight bash %}
$ vim README.md
( changes ...)
$ git add README.md
$ git commit -m "Initial commit"
$ git branch branch1
$ git checkout branch1
$ vim README.md
( changes ...)
$ git add README.md
$ git commit -m "Added a small change"
$ vim README.md
( more changes ... )
$ git add README.md
$ git commit -m "Yet another change"
$ git checkout master
$ touch colour.txt
$ git add colour.txt
$ git commit -m "Added colour file"
{% endhighlight %}

I did this of course using my [beloved git aliases](https://github.com/LuRsT/Setup/blob/master/.gitconfig)
, but for readability, I wrote them down in the "normal" way.

Now after setting it up, I hope you have a guess on how the tree looks like,
`master` has 2 commits, one that is shared with `branch1` and the other which is
new, while `branch1` has the first `master` commit, but not the last one.

Notice that we don't have any conflicts for simplicity.

So, how should we proceed to have a clean tree? First, let's see what a merge does:

{% highlight bash %}
$ git checkout master # Make sure you are in the correct branch
$ git merge branch1
{% endhighlight %}

Now, I have an alias that displays a little awesome graph showing the tree, I
took a screenshot of the resulting graph:

![merge](http://imgur.com/K6T2rtX.png)

Not a very clean tree...

Let's see how rebase behaves, then:

{% highlight bash %}
$ git reset --hard HEAD^ #This will kill the last commit which was our merge
$ git rebase branch1
{% endhighlight %}

Without delay, let's take a look at the tree:

![rebase](http://imgur.com/G7FbKtT.png)

Much better!
