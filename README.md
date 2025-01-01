# Image Detection

This project implements an image detection system using Python, focusing on detecting objects within images through a web interface.

## Features

- **Object Detection**: Identifies and labels objects within images.
- **Web Interface**: Provides a user-friendly front-end for uploading images and viewing results.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Soking511/image_detection.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd image_detection
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the API server**:

   ```bash
   python api.py
   ```

   This will launch the backend server that handles image processing.

2. **Run the front-end application**:

   Navigate to the `front-end` directory and follow the instructions in its README to start the web interface.

3. **Access the application**:

   Open your web browser and go to `http://localhost:5000` to use the image detection interface.

## Project Structure

```plaintext
image_detection/
├── front-end/           # Contains the web interface files
├── api.py               # Backend API server
├── code.py              # Core image detection logic
├── detection.py         # Helper functions for detection
├── paths.py             # Configuration for file paths
├── requirements.txt     # List of dependencies
└── .gitignore           # Git ignore file
```

## Dependencies

- Python 3.x
- Flask
- OpenCV
- NumPy

All required Python packages are listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
