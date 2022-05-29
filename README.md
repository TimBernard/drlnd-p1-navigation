# Udacity Deep Reinforcement Learning: Project 1, Navigation 

## Environment 
* Banana Collection Environment 
* The goal of this problem is for the agent to collect yellow bananas (+1 reward) and avoid blue bananas (-1 reward). 
* For the purposes of this project, the environment is considered solved when the agent achieves an average score (accumulated reward over an episode) of +13.0 over 100 episodes. 

## State Space: 
* 37-Dimensional continuous observation space, (includes agent velocity and ray-based perception of objects in realm of agent's forward direction)

## Action Space: 
* 4-Dimensional discrete space, (Forward, Backward, Left, Right) 

## Installation and Usage 
* This notebook can be used by simply opening it in the provided Udacity Project Workspace 
* Alternatively, you can run this locally: 
    1. Clone this repository
    2. To get the python/conda environment setup, follow these instructions: https://github.com/udacity/Value-based-methods#dependencies
    3. Make sure you have jupyter properly installed, and you may have to get an archived version of pytorch 
    3. Download the environment for Linux: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip or for Mac: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip
    4. Run 'conda activate drlnd' 
    5. In your local directory, 'python run.py "<path/to/banana/environment/executable\>"' to see the trained agent in action
    6. 'jupyter notebook Navigation.pynb' to run the notebook and train the agent yourself, the resulting parameters will be overwrite checkpoint.pth 
