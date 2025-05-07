# TEST TEST

# Article CMS (FlaskWebProject)

This project is a Python web application built using Flask. The user can log in and out and create/edit articles. An article consists of a title, author, and body of text stored in an Azure SQL Server along with an image that is stored in Azure Blob Storage. You will also implement OAuth2 with Sign in with Microsoft using the `msal` library, along with app logging.

## Log In Credentials for FlaskWebProject

- Username: admin
- Password: pdm-admin-2025#!

Or, use the Microsoft Login button to authenticate using your Microsoft account.

## Project Instructions (For Student)

You are expected to do the following to complete this project:
Project Implementation Details
1. ✅ Resource Group created in Azure: pdmflasksqlserver-rg
2. ✅ Azure SQL Database Configuration:
Server: pdmflasksqlserver.database.windows.net
Database: pdmflasksqldb
Username: pdmsqladmin
Tables: USERS and POSTS
3. ✅ Azure Blob Storage:
Account: pdmflaskstorageaccount
Container: images
Access Level: Blob (anonymous read access for blobs only)
4. ✅ Microsoft Authentication:
Client ID: 79b517eb-b734-4d7d-b831-4173fe9cf6fc
Redirect Path: /getAToken

5. ✅ App Service selected to deploy the FlaskWebProject to Azure. Completed
6. ✅ Add logging for whether users successfully or unsuccessfully logged in. Completed

7. ✅ Completed - To prove that the application in on Azure and working, go to the URL of your deployed app, log in using the credentials in this README, click the Create button, and create an article with the following data:
	- Title: "Hello World!"
	- Author: "Jane Doe"
	- Body: "My name is Jane Doe and this is my first article!"
	- Upload an image of your choice. Must be either a .png or .jpg.
   After saving, click back on the article you created and provide a screenshot proving that it was created successfully. Please also make sure the URL is present in the screenshot.
	  ![Post successful](docs/post-successful.png "post successful")
8. ✅ Completed -  Log into the Azure Portal, go to your Resource Group, and provide a screenshot including all the resources that were created to complete this project. (see sample screenshot in "example_images" folder)
   ![Resource group](docs/resource-group.png "resource group")
9. ✅ Completed - Take a screenshot of the Redirect URIs entered for your registered app, related to the MS Login button.
   ![redirect URI](docs/redirect-URI.png "redirect uri")
10. ✅ Completed - Take a screenshot of your logs (can be from the Log stream in Azure) showing logging from an attempt to sign in with an invalid login, as well as a valid login.
	* **Invalid login**
	![invalid login](docs/invalid-login.png "invalid login")
	* **Valid login**
	![alid login](docs/succeesful-login.png "valid login")
## example_images Folder

This folder contains sample screenshots that students are required to submit in order to prove they completed various tasks throughout the project.

1. article-cms-solution.png is a screenshot from running the FlaskWebProject on Azure and prove that the student was able to create a new entry. The Title, Author, and Body fields must be populated to prove that the data is being retrieved from the Azure SQL Database while the image on the right proves that an image was uploaded and pulled from Azure Blob Storage.
2. azure-portal-resource-group.png is a screenshot from the Azure Portal showing all the contents of the Resource Group the student needs to create. The resource group must (at least) contain the following:
	- Storage Account
	- SQL Server
	- SQL Database
	- Resources related to deploying the app
3. sql-storage-solution.png is a screenshot showing the created tables and one query of data from the initial scripts.
4. blob-solution.png is a screenshot showing an example of blob endpoints for where images are sent for storage.
5. uri-redirects-solution.png is a screenshot of the redirect URIs related to Microsoft authentication.
6. log-solution.png is a screenshot showing one potential form of logging with an "Invalid login attempt" and "admin logged in successfully", taken from the app's Log stream. You can customize your log messages as you see fit for these situations.

## Dependencies

1. A free Azure account
2. A GitHub account
3. Python 3.10
4. Visual Studio 2019 Community Edition (Free)
5. The latest Azure CLI (helpful; not required - all actions can be done in the portal)
