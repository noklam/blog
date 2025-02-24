---
badges: true
categories:
- llm

date: '2025-02-05'
description: ''
hide: false
title: 'Day 1 into LLMs'
toc: true
---


# What's the Model Context Protocol(MCP)?
Model Context Protocol is a bit like the Language Server Protocol (LSP) that I have worked with recently. In simplified words, it's a set of specification that defines how a server communicate to a client. A server can be a web server, and a client could be a Desktop application for example.

The benefit of having protocols is that you can reuse the majority of the code to avoid the M*N integration problem (M server, N client). Essentially, you build the server once, then build up a thin client (think VSCode, Claude Desktop, Cursor).

I have been very hesitate towards the LLM wave, partly because of my prior experience (moving from ML to software engineering). However, I think the application space is now mature enough to actually build something with it. There are so many fuss around LLM/Agents or what so ever, but (surprisingly), the most effective way to learn this is sit down for a few hours and actually build something with it.


# Obisidian
I have been an user of Obsidian, a markdown based editor. I was never a good note taker or religous about cleaning up my notes, so I write a lot of them but I barely spend time to organise them. So, when I think of learning this MCP thing, I ask myself, can I build something that query my own notes?

This would takes:
- Building a MCP server for obsidian
- A MCP client / plugin for Obsidian (If it does not exist yet, I have no idea now)


# Reference
- https://docs.anthropic.com/en/docs/build-with-claude/mcp