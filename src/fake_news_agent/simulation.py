from social_simulation.env import Environment
from .agent import FakeNewsDetectionAgent
import yaml
import random

class FakeNewsSimulation:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
            
        self.environment = Environment()
        self.agents = self._initialize_agents()
        
    def _initialize_agents(self):
        return [
            FakeNewsDetectionAgent(f"agent_{i}", self.config)
            for i in range(self.config['simulation']['num_agents'])
        ]
    
    def run_simulation(self):
        """Run the fake news detection simulation"""
        for step in range(self.config['simulation']['time_steps']):
            print(f"Simulation step: {step}")
            self._run_step(step)
    
    def _run_step(self, step):
        """Execute one simulation step"""
        new_posts = self.environment.get_new_posts()
        
        for agent in self.agents:
            if random.random() < self.config['simulation']['activation_probability']:
                for post in new_posts:
                    analysis = agent.analyze_content(post)
                    action = agent.take_action(post, analysis)
                    
                    if action['action'] == 'flag':
                        self.environment.flag_content(post.id)
