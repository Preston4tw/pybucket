"""
For a psuedo spec, see http://wiki.xkcd.com/irc/Bucket
"""
## Factoids
# X is Y
# X is also Y
# X is Y is Z
# X are y
# X <verb> y, ex. X <hates> Y
# X<'s> Y
# X <reply> Y
# X <action> Y
# remember {nick} {snippet}
# literal X
# literal[#] X
# literal[*] X
# X =~ /m/
# "what was that?"
# X =~ s/m/n/
# X =~ s/m/n/i
# X =~ s/m/n/g
# undo last

## Variables
# $noun
# $nouns
# $verb
# $verbs
# $verbed
# $verbing
# $adjective
# $preposition
# $who
# $someone
# $to
# $op
# $vehicle
# $room
# $celebrity
# $mood
# $color
# $bodypart
# $digit
# $nonzero

## Inventory
# inventory
# list items
# puts <item> in Bucket
# gives Bucket <item>
# gives <item> to Bucket
# gives Bucket (his|her) <item>
# delete item #<N>
# $item
# $giveitem
# $newitem
# detailed inventory

# Bucket: I am (male|female|androgynous|inanimate|full name)
# what gender is <username>
# Gender variables: $subjective, $objective, $reflexive, $possessive, $determiner

# list vars
#  (n) for noun, (v) for verb
# list var <variable>
# add value <variable> <value>
# remove value <variable> <value>
# var <variable> type <var|verb|noun>
#  verb types can accept -ing, -ed, -s suffix
#  noun types can accept -s

# If no one has said anything for a while...
#  mylifeisaverage.com
#  twitter.com/shitmydadsays
#  twitter.com/fakeapstylebook
#  twitter.com/fakeanimalfacts
#  twitter.com/god_damn_batman

# alias x => y
# merge x => y
# delete x
# delete #nnnnn
# forget that
# forget #nnnnn
# undo last [#channel]
# protect X
# unprotect X
# lookup n
# load plugin foo
# unload plugin foo
# create var <variable>
# remove var <variable>

# set X Y
# get X

# ignore X
# unignore X
# list ignored
# exclude X
# unexclude X
# <nick> is <gender>
# don't quote <nick>
# do quote <nick>

# shut up
# go away
# shut up for <time>
# unshut up
# come back
# join #X
# Part #X
# stat keys
# stat <key>
# restore topic #channel
# <word> has <N> syllables

## Special factoids
# Don't know
# Band name reply
# Tumblr name reply
# Duplicate item
# Drops item
# Pickup full
# Takes item
# List items
# Uses reply
# Automatic Haiku

## Special functions
# Math: 10 + 2
# Bad-ass: bad-ass car => bad ass-car
# "do you know.*" <reply> "No, but if you hum a few bars I can fake it"
# Say it again
# sexchange
# super efective
# TLA
# the fucking
