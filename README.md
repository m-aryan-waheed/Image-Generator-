# AI Image Generator

AI Image Generator is a full-stack web application built using Flask, HTML, CSS, and JavaScript that allows users to generate AI-powered images from text prompts in real time. The project integrates with the Pollinations AI image generation API and provides a clean, responsive interface for creating and downloading generated artwork instantly.

The application was designed to provide a simple but visually modern experience where users can enter prompts, customize image dimensions, optionally use seeds for reproducible outputs, and generate high-quality AI images directly in the browser.

The backend handles API communication, image validation, retry logic, and dynamic URL generation, while the frontend focuses on responsive design, image rendering, loading states, and download functionality.

---

# Features

* AI image generation using text prompts
* Flask-powered backend
* Real-time image rendering
* Responsive modern UI
* Download generated images
* Optional seed support
* Dynamic image size customization
* Automatic retry and validation system
* Lightweight frontend without frameworks

---

# Tech Stack

## Backend

* Python
* Flask
* Requests

## Frontend

* HTML5
* CSS3
* JavaScript

## APIs Used

* Pollinations AI Image API

---

# Project Structure

```bash id="epnnjm"
AI-Image-Generator/
│
├── app.py
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── README.md
```

---

# Installation

To run the project locally, first clone the repository and navigate into the project directory.

```bash id="bov0hn"
git clone https://github.com/yourusername/ai-image-generator.git
cd ai-image-generator
```

Create and activate a virtual environment.

### Windows

```bash id="xhys8n"
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash id="10mjlwm"
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies.

```bash id="y6ibav"
pip install flask requests
```

You can also install dependencies using a requirements file.

```txt id="w0bqf7"
flask
requests
```

```bash id="q8c1ys"
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask development server using:

```bash id="38a3fx"
python app.py
```

The application will run locally at:

```txt id="gnv4l2"
http://127.0.0.1:5008
```

---

# API Endpoint

The backend exposes an API endpoint for generating images.

```http id="mnp2b6"
GET /api/generate
```

### Query Parameters

| Parameter | Type    | Description                      |
| --------- | ------- | -------------------------------- |
| prompt    | string  | Text prompt for image generation |
| width     | integer | Width of generated image         |
| height    | integer | Height of generated image        |
| seed      | string  | Optional seed value              |
| nologo    | boolean | Removes API logo watermark       |

---

# Example Request

```http id="g0plv0"
GET /api/generate?prompt=cyberpunk+city&width=768&height=768
```

### Example Response

```json id="5e6mja"
{
  "success": true,
  "image_url": "https://image.pollinations.ai/..."
}
```

---

# Frontend Design

The frontend interface was developed using vanilla HTML, CSS, and JavaScript with a focus on simplicity and usability. The UI includes responsive layouts, modern typography, interactive buttons, loading states, image cards, and download functionality.

Generated images are displayed dynamically inside a gallery layout where newly created images appear at the top. Users can instantly download generated images directly from the browser.

---

# Backend Workflow

The Flask backend processes incoming prompts and dynamically generates image URLs using the Pollinations API. Before returning an image to the frontend, the backend validates the generated image by checking the response status and image content.

If an image generation request fails, the application automatically retries multiple times while reducing image dimensions to improve reliability and avoid API failures.

This retry-and-validation approach improves application stability and user experience.

---

# Future Improvements

Potential future enhancements for the project include:

* Multiple AI model support
* User authentication system
* Image history storage
* Dark mode support
* Image upscaling
* Prompt templates
* Docker deployment
* Cloud hosting integration
* Gallery persistence using a database

---

# License

This project is licensed under the MIT License.

---

# Author

Developed by Aryan
