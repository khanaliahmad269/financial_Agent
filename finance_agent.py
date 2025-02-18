from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

## Web Search Agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
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
    instructions=["Format your response using markdown and use tables to display data where possible."  ],
    show_tools_calls=True,
    markdown=True,
)

multi_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources", "Use table to display the data","You are a financial analyst"],
    show_tools_calls=True,
    markdown=True,
)

multi_agent.print_response("who are you?", markdown=True)