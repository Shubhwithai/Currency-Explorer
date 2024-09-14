# Currency Explorer

Currency Explorer is a Streamlit-based web application that allows users to upload an image of a currency note or coin and get a detailed description, including the country of use, name, denomination, and historical facts. The app uses Google's Generative AI (Gemini model) for content generation based on image input.

## Features

- **Upload Currency Image**: Upload a currency note or coin image in JPG, PNG, or JPEG format.
- **Get Description**: Get detailed information about the uploaded currency such as the country, name, and denomination.
- **Get Historical Information**: Learn about the historical background of the currency, including notable events or milestones associated with it.
- **Image Preview**: See a preview of the uploaded image.
- **Error Handling**: If the uploaded image doesn't show a valid currency, the app provides clear feedback.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/currency-explorer.git
    cd currency-explorer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

4. Upload an image of a currency note or coin in the supported formats (JPG, PNG, JPEG).

5. Click "Get Currency Description" to get a detailed description of the currency, or "Get Historical Information" for a brief history.

## Requirements

- Python 3.x
- Streamlit
- PIL (Pillow)
- google-generativeai

## API Key Setup

1. Add your Google Generative AI API key to a `.streamlit/secrets.toml` file:
    ```toml
    [secrets]
    api_key = "your-google-generative-ai-api-key"
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
