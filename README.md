# GoodToEat - Handcrafted Irish Ghee Website

An interactive website for GoodToEat company showcasing premium handcrafted Irish ghee.

## Features

- **Home Page**: Hero section with company overview, key features, and product highlights
- **Products Page**: Three product sizes (200g, 500ml, 1KG) with detailed information and ordering functionality
- **The Founder Page**: Personal story and background of the founder
- **The Brand Page**: Mission, values, and brand identity
- **About Ghee Page**: Comprehensive information about ghee, health benefits, and culinary uses
- **Ghee Moments Page**: Customer testimonials and recipe ideas
- **Ghee Blogs Page**: Blog posts and articles about ghee
- **Contacts Page**: Contact information and interactive contact form
- **FAQs Page**: Frequently asked questions with expandable answers

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the Streamlit app locally:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Deployment

### Deploy to Streamlit Cloud

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository and branch
6. Set the main file path to `app.py`
7. Click "Deploy"

### Alternative Deployment Options

- **Heroku**: Use the Procfile and requirements.txt
- **AWS/Azure/GCP**: Deploy as a containerized application
- **Docker**: Create a Dockerfile for container deployment

## Project Structure

```
GoodToEat/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── Images/            # Product and content images
│   ├── 200G_Mockup.png
│   ├── 500ml_V4.png
│   ├── 1KG_V3_Mockup_2.png
│   └── ... (other images)
└── .streamlit/        # Streamlit configuration
    └── config.toml
```

## Technologies Used

- **Streamlit**: Web framework for creating interactive web applications
- **Python**: Programming language

## Product Information

Our premium Irish ghee is:
- Handcrafted in Ireland
- Made from 100% Irish dairy products
- Produced in small batches for freshness
- Free from additives and preservatives

## Contact

For inquiries, please use the Contact Us page in the application or email: info@goodtoeat.ie

