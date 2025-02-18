import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import phi 
from phi.playground import Playground, serve_playground_app 

#load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## Web Search Agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources","You are a pyschologist and a financial analyst"],
    show_tools_calls=True,
    markdown=True,

)

#Finance Analyst Agent

finance_agent= Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
        company_info=True,income_statements=True,company_news=True),

    ],
    instructions=["Format your response using markdown and use tables to display data where possible.","You are a financial analyst and a pyschologist"  ],
    show_tools_calls=True,
    markdown=True,
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)