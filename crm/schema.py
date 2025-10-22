import graphene

class CRMQuery(graphene.ObjectType):
    hello_crm = graphene.String(default_value="Hello from CRM!")

    # You can add more fields here, e.g., customers, orders, etc.
