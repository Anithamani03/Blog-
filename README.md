Flask Blog Project Description
Project Name: Simple Blog Application

Overview:
A lightweight Flask web application that allows users to create, view, and manage blog posts through a clean web interface.

Key Features:

Home Page – Landing page for your blog
View Posts – Display all created blog posts in a list format
Add New Post – Form to create and submit new blog posts with title and content
Simple Data Storage – Posts are stored in memory (in a Python list)
Technology Stack:

Backend: Python Flask (web framework)
Frontend: HTML, CSS, Jinja2 templates
Styling: Custom CSS for layout and design

Project Structure:
App.py                  # Main Flask application
Templates/
  ├── Base.html        # Base template (inherited by other pages)
  ├── Home.html        # Home page
  ├── Posts.html       # Posts listing page
  └── Add_post.html    # Form to add new posts
Static/
  └── Style.css        # CSS styling

Routes:
/ – Home page
/posts – View all blog posts
/add – Create new post (GET for form, POST to submit)
Current Limitations:

Data is stored in memory, so posts are lost when the app restarts
No user authentication
No database integration
No post editing or deletion features
