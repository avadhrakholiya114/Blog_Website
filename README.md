# Django Blogs Website

Welcome to the Django Blogs project, a website where users can read and explore blog posts categorized by topics.

## Project Overview


- **iblog:** Django app containing models, views, and templates for handling blog-related functionality.

## Features

- Users can view blog posts categorized by topics.
- Admins can add, edit, or delete blog posts and categories.
- Responsive design for optimal viewing on various devices.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

      ```bash
   
   mkdir bolg_Web
    
    ```
    ```bash
    git clone https://github.com/avadhrakholiya114/Blog_Website.git
       cd Blog_Website
  
    ```
 

2. Create a virtual environment:

    ```bash
    python -m venv myworld
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\myworld\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source myworld/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin account.

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the admin panel at `http://localhost:8000/admin/` to add blog posts and categories.


