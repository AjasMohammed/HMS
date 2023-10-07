
# Hospital Management System API

## Project Description

Provide a brief overview of your project, its purpose, and its main features. You can include information such as:

- The goal of the project.
- Key technologies used (e.g., Django, React, Django Rest Framework).
- Any unique or noteworthy aspects of the project.


## API Endpoints

Describe the available API endpoints and their functionalities. Provide examples of how to use each endpoint. For example:

### Authentication

- **POST `/auth/login/`**
  - Description: Log in a user and obtain an access token.
  - Input: Provide valid username and password.
  - Output: Returns an access token.
  
- **POST `/auth/register/`**
  - Description: Register a new user.
  - Input: Provide user details (username, password, etc.).
  - Output: Returns the registered user's details.

- **POST `/auth/logout/`**
  - Description: Log out a user by revoking their access token.
  - Input: Requires a valid access token.
  - Output: Logs out the user.

### User Management

- **GET `/api/doctors/`**
  - Description: Retrieve a list of doctors.
  - Input: Requires authentication as a doctor.
  - Output: Returns a list of doctor profiles.

- **GET `/api/doctors/<int:pk>`**
  - Description: Retrieve details of a specific doctor.
  - Input: Requires authentication as a doctor.
  - Output: Returns the profile of the specified doctor.

- **GET `/api/patients/`**
  - Description: Retrieve a list of patients.
  - Input: Requires authentication as a doctor.
  - Output: Returns a list of patient profiles.

- **GET `/api/patients/<int:pk>`**
  - Description: Retrieve details of a specific patient.
  - Input: Requires authentication as a doctor.
  - Output: Returns the profile of the specified patient.

### Patient Records

- **GET `/api/patient_records/`**
  - Description: Retrieve patient records for the doctor's department.
  - Input: Requires authentication as a doctor.
  - Output: Returns a list of patient records.

- **GET `/api/patient_records/<int:pk>`**
  - Description: Retrieve details of a specific patient record.
  - Input: Requires authentication as a patient or doctor.
  - Output: Returns the specified patient record.

### Departments

- **GET `/api/department/`**
  - Description: Retrieve a list of departments.
  - Input: Requires authentication.
  - Output: Returns a list of departments.

- **GET `/api/department/<int:pk>/doctors`**
  - Description: Retrieve doctors in a specific department.
  - Input: Requires authentication as a doctor.
  - Output: Returns a list of doctors in the department.

- **GET `/api/department/<int:pk>/patients`**
  - Description: Retrieve patients in a specific department.
  - Input: Requires authentication as a doctor.
  - Output: Returns a list of patients in the department.
