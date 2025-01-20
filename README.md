# Personal Gallery with Image Captioning

This project allows users to create a personal image gallery where images can be uploaded and automatically captioned using Hugging Face's `Salesforce/blip-image-captioning-base` model.

## Installation and Running the Application

Follow these steps to install and run the application:

1. Clone the repository from GitHub

   ```bash
   git clone https://github.com/xNatthapol/image-gallery-captioning.git
   ```

2. Navigate to the project directory

   ```bash
   cd image-gallery-captioning
   ```

3. Create a Virtual Environment

   ```bash
   python -m venv venv
   ```

4. Activate the Virtual Environment

- On MacOS or Linux
  ```bash
  source venv/bin/activate
  ```
- On Windows
  ```cmd
  venv\Scripts\activate
  ```

5. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

6. Create `.env` file and copy the content from `sample.env`

- On MacOS or Linux
  ```bash
  cp sample.env .env
  ```
- On Windows
  ```cmd
  copy sample.env .env
  ```

7. Run the application

   ```bash
   python app.py
   ```

   Once the app is running, go to http://127.0.0.1:5000/ to view the gallery and captions.
