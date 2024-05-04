DC = "default"

images = {  #fill in your images here
}
"""
Ex:
    "purchase_search_x": DC,
    "receipt_detail_page": DC,
    "receipt_details_link": 0.8,    
    "search_your_purchases": DC,
"""

def getConfidence(image):
    try:
        return images[image]
    
    except KeyError:
        return DC
    