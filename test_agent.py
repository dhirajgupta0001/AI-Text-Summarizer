from agent import agent

text = """
Artificial intelligence is changing how businesses operate.
Companies use AI to automate repetitive tasks, analyze large
datasets, improve customer service, and support decision-making.
However, successful adoption requires data quality, employee
training, security, and careful implementation.
"""

response=agent.invoke({
  "messages":[
    {
      "role":"user",
      "content":f"""
      Summarize the following text in a short paragraph:

      {text}
      """
    }
  ]
})
print(response["messages"][-1].content)
