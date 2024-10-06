# AFAQY

# User Profile Microservice

## Overview
A microservice for managing user profiles, integrating with a weather API, and managing user states.

### Features
- User CRUD operations
- JWT authentication and role-based access control
- Integration with a weather API
- Automatic weather updates and state transitions

### How to Run
1. **Install Python on Windows:**

   - Go to the official Python website: [Python Downloads](https://www.python.org/downloads/).
   - Download the latest version of Python (ensure it's Python 3.7+).
   - Run the Python installer.
   - During installation, **check the option "Add Python to PATH"** before clicking Install.
   - Once installed, open the **Command Prompt** and verify Python installation with:
     ```
     python --version
     ```
     ---
2.**Clone the repository**
   ```
   git clone <repository-url>
   cd your_folder
    ```
---
```
3.**Create a virtual environment**  
   Set up a Python virtual environment to manage dependencies:
   ```
   python -m venv venv
```


### 3. **Activate the Virtual Environment**

```markdown
3. **Activate the virtual environment**  
   Activate the virtual environment:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```
     source venv/bin/activate
     
     
```
4. **Ensure `pip` is installed:**

   - `pip` is the package installer for Python, usually installed with Python. If not, you can install it manually:
     ```
     python -m ensurepip --upgrade
     ```

   - Verify `pip` is installed by running:
     ```
     pip --version

5. **Install Dependencies**

- Use `pip` to install all required packages from the `requirements.txt` file:

  ```bash
  pip install -r requirements.txt


5. **Set Up Environment Variables**

- Create a `.env` file in the root directory of your project to store sensitive information like your API key and other variables:
mine is :

  ```
WEATHER_API_KEY=fc991c99234d4526aae42339240310
BASE_URL = "http://api.weatherapi.com/v1/current.json"



---
```
6. **Run the Application**


- Start the FastAPI server using `uvicorn`:

```
uvicorn main:app --reload

# AFAQY

# User Profile Microservice

## Overview
A microservice for managing user profiles, integrating with a weather API, and managing user states.

### Features
- User CRUD operations
- JWT authentication and role-based access control
- Integration with a weather API
- Automatic weather updates and state transitions

### How to Run
1. **Install Python on Windows:**

   - Go to the official Python website: [Python Downloads](https://www.python.org/downloads/).
   - Download the latest version of Python (ensure it's Python 3.7+).
   - Run the Python installer.
   - During installation, **check the option "Add Python to PATH"** before clicking Install.
   - Once installed, open the **Command Prompt** and verify Python installation with:
     ```
     python --version
     ```
     ---
2.**Clone the repository**
   ```
   git clone <repository-url>
   cd your_folder
    ```
---
```
3.**Create a virtual environment**  
   Set up a Python virtual environment to manage dependencies:
   ```
   python -m venv venv
```


### 3. **Activate the Virtual Environment**

```markdown
3. **Activate the virtual environment**  
   Activate the virtual environment:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```
     source venv/bin/activate
     
     
```
4. **Ensure `pip` is installed:**

   - `pip` is the package installer for Python, usually installed with Python. If not, you can install it manually:
     ```
     python -m ensurepip --upgrade
     ```

   - Verify `pip` is installed by running:
     ```
     pip --version

5. **Install Dependencies**

- Use `pip` to install all required packages from the `requirements.txt` file:

  ```bash
  pip install -r requirements.txt


5. **Set Up Environment Variables**

- Create a `.env` file in the root directory of your project to store sensitive information like your API key and other variables:
mine is :

  ```
WEATHER_API_KEY=fc991c99234d4526aae42339240310
BASE_URL = "http://api.weatherapi.com/v1/current.json"



---
```
6. **Run the Application**


- Start the FastAPI server using `uvicorn`:

```
uvicorn main:app --reload

# AFAQY

# User Profile Microservice

## Overview
A microservice for managing user profiles, integrating with a weather API, and managing user states.

### Features
- User CRUD operations
- JWT authentication and role-based access control
- Integration with a weather API
- Automatic weather updates and state transitions

### How to Run
1. **Install Python on Windows:**

   - Go to the official Python website: [Python Downloads](https://www.python.org/downloads/).
   - Download the latest version of Python (ensure it's Python 3.7+).
   - Run the Python installer.
   - During installation, **check the option "Add Python to PATH"** before clicking Install.
   - Once installed, open the **Command Prompt** and verify Python installation with:
     ```
     python --version
     ```
     ---
2.**Clone the repository**
   ```
   git clone <repository-url>
   cd your_folder
    ```
---
```
3.**Create a virtual environment**  
   Set up a Python virtual environment to manage dependencies:
   ```
   python -m venv venv
```


### 3. **Activate the Virtual Environment**

```markdown
3. **Activate the virtual environment**  
   Activate the virtual environment:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```
     source venv/bin/activate
     
     
```
4. **Ensure `pip` is installed:**

   - `pip` is the package installer for Python, usually installed with Python. If not, you can install it manually:
     ```
     python -m ensurepip --upgrade
     ```

   - Verify `pip` is installed by running:
     ```
     pip --version

5. **Install Dependencies**

- Use `pip` to install all required packages from the `requirements.txt` file:

  ```bash
  pip install -r requirements.txt


5. **Set Up Environment Variables**

- Create a `.env` file in the root directory of your project to store sensitive information like your API key and other variables:
mine is :

  ```
WEATHER_API_KEY=fc991c99234d4526aae42339240310
BASE_URL = "http://api.weatherapi.com/v1/current.json"



---
```
6. **Run the Application**


- Start the FastAPI server using `uvicorn`:

```
uvicorn main:app --reload
```
## importnant info
1-when you start the app an admin user will be created if its not there.
```
email: admin@example.com                         
password: admin
```

