{
    "name": "Comprador en proveedores",
    "summary": "Integración para segmentar compras por comprador",
    "description": """
        Este módulo agrega el campo comprador al modelo de Contactos (res.partner)
        Coninsamatik. Pro medio de una regla de registro, al entrar a compras 
        solamente mostrará solo las compras donde el proveedor tenga defininido 
        como comprador al usuario.
    """,
    "author": "Samuel Mtz",
    "category": "Purchase",
    "version": "0.1",
    "depends": [
        "base",
        "account",
        "purchase",
    ],
    "data": [
        # "security/ir.model.access.csv",
        "security/groups.xml",
        "data/data.xml",
        "views/purchase_views.xml",
        "views/res_partner_views.xml",
        "views/res_users_views.xml",
    ],
    "demo": [],
    "license": "LGPL-3",
}
