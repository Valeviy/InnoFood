# Class diagram
## Introduction
Class diagram showed here is a continuation of activity diagrams that you can see here [Activity diagrams](https://github.com/maloescher/InnoFood/blob/master/Requirements/Activity%20Diagrams.md)

## Tracing changes
To make the diagram changes traceable we are adding csv file, that represents the diagram’s relationships.

[Traceable](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Class%20diagram.csv)

## Diagram

![Diagram](https://github.com/VASemenov/InnoFood/blob/master/Requirements/Iteration%202%20diagrams/Class%20diagram.png?raw=true)

## Description
### Setters and getters
Setters and getters aren’t specified for every parameter, because it’s not necessary. Consider that every private parameter is accessed trough them. 

Nevertheless, we specified some of them in cases where setter and getter have different security modifiers. For example, protected setter and public getter.

### Soft deletion
All of the classes, except OrderDetail have a boolean parameter called **visible**. If visible=True, then instance is soft-deleted. It’s done to prevent accidental data loss and not to deal with cascading deletion, as it will complicate the work.

### User class
It’s a super class for all kinds of users. There are parameters and methods for logging in, logging out, changing parameters of the account.

### Customer class
Inherits User class. The only type of user that can register in the system. User can create order.

### Manager class
Inherits User class. Manager is only created directly by the Admin. Manager is assigned to one instance of Cafe. Manager can be deleted by the Admin.

### Admin class
Inherits User class. Admin can create Manager and create Cafe. Admin is created with system and can not be deleted.

### Order class
Order is created by Customer. Order has a destination as a string (in other words address), status of confirmation by the Manager, and details about an ordered dishes (link to the table OrderDetail).

Customer can delete order or create Complaint about it. Manager can decline order, or confirm it. 

### OrderDetail class
To have the table of an instances of the Dish classes we needed to create this class. It has dishes parameter as the column in the table that will store instances.

Class has a method that returns a column dishes as list of all of the entries in this column.

### Cafe class
Cafe is created by Admin. It has a name, location and Manager assigned to it.

With creation of Cafe, Menu class is created automatically.

### Menu class
Menu is a table of all of the instances of Dish in the system. Menu can not exist without Cafe (composition). Hence, it has parameter cafe with the link to the parent instance of Cafe. Also, there is a method for creating new Dish instances.

### Dish class
Dish class represents Menu entry. It has name and price parameters. Dish can be edited.

### Complaint class
Complaint represents a feedback message about Order, created by Customer. It can be resolved by Manager.

Complaint has links to responsible Manager, Order, status (is resolved?) and description of a problem.








