# battleship
Distributable Battleship game capable of being played over a network

# ai_graph_coloring

Artificial intelligence project to color graphs

## Local setup

### Requirements

- python 2.7

### Environment Setup

#### Installing virtualenv

    $ pip install virtualenv

#### Creating a virtual environment
    $ virtualenv venv
    
#### Activating your virtual environment

    $ source venv/bin/activate
    
#### Installing requirements

1. Activate your virtual environment

2. `$ pip install requirements.txt`

### Local Development

#### Adding a git hook

This will make git run tests before you make a commit

From the root directory of your project:

    $ echo "./run-tests.sh" > .git/hooks/pre-commit
    $ chmod +x .git/hooks/pre-commit    

### Contributing

1. Create a new branch to do changes on
- Branch should be appropriately named for the changes made
2. Create a PR from your branch to master
3. After your branch receives a `+1` it can be merged
