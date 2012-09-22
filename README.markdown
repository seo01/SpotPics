Spot Pics
=========
An application for generating Damian Hirst style spot pictures from digital images.

Why?
----
Damian Hirst's spot paintings were an exploration of colour, materials and structure without form. Inspired by [his paintings](http://en.wikipedia.org/wiki/File:Hirst-LSD.jpg) I started getting interested in how web pages use colour. This is the results.

Examples
--------
* http://numenore.co.uk/store/images/spots.html
* http://numenore.co.uk/stuff#spots

Requires
--------
* PIL (the [Python Image Library](http://www.pythonware.com/products/pil/)).
* If you want to generate images of web pages, I recommend paulhammond's available on github.

Execution Examples
------------------
~~~
python grid_from_path.py <<directory of images>> <<output html file>>
~~~

~~~
python spot_svg.py <<input image>> <<output svg>>
~~~