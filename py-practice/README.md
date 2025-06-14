## For initializing and running 

```uv init code
uv run main.py
```
## to add dependencies 
### ex:- uv add fastapi
```
uv add <package/module name> 
```

when running a script with multiple dependencies  

```
uv add --script <scripts.py> 'flask' 'requests'
uv run scripts.py
```