## User Story testing

Issue No. | Title | Acceptance criteria | Manual test carried out
----------|-------|---------------------|-------------------------
#01 | Manage content | Site admin can create, edit and delete posts. | Ensure that site admin can have full CRUD functionality and control over the site content.
#02 | Manage comments | Site admin can edit and delete comments. | Ensure that site admin have full control over the comment section under all posts.
#03|  View posts | Site user can view a list of posts and see two categories of posts. | Ensure that site user can see all posts.
#04 | Access posts | Site user can click and access each of the posts published. | Ensure that site user can access the content published.
#05 | Account creation | Site user can register account, then view and leave comments. | Ensure that every site visitor can easily become a registered member with appertaining rights.
#06 | Contact form | Site user can fill the contact form and submit it. | Ensure that any site visitor can easily use the contact form to reach out to the website owner.
#07 | Draft creation | Site admin can change post status within admin area from active to draft and vice versa. | Ensure that site admin can actively use option to draft posts before publishing them.
#08 | Comment on posts | Registered site user can submit, edit and delete comments when logged in. | Ensure that only registered users have full CRUD functionality within the comment area.
#09 | Login possibility | Site user can log in easily which triggers permissions for submitting, editing and deleting comments. | Ensure that site user can log in without any issues.
#10 | Logout possibility | Site user can easily log off. | Ensure smooth experience of logging out safely.
#11 | Search for posts |  Site user can search for a specific keyword within posts. | Ensure that every site visitor and user can user this option.

* Manual testing was performed to ensure that website is fully working without any issues.

Each page has been manually tested to ensure that the links and the contents are properly placed and functioning, and that all data entry is appropriately handled as expected. 
Restricted areas access has also been thoroughly tested.

All buttons and links were manually tested to ensure full functionality across the website.

## Manual testing on each page
  
#### Home page

**Users who are logged in**  

Ensure that users can see their username in the upper right corner of the navbar and that they can click on "logout" no matter where they are within the website.
All the links and buttons have been manually tested across various devices.

#### Post Detail page

**For site visitor who has not logged in**

Ensure that they cannot see, leave, edit or delete comments. 
Ensure that links for easing the access to "log in" and "register" areas are functioning properly below posts.

**For registered and logged in users**

Ensure that users have full CRUD functionality enabled for commenting below posts.

#### Delete/Edit Comment page

**For registered and logged in users**

Ensure that both buttons perform the willing functions, whether to submit the change or just to return to the previous page.

#### Contact page

**For both users and site visitors**

Ensure that both users and visitors can access the page and submit their messages easily.
Ensure that notification informs users that they were successful in submitting a message.

#### Register page

Ensure that validations are in place and that user cannot register the same username twice.

#### Login option

Ensure that upon successful login, the user is redirected to home page where they can see their username in the upper right corner of the screen (navbar).

#### Logout page
Ensure logout message shows up.

[Link Checker](https://validator.w3.org/checklink) was used to ensure that there is no broken link within the website