from woocommerce import API

wcapi = API(
    url="http://localhost:10005",
    consumer_key="ck_0f2f6d6153cad0d5d56cd04b7370ec3fa1992766",
    consumer_secret="cs_f252955cff89d3efdd4f88cdc93acd7a4358a44d",
    version="wc/v3"
)

r = wcapi.get("products")

print(r.json())