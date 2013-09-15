Introduction
======================
Welcome to Hack Jam 2013! If you don't know already, a Hack Jam is a low-stakes, low-pressure, shorter hackathon that Hackers at Berkeley holds at least once every semester.

If you've never hacked before, don't be afraid! This is a guide that will help you through your first hack. We'll be building Cheeper, a lightweight, simpler version of Twitter.

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
sudo easy_install virtualenv
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

If you look inside `cheeper` now, you'll see that there are now 3 folders inside called `bin/`,`include/`, and `lib/`.

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

Step 3: Flask
=====================================
[Flask](http://flask.pocoo.org/) is a Python web framework. 
