# Setting this project up (First-time)
run `pip install playwright`

run `pip install pip-tools`

create [requirements.in](requirements.in) file so we can generate `requrements.txt` file

run `pip-compile --output-file=- > requirements.txt`

run `playwright install-deps` first as trying to install browsers generates an error:

```
 Host system is missing dependencies to run browsers.
 Please install them with the following command:     
                                                     
     sudo playwright install-deps                    
```

run `playwright install`

create `scrape_fixtures.py`

