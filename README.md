# better-bionic-workshop


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

Now you should be able to use dash.
To test this just run the following.

> `python simple-examples/palindrome.py`


Go to the website and things should work!

**Now, just go to the simple-examples section, learn stuff and make websites!**


# Projects: Use this section for ideas

## What can we do to better bionic?

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
      


## Other internship projects

* A website to help you find bico events and stuff nearby (like philly)
* A twitter for haverford
* You can probably think of something
 * Websites are really cool and useful!

















