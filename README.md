# swe-agent-test

## REST API Endpoints

### GET /

Returns a JSON object with a greeting.

**Response:**
{
  "greeting": "Hello, World!"
}

### POST /

Accepts a JSON object with a `name` parameter and returns a greeting addressed to the name provided.

**Request:**
{
  "name": "Jimmie"
}

**Response:**
{
  "greeting": "Hello, Jimmie!"
}

## Running the Application Locally

To run the application, you will need Python and Flask installed on your system. If you have Python installed, you can install Flask using pip:

pip install Flask

Once Flask is installed, you can run the application by executing:

python app.py

The application will start on http://localhost:5000/.
