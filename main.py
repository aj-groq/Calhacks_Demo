#!/usr/bin/env python3
import os, json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
hackathon = input("🏆 Enter hackathon: ")

stream = client.chat.completions.create(
    model="compound-beta",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that searches for information about hackathon winning projects to give ideas for a hackathon project. Provide a list of projects with their names, descriptions, and links to the projects while also providing a list of the technologies used in the projects."},
        {"role": "user", "content": f"Find winning projects from {hackathon}"}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.reasoning:
        print(chunk.choices[0].delta.reasoning, end='')
    
    if chunk.choices[0].delta.executed_tools:
        for tool in chunk.choices[0].delta.executed_tools:
            if tool.type == 'search' and tool.search_results:
                query = json.loads(tool.arguments).get('query', '')
                print(f"\n🔍 {query}")
                for i, r in enumerate(tool.search_results.results[:2], 1):
                    print(f"{i}. {r.title}\n   {r.url}\n   {r.content[:100]}... \n   Score: {r.score:.3f}")
    
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='')

    # Check if this chunk contains usage information
    if chunk.x_groq:
        usage = chunk.x_groq.usage
        tokens_per_second = usage.completion_tokens / usage.completion_time
        print(f"\n⚡️ Tokens/s: {tokens_per_second:.2f}")