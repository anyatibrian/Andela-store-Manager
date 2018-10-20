
[![Coverage Status](https://coveralls.io/repos/github/anyatibrian/Andela-store-Manager/badge.svg?branch=Develop)](https://coveralls.io/github/anyatibrian/Andela-store-Manager?branch=Develop)[![Build Status](https://travis-ci.org/anyatibrian/Andela-store-Manager.svg?branch=develop)](https://travis-ci.org/anyatibrian/Andela-store-Manager)
[![Maintainability](https://api.codeclimate.com/v1/badges/7aed395af0c0d5463a76/maintainability)](https://codeclimate.com/github/anyatibrian/Andela-store-Manager/maintainability)

# Store Manager 
is a web application that helps store owners manage sales and product inventory records and 
should only be used in single store

## Requirements
- `Python3.6` - programming language that can be used on any modern computer operating system. 
- `Flask` - Python based web micro framework
- `Virtualenv` - Allows you to work on a specific project without worry of affecting other projects.
- `python-pip` - Package management system used to install and manage software packages,its a replacemnt of easy_install

## Functionality
- `create products` Enables admin user to create create products
- `Get all products` Enables Admin\attendant to view all available product
- `Get single product` Enables Admin\attendant  to get specific order
- `Edit Product` Enables an admin user to edit a particular product
- `Delete Product` Admin  to delete a particular Product
- `Add sales record ` enable an Attendant to create sales records reflecting their Daily sales
- `Get all sales record` enables admin to view all the sales made 


## To view the API on Heroku 
Copy this url paste it in a new tab
```
- https://store-manager-123.herokuapp.com/api/v1/products

```

## Installation
First clone this repository
```
$ https://github.com/anyatibrian/Andela-store-Manager/tree/Develop
$ cd Andela-store-Manager
```
Create virtual environment and install it
```
$ virtualenv venv
$ source/venv/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal
```
pytest
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                      |     Functionality           |
|   -------------------------------------- |-----------------------------|
|     POST api/v1/products                 | creates a new product item  |  
|     GET  api/v1/products                 | get all the product item    |   
|     GET  api/v1/products/product_id      |get a specific product by id |  
|     PUT api/v1/products/product_id       |updates a specific product.  |
|     POST api/v1/sales                    |create sales record          |   
|     GET api/v1/sales                     |Fetch all sales record       |  
|     GET  api/v1/sales/sales_id           |get a particular sales record|



## Contributors
- Anyatibrian
