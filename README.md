# WSL: Version check
    wsl
    python3 --version
        Python 3.8.10

# WSL: Run program
    cd /mnt/d/Users/lars/software/python_projects/python
    python3 python.py
        Hello, World

# Docker: Version check
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run --rm --name sletmig py_img python --version

# Docker: Run program
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run --rm --name sletmig -v $PWD:/mycode py_img python /mycode/python.py

# Docker: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run -d --rm --name sletmig py_img
    docker exec sletmig python --version
    docker exec sletmig /bin/bash -c "cd /mycode && python python.py"
    docker stop sletmig

# Docker-compose: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker-compose build
    docker-compose up -d
    docker exec sletmig python --version
    docker exec sletmig /bin/bash -c "cd /mycode && python python.py"
    docker stop sletmig




    docker compose up
        Hello, World

    cmd
    d:
    cd d:\Users\lars\software\python_projects\python\
    python python.py
    python test_calculator.py

