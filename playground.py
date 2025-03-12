from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai 
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground,serve_playground_app
load_dotenv()

openai.api_key=os.getenv("OPNEAI_API_KEY")
phi.api=os.getenv("PHI_API_KEY")

#web serachagent
web_serach_agent=Agent(
    name="web search agent",
    role="Search the web for importmation",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tools_calls=True,
    markdown=True
)

#finacial agent
finacial_agent= Agent(
    name="Finanical AI Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,technical_indicators=True,company_news=True,key_financial_ratios=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True

)

app=Playground(agents=[finacial_agent,web_serach_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
