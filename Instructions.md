1. Install requirements with pip
2. Change the settings.py, add your email host and password
3. Go to events/view.py and change the line 75, change the static directory to your local path
4. Make migrations
5. Go to localhost:port/events/
6. Grab a coke and start testing :) 

Bugs:
1. The project is intended to run into a website and not a local site, thus there might
 be a missconfigation that will get you a "Permission matching query does not exist" exception
 Sometimes Django decides not to install the default permissions for a model and thus the change_profile permission
 goes missing. To fix this, run the check_permissions in Commands.. This checks all permissions and adds those that are missing.
