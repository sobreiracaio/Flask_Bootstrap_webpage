# Community Site

A Flask-based community platform that allows users to create accounts, share posts, and connect with other members through course affiliations.

## Project Overview

This is a full-stack web application built with Flask that serves as a community platform where users can:

- Create and manage user accounts with authentication
- Share posts with the community
- Edit and delete their own posts
- Manage personal profiles with profile pictures
- Connect with other users through course affiliations
- Browse all community members and their posts

## Technologies Used

### Backend
- **Flask** - Python web framework for building the application
- **SQLAlchemy** - Object-Relational Mapping (ORM) for database operations
- **Flask-Login** - User session management and authentication
- **Flask-Bcrypt** - Password hashing and security
- **Flask-WTF** - Form handling and validation
- **WTForms** - Form creation and validation
- **Pillow (PIL)** - Image processing for profile pictures
- **Gunicorn** - WSGI HTTP Server for production deployment

### Frontend
- **HTML5** - Markup structure
- **CSS3** - Custom styling (main.css)
- **Bootstrap 5.3.7** - Responsive design framework
- **Jinja2** - Template engine for dynamic content rendering

### Database
- **SQLite** - Default database for development
- **PostgreSQL** - Production database (configured via DATABASE_URL environment variable)

### Deployment
- **Railway** - Cloud platform deployment ready (Procfile included)

## Project Structure

```
community_site/
├── community_site/
│   ├── __init__.py          # Flask app initialization and configuration
│   ├── models.py            # Database models (User, Post)
│   ├── forms.py             # WTForms form classes
│   ├── routes.py            # Application routes and view functions
│   ├── static/
│   │   ├── main.css         # Custom CSS styles
│   │   └── images/          # User profile pictures
│   └── templates/
│       ├── base.html        # Base template
│       ├── navbar.html      # Navigation component
│       ├── home.html        # Homepage with posts feed
│       ├── login.html       # Login and registration forms
│       ├── profile.html     # User profile display
│       ├── profile_edit.html # Profile editing form
│       ├── post.html        # Individual post view
│       ├── post_create.html # Post creation form
│       ├── users.html       # All users listing
│       └── contact.html     # Contact information
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── Procfile                # Heroku deployment configuration
└── .gitignore              # Git ignore rules
```

## Key Features

### Authentication System
- User registration with email validation
- Secure password hashing using bcrypt
- Session management with Flask-Login
- Login/logout functionality with "Remember Me" option

### User Management
- Profile creation and editing
- Profile picture upload with automatic resizing
- Course affiliation system (6 available courses)
- User statistics (post count, course count)

### Content Management
- Post creation with title and body content
- Post editing and deletion (only by post authors)
- Chronological post feed on homepage
- Individual post view with author information

### Database Models

#### User Model
- `id` - Primary key
- `username` - Display name
- `email` - Unique email address
- `password` - Hashed password
- `profile_photo` - Profile picture filename
- `courses` - Semicolon-separated course list
- `posts` - Relationship to user's posts

#### Post Model
- `id` - Primary key
- `title` - Post title
- `body` - Post content
- `creation_date` - Timestamp
- `id_user` - Foreign key to User

## Technical Implementation

### Security Features
- CSRF protection on all forms
- Password hashing with bcrypt
- SQL injection prevention through SQLAlchemy ORM
- File upload validation for profile pictures
- User authorization for post editing/deletion

### Image Processing
- Automatic image resizing to 200x200 pixels
- Unique filename generation using secrets module
- Support for JPG, JPEG, and PNG formats
- Thumbnail creation for optimized loading

### Form Validation
- Email format validation
- Password length requirements (6-20 characters)
- Password confirmation matching
- Duplicate email prevention
- File type validation for uploads

### Database Design
- Proper foreign key relationships
- Automatic timestamp creation
- Lazy loading for post relationships
- Database initialization check on startup

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sobreiracaio/Flask_Bootstrap_webpage.git
   cd community_site
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables (optional)**
   ```bash
   export DATABASE_URL=<your-database-url>  # For PostgreSQL
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## Deployment

This application is ready for Railway deployment:

1. **Create Railway account and project**
   - Go to [Railway](https://railway.app)
   - Sign up/login with GitHub
   - Create a new project

2. **Connect your repository**
   - Connect your GitHub repository to Railway
   - Railway will automatically detect it's a Python project

3. **Add PostgreSQL database**
   - In your Railway project dashboard
   - Click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

4. **Configure environment variables**
   - Railway automatically detects and sets `DATABASE_URL`
   - No additional configuration needed for basic deployment

5. **Deploy**
   - Railway will automatically deploy when you push to your main branch
   - Your app will be available at the provided Railway URL

## Configuration

### Development
- Uses SQLite database (`community.db`)
- Debug mode enabled
- Local file storage for images

### Production
- PostgreSQL database via `DATABASE_URL` environment variable
- Gunicorn WSGI server
- Production-ready settings

## API Endpoints

- `GET /` - Homepage with posts feed
- `GET /login` - Login and registration forms
- `POST /login` - Process login/registration
- `GET /logout` - User logout
- `GET /profile` - User profile view
- `GET /profile/edit` - Profile editing form
- `POST /profile/edit` - Process profile updates
- `GET /post/create` - Post creation form
- `POST /post/create` - Process new post
- `GET /post/<id>` - Individual post view
- `POST /post/<id>` - Edit post (author only)
- `POST /post/<id>/delete` - Delete post (author only)
- `GET /users` - All users listing
- `GET /contact` - Contact information

## License

This project is open source and available under the MIT License.
