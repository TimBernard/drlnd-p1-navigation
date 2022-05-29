import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        # Network Architecture 
        self.h1 = 100
        self.h2 = 100
                
        "*** YOUR CODE HERE ***"
        self.fc1 = nn.Linear(state_size, self.h1)
        self.fc2 = nn.Linear(self.h1, self.h2) 
        self.fc3 = nn.Linear(self.h2, action_size)
        
        self.relu = nn.ReLU()
        
    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        out = self.relu(self.fc1(state))
        out = self.relu(self.fc2(out))
        out = self.fc3(out)
        return out