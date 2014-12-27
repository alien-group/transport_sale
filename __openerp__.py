{
    "name": "Transport sale",
    "version": "1.0",
    "depends": ["base","fleet","sale","hr"],
    "author": "Alien Group Lda",
    'website':'http://www.alien-group.com',
    "category": "Sales Management",
    "description": """
    This module provide :
    Vehicles that executed a transport sales order in the sale order
    All sales by each vehicle in Vehicles form
    All sales by each vehicle driver in employee form
    """,
    'data':['transport_sale.xml','security/ir.model.access.csv'],
    'installable': True,

}
