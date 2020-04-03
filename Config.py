"""The canonical way to share information across modules within a single program is to create a special configuration module (often called config or cfg). Just import the configuration module in all modules of your application; the module then becomes available as a global name. Because there is only one instance of each module, any changes made to the module object get reflected everywhere. For example:
File: config.py
x = 0   # Default value of the 'x' configuration setting
File: mod.py
import config
config.x = 1
File: main.py
import config
import mod
print config.x
Module variables are also often used to implement the Singleton design pattern, for the same reason."""

stringaServer ="" #default value stringa vuota