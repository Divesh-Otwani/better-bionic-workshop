# better-bionic-workshop

> Update on 2/11/18: I've fallen behind. This will be done by thursday 2/15/18
> Check this after then :}

This is a collection of examples to help bico students 
learn a tool called dash which helps you
build parts of a course scheduling tool to replace bionic.

Dash is a web framework in python.

The file structure is the following.

* references-for-divesh
  * Ignore these
  * This just stores a bunch of examples for me to use
* simple-examples
  * Read the readme in that folder. It gives directions on
    how you should run through the examples to learn the basics of 
    dash
  * Each examples is a self-contained web server.
    Everything is extensively documented and you should be able
    to just read the file and understand everything.
    Please email me at dotwani@haverford.edu if you don't 
    understand something. I'll improve it!
* starter-files
  * There are three starter files
  * Each is self contained and explains basic tasks to do
    and an overall task. Also, a full version of the project 
    requires you to learn more.



## Rundown

### What are web servers?

If you're unfamiliar, a web server is just an infinite while loop
that responds to messages it gets sent over the internet.

#### Intuition

So, when you visit gmail and click on things,
type things in, (or even hit enter to the url),
messages are sent to that program, the web server, on a computer 
far away and that program responds responds by changing the web page
that's displayed to you.


#### A Clear Description

* Your web browser displays websites with all their buttons, text fields and 
  stuff using html files. Html files are like instructions on how to 
  display a nice looking website.
  * Read [this](http://www.simplehtmlguide.com/whatishtml.php) and 
    test the example on your own computer.
* When you visit a website, your web browser sends a message to the program 
  called the web server (which runs on a computer far away) to 
  send you the html file to display the web page. This message
  is sent over the internet.
  * This is what loads the first page.
  * This also happens anytime you click on links
* Then, sometimes you click buttons and enter input.
  Some of this input can be responded to with tiny programs 
  inside your html, written in a (terrible) programming langugage
  called javascript.
  But, responding to some of your input requires the program that sent 
  you the website to do something. For example, clicking the sent mail button
  in gmail. In these cases your web browser sends a  message over the internet
  to the web server.
  That program, the web server, understands your message and sends you a new 
  html file for your web browser to display.
* This summarizes the basics of websites and internet use.
* Other notes
  * Sometimes the web server saves some information you send it
    on the computer it runs on (far, far away).
  * The messages you send are broken into categories, 
    'get' messages, 'post' messages are two.
  * With secure sites, rsa encrytpion is used to 
    hide the messages sent to the web server.
  



### What can we do with bionic?

Bionic has many features, all of which are made poorly.
I see three fantastic projects.

* Course visualization
  * I give you 15 courses I'm interested in, maybe ranked
  * Show me a tree of all the possible choices and schedules 
    or calanders of what my week would look like.
  * I should filter so I don't get schedules that 
    are impossible. I should also be able to start with a few 
    courses I know I'm going to take for sure.
* Waitlist Exchange
  * Often we get waitlisted for classes but other people don't
    but ... we have classes they want more. We could trade.
  * Freshmen trade writing seminars a lot.
  * It would be awesome if everyone could input 
    (class I have, class I want) pairs and a web server could
    automatically make trading circles. 
    * For example, say I have class A but want B more. 
      Say you have class B and want C more.
      Say your roomate has C but wants A more.
      We could all put our info on this website and it could match us up.
      Then, after we're all connected from this app, we email each other 
      and the registrar;
      I give your roomate class A, he gives you class C and you give me class B.
* Graduation Requirements
  * A nice tool where you can input your classes and 
    visualize possible paths to finish your major, or just graduate.
      


### Other internship projects


* A website to help you find bico events and stuff nearby (like philly)
* A twitter for haverford
* A meme website
* You can probably think of something



## Setup

From the [website](https://plot.ly/dash/installation), 
do this:

```python
pip install dash==0.20.0  # The core dash backend
pip install dash-renderer==0.11.3  # The dash front-end
pip install dash-html-components==0.8.0  # HTML components
pip install dash-core-components==0.18.1  # Supercharged components
pip install plotly -U
```

Then, just run the following.

> `python simple-examples/palindrome.py`


Go to the website and things should work!



















