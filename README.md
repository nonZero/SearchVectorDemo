# Requirements
* Python 3.8
* pipenv
* postgers + current user should be a postgres superuser.
   

# Setup
    
    git clone
    cd SearchVectorDemo
    pipenv install --skip-lock
    createdb svdemo
    pipenv run manage.py migrate
    
    git clone https://github.com/projectbenyehuda/public_domain_dump.git
    
    pipenv run manage.py populate_works  
    pipenv run manage.py update_sv

# Run

    pipenv run manage.py runserver
    
And open <http://127.0.0.1:8000> .
      
        
    
