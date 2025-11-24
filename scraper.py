import requests
from bs4 import BeautifulSoup
# Step 1: Define the target URL
URL = "https://store.botlfarm.com"
# Step 2: Fetch the HTML content
response = requests.get(URL)
if response.status_code == 200:
   soup = BeautifulSoup(response.content, "html.parser")
   
   print("Page Title:", soup.title.string if soup.title else "No title found")
   print("\n" + "="*50)
   
   # Look for product links in the left navigation
   product_links = soup.find(id="left-product-links")
   
   if product_links:
       print("Found product categories:")
       links = product_links.find_all("a")
       for link in links:
           print(f"  - {link.text.strip()}: {link.get('href', 'No link')}")
   
   # Look for products in the main content area
   editable_page = soup.find(id="editable-page")
   
   if editable_page:
       print("\n" + "="*50)
       print("Main content area found. Looking for products...")
       print("="*50)
       
       # Try to find product elements (common patterns)
       products = editable_page.find_all("div", class_=lambda x: x and "product" in x.lower())
       
       if not products:
           # Try finding links with product info
           products = editable_page.find_all("a", href=True)
       
       print(f"\nFound {len(products)} potential product elements")
       
       # Show first few products
       for i, product in enumerate(products[:5]):
           print(f"\nProduct {i+1}:")
           print(f"  Text: {product.text.strip()[:100]}")
           if product.get('href'):
               print(f"  Link: {product.get('href')}")
   else:
       print("\nNo main content area found")
else:
   print(f"Failed to fetch data. Status code: {response.status_code}")