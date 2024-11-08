# CMD
    cmd
    d:
    cd d:\Users\lars\software\python_projects\
    python --version
WTF???:
    cd d:\Users\lars\software\python_projects\python
    python --version

# WSL
    wsl
    cd /mnt/d/Users/lars/software/python_projects/python
    python3 --version
        Python 3.8.10
    python3 python.py
        Hello, World
    python3 test_python.py

# Docker: Run program
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run --rm --name sletmig -v $PWD:/mycode py_img python --version
        Python 3.13.0
    docker run --rm --name sletmig -v $PWD:/mycode py_img python /mycode/python.py
    docker run --rm --name sletmig -v $PWD:/mycode py_img python /mycode/test_python.py

    docker run --rm --name sletmig -v $PWD:/mycode py_img pip --version
        pip 24.2 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
    docker run --rm --name sletmig -v $PWD:/mycode py_img pytest --version
        pytest 8.3.3
    docker run --rm --name sletmig -v $PWD:/mycode py_img pytest /mycode/pytest_python.py

# Docker: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run -d --rm --name sletmig -v $PWD:/mycode py_img
    docker exec sletmig /bin/bash -c "python --version"
    docker exec sletmig /bin/bash -c "pip --version"
    docker exec sletmig /bin/bash -c "pytest --version"
    docker exec sletmig /bin/bash -c "cd /mycode && python python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && python test_python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && pytest /mycode/pytest_python.py"
    docker stop sletmig

# Docker-compose: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker-compose build
    docker-compose up -d
    docker exec sletmig /bin/bash -c "python --version"
    docker exec sletmig /bin/bash -c "cd /mycode && python src/python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && python test/test_python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && pytest test/pytest_python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && pytest test/pytest_parameters.py"
    docker-compose down

Starting a shell session, enables colour coding of the output:

    docker exec -it sletmig /bin/bash
        cd /mycode/test/
        pytest -v pytest_python.py
        pytest -v pytest_parameters.py


# References
https://www.lambdatest.com/learning-hub/pytest-tutorial
