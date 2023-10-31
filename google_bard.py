TELEGRAM_TOKEN = "6715995399:AAGdCFwCqbnX_etoQ5p7uc9MVqiLiRqouxY"

import google_bard
 
# Replace "YOUR_API_KEY" with the actual API Key obtained earlier
API_KEY = "AIzaSyD5shEb6xHZR95iJeL-4wWKblqOcxO3q4U"
 
def main():
    query = "What is the meaning of life?"
    response = google_bard.(query, api_key=API_KEY)
    print("Google Bard Response (Using google_bard Module):")
    print(response)
 
if __name__ == "__main__":
    main()