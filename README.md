# whatisonthe.tv 

**what·isonthetv**  */ˈwhatˌisonthetv/*

[ ![Codeship Status for swmcc/whatisonthe.tv](https://codeship.com/projects/11a1b900-8f7f-0132-6404-6add16588dd2/status?branch=master)](https://codeship.com/projects/61263)

*Noun:*  
A set for receiving television broadcasts.

*Synonyms:*	
audi, box, video, telly, tube, small screen

![TEE-VEE](http://f.cl.ly/items/3d0M1Z113y2L2A2r293U/Old-School-TV-television-296019_1544_1500.jpg "TEE-VEE")

## Description

Takes the feed(s) given to it and puts the informtion ingested into various
black boxes.

At the time of writing (Feb 2015) the only feed given is an [XMLTV](http://wiki.xmltv.org/index.php/Main_Page) one.

I've had several iterations of a tvlistings site over the years. Mainly built 
around [this](https://github.com/swmcc/TV-Listings) version. 

I want to utilise several bits of technology to offer a unique way of seeing what is on the tv.
This will solve a problem for me and also give me an actual use case (other than a TODO list).

## Purpose

There are lots of TV Listings sites/apps out there. All of them present the same information in the same way and it is usually based around a channel and time.
To me this is an old fashioned way of browsing and woefully ineffective. With the advent of ['VOD'](http://en.wikipedia.org/wiki/Video_on_demand) and ['Internet TV'](http://en.wikipedia.org/wiki/Internet_television) the model of basing a listings site around a channel and/or time isn't really viable anymore.

As a user I want to be able to do several things:

 ```Can I see at a glance all the films that Jack Nicholsan is starring in any given (reasonable) time frame?```

 ```Can I see any episodes that are going to air in the next two weeks of the X-Files that are related to the 'arc'?```

 ```Can I see any films that star Martin Sheen that were made between 1975-1982 and any guest star appearances in any TV show ever? And if not can I see this information anyway.```

 ```Can I browse by genre on all channels and then search on the synopsis. For example "startups".```

## Development Info

```
git clone https://github.com/swmcc/whatisonthe.tv.git 
cd whatisonthe.tv 
virtualenv venv # if you install venv somewhere else or use mkvirtualenv then amend the Makefile accordingly
make pip
make run # starts a server locally on port 8010 
```

## Testing

```make tests```

## Deployment

```git push origin master```

[Codeship](http://www.codeship.com) will know what to do.
