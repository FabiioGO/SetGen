# SetGen-Python [(https://setgen-app-5i7dqc47ea-nn.a.run.app/)]

## Description
SetGen-Python is a comprehensive full-stack project developed in Python, enabling users to create setlists for shows or showcases while minimizing the number of consecutive performances for dancers. The project leverages an SQL database and a custom REST API built with Flask. Users can sign in to different shows to access their respective setlists.

## How to Use
Using SetGen-Python is simple. Follow these steps:

1. Access the website by clicking the link at the top of the page.
2. If you have an account, click the "Login" button and enter your credentials. Otherwise, click "Create Show" to register a new show.
3. After logging in, you'll be directed to the home page where you can add songs and dancers to your show's setlist.
4. Enter the song title and the dancers' names, ensuring the required fields are filled and the input format is correct.
5. Click "Add Song" to include the song in the setlist or "Generate Setlists" to produce optimized setlists based on the added songs.
6. You can also set beginning and end songs to allow for more customization.
7. The setlists will be displayed, showing the song order and any consecutive performances.
8. You can log out anytime by clicking the "Logout" button in the navigation bar.

## Key Features
- User validation and error messages for input validation failures (e.g., empty song name, insufficient dancers).
- Client-side input validation using JavaScript for real-time feedback on length, format, and other requirements.
- Responsive web design with media queries and flexible layouts for a seamless experience on desktop and mobile devices.
- Refined user interface elements, including typography, color scheme, and overall visual design, to enhance aesthetics and usability.
- Database implementation to store songs, dancers, and setlists, ensuring data persistence even after server restarts.
- User authentication and authorization to provide personalized setlists and secure data access.

## Technologies Used
- Flask: A Python web framework used to build the REST API and handle server-side logic.
- HTML, CSS, JavaScript: Front-end technologies for building the user interface and client-side validation.
- SQL: Database management system for storing and retrieving data.
- Google Cloud Run, Google Cloud SQL, Google Artifact Registry, Docker: Deployment and cloud management tools.

## Demo
To experience SetGen-Python, visit the live demo by clicking here: [https://youtu.be/MpTHXrgis6U]. Explore and generate setlists for different shows!

Thank you for checking out SetGen-Python! We hope you find it helpful in generating optimized setlists for your shows.

## The next step ?

- Add an edit feature to be able to edit songs and dancers within the database.
- Add an export feature that would allow users to export setlists into an Excel file.
