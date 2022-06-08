# Logistics Company Inventory Management App #
Fall 2022 - Shopify Developer Intern Challenge Submission. An inventory tracking application for a logistics company. A web application that meets the requirements listed below, along with one additional feature, with the options also listed below.

## Contents ##
- [Requirements](#requirements)
- [Structure](#structure)
- [Features](#features)
    - [Current Features](#current-features)
    - [Potential Future Features](#future-features)
- [Technologies](#technologies)

<a name="requirements"></a>
## Requirements ##
- Basic CRUD Functionality. You should be able to:
    - Create inventory items
    - Edit Them
    - Delete Them
    - View a list of them

- ONLY ONE OF THE FOLLOWING _(We will only evaluate the first feature chosen, so please only choose one)_
    - When deleting, allow deletion comments and undeletion
    - Ability to create warehouses/locations and assign inventory to specific locations
    - Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately

- Authentication and CSS/Design are not required and will not be considered during evaluation.

**Chosen Additional feature:** Ability to create warehouses/locations and assign inventory to specific locations

<a name="structure"></a>
## Structure ##

Database Diagrams

![Diagram showing database structure](docs/db-diagrams.png)

****

|   | Product Model  |   |
|---|---|---|
| id  | IntegerField  | OnetoMany(Inventory) |
| SKU  | IntegerField  |   |
| name | CharField  |  |
| weight  | DecimalField  |   |
| value  | DecimalField  |   |
| notes  | textField  |   |

**Product Model:** Stores info on each product type

****

|   | Inventory Model  |   |
|---|---|---|
| id  | IntegerField  |  |
| product  | ForeignKey  | ManytoOne(Products) |
| quantity | IntegerField  |  |
| location  | ForeignKey  | ManytoOne(Locations)  |

**Inventory Model:** Links Products to locations, stores amount of each product at a given location allowing for each product stock to be split between locations

****

|   | Location Model  |   |
|---|---|---|
| id  | IntegerField  | OnetoMany(Inventory) |
| name  | CharField  |  |
| address | CharField  |  |

**Location Model:** Stores name and address of each location.

<a name="features"></a>
## Features ##

<a name="current-features"></a>
### Current Features ###

<a name="potential-features"></a>
### Potential Future Features ###

<a name="technologies"></a>
## Technologies ##
