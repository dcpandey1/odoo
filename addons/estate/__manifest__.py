{
    "name": "Real Estate",
    "summary": "Real Estate Property Management",
    "description": """
Real Estate Property Management
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Others",
    "version": "0.1",
    "depends": ["base"],
    # always loaded/
    "data": [
        "security/ir.model.access.csv",
        "views/real_estate_views.xml",
        # "views/real_estate_type_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        # "demo/demo.xml",
    ],
}
