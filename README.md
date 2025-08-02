# 🛍️ Django Online Shop with Payment Gateway (Zarinpal)

This is a simple **Django-based online store** project that supports product listing, cart functionality, and payment integration via **Zarinpal**. The current version is built for **testing purposes**. To use it in a production environment, users must replace the test merchant code with their own.

## 💡 Key Features

- 🧾 Add, view, and manage products  
- 🛒 Shopping cart functionality  
- 💳 Integrated with **Zarinpal payment gateway**  
- ✅ Includes sample test transactions  
- 📦 Focused on **backend logic** rather than frontend design  

## 🛠 Technologies Used

- Python & Django (backend)  
- HTML, CSS, JavaScript  
- Bootstrap (for basic styling)  

## ⚠️ Important Note

This project currently uses **Zarinpal’s test merchant code**.  
If you plan to deploy this project or use it in production, you **must**:

1. Register at [Zarinpal](https://www.zarinpal.com/)  
2. Replace the test merchant code in the codebase with your **own merchant code**  

```python
# Example (in settings.py or wherever it's used)
MERCHANT = 'your-merchant-code-here'
