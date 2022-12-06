# Static HTML
To create a simple static HTML page and style it using CSS. See the *HTML_template.html* and *CSS_template.css* under the `lib/templates/HTML_CSS_templates` folder to get you going.

Create a valid HTML 5 pages that will have a page containing:
* Information regarding the project
* A page describing the chosen format.
* Add a menu that will allow users to navigate the different pages. 
* Include a footer with contact information. 

Use CSS3 styling in an external stylesheet document to add styling to your pages.
HTML and CSS pages should be validated.

The following online tools can be used to validate:

* [HTML5](https://html5.validator.nu/); select as validator input: *text field*
* [CSS3](https://jigsaw.w3.org/css-validator/#validate_by_input)


# Dynamic site - upload
Finally, time to add some dynamic content to your site!

The user should get instructions on what settings from your tool he/she can change. Also your tools is probably goint to need some input data which should be uploaded to your program.

One way to deal with this dynamic settings is by using forms that allows an user to upload settings, data or change visualization settings of you program. 


For details over the use of *forms* see the presentation "HTML5" on Blackboard and [W3schools](https://www.w3schools.com/html/html_forms.asp)

Some example code is given provided by the teacher. See the scripts:
* *basic_Flask_app.py*
* *simple_routing.py*
* *form_handling.py*
* *Flask_static_folder.py*
  
 in the */lib* directory.


 # Dynamic site - showing results
Use templating (Jinja2) to incorporate the dynamic results from your analysis into your site.

For example code see the scripts:
* *basic_Flask_app.py*
* *Flask_app_without_templating.py*
* *Flask_app_with_templating.py*

For more advanced Jinja and CSS inclusion see:
* *Jinja2_inheritance.py*

in the */lib* directory.

**Briefly:** 

Lines of Jinja code between {% ... %}

variables between {{...}}

For information about Jinja templating see [Jinja](http://jinja.pocoo.org)

You also want to use **matplotlib** from python for easy and nice graph generation. See [matplotlib](https://matplotlib.org) for more information