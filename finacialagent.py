from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai 
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key=os.getenv("OPNEAI_API_KEY")

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

multi_ai_agent= Agent(
    team=[web_serach_agent,finacial_agent],
    instructions=["Always include sources ","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summerize analyst recommendation and share the latest news for the Tata Steel",stream=True)


