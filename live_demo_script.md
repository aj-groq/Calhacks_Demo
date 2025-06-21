# 🏆 Hackathon Project Finder - Live Demo Script

## Overview
This Python application uses Groq's AI to search for winning hackathon projects, providing inspiration and insights for your next hackathon submission.

## Prerequisites
- Python 3.x installed
- Groq API key set as environment variable
- `groq` Python package installed

## Setup Instructions

### 1. Install Dependencies
```bash
pip install groq
```

### 2. Set Environment Variable
```bash
export GROQ_API_KEY="your-groq-api-key-here"
```

### 3. Run the Application
```bash
python3 main.py
```

## Demo Walkthrough

### Step 1: Launch Application
When you run the script, you'll see:
```
🏆 Enter hackathon: 
```

### Step 2: Enter Hackathon Name
Type the name of a hackathon you're interested in. Examples:
- `CalHacks`
- `HackMIT`
- `TechCrunch Disrupt`
- `AngelHack`

### Step 3: AI Processing & Search
The application will:
1. **Show reasoning process** - The AI's thought process as it plans the search
2. **Execute web searches** - You'll see search queries like:
   ```
   🔍 CalHacks winning projects 2024
   ```
3. **Display search results** - For each search, you'll see:
   ```
   1. Project Title
      https://project-url.com
      Brief description of the project...
      Score: 0.xxx
   ```

### Step 4: AI Analysis & Recommendations
The AI will provide:
- **Project summaries** with names and descriptions
- **Technology stacks** used in winning projects
- **Links** to project repositories or demos
- **Insights** about common patterns in winning projects

### Step 5: Performance Metrics
At the end, you'll see processing speed:
```
📊 Tokens/s: [speed metrics]
```

## Sample Output Structure

```
🏆 Enter hackathon: CalHacks

[AI reasoning about search strategy...]

🔍 CalHacks 2024 winning projects
1. EcoTrack - Sustainability Dashboard
   https://devpost.com/software/ecotrack
   An AI-powered platform that helps users track their carbon footprint...
   Score: 0.892

2. MindBridge - Mental Health Assistant  
   https://github.com/team/mindbridge
   A conversational AI that provides personalized mental health support...
   Score: 0.875

## Winning Projects from CalHacks 2024:

### 1. EcoTrack
- **Description**: Sustainability tracking platform with ML insights
- **Technologies**: React, Python, TensorFlow, Firebase
- **Link**: https://devpost.com/software/ecotrack

### 2. MindBridge
- **Description**: AI-powered mental health conversation companion
- **Technologies**: Node.js, OpenAI API, MongoDB, React Native
- **Link**: https://github.com/team/mindbridge

[Additional projects and analysis...]

📊 Tokens/s: 45.2
```

## Key Features

- 🔍 **Real-time web search** for hackathon projects
- 🤖 **AI-powered analysis** and summarization
- ⚡ **Streaming responses** for immediate feedback
- 📊 **Performance metrics** tracking
- 🔗 **Direct links** to project repositories and demos

## Tips for Best Results

1. **Be specific** with hackathon names (include year if known)
2. **Try variations** like "HackMIT 2024" vs "MIT Hackathon"
3. **Look for patterns** in winning technologies and approaches
4. **Follow the links** to explore full project details

## Troubleshooting

- **No results?** Try a more general hackathon name
- **API errors?** Check your GROQ_API_KEY environment variable
- **Slow responses?** This is normal for web search operations

---
*Ready to find your next hackathon inspiration? Run `python3 main.py` and start exploring!*
