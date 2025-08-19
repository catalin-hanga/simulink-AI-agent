# Simulink AI Agent 🤖

## Project Description

An AI agent that provides a conversational interface for interacting with Simulink models through natural language. <br>
The agent has access to a list of tools, that allows it to autonomously perform any combination of the following tasks:
- provide information about the installed Matlab application (such as version number, license number or installed packages)
- create a new (blank) Simulink model, with a given name
- open or close an existing model
- add or delete a specific Simulink block from a model
- replace a certain block with a different one
- connect or disconnect two blocks
- run the simulation
- move a block in a certain direction (up, down, left, right), by a given length (expressed in cm)
- provide information about an existing model (such as what blocks it has, and whether they are connected)
  
The agent is able to accept user inputs in the form of both text and audio. <br>
It can be run locally, in one of three different ways:
1. with Claude Desktop, using a Model Context Protocol (MCP) server
2. in the browser, as a Streamlit application
3. from the command line

## Pre-requisites and Requirements

- A [Mathworks account](https://www.mathworks.com/mwaccount/account/create), with Matlab ≥ R2023a, and the Simulink package <br>
  Instructions on how to download and install Matlab can be found at https://mathworks.com/help/install/ug/install-products-with-internet-connection.html <br>
  A free trial license for Matlab can be obtained from https://mathworks.com/campaigns/products/trials.html
- Python 3.8, 3.9, 3.10, 3.11 or 3.12
> [!NOTE]
The version of Python should match with the corresponding release of Matlab, according to this [table](https://mathworks.com/support/requirements/python-compatibility.html).
- The [Matlab Engine API for Python](https://ch.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html)
> [!NOTE]
By default, Python will install the latest version available. If you do not have the latest release of Matlab, then you need to specify in the ```requirements.txt``` file a version of the Matlab engine that is compatible with your release. You can determine a compatible version of the Matlab engine by using the [PyPI page for Matlab Engine API for Python](https://pypi.org/project/matlabengine): from the Release history tab, review the Required MathWorks Products section for each Matlab Engine release. (More information about how to install the Matlab Engine API can be found [here](https://mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)).

## Option 1: MCP server

### Installation Steps
Clone the repository
```
git clone https://github.com/catalin-hanga/simulink-AI-agent
cd simulink-AI-agent
```
Install the ```uv``` library
```
pip install uv
```
Create a new directory for this project, and initiate it
```
uv init mcp-project --python 3.12
```
Copy the relevant files to this project folder
```
cp mcp_server.py mcp-project\main.py
cp functions.bin, functions.py mcp-project
cd mcp-project
```
Create a virtual environment, and activate it
```
uv venv
.venv\Scripts\activate
```
Install dependencies
```
uv add "mcp[cli]" matlabengine dill numpy
```
Download and install [Claude Desktop](https://claude.ai/download). <br>
Open Claude Desktop, go to File -> Settings -> Developer -> Edit Config. <br>
Open the ```claude_desktop_config.json``` file, and add the details of the MCP server:
```
{
  "mcpServers": {
    "simulang": {
      "command": "C:\\absolute\\path\\to\\executable\\uv",
      "args": [
        "--directory",
        "C:\\absolute\\path\\to\\folder\\simulink-AI-agent\\mcp-project",
        "run",
        "main.py"
      ]
    }
  }
}
```
Finally, restart the operating system.

### Quick Start
Open Claude Desktop, and check the ```Search and tools``` section, to see if the MCP server is running properly, and has all the 12 tools available.

<img width="865" height="521" alt="mcp" src="https://github.com/user-attachments/assets/af3beb3a-7886-433e-91f6-c22020f0f111" />

### Short Demo


## Option 2: Streamlit app

### Installation Steps
Clone the repository
```
git clone https://github.com/catalin-hanga/simulink-AI-agent
cd simulink-AI-agent
```
Install dependencies
```
pip install -r requirements.txt
```
Create an [OpenAI account](https://auth.openai.com/create-account), with a valid [API key](https://platform.openai.com/settings/organization/api-keys). <br>
Create an .env file, and provide your OpenAI API key as an enviroment variable:
```
OPENAI_API_KEY=sk-...
```
(This is required for a multi-modal LLM, such as GPT-4o mini, as well as for the speech-to-text Whisper model).

### Quick Start
From the command line, run:
```
streamlit run main.py
```
The app can be accessed in the browser at http://localhost:8501/. <br>
(Ideally, the broswer should be placed on the right half side of the screen, like in the demo).

### Short Demo
https://github.com/user-attachments/assets/39ec886e-4a73-4c51-8b3b-a49391e18abf

## Option 3: Command line

### Installation Steps
Same as the above, in Option 2.

### Quick Start
From the command line, run:
```
python app.py
```

### Short Demo



## Questions and Bugs
To report a potential bug, or to request a new feature, please open an issue.

## License 
This code repository is licensed under the MIT License.
