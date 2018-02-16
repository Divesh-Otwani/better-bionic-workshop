# simple-examples

Hopefully these are simple enough 
and clear enough to give you an idea of how things work.


To learn dash and these tools, you should go through 
the materials in this order.

_Note: You don't need to do all of these. Do the first three or four at least_


* Read the ** section below
* hello.py
  * A basic hello world app.
* palindrome.py
  * A minimal app to show you all the basics.
* inputstuff.py
  * Adding on multiple ways to add input.
* table.py
  * Making html tables
* style.py
  * Using css to make things look pretty

When your done, read
[this](https://plot.ly/dash/sharing-data-between-callbacks)
and browse the rest of the documentation [here](https://plot.ly/dash/).




> **Read this part below here !!!**


# Background on what we're doing


## What are web servers?

If you're unfamiliar, a web server is just an infinite while loop
that responds to messages it gets sent over the internet.

### Intuition

So, when you visit gmail, facebook, reddit, twitter, and click on things,
type things in, (or even hit enter to the url),
messages are sent to that program, called a web server, on a computer 
far far away and that program responds responds by changing the web page
that's displayed to you.


### More than Intuition: A Clear Description

* Your web browser displays websites with all their buttons, text fields,
  colors and stuff using html files. 
  Html files are like instructions on how to 
  display a nice looking website.
  * Read [this 'simple guide to html'](http://www.simplehtmlguide.com/whatishtml.php) and 
    test the example on your own computer.
  * This is an example of a static web site.
    You don't need to run a while loop because it does 
    just one task.
  * Also, skim some of [https://www.w3schools.com/html/default.asp](https://www.w3schools.com/html/default.asp)
* When you visit a website, your web browser sends a message to the program 
  called the web server (which runs on a computer far away) to 
  send you the html file to display the web page. This message
  is sent over the internet.
  * This is what loads the first page.
  * This also happens anytime you click on links
* You can think of a web page as just some really long string
  (that's basically what files are). This string is sent over the internet
  from the web server to your computer and then your web browser 
  displays it really nicely.
* Then, sometimes you click buttons and enter input.
  Some of this input can be responded to with tiny programs 
  inside your html, that string, written in a (terrible) programming langugage
  called javascript.
* But, responding to some of your input requires the webserver to do things. 
  For example, clicking the sent mail button
  in gmail. 
  In these cases your web browser sends a message over the internet
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


#### What do I need to know to make web servers?

* You need to know some background
  * You need to know how html is displayed in your web browser
  * Make sure you read the 'simple guide to html' referenced above
  * Also checkout [w3 schools](https://www.w3schools.com/tags/tag_hn.asp)
    just enough to be able to have a very very basic idea of how 
   [my website](http://divesh-otwani.github.io/My-Online-Workspace/)
    works
* You need to understand tools like dash that help you build html
  * This is what we teach you here!
  * You do NOT need to know exactly what html is built.
    You just need to have a clear idea of what that html does.


## How does dash work to build a webserver?

 * See the examples

## Why dash and not some other tool?

 * Other tools are not in python and are 
   really complicated.
 * (If we did this in haskell, it would 
   be way simpler!)
  
## How do I put my web server "online"?

This is called deploying a website.
You can read about it [here](https://www.codeschool.com/beginners-guide-to-web-development/deploying-your-first-website), but 
we can just take care of that for you if you want.
(Obviously, we won't take any credit for your work!)






