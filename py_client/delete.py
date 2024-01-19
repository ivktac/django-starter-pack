import requests

product_id = input("What is the product id you want to use?\n")

try:
    product_id = int(product_id)
except ValueError:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    if get_response.status_code == 204:
        print("Product delete successfully.")
        print(get_response.text)
    else:
        print(f"Failed to delete product. Status Code: {get_response.status_code}")
