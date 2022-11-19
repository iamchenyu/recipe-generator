<!-- README TOP -->

<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/iamchenyu/recipe-generator">
    <img src="static/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Recipe Generator</h3>

  <p align="center">
    An easy-to-use tool to save time and spark inspiration in cooking! 
    <br />
    <a href="https://github.com/iamchenyu/recipe-generator/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://jd-recipe-generator.herokuapp.com/">View Demo</a>
    ·
    <a href="mailto:jadeyw7@gmail.com">Contact</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#user-flow">User Flow</a></li>
    <li><a href="#about-api">About API</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details> 
<br />

<!-- ABOUT THE PROJECT -->

## About The Project

[![Web Application Screen Shot](/static/screenshot.png)](https://jd-recipe-generator.herokuapp.com/)

Have you ever had a moment of staring at the food in your fridge but having no idea what
to make?  
Have you ever wasted any food by throwing it in the trash can because it sit in
your fridge for too long but you still didn’t know how to make it?  
Are you tired of making the same dish at least 5 days a week?  
What about the frustration when you finally treat yourself to a hearty, homey, and healthy meal and realize you don’t know how to cook?

The web application is designed to help users eat brighter and healthier. No more scratching your head to think of how to make a meal out of broccoli, eggplant, and carrot.  
Type in the ingredients you have on hand and Tada! Easy Vegetable Fried Rice! It only takes 5 steps in 25 minutes and has calories as low as 235 kcal per serving!

Save your time and your leftover ingredients in the fridge! Explore new recipes to eat
healthily and have fun!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

- [![Javascript][javascript.com]][javascript-url]
- [![Bootstrap][bootstrap.com]][bootstrap-url]
- [![JQuery][jquery.com]][jquery-url]
- [![Python][python.com]][python-url]
- [![Flask][flask.com]][flask-url]
- [![WTForms][wtforms.com]][wtforms-url]
- [![SQLAlchemy][sqlalchemy.com]][sqlalchemy-url]
- [![Jinja][jinja.com]][jinja-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->

## Features

- [ ] Feature 1

User registration & login & edit profile

- [ ] Feature 2

Search recipes based on user typed-in ingredients

- [ ] Feature 3

Check the detailed information of a recipe, including diets, cuisines, nutrition information, ingredients, and cooking instructions

- [ ] Feature 4

Save & Unsave a recipe to a user's profile

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## User Flow

- This web application acts as a private backyard for users to search, check, save and unsave recipes based on the ingredients they typed in. So users need to either register or log in before playing around with the application.
- After the authentication, users will be redirected to the homepage where they can input ingredients and make the recipe research.
- By default, users will get no more than 6 recipes back and have an overlook of each one's diet labels, cuisines, and calorie information. Users can also click on one recipe to find more detailed information, including a summary, ingredients, nutrition labels, and cooking instructions.
- If users like this recipe, they can click the heart button on the top right of the recipe photo and save it to the local database. Likewise, they can click the heart button again to unsave the recipe.
- Users can check their saved recipes as a list. They can also edit their user profile in the application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ABOUT API -->

## About API

This web application is using an external API [spoonacular](https://spoonacular.com/food-api/docs#Search-Recipes-Complex) to fetch recipe data. The API has a daily quota limit and will respond with the error code 402 and no more calls can be made until the quota resets the next day.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Chenyu Wang - [@iamchenyu](https://github.com/iamchenyu) - email@<jadeyw7@gmail.com>

Project Link: [https://github.com/iamchenyu/recipe-generator](https://github.com/iamchenyu/recipe-generator)

[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/chenyuwang-/
[product-screenshot]: images/screenshot.png
[javascript.com]: https://img.shields.io/badge/javascript-000000?style=for-the-badge&logo=javascript&logoColor=white
[javascript-url]: https://www.javascript.com/
[bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[bootstrap-url]: https://getbootstrap.com
[jquery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[jquery-url]: https://jquery.com
[python.com]: https://img.shields.io/badge/python-35495E?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[flask.com]: https://img.shields.io/badge/flask-blue?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://www.python.org/
[wtforms.com]: https://img.shields.io/badge/wtforms-20232A?style=for-the-badge&logoColor=white
[wtforms-url]: https://wtforms.readthedocs.io/en/3.0.x/
[sqlalchemy.com]: https://img.shields.io/badge/sqlalchemy-red?style=for-the-badge&logo=sqlalchemy&logoColor=white
[sqlalchemy-url]: https://www.sqlalchemy.org/
[jinja.com]: https://img.shields.io/badge/jinja-8b0000?style=for-the-badge&logo=jinja&logoColor=white
[jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/
