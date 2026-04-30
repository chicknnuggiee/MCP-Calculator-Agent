# MCP Calculator Agent

This project is a simple Python-based MCP Agent that demonstrates how an AI application can connect to external tools through an MCP server.

The MCP server exposes basic calculator tools that can be called by an MCP client or tested through the MCP Inspector.

## Project Overview

MCP stands for Model Context Protocol. It allows AI agents to use external tools in a structured way.

In this project, the MCP server provides calculator functions as tools. These tools allow the agent to perform basic math operations instead of only responding with text.

## Tools Included

The server provides the following MCP tools:

- `add_numbers(a, b)` — adds two numbers
- `subtract_numbers(a, b)` — subtracts the second number from the first
- `multiply_numbers(a, b)` — multiplies two numbers
- `divide_numbers(a, b)` — divides the first number by the second

## Project Files

```text
MCP-Calculator-Agent/
│
├── server.py
├── requirements.txt
├── README.md
└── .gitignore