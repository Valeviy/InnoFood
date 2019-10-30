# Activity Diagrams assignment

## **FoodDelivery**

**Project description:** [Link](https://github.com/VASemenov/InnoFood/blob/master/README.md)

Developer: Team 4 
 

Vladimir Solovev
Vladimir Semenov
Marvin Lopez
Valeriia IUrinskaia




## Main Use cases diagram

![MainUC](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/MainUseCases.jpg?raw=true)

## Administrator main activity diagram

![AdminMain](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Administrator%20main%20activity.jpg?raw=true)

## Create cafe

| Use case name          | Create Cafe                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 001                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Secondary actor(s)** | Managers. <br/>Database.                                     |
| **Brief description**  | Administrator creates a new cafe, and sets up all parameters for it, Administrator also assigns manager to that canteen. |
| **Preconditions**      | Newly built, or cafe not entered at the system, manager, earlier created by admin. |
| **Flow of events**     | 1. Administrator enter the administrator panel.<br/>2. Administrator choose the option "Create new cafe". <br/>2. Administrator fill the "new cafe" form. <br/>3. Administrator click on "save data" bottom.<br/>4. A new register is created on the data base. <br/>5. Administrator receive a confirmation message. |
| **Postconditions**     | A New cafe has been added to the database and is visible from the administrator panel.<br/>A managers has been assigned to the Cafe |
| **Alternative Flow **  | Administrator does not receive confirmation message (error message). <br/>Administraror must contact IT department. |

![cafeCreation](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Cafe%20deletion.jpg?raw=true)

## Edit cafe

| Use case name                   | Edit Cafe                                                    |
| ------------------------------- | ------------------------------------------------------------ |
| **Unique use case ID**          | 002                                                          |
| **Primary actor(s)**            | Administrator                                                |
| **Secondary actor(s)**          | Database                                                     |
| **Brief description**           | Administrator wants to update information about a cafe.      |
| **Preconditions**               | The cafe already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**              | 1. Administator choose enter administration panel<br/>2. Administator click on the edit buttom of the cafe to edit <br/>3. Administrator makes the modifications needed<br/>4. Administrator click on "Save changes" buttom.<br/>5. System display a confirmation message.<br/>6. System perform update action in the DB.<br/>7. System display "Sucessfull message". |
| **Alternative Flow **           | 1. Administrator press cancel on the confirmation message.<br/>2. System must display again the form. <br/>1. Administrator does not receive confirmation message (error message). <br/>2. Administraror must contact IT department. |
| **Postconditions**              | The information of the cafe has been updated.                |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |

![EditCafe](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Cafe%20edit.jpg?raw=true)



## Delete cafe

| Use case name          | Delete Cafe                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 003                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Brief description**  | Administrator wants to delete a cafe.                        |
| **Preconditions**      | The cafe already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**     | 1. Administator choose enter administration panel<br/>2. Administator click on the delete buttom of the cafe to delete<br/>3. System display a confirmation message<br/>4. System perform soft delete in the DB.<br/>5. System display "Sucessfull message". |
| **Postconditions**     | The cafe has been soft deleted.                              |
| **Alternative Flow**   | Administrationr does not receive confirmation message (error message). <br/>Administrator must contact IT department. |
| **Assumptions**        | The Administrator is logged in the system and has the needed rights to perform this action. |



![CafeDelete](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Cafe%20deletion.jpg?raw=true)

## Create manager

| Use case name          | Create Manager                                               |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 004                                                          |
| **Primary actor(s)**   | Administrator                                                |
| **Secondary actor(s)** | Managers. <br/>                                              |
| **Brief description**  | Administrator creates a new manager, and sets up all parameters for it. |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Administrator enter the administrator panel.<br/>2. Administrator choose the option "Create new administrator". <br/>2. Administrator fill the "new administrator" form. <br/>3. Administrator click on "save data" bottom.<br/>4. A new register is created on the data base. <br/>5. Administrator receive a confirmation message. |
| **Postconditions**     | A New administrator has been added to the database and is visible from the administrator panel.<br/> |
| **Alternative Flow **  | Administrator does not receive confirmation message (error message). <br/>Administraror must contact IT department. |
| **Assumptions**        | The Administrator is logged in the system and has the needed rights to perform this action. |

![CreateManager](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Manager%20creation.jpg?raw=true)





| Use case name                   | Edit Manager                                                 |
| ------------------------------- | ------------------------------------------------------------ |
| **Unique use case ID**          | 005                                                          |
| **Primary actor(s)**            | Administrator                                                |
| **Secondary actor(s)**          | Manager, Database                                            |
| **Brief description**           | Administrator wants to update information about a Manager.   |
| **Preconditions**               | The Manageralready exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**              | 1. Administator choose enter administration panel<br/>2. Administator click on the edit buttom of the Manager to edit <br/>3. Administrator makes the modifications needed<br/>4. Administrator click on "Save changes" buttom.<br/>5. System display a confirmation message.<br/>6. System perform update action in the DB.<br/>7. System display "Sucessfull message". |
| **Alternative Flow **           | 1. Administrator press cancel on the confirmation message.<br/>2. System must display again the form. <br/>1. Administrator does not receive confirmation message (error message). <br/>2. Administraror must contact IT department. |
| **Postconditions**              | The information of the Manager has been updated.             |
| **Non-behavioral requirements** | Changes must be visible for the administrator without having to refresh the page. |



![EditManager](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/manager%20edit.jpg?raw=true)

## Delete manager

| Use case name           | Delete Manager                                               |
| ----------------------- | ------------------------------------------------------------ |
| **Unique use case ID**  | 006                                                          |
| **Primary actor(s)**    | Administrator                                                |
| **Secondary actors(s)** | Manager, Database                                            |
| **Brief description**   | Administrator wants to delete a Manager.                     |
| **Preconditions**       | The Manager already exist. <br/>The Administrator has the right for making the changes. |
| **Flow of events**      | 1. Administator choose enter administration panel<br/>2. Administator click on the delete buttom of the Manager to delete<br/>3. System display a confirmation message<br/>4. System perform soft delete in the DB.<br/>5. System display "Sucessfull message". |
| **Postconditions**      | The Manager has been soft deleted.                           |
| **Alternative Flow**    | Administrationr does not receive confirmation message (error message). <br/>Administrator must contact IT department. |
| **Assumptions**         | The Administrator is logged in the system and has the needed rights to perform this action. |

 ![DeleteManager](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Manager%20deletion.jpg?raw=true)

## Create order

| Use case name          | Create order                                                 |
| ---------------------- | :----------------------------------------------------------- |
| **Unique use case ID** | 007                                                          |
| **Primary actor(s)**   | User                                                         |
| **Brief description**  | User makes an order through the application                  |
| **Preconditions**      | The meals/dishes to be ordered are available                 |
| **Flow of events**     | 1. User selects the desired option from menu<br />2. User enters his location<br />3. User presses the submit button |
| **Postconditions**     | Order is completed                                           |
|                        |                                                              |
|                        |                                                              |

![Createorder](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Create%20order.png?raw=true)



## Delete order

| Use case name          | Delete order                                                 |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 008                                                          |
| **Primary actor(s)**   | User                                                         |
| **Brief description**  | Canceling order by user                                      |
| **Preconditions**      | Order is created less than 10 minutes ago                    |
| **Flow of events**     | 1. User selects his order<br />2. User presses delete button |
| **Postconditions**     | Order is deleted                                             |

![DelOrderUser](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Delete%20order(user).png?raw=true)



## Confirm Order

| Use case name          | Confirm order                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 009                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager confirms the order created by User                   |
| **Preconditions**      | Order is created by User                                     |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses confirm button |
| **Postconditions**     | Order is confirmed                                           |

![ConfirmOrder](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Confirm%20order.png?raw=true)



## Decline order

| Use case name          | Decline order                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 010                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager declines order                                       |
| **Preconditions**      | Order is created by User                                     |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses decline button |
| **Postconditions**     | Order is declined and deleted                                |

![DeclineOrder](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Decline%20order.png?raw=true)



## Create dish

| Use case name          | Create dish                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 011                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager creates an entry in Menu table                       |
| **Preconditions**      | There is a Cafe entity that Manager is assigned to           |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Add' button<br />3. Pop-up window with the form containing name and price fields appears<br />4. Manager enters dish name<br />5. Manager enters dish price<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | New Dish entry added into Menu table                         |

![CreateDish](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Add%20new%20dish.png?raw=true)



## Edit dish

| Use case name          | Edit dish                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 012                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager edits an entry in Menu table                         |
| **Preconditions**      | There are entries in the Menu table                          |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Edit' button<br />3. Pop-up window with the form containing name and price fields appears filled with the current values<br />4. Manager edits values<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | Dish entry is updated                                        |

![EditDish](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Edit%20dish.png?raw=true)



## Edit menu

| Use case name          | Edit menu                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 013                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | A manager sets available menu for each week                  |
| **Preconditions**      | There are entries in Menu table                              |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manger checks all of the checkboxes next to entries setting their visibility for the user to True/False |
| **Postconditions**     | All of the unavailible meals are hidden from the user, all of the availible are shown |

![EditMenu](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Edit%20menu.png?raw=true)



## Create complaint

| Use case name          | Create complaint                                             |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 014                                                          |
| **Primary actor(s)**   | User                                                         |
| **Brief description**  | If User is not satisfied or unhappy with the order/delivery, he creates |
| **Preconditions**      | Order was confirmed by Manager                               |
| **Flow of events**     | 1. User selects order from his order history<br />2. User presses 'Complain' button<br />3. User enters description of the problem in the form<br />4. User submits the form to the system |
| **Postconditions**     | Complaint is created and stored in the database              |

![CreateComplaint](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Add%20complain.png?raw=true)



## Resolve complaint

| Use case name          | Resolve complaint                                            |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 015                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | When Manager contacted User outside the system, check in the system that the complaint is resolved |
| **Preconditions**      | User created complaint                                       |
| **Flow of events**     | 1. Manager selects resolved complaint from the list<br />2. Manager changes it's state to 'Resolved' |
| **Postconditions**     | Complaint is hidden from both user and manager               |

![ResolveComplaint](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Resolve%20complaint.png?raw=true)
