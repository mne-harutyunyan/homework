# Create a function that updates user settings by passing keyword arguments dynamically.
# Use **kwargs to accept dynamic user settings.
# Use a function to pass these settings as keyword arguments to another function.

def update_settings(**settings):
    user_settings = {'country':'Armenia',
                     'language': 'armenian',
                     'notifications' : 'off',
                     'dark mode' : 'on'
                     }
    user_settings.update(settings)
    return user_settings
print(update_settings(country = "USA",language = "english", notifications = "on"))

def apply_settings(settings):
    return settings

print(apply_settings(update_settings(country = "USA",notifications = "on")))