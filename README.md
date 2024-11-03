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
    docker run --rm --name sletmig -v $PWD:/mycode py_img python /mycode/python.py
    docker run --rm --name sletmig -v $PWD:/mycode py_img python /mycode/test_python.py

# Docker: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker build -t py_img .
    docker run -d --rm --name sletmig -v $PWD:/mycode py_img
    docker exec sletmig /bin/bash -c "python --version"
    docker exec sletmig /bin/bash -c "cd /mycode && python python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && python test_python.py"
    docker stop sletmig

# Docker-compose: Version check and run program (running image)
    cd /mnt/d/Users/lars/software/python_projects/python
    docker-compose build
    docker-compose up -d
    docker exec sletmig /bin/bash -c "python --version"
    docker exec sletmig /bin/bash -c "cd /mycode && python python.py"
    docker exec sletmig /bin/bash -c "cd /mycode && python test_python.py"
    docker-compose down

