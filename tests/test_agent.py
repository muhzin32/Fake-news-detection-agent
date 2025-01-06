import pytest
from src.fake_news_agent.agent import FakeNewsDetectionAgent

def test_agent_initialization():
    config = {
        'content_analysis': {
            'threshold': 0.75
        }
    }
    agent = FakeNewsDetectionAgent('test_agent', config)
    assert agent.agent_id == 'test_agent'
    assert agent.config['content_analysis']['threshold'] == 0.75
