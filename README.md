# SetGen-Python [https://setgen.onrender.com/]

## Description
SetGen-Python is a fully functional full-stack project written in Python that allows users to generate setlists for a given show or showcase in order to minimize the number of dancers that have consecutive performances. It utilizes an SQL database and a custom REST API built with Flask. Users can log in to different shows to access their corresponding setlists.

## How to Use
Using SetGen-Python is straightforward. Follow the steps below:

1. Access the website by clicking the link at the top of the page.
2. If you already have an account, click the "Login" button and enter your credentials. Otherwise, click "Create Show" to register a new show.
3. Once logged in, you will be directed to the home page where you can add songs and dancers to your show's setlist.
4. Enter the song title and the dancers' names, ensuring the required fields are not empty and the input format is correct.
5. Click "Add Song" to add the song to the setlist or "Generate Setlists" to generate optimized setlists based on the added songs.
6. The setlists will be displayed, showing the order of songs and any consecutive performances.
7. You can log out at any time by clicking the "Logout" button in the navigation bar.

## Key Features
- User validation and error messages for input validation failures (e.g., empty song name, insufficient dancers).
- Client-side input validation using JavaScript to provide real-time feedback on length, format, and other requirements.
- Responsive web design techniques, including media queries and flexible layouts, for a seamless experience on desktop and mobile devices.
- Refined user interface elements, such as typography, color scheme, and overall visual design, to enhance aesthetics and usability.
- Database implementation to store songs, dancers, and setlists, ensuring data persistence even after server restarts.
- User authentication and authorization mechanisms to provide personalized setlists and secure data access.

## Technologies Used
- Flask: A Python web framework used to build the REST API and handle server-side logic.
- HTML, CSS, JavaScript: Front-end technologies used for building the user interface and client-side validation.
- SQL: Database management system for storing and retrieving data.

## Demo
To experience the functionality of SetGen-Python, you can visit the live demo by clicking here : [https://youtu.be/MpTHXrgis6U]. Feel free to explore and generate setlists for different shows!

Thank you for checking out SetGen-Python! We hope you find it helpful in generating optimized setlists for your shows.

## The next step ?

- Add an edit feature to be able to edit songs and dancers within the database.
- Add an export feature that would allow users to export setlists into an Excel file.
