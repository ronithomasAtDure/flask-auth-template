# Authentication using Flask

  * **__init__.py** 
let you see who's using your docs, what your best and worst pages are, what people are searching for and more!
   * **auth.py** 
Takes care of the authorization of the login session. Checks passwords against the username, directs to signup page if the user is not found in the users table, and stores the signup info into a hashed DB.  Also holds the routes for authentication html like login, signup, logout
 * **main.py** 
All the routes for the particular application is mentioned here in main file. To run the application use the command:
```bash
python main.py
```
Mention `@login_required` before defining a function for the route to make it limited to the user. Example below
```python
@main.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html")
```
 * **model.py** 
The column name and character limits are mentioned in this file, basically creating an SQL table to home the collected signup information.
