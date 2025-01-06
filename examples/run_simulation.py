import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.fake_news_agent.simulation import FakeNewsSimulation

def main():
    config_path = project_root / 'config' / 'fake_news_config.yaml'
    simulation = FakeNewsSimulation(config_path)
    simulation.run_simulation()

if __name__ == "__main__":
    main()
