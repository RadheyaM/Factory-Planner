[View the Live Project](https://packing-calc.herokuapp.com)

# Packing Calc App - Overview

The packing calculator app is designed for use in a production scheduling setting.  The app allows the user to create, retrieve, update and delete runs of products and packaging and assign them to weekly plans.  Reports are generated in the detail view / live plan pages with information relevant to other team members involved in the physcial packing of finished products.

# Table of Contents
+ [Planning](#planning)
  - [Account Permissions](#account-permissions)
  - [User Stories](#user-stories)
  - [Database Schema](#database-schema)
  - [Application Flowcharts](#application-flowcharts)
  - [Initial Wireframes](#initial-wireframes)
  - [Visual Design Choices](#visual-design-choices)
+ [Features](#features)
  - [Navigation](#navigation)
  - [Search Pages](#search-pages)
  - [Create Form](#create-form)
  - [Update Form](#update-form)
  - [Delete Form](#delete-form)
  - [Detail Pages](#update-form)
  - [Modals](#modals)
  - [User Accounts](#user-accounts)
  - [Messages](#messages)
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
  - [Python Validation](#python-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Functionality Tests](#functionality-tests)
  - [Issues](#issues)
  - [Planned Improvements](#planned-improvements)
  - [Web Browser Compatibility](#web-browser-compatibility)
  - [Adaptability](#adaptability)
+ [Deployment](#deployment)
+ [Credits](#credits)

# Planning

  Access the [Projects Board](https://github.com/users/RadheyaM/projects/2) for this app.

## Account Permissions
Users lacking appropriate permissions cannot see the buttons for those functions, thus reducing error 403 forbidden instances.
 - Admin, all access.
 - OpsManager, CRUD functionality except to delete plans.  Can't access the Admin site.
 - PackingManager, View and Edit a Packing Run to indicate when it has been successfully packed.
 - Manager, can View but not change anything.
 - New User, For the purposes of development/submitting to be marked a user can create an account and immediately have access to  view the site, although not any CRUD functionality - in real use setting that would not be desirable.

## User Stories

As a User I want to be able to:
 - Navigate the site quickly and effectively.
 - Login, logout.
 - View which plan is current, in planning or complete.
 - View reports on a given week.
 - Search for specific Plans, Products, Runs and Packaging Configurations.
 - View Products, Runs and Packing Configurations.
 - Access instructions on how to use and navigate the site.

As the Operations Manager I want to be able to:

 - Create, retrieve, update and delete all important database objects relating to a plan.
 - Leave notes relating to a particular run.
 - Be the only non-admin user able to make changes to a plan or its components.
 - Generate effective and useful reports in the Detail/Live Plan views for other members of the team to get their jobs done.

As the Packing Manager I want to be able to:

 - See what runs are planned for the week.
 - See what times are assigned to each packing team.
 - View notes left by the OpsManager.
 - Mark an assigned run as complete adding a note if necessary.

As the Raw Materials Manager I want to be able to:

 - See what packaging will be required for a week
 - View notes left by the OpsManager.
 - View existing packaging configurations to confirm correct.

## Database Schema

Packing Runs are objects consisting of information concerning how many cases of a product should be packed at a given time.  In relation to a Packing Run information can be accessed for all other tables in the database, such as packaging required, team times etc.

Runs contain product packing information, the product, cases required and a name.  The user creates a run and can assign it to as many plans as necessary rather than having to create a new run for each plan.  There are usually regular case quantites required each week for a particular product, so runs act as a sort of 'favourite settings' system.

Weeks are the basis for distinguishing/organising a timeframe for particular runs.

Teams pack the products and are included to help scheduling staff as well as for the user to get an idea what schedule is viable in terms of time restrictions in a given week.

Products ready for sale, each product has a packaging configuration assigned to calculate packaging required for a particular run quantity.

Pack - this is the packing configuration for a particular product or set of products.

<img src="media/readme-design/database-schema.png">

## Initial Wireframes

[Wireframes PDF](media/readme-design/initial-wireframes.pdf)

## Application Flowcharts
<img src="media/readme-design/app-flowchart1.png">
<img src="media/readme-design/app-flowchart2.png">
<img src="media/readme-design/app-flowchart3.png">

## Visual Design Choices 

### The use of colour
The site has a red navigation bar and footer as that is the colour of the company it's designed for.

Colour on the rest of the site is used mostly to signify function to the user.  The colour in buttons shows function is available and particular colour used also indicates if the action is to view/create (greens), edit (blue), delete (red).  Text can be missed but the combination of text and a particular colour should help reinforce meaning to the user. 

Just as stars stand out in the night sky because of the surrounding blackness, so the buttons and colourful highlights of the site stand out and are much more effect against a clear white background.  This approach is taken by many large and successful sites, such as Google and Amazon.

Colour used to indicate function to the user:
<br>
<img src="media/readme-colors/complete-black.png">
<br>
<img src="media/readme-colors/planning-yellow.png">
<br>
<img src="media/readme-colors/current-blue.png">

<br>
<img src="media/readme-colors/planning-plan.png">
<br>
<img src="media/readme-colors/current-plan.png">
<br>
<img src="media/readme-colors/complete-plan.png">
<br>
<img src="media/readme-colors/red-danger-delete.png">

### Icons
Icons are used throughout the site to signify function to the user.  An image speaks a thousand words and a trash can is just as effect as writing 'delete' while being more visually appealing.  Images alongside words look good and convey meaning quicker to the user giving the whole experience of navigation a more intuitive feeling.

# Features
<img src="media/readme-features/detail-top.png">

## Navigation
<br>
<br>
<img src="media/readme-features/nav-right.png">
<br>
<img src="media/readme-features/nav-login.png">
<br>
At the top of the app is a navigation bar.  The left-hand side contains a link to the Live Plan (as shown above) and the other four links lead to the Plans, Packaging, Products and Runs search pages respectively.  To the right we have an Account Logged in name (unless not loggedin), which when clicked provides a dropdown with change password and logout functionality.  Next to that is a button that triggers a help modal and finally a previous page button.

## Search Pages
<br>
<img src="media/readme-features/search-plan-template.png">

There are four search pages, one for each of the objects that can be created to make up a plan run.  Each search page starts with extra in-page navigation buttons to toggle smoothly between the pages and to indicate which page is active with a red background.  
Below that is a search bar.  On searching a term in the title of the items listed below, the items will be filtered accordingly.  The clear button will reveal all objects once again.

<img src="media/readme-features/search-plan-in-operation.png">

Each item is created as a card with a title and relevant information.  At the top of this section is a Create New button which gives the user Create functionality.  Attached to the bottom of the card items are View, Edit and Delete buttons displayed variably according the item and to the level of permission which the current user has been granted by Admin.

<img src="media/readme-features/search-products-template.png">

## Create Form
  Example given is for product, but the same functionality is available for all the essential database objects.  Only users with permission can use this functionality.

  <br>
  <img src="media/readme-features/create-product-form.png">

### Form Field Data Validation
  <br>
  <img src="media/readme-features/form-validation-2.png">
  <br>
  <img src="media/readme-features/form-validation-3.png">

### On Success Message
  <img src="media/readme-features/product-created-message.png">

### Newly Created Object
  <img src="media/readme-features/newly-created-product.png">

## Update Form

<br>
<img src="media/readme-features/update-product-form.png">
<br>
<img src="media/readme-features/product-updated-message.png">

## Delete Form
<img src="media/readme-features/delete-product.png">

## Detail Pages
<img src="media/readme-features/live-plan-full.png">

The Detail Page displays what runs are assigned to a particular plan.  It contains four reports tailored to certain managers and their specific tasks.  The Live Plan can be accessed via the Live Plan navlink.  A detail view can be accessed for any plan from the plan search page by clicking 'view'.

### Add Run to Plan
  A plan is made up of a collection of runs assigned to it, all the information contained within the detail pages are made up from the runs assigned and the information contained within each run, which in turn is linked to products, teams, packaging.
  To add a run, click the button in the header.

  <img src="media/readme-features/add-run-to-plan.png">


### Update and Delete
  same templates as outlined above.

### Notes
  There is also a button in the header to trigger the notes modal which will be detailed below in the Modals section.
### Accrodion Format
  Each table can be expanded/minimised to see the relevant info quickly and hide irrelevant data according to the users preference.
  <br>
  <img src="media/readme-features/live-plan-collapsed.png">


### Plan Summary Table
  Shows summary information.  If completed the row turns green.  Displays Edit and Delete buttons for users with permission to perform these changes.

  <br>
  <img src="media/readme-features/live-plan-summary.png">

### Plan Calculations Table
  Information useful to the Operations Manager when conducting meetings with Production Managers and making plans etc.

  <br>
  <img src="media/readme-features/detail-plan-calcs.png">

### Team Times Table
  Information particularly useful to the Packing Manager when scheduling in teams for the week.  Minutes are used in this particular bakery.

  <br>
  <img src="media/readme-features/detail-team-times.png">

### Packaging Required Table(s)
  This information is for the Raw Materials Manager and Stores to check and make sure that packaging is in stock and available when needed for the packing teams.

  <br>
  <img src="media/readme-features/detail-packaging-req.png">


## Modals

  <br>
  <img src="media/readme-features/help-modal.png">

### Help Modal
  On clicking 'HELP' in the navbar the user opens a modal which gives help depending on the level of permission granted to the user.  If the user doesn't have creation permission they won't get advice on how to create for instance.


  <br>
  <img src="media/readme-features/notes-modal.png">

### Notes Modal
  Within the detail and live-plan templates the user can click on the notes button in the header and view a modal with all notes ascribed to a packing run displayed in descending order by day and with product info etc.


## User Accounts
 <img src="media/readme-features/opsmanager.png">

 The Username is displayed in the dropdown button on the right of the navigation bar.

### SignUp
  <img src="media/readme-features/signup.png">

### SignIn
  <img src="media/readme-features/not-correct.png">
  <img src="media/readme-features/signin.png">
  <img src="media/readme-features/success-singin.png">
  
### Change Password
  <img src="media/readme-features/change-password.png">

### SignOut
  <img src="media/readme-features/nav-right.png">
  <img src="media/readme-features/sure.png">
  <img src="media/readme-features/signed-out.png">

## Messages
As seen above there are success messages generated for all actions that affect a database object.
There are also info messages on the forms giving useful hints to the user.

On the Search Plan page there is a grey expandable and dismissable alert box for some very important information.

<img src="media/readme-features/current-status-alert.png">

# Technologies Used
 - [Django version 3.2.16](https://docs.djangoproject.com/en/3.2/)
 - See [requirements.txt](requirements.txt) for a full list of Django Requirements.
 - Python 3.8.11
 - HTML5
 - CSS3
 - [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
 - [Cloudinary Image Storage](https://cloudinary.com)
 - [ElephantSQL](https://www.elephantsql.com) Postgresql database service.
 - [Git](https://git-scm.com)
 - [GitHub](https://github.com)
 - Deployed on [Heroku](https://devcenter.heroku.com)
 
# Testing
## Python Validation
[CI Python Linter](https://pep8ci.herokuapp.com/) used to check Python files.

### HTML Validation
[Nu HTML Checker - PASSED](media/readme-test/Showing%20results%20for%20https%3Apacking-calc.herokuapp.com%20-%20Nu%20Html%20Checker.pdf)  - I disabled the login requirement so that the site could be checked by Address.

### CSS Validation
[Jigsaw CCS Validation Service Result](media/readme-test/jigsaw-css-validation-result.pdf) - There are lots of errors associated with the Bootsrap CDN, which I am not considering, my custom css is in the valid code block if you scroll to the bottom of the results.

<img src="media/readme-test/jigsaw-my-css-valid.png">

### JavaScript Validation
I did not use any custom JavaScript so no testing necessary.

## Functionality Tests
[Tests Excel Sheet](media/readme-test/Packing_calc_testing.xlsx) - Source of the tables below.

<img src="media/readme-test/navbar-tests.png">
<img src="media/readme-test/search-page-tests.png">
<img src="media/readme-test/live-detail-test.png">
<img src="media/readme-test/detail-view-tests.png">
<img src="media/readme-test/crud-form-tests.png">
<img src="media/readme-test/plan-run-crud-form-tests.png">
<img src="media/readme-test/account-page-tests.png">
<img src="media/readme-test/user-accounts-tests.png">
<img src="media/readme-test/footer-link-test.png">

## Error Handling

Test that 404 not found, 403 forbidden and 500 server error custom templates are displayed on these errors being triggered.  - PASSED.

## Issues

 - The 'Live Plan' page relies on one and only one plan being set status 'Current'.  If not there will be a 500 server error.  As plans can only be edited by Admin and OpsManager who will be well informed this should not be a huge issue until a fix can be implemented.

 - On opening an update form, if the user clicks update without making any changes the success message still displays.

 - Success messages need to be manually dismissed.

 - The notes modal displays blank notes.

 - The packaging displays 0 Rolls for less than 1 required.

 - On the search pages, when search is executed the term disappears from the bar.

## Planned Improvements

- Logic so that only one plan can be set to current, when a new one is set the old automatically changes to complete.

- Print reports functionality.

- Message Admin with any issues.

- A general team messaging thread.

- Improved filter options in the plan detail views.

- A detailed search option in each search page, not just a title term as is now the case.

- Ability to upload sheets of products in bulk.


## Web Browser Compatibility
Working fine on the three browsers below.
- Google Chrome Version 108.0.5359.98 (Official Build) (arm64)
- Safari Version 16.1 (18614.2.9.1.12)
- Microsoft Edge Version 108.0.1462.46 (Official build) (arm64)

## Adaptability
The app is designed to be used primarily on medium size screens such as a desktop/laptop/tablet in a production environment.  However it is generally good on all screen sizes as shown in Google Chrome Dev Tools.  The use of Bootstrap throughout brings good responsiveness overall.  
One issue - on very small screens the detail page tables overflow a little but there is a lot of information to be crammed in and it is still readable if not very pretty.

# Deployment
This site is deployed using Heroku combined with a Github repository updated from the IDE using Git.  Once you have an Heroku account and have linked that with your Github account you can create a 'new' project by clicking that button in the top right corner, in the current version.  Enter the name and regional information and in the next page click the 'Connect to Github' option and select the appropriate repository from your Github (or link the accounts and then do so, if not yet linked).

Enter the appropriate configuration variables in the settings tab of Heroku.  If you do not know what to do here then find help for your specific case.  Once the appropriate settings in Heroku match those in your repository you can navigate to the 'Deploy' tab of the Heroku dashboard.  

Heroku can automatically deploy the selected Git branch of your respository when it is updated, or you can choose to manually update after each change, the choice is yours.  Select your branch and click 'Deploy Branch'.  Wait for the deployment to execute and then click 'View' to open your new app.

# Credits
I consumed a large amount of video/course material for inspiration, but the specific ideas and code implemented in this project are my own.
Many thanks to my mentor Brian Macharia for pointing me in the right direction with resources and advice.
Many thanks to Code Institute for providing the learning materials.
