Back in 2006, a group of guys created a Cheeper clone that took off and made them millionaires. I'm not sure if you've heard of this site, but it's called Twitter. It's not quite as cool as what we've built.

Anyways, one awesome thing that a team of engineers at Twitter did was create something called Bootstrap. Bootstrap is a tool that provides you with a bunch of customizable features to make your website look pretty. Among them are a grid system to help you organize and place your content, good typogrpahy choices, pretty button designs, and cool animations.

They have all their documentation on their [site](http://getbootstrap.com/). We recommend browsing through it and getting familiar with it first. Definitely look at their [examples](http://getbootstrap.com/getting-started/#examples) section and browse through the source code of their page (Right click and click on "View Page Source"). The [Grids](http://getbootstrap.com/examples/grid/) example is particularly important.

Setting up
================
You can download Bootstrap [here](http://getbootstrap.com/getting-started/).

You're going to get a zip file called `bootstrap-3.0.0-dist.zip` with the folders `css`, `fonts`, and `js`. Copy those three folders into your `static` folder. You'll also need jQuery, which is a widely used Javscript library that makes it easier to add interactive elements to your website. Download it from [here](http://code.jquery.com/jquery-2.0.3.js) and put it in your `static/js` folder. Now you're ready to use bootstrap!

First steps
================
Let's first get the [starter template](http://getbootstrap.com/examples/starter-template/) working on our site. Copy paste the HTML from the [page source](view-source:http://getbootstrap.com/examples/starter-template/) and put it in a new file inside `templates` called `index2.html`. You'll have to update your `server.py` to render this file instead of the old `index.html` file. 

We're going to have to make some changes to this file, namely with the file paths to the CSS and Javascript files.
```html
<link href="../../dist/css/bootstrap.css" rel="stylesheet">
```
```html
<script src="../../assets/js/jquery.js"></script>
<script src="../../dist/js/bootstrap.min.js"></script>
```
