# 3D Terrain Visualization

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Frontend Details](#frontend-details)
9. [Backend Processing](#backend-processing)
10. [Customization](#customization)
11. [Known Issues and Limitations](#known-issues-and-limitations)
12. [Future Enhancements](#future-enhancements)
13. [Contributing](#contributing)
14. [License](#license)

## Introduction

This project is a web-based 3D Terrain Visualization tool that allows users to upload Digital Terrain Model (DTM) files and view them as interactive 3D models in their web browser. It provides a simple and intuitive interface for exploring topographical data in three dimensions.

## Features

- File upload functionality for DTM files (currently supporting .tif and .png formats)
- Server-side processing of DTM data using rasterio
- Normalization of elevation data for consistent visualization
- Interactive 3D rendering of terrain models in the browser
- Adjustable height scale factor for emphasizing terrain features
- Optional texture overlay for enhanced visual detail

## Technologies Used

- Backend:
  - Python 3.x
  - Flask (Web framework)
  - rasterio (Geospatial data processing)
  - NumPy (Numerical operations)

- Frontend:
  - HTML5
  - JavaScript (assumed for 3D visualization, specific library not shown in provided code)
  - CSS (assumed for styling, not shown in provided code)

## Project Structure

```
project_root/
│
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html         # Main page template
│   └── view.html          # 3D visualization template
├── uploads/               # Directory for uploaded DTM files
└── static/                # Assumed directory for static assets (JS, CSS)
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/3d-terrain-visualization.git
   cd 3d-terrain-visualization
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask rasterio numpy werkzeug
   ```

4. Ensure you have the necessary system libraries for rasterio. This may vary depending on your operating system.

## Usage

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the file upload form to select and upload a DTM file (.tif or .png format)

4. Adjust the Height Scale Factor slider to emphasize or de-emphasize terrain features

5. Toggle the "Enable Texture" checkbox to add or remove textural detail (if implemented)

6. Interact with the 3D model using your mouse or touchpad (exact controls depend on the visualization library used)

## API Endpoints

- `GET /`: Renders the main page with the file upload form
- `POST /upload`: Handles file uploads, processes the DTM, and returns JSON data for 3D rendering

## Frontend Details

The frontend consists of two main HTML templates:

1. `index.html`: Contains the file upload form, controls for Height Scale Factor and texture toggle, and a placeholder for the 3D visualization.

2. `view.html`: A template for rendering the 3D terrain model (implementation details not provided in the given code).

## Backend Processing

The backend, implemented in `app.py`, performs the following key functions:

1. File upload handling and security checks
2. DTM processing using rasterio:
   - Reading the elevation data
   - Normalizing the data to a 0-1 range
   - Flattening the data for frontend consumption
3. Returning processed data as JSON for frontend rendering

## Customization

- To add support for additional file formats, extend the `ALLOWED_EXTENSIONS` set in `app.py`
- Adjust the normalization process in the `process_dtm` function to handle different data ranges or apply custom transformations
- Modify the frontend controls in `index.html` to add new visualization options

## Known Issues and Limitations

- Currently only supports .tif and .png file formats
- Large DTM files may cause performance issues or timeout errors
- No error handling for corrupted or incompatible DTM files

## Future Enhancements

- Add support for more DTM file formats
- Implement server-side caching of processed DTM data
- Add color mapping options for elevation visualization
- Incorporate additional data layers (e.g., satellite imagery, vegetation data)
- Implement user accounts and saved visualizations

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

© 2024 3D Terrain Visualization. All rights reserved.
