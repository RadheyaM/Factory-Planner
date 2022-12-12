[View the Live Project](https://packing-calc.herokuapp.com)

# Packing Calculator App - Overview

The app is designed to replace an excel sheet that is currently used in a factory bakery to enter a packing plan for a given week.  This plan is used as a reference by various managers in completing their designated tasks.  For the time being the app can create a plan, and its components, and output certain data in tables for reference.  It is assumed that the users communicate outside the bounds of the site when coordinating changes to a plan or other complicated actions (such as stock level monitoring) until more complete systems are implemented in the app.

# Table of Contents
+ [Agile Planning](#agile-planning)
  - [Target Users](#target-users)
  - [User Stories](#user-stories)
  - [Database Schema](#database-schema)
  - [Initial Wireframes](#initial-wireframes)
  - [Visual Design Choices](#visual-design-choices)
+ [Features](#features)
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

# Agile Planning

## Target Users
A specific set of managers in a bakery, could be adapted to a different production planning setting.
- Admin who has access to the whole backend, only user who can delete a plan.
- Operations Manager who creates, updates and deletes components of a plan.
- Packing Manager who views the Packing Calculator to coordinate the packing teams.
- Raw Materials Manager who views the Packing Calculator required packaging.

## User Stories - Big Picture

As a User I want to be able to:
 - Navigate the site quickly and effectively.
 - Login.
 - View which plan is current, in planning or complete.
 - View Reports on a given week.
 - Search for specific Plans, Products, Runs and Packaging Configurations.
 - View Products, Runs and Packing Configurations.
 - Access instructions on how to use and navigate the site.

As the Operations Manager I want to be able to:

 - Create, retrieve, update and delete all important database objects relating to a plan.
 - Leave notes relating to a particular run.
 - Be the only non-admin user able to make changes to a plan or its components.

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

<img src="static/media/database-schema.png">

## Initial Wireframes

[Wireframes PDF](static/media/initial-wireframes.pdf)

# Features
<img src="static/media/readme-features/detail-top.png">
## Navigation
<br>
<br>
<img src="static/media/readme-features/nav-right.png">
<br>
<img src="static/media/readme-features/nav-login.png">
<br>
At the top of the app is a navigation bar.  The left-hand side contains a link to the Live Plan (as shown above) and the other four links lead to the Plans, Packaging, Products and Runs search pages respectively.  To the right we have an Account Logged in name, which when clicked provides a dropdown with change password and logout functionality.  Next to that is a button that triggers a help modal and finally a previous page button.

## Search Pages
<br>
<img src="static/media/readme-features/search-plan-template.png">

There are four search pages, one for each of the objects that can be created to make up a plan run.  Each search page starts with extra in-page navigation buttons to toggle smoothly between the pages and to indicate which page is active with a red background.  
Below that is a search bar.  On searching a term in the title of the items listed below, the items will be filtered accordingly.  The clear button will reveal all objects once again.

<img src="static/media/readme-features/search-plan-in-operation.png">

Each item is created as a card with a title and relevant information.  At the top of this section is a Create New button which gives the user Create functionality.  Attached to the bottom of the card items are View, Edit and Delete buttons displayed variably according the item and to the level of permission which the current user has been granted by Admin.

<img src="static/media/readme-features/search-products-template.png">

## Create Form
  Example given is for product, but the same functionality is available for all the essential database objects.  Only users with permission can use this functionality.

  <br>
  <img src="static/media/readme-features/create-product-form.png">

### Form Field Data Validation
  <br>
  <img src="static/media/readme-features/form-validation-2.png">
  <br>
  <img src="static/media/readme-features/form-validation-3.png">

### On Success Message
  <img src="static/media/readme-features/product-created-message.png">

### Newly Created Object
  <img src="static/media/readme-features/newly-created-product.png">

## Update Form

<br>
<img src="static/media/readme-features/update-product-form.png">
<br>
<img src="static/media/readme-features/product-updated-message.png">

### Delete
<img src="static/media/readme-features/delete-product.png">

## Detail Pages
<img src="static/media/readme-features/live-plan-full.png">

### Two kinds of Detail Pages
  There are two kinds, the live-plan which is accessable through the nav bar link and which will always display the 'Current' live plan, provided there is one selected.  The content format is the same for both.

### Add Run to Plan
  A plan is made up of a collection of runs assigned to it, all the information contained within the detail pages are made up from the runs assigned and the information contained within each run.
  To add a run, click the button in the header.

  <img src="static/media/readme-features/add-run-to-plan.png">


### Update and Delete
  same templates as outlined above.

### Notes
  There is also a button in the header to trigger the notes modal which will be detailed below in the Modals section.
### Accrodion Format
  Each table can be expanded/minimised to see the relevant info quickly and hide irrelevant data according to the users preference.
  <br>
  <img src="static/media/readme-features/live-plan-collapsed.png">


### Plan Summary Table
  Shows summary information.  If completed the row turns green.  Displays Edit and Delete buttons for users with permission to perform these changes.

  <br>
  <img src="static/media/readme-features/live-plan-summary.png">

### Plan Calculations Table
  Information useful to the Operations Manager when conducting meetings with Production Managers and making plans etc.

  <br>
  <img src="static/media/readme-features/detail-plan-calcs.png">

### Team Times Table
  Information particularly useful to the Packing Manager when scheduling in teams for the week.  Minutes are used in this particular bakery.

  <br>
  <img src="static/media/readme-features/detail-team-times.png">

### Packaging Required Table(s)
  This information is for the Raw Materials Manager and Stores to check and make sure that packaging is in stock and available when needed for the packing teams.

  <br>
  <img src="static/media/readme-features/detail-packaging-req.png">


## Modals

  <br>
  <img src="static/media/readme-features/help-modal.png">

### Help Modal
  On clicking 'HELP' in the navbar the user opens a modal which gives help depending on the level of permission granted to the user.  If the user doesn't have creation permission they won't get advice on how to create for instance.


  <br>
  <img src="static/media/readme-features/notes-modal.png">

### Notes Modal
  Within the detail and live-plan templates the user can click on the notes button in the header and view a modal with all notes ascribed to a packing run displayed in descending order by day and with product info etc.


## User Accounts
 <img src="static/media/readme-features/opsmanager.png">

 The Username is displayed in the dropdown button on the right of the navigation bar.

### SignUp
  <img src="static/media/readme-features/signup.png">

### SignIn
  <img src="static/media/readme-features/not-correct.png">
  <img src="static/media/readme-features/signin.png">
  <img src="static/media/readme-features/success-singin.png">
  
### Change Password
  <img src="static/media/readme-features/change-password.png">

### SignOut
  <img src="static/media/readme-features/nav-right.png">
  <img src="static/media/readme-features/sure.png">
  <img src="static/media/readme-features/signed-out.png">

### 

## Messages

# Technologies Used
# Testing
# Deployment
# Credits
