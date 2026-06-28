# 📝 Django Blog Platform

A modern **Blog & Social Platform** built with **Django**, allowing users to publish articles, interact with posts, and connect with other users through likes, bookmarks, and a follow system.

This project demonstrates the implementation of several advanced Django concepts, including a **Custom User Model**, **Custom Authentication Backends**, **Signals**, **Optimized Database Queries**, and **Tag-based Content Discovery**.

---

## 🚀 Features

### 👤 User Management
- Custom User model using `AbstractUser`
- User registration
- Login & Logout
- Password change
- Password reset via email
- User profile page
- Profile image upload
- User bio, job and phone number

### 📰 Blog System
- Create posts
- Edit posts
- Delete posts
- Rich post content
- Categories
- Tags using **django-taggit**
- SEO-friendly slug generation
- Meta description support
- Automatic publish date

### ❤️ Social Features
- Like / Unlike posts (AJAX)
- Save / Unsave posts (Bookmarks)
- Follow / Unfollow users
- Followers & Following lists

### 🖼 Media Support
- Multiple images for posts
- User profile images
- Automatic image cleanup after deleting a post

### 🔍 Content Discovery
- Filter posts by category
- Filter posts by tag
- Similar posts recommendation based on shared tags
- Popular posts ordering by total likes

### ⚡ Performance
- Optimized queries using:
  - `select_related()`
  - `prefetch_related()`
- Database indexing
- Custom model managers

### 📧 Notifications
- Email notification when a post is deleted

### 🔐 Authentication
Supports authentication using:
- Username
- Email
- Phone Number

---

# 🛠 Built With

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Django Template Language (DTL)
- django-taggit

---

# 📂 Project Structure

```
blog/
│
├── models.py
├── views.py
├── forms.py
├── urls.py
├── signals.py
├── authentication.py
│
templates/
static/
media/
```

---

# 🗄 Database Models

## User

Custom user model containing:

- Username
- Email
- Phone Number
- Bio
- Job
- Date of Birth
- Profile Image

---

## Post

Stores blog posts.

Fields include:

- Title
- Slug
- Meta Description
- Content
- Category
- Publish Date
- Status
- Likes
- Saved Users
- Tags

---

## PostImage

Stores images related to posts.

---

## UserImage

Stores profile images.

---

## UserContact

Implements the Follow / Unfollow relationship between users.

---

# 🔥 Main Functionalities

## Authentication

- Register
- Login
- Logout
- Change Password
- Reset Password

---

## Blog

- Publish article
- Update article
- Delete article
- Upload images
- Browse by category
- Browse by tag

---

## Social

- Like posts
- Bookmark posts
- Follow users
- View followers
- View following

---

# ⚙ Custom Django Features Used

## ✅ Custom User Model

Implemented using:

```python
AbstractUser
```

---

## ✅ Custom Model Manager

```python
PublishedManager
```

Used for retrieving only published posts.

---

## ✅ Signals

Implemented using Django Signals.

Current signals:

- Update total likes automatically
- Send email after deleting a post

---

## ✅ Custom Authentication Backends

Supports login using:

- Email
- Phone Number

---

## ✅ AJAX APIs

The project uses AJAX endpoints for:

- Like
- Save
- Follow

Returning JSON responses without refreshing the page.

---

# 📊 Database Optimization

Optimizations include:

- `select_related()`
- `prefetch_related()`
- Database indexes
- Query optimization

---

# 🏷 Categories

- Culture
- Business
- Lifestyle
- Technology

---

# 🏷 Tags

Powered by:

```
django-taggit
```

Users can:

- Add tags
- Search by tags
- Discover similar posts

---

# 📸 Media

Uploaded files are stored inside:

```
media/

account_images/
post_image/
user_image/
```

---

# 📧 Email Support

The application integrates Django's email system for notifications.

Example:

- Notify authors after deleting their posts.

---

# 🔑 Authentication Flow

```
Register
      │
      ▼
Login
      │
      ▼
Profile
      │
      ├── Create Post
      ├── Like
      ├── Save
      ├── Follow Users
      └── Manage Posts
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/django-blog.git
```

Enter project directory

```bash
cd django-blog
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

# ⚙ Environment Variables

Example:

```env
SECRET_KEY=

DEBUG=True

EMAIL_HOST=

EMAIL_PORT=

EMAIL_HOST_USER=

EMAIL_HOST_PASSWORD=

DEFAULT_FROM_EMAIL=
```

---

# 📈 Future Improvements

- REST API using Django REST Framework
- JWT Authentication
- Comment System
- Nested Comments
- Search Engine
- Pagination
- Notifications
- User Dashboard
- Image Compression
- Docker Support
- PostgreSQL
- Unit Testing
- Deployment

---

# 🎯 Skills Demonstrated

- Django ORM
- Authentication
- Authorization
- Model Relationships
- Signals
- Custom Managers
- Query Optimization
- Forms
- Class-Based Design
- Media Handling
- AJAX
- JSON Responses
- Email Integration
- CRUD Operations

---

# 📜 License

This project is created for educational and portfolio purposes.

---

# 👨‍💻 Developer

**Hossein Salehi**

Backend Developer | Python & Django

GitHub:
```
https://github.com/hossein81-star
```



---

