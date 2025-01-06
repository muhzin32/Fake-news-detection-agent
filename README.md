# Fake News Detection Agent

An AI-powered fake news detection system built using the OASIS framework, designed to identify and counter political misinformation.

## Features

- Real-time content analysis
- Source credibility checking
- Political bias detection
- Automated fact-checking
- Network spread monitoring

## Installation

1. Clone the repository:
```bash
git clone https://github.com/muhzin32/fake-news-detection-agent.git
cd fake-news-detection-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the simulation:
```bash
python examples/run_simulation.py
```

## Configuration

Adjust settings in `config/fake_news_config.yaml`:
- Model parameters
- Number of agents
- Analysis thresholds
- Content criteria

## Testing

Run tests:
```bash
pytest tests/
```

## License

Apache License 2.0
