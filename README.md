# My personal website
---    

## File Structure

```
/data/www/root
├── venv
├── tests
├── app
│   ├── api
│   ├── errors
│   ├── static
│   ├── templates
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── forms.py
|
├── config.py
├── manage.py
├── uwsgi.ini
└── README.md
```


## URL Structure    

    ```
    domain
    |   |____ index
    |   |____ about
    |   |____ pubkey
    |   |____ blog -> blog.~
    |   |____ resume -> resume.~
    |____ blog.~
    ```

