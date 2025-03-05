# Project Title

## Description
This project is a financial agent that utilizes AI to provide stock market insights and web search capabilities. It can summarize analyst recommendations and share the latest news for specific stocks.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/kri-sh27/Finacial_Agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Finacial_Agent
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
This project requires a `.env` file for configuration. Create a `.env` file in the root of the project and add the following variables:

```
# Example environment variables
OPNEAI_API_KEY=<your-openai-api-key>
GROQ_API_KEY=<your-groq-api-key>
PHI_API_KEY=<your-phi-api-key>
```

Make sure to replace the placeholder values with your actual configuration values.

## Dependencies
The following packages are required for this project:
- `phidata`
- `python-dotenv`
- `yfinance`
- `packaging`
- `duckduckgo-search`
- `fastapi`
- `uvicorn`
- `groq`
- `openai`

## Usage
To run the financial agent, execute the main script that is finacialagent.py. It will summarize analyst recommendations and provide the latest news for the specified stocks.