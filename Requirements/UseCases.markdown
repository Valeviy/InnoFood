# Use cases

**Table of contents**

[TOC]

## Roles

| Role              | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| **Administrator** | Person that is responsible for creating and administrating cafes (assigning managers, changing contact data and info). |
| **Manager**       | Person, that fills in info about canteen(menu, if canteen is open or closed, etc.) and responses to the orders. |
| **Customer**          | Person which orders food.                                    |

## Use cases

### Overall use case diagram

![01](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%20I%20diagrams/01.png?raw=true)

### Create cafe

| Use case name          | Create Cafe                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 001                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Secondary actor(s)** | Managers. <br/>Database.                                     |
| **Brief description**  | Administrator creates a new cafe, and sets up all parameters for it, Administrator also assigns manager to that canteen. |
| **Preconditions**      | Newly built, or cafe not entered at the system, manager, earlier created by admin. |
| **Flow of events**     | 1. Administrator enter the administrator panel.<br/>2. Administrator choose the option "Create new cafe". <br/>2. Administrator fill the "new cafe" form. <br/>3. Administrator click on "save data" bottom.<br/>4. A new register is created on the data base. <br/>5. Administrator receive a confirmation message. |
| **Postconditions**     | A New cafe has been added to the database and is visible from the administrator panel.<br/>A managers has been assigned to the Cafe |
| **Alternative Flow **  | Administrator does not receive confirmation message (error message). <br/>Administrator must contact IT department. |
| **Assumptions**        | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Edit cafe

| Use case name                   | Edit Cafe                                                    |
| ------------------------------- | ------------------------------------------------------------ |
| **Unique use case ID**          | 002                                                          |
| **Primary actor(s)**            | Administrator                                                |
| **Secondary actor(s)**          | Database                                                     |
| **Brief description**           | Administrator wants to update information about a cafe.      |
| **Preconditions**               | The cafe already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**              | 1. Administrator choose enter administration panel<br/>2. Administrator click on the edit button of the cafe to edit <br/>3. Administrator makes the modifications needed<br/>4. Administrator click on "Save changes" button.<br/>5. System display a confirmation message.<br/>6. System perform update action in the DB.<br/>7. System display "Successful message". |
| **Postconditions**              | The information of the cafe has been updated.                |
| **Alternative Flow **           | 1. Administrator press cancel on the confirmation message.<br/>2. System must display again the form. <br/>1. Administrator does not receive confirmation message (error message). <br/>2. Administraror must contact IT department. |
| **Assumptions**        		  | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Delete cafe

| Use case name          | Delete Cafe                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 003                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Brief description**  | Administrator wants to delete a cafe.                        |
| **Preconditions**      | The cafe already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**     | 1. Administrator choose enter administration panel<br/>2. Administrator click on the delete button of the cafe to delete<br/>3. System display a confirmation message<br/>4. System perform soft delete in the DB.<br/>5. System display "Successful message". |
| **Postconditions**     | The cafe has been soft deleted.                              |
| **Alternative Flow**   | Administrator does not receive confirmation message (error message). <br/>Administrator must contact IT department. |
| **Assumptions**        | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Create manager

| Use case name          | Create Manager                                               |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 004                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Secondary actor(s)** | Managers. <br/>                                              |
| **Brief description**  | Administrator creates a new manager, and sets up all parameters for it. |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Administrator enter the administrator panel.<br/>2. Administrator choose the option "Create new administrator". <br/>2. Administrator fill the "new administrator" form. <br/>3. Administrator click on "save data" bottom.<br/>4. A new register is created on the data base. <br/>5. Administrator receive a confirmation message. |
| **Alternative Flow **  | Administrator does not receive confirmation message (error message). <br/>Administraror must contact IT department. |
| **Postconditions**     | A New administrator has been added to the database and is visible from the administrator panel.<br/> |
| **Assumptions**        | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Edit manager

| Use case name                   | Edit Manager                                                 |
| ------------------------------- | ------------------------------------------------------------ |
| **Unique use case ID**          | 005                                                          |
| **Primary actor(s)**            | Administrator                                                |
| **Secondary actor(s)**          | Manager, Database                                            |
| **Brief description**           | Administrator wants to update information about a Manager.   |
| **Preconditions**               | The Manager already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**              | 1. Administrator choose enter administration panel<br/>2. Administrator click on the edit button of the Manager to edit <br/>3. Administrator makes the modifications needed<br/>4. Administrator click on "Save changes" button.<br/>5. System display a confirmation message.<br/>6. System perform update action in the DB.<br/>7. System display "Successful message". |
| **Alternative Flow **           | 1. Administrator press cancel on the confirmation message.<br/>2. System must display again the form. <br/>1. Administrator does not receive confirmation message (error message). <br/>2. Administrator must contact IT department. |
| **Postconditions**              | The information of the Manager has been updated.             |
| **Assumptions**                 | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Delete manager


| Use case name           | Delete Manager                                               |
| ----------------------- | ------------------------------------------------------------ |
| **Unique use case ID**  | 006                                                          |
| **Primary actor(s)**    | Administrator                                                |
| **Secondary actors(s)** | Manager, Database                                            |
| **Brief description**   | Administrator wants to delete a Manager.                     |
| **Preconditions**       | The Manager already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**      | 1. Administrator choose enter administration panel<br/>2. Administrator click on the delete buttom of the Manager to delete<br/>3. System display a confirmation message<br/>4. System perform soft delete in the DB.<br/>5. System display "Sucessfull message". |
| **Alternative Flow**    | Administration does not receive confirmation message (error message). <br/>Administrator must contact IT department. |
| **Postconditions**      | The Manager has been soft deleted.                           |
| **Assumptions**         | The Administrator is logged in the system and has the needed rights to perform this action. |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

### Create order

| Use case name          | Create order                                                 |
| ---------------------- | :----------------------------------------------------------- |
| **Unique use case ID** | 007                                                          |
| **Primary actor(s)**   | Customer                                                         |
| **Brief description**  | Customer makes an order through the application                  |
| **Preconditions**      | The meals/dishes to be ordered are available                 |
| **Flow of events**     | 1. Customer selects the desired option from menu<br />2. Customer enters his location<br />3. Customer presses the submit button |
| **Postconditions**     | Order is completed                                           |


### Delete order

| Use case name          | Delete order                                                 |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 008                                                          |
| **Primary actor(s)**   | Customer                                                         |
| **Brief description**  | Canceling order by Customer                                      |
| **Preconditions**      | Order is created less than 10 minutes ago                    |
| **Flow of events**     | 1. Customer selects his order<br />2. Customer presses delete button |
| **Postconditions**     | Order is deleted                                             |

### Confirm order

| Use case name          | Confirm order                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 009                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager confirms the order created by Customer                   |
| **Preconditions**      | Order is created by Customer                                     |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses confirm button |
| **Postconditions**     | Order is confirmed                                           |

### Decline order

| Use case name          | Decline order                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 010                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager declines order                                       |
| **Preconditions**      | Order is created by Customer                                     |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses decline button |
| **Postconditions**     | Order is declined and deleted                                |

### Create dish

| Use case name          | Create dish                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 011                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager creates an entry in Menu table                       |
| **Preconditions**      | There is a Cafe entity that Manager is assigned to           |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Add' button<br />3. Pop-up window with the form containing name and price fields appears<br />4. Manager enters dish name<br />5. Manager enters dish price<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | New Dish entry added into Menu table                         |

### Edit dish

| Use case name          | Edit dish                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 012                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager edits an entry in Menu table                         |
| **Preconditions**      | There are entries in the Menu table                          |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Edit' button<br />3. Pop-up window with the form containing name and price fields appears filled with the current values<br />4. Manager edits values<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | Dish entry is updated                                        |

### Edit menu

| Use case name          | Edit menu                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 013                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | A manager sets available menu for each week                  |
| **Preconditions**      | There are entries in Menu table                              |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manger checks all of the check boxes next to entries setting their visibility for the Customer to True/False |
| **Postconditions**     | All of the unavailable meals are hidden from the Customer, all of the available are shown |

### Create complaint

| Use case name          | Create complaint                                             |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 014                                                          |
| **Primary actor(s)**   | Customer                                                         |
| **Brief description**  | If Customer is not satisfied or unhappy with the order/delivery, he creates |
| **Preconditions**      | Order was confirmed by Manager                               |
| **Flow of events**     | 1. Customer selects order from his order history<br />2. Customer presses 'Complain' button<br />3. Customer enters description of the problem in the form<br />4. Customer submits the form to the system |
| **Postconditions**     | Complaint is created and stored in the database              |

### Resolve complaint

| Use case name          | Resolve complaint                                            |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 015                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | When Manager contacted Customer outside the system, check in the system that the complaint is resolved |
| **Preconditions**      | Customer created complaint                                       |
| **Flow of events**     | 1. Manager selects resolved complaint from the list<br />2. Manager changes it's state to 'Resolved' |
| **Postconditions**     | Complaint is hidden from both Customer and manager               |

### Sign Up

| Use case name          | Sign Up                                                      |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 016                                                          |
| **Primary actor(s)**   | Customer                                                     |
| **Brief description**  | Process where a customer create a new account to use the system. |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Customer is located in the home page. <br/> 2. Customer clic on "sing up" option <br/> 3. Customer fill the form with all the information required. <br/> 4. Customer click on submit buttom. <br/> 5. Customer reciebe a confirmation message. |
| **Alternative Flow **  | Customer does not receive confirmation message (error message). <br/> System display "Try again later" screen. |
| **Postconditions**     | A New Customer has been added to the database and is able to create new orders.<br/> |
| **Assumptions**        | The customer has a valid email acount. |
| **Non-behavioral requirements** | Changes must be visible for the customer without having to refresh the page. |

### Sign In

| Use case name          | Sign In                                                      |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 017                                                          |
| **Primary actor(s)**   | Customer, Administrators, Managers                           |
| **Brief description**  | Sing in page to enter the system. Screen must be display acoording to user rights |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Actor is located in the home page. <br/> 2. Actor clic on "Sing in" option <br/> 3. Actor fill the user and password field <br/> 4. Actor click on "Sing in" butron <br/> <br/> 5. System validate actor credentials <br/> 6. System redirect actor to the home page depending on the actors rights on the system. |
| **Alternative Flow **  | Invalid credentials. <br/> Error message must be displayed. <br/> Actor has the option to reset the password. |
| **Postconditions**     | The actor access to the system |
| **Assumptions**        | - |
| **Non-behavioral requirements** | Changes must be visible for the actors without having to refresh the page. |

