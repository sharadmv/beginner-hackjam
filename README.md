Introduction
======================
Welcome to Hack Jam 2013! If you don't know already, a Hack Jam is a low-stakes, low-pressure, shorter hackathon that Hackers at Berkeley holds at least once every semester.

If you've never hacked before, don't be afraid! This is a guide that will help you through your first hack. We'll be building Cheeper©, a lightweight, simpler version of Twitter.

After you finish this, you'll have:

* Created a Flask web server

Step 1: Learn and install Python
=========================

The rest of the guide will assume some basic knowledge of the Python 2 language. Hopefully you've picked up from Python from 61A, but if you haven't, head over to the official Python [tutorial](http://docs.python.org/tutorial), which is pretty good! 

You need to install Python 2.7 to complete this hack. You can do that [here](http://www.python.org/download/releases/2.7/).

Step 2: Set up your environment
================================

Before any hack, you need to make sure all your dependencies are set up. 

Python has two amazing tools, called `virtualenv` and `pip` that enable developers to create sandboxes for their projects and easily install any online packages and libraries that other people have written. We'll be using mainly these two tools.

The first thing you need is to make sure you have a Python package called `setuptools` installed. Here's how to install it:

* Ubuntu: `sudo apt-get install python-setuptools`
* OSX: 
* Windows:



Installing `setuptools` will give you a command line tool called `easy_install`, which we'll use to install `virtualenv`.

Enter the following in your terminal to install `virtualenv`.
```
$ sudo easy_install virtualenv
```

Now a quick word about `virtualenv`. It's a Python tool that allows you to create "sandboxes," or isolated environments in which you can code. When you need a Python library, you could install it globally, which means all your Python projects on your computer could use it. You could also install it locally, which means you install libraries on a project-by-project basis and no project will have any more dependencies available than it needs. The "sandbox" mentality means that we make sure each project stands alone, which means a lot when you may want to deploy these projects to remote computers.

`virtualenv` comes with a "package manager" called `pip`. `pip` allows you to actually install libraries from online. Suppose I want to use a library that parses PDFs for me. BAM! `pip install pdfminer`. If I want a library that scrapes web pages for me: BAM! `pip install beautifulsoup`. You get the idea. `pip` stores all the awesome libraries that people have built for Python and with a single command, you get access to them.

Now that you have `virtualenv` installed, you have to create a folder for your project.

```
$ mkdir cheeper
```

We want to make the `cheeper` directory a `virtualenv` environment, so we run the command:
```
$ virtualenv -p python2.7 cheeper/
```

If you look inside `cheeper` now, you'll see that there are now 4 folders inside called `bin/`,`include/`, `lib/`, and `local/`.

To jump into the `virtualenv` you've created, `cd` into the `cheeper` directory and run:
```
$ source bin/activate
```

Your terminal prompt should now have a `(cheeper)` at the front. This is how you know you're inside your virtual environment. 


Whoa, this is awesome. You're in your own sandbox now. You can see what libraries you currently have installed by running:

```
$ pip freeze
```

To leave your `virtualenv`, just run:
```
$ deactivate
```

We'll be using `virtualenv` more in the next section. If you're curious as to what else it can do, look up more on [this site](https://pypi.python.org/pypi/virtualenv).

Step 3: Setting up Flask
=====================================
[Flask](http://flask.pocoo.org/) is a Python web framework.

After this point, make sure you're working in your `virtualenv`. (It should say "`(cheeper)`" at the left of your terminal prompt).

To install Flask just run:
```
$ pip install flask
```

Wow that was simple (hopefully)! Remember that if at any point, stuff isn't installing/working properly, ask a neighbour the nearest H@B office for help.

Okay, so let's get started with Flask. 

First, what exactly is a web framework? When a person goes to a website, they send a request to that website, asking for the site's content. Since we're building the website, our web framework, Flask, will handle requests that are sent to us, and send back our site's content.

Let's try running the "Hello World" example on the [Flask website](http://flask.pocoo.org).

Copy and paste the example and put it into a file called `server.py`. This code imports Flask, creates an application (`app`), and defines a "route" (we'll go over that in a second), and finally starts up the server.

Try running it to make sure Flask was installed correctly.
```
$ python server.py
```
If it says Flask isn't importing, make sure you're in the `virtualenv`.
If it says something like: "Running on http://127.0.0.1:5000", then it's working! Test it yourself by going to either `localhost:5000` or `127.0.0.1:5000` in your favorite browser. It should say "Hello World!".

> *Note*: both `localhost` and `127.0.0.1` are addresses for your own computer and `5000` is the "port" number.

Now that you have this working, please go through the examples on the Flask [quick start page](http://flask.pocoo.org/docs/quickstart/) and familiarize yourself with the Flask framework. Make sure you understand what a route is and how to do routing with Flask. Hint: decorators.

Step 4: Creating a user interface
===========================
Let's create our home page for Cheeper©. Create a directory in your `cheeper` directory called `static`. This will be the folder for our *static* files, or the files that don't change and are just retrieved and sent down by Flask when a browser asks for them.

Your project directory should look like this now:
```
cheeper/
    bin/
    include/
    lib/
    local/
    server.py
    static/
```

Now inside your static folder, create a file called `index.html`.
In it, put the following skeleton.
```html
<html>
  <head>
    <title>Cheeper© - better than Twitter</title>
  </head>
  <body>
  Hello World!
  </body>
</html>
```

This is HTML, or HyperText Markup Language. It's a language that browsers understand and use to render web pages. In HTML files, you define the content and layout of your web page. `index.html` is the canonical name for the default web page that's rendered when you go to a site, so `index.html` will function as the home page.

Right now, if you open the file in your web browser, you'll get a page that says "Hello World!", but on your tab, it should say what we put into the `<title>` tag.

Now, I suggest reading up on the basics of HTML. Make sure you understand how to create forms. Here's a [Codecademy tutorial](http://www.codecademy.com/courses/web-beginner-en-Vfmnp/0/2) on creating web forms for your edification!

So now for some user interface design (which is something I, the writer of this guide, am terrible at, so feel free to rage at my designs). And of course, if you are design inclined yourself, feel free to throw away my suggestions and use your own.

Our Cheeper© webpage should include some glamorous logo, a space to type your cheep and cheep it to the world. We also need a feed, for all the cheeps that have been cheeped.

First let's add the logo, which will just be really big text. We can do this with the `<h1>`. Add an `<h1>` tag into the body of `index.html`, which will be our logo.

```html
...
<body>
  <h1>Cheeper©</h1>
</body>
...
```

Now let's add the form to write and submit your cheeps. Cheeps are only 76 characters long, right?

```html
...
<body>
  <h1>Cheeper©</h1>
  <form>
    Name:
    <input type="text" /> 
    Cheep:
    <input type="text" maxlength="76"/> 
    <input type="submit">
  </form>
</body>
...
```

Awesome! Our awesome, beautiful user interface is almost done. Let's now add a splace for the Cheeper© feed to appear.

```html
...
<body>
  <h1>Cheeper©</h1>
  <form>
    Name:
    <input type="text" /> 
    Cheep:
    <input type="text" maxlength="76"/> 
    <input type="submit">
  </form>
  <div id="feed">
  </div>
</body>
...
```
