# Simulink AI Agent

## 1. Project Description

An AI agent that provides a natural language interface for interacting with Simulink models. <br>
The agent has access to tools that allow it to autonomously perform the following tasks:
- provide information about the installed Matlab application (such as version number, license number or installed packages)
- create a new (blank) Simulink model, with a specific name
- open an existing model
- add or delete a Simulink block from a model
- replace an existing block with a different block
- connect or disconnect two existing blocks
- run the simulation
- move a block in a certain direction (up, down, left, right), by a specific length (expressed in cm)
- provide information about an existing model (such as what blocks it has, and whether they are connected)
  
The agent is able to accept inputs in the form of both text and audio.

## 2. Setup Enviroment

### Requirements

- A [Mathworks account](https://www.mathworks.com/mwaccount/account/create), with Matlab ≥ R2023a, and the Simulink package <br>
  Instructions on how to download and install Matlab can be found at https://mathworks.com/help/install/ug/install-products-with-internet-connection.html <br>
  A free trial license for Matlab can be obtained from https://mathworks.com/campaigns/products/trials.html
- Python 3.8, 3.9, 3.10, 3.11, or 3.12 <br>
  The version of Python should match with the corresponding release of Matlab, according to this table https://mathworks.com/support/requirements/python-compatibility.html
- An [OpenAI account](https://auth.openai.com/create-account), with a valid [API key](https://platform.openai.com/settings/organization/api-keys)

### Installation Steps
**1. Clone the repository**
```
git clone https://github.com/catalin-hanga/simulink-AI-agent
cd simulink-AI-agent
```
**2. Install all dependencies**
```
pip install -r requirements.txt
```
By default, this command will install the latest version available of the Matlab Engine API for Python. If you do not have the latest release of Matlab, then you need to specify in the requirements.txt file a version of the Matlab engine that is compatible with your release. You can determine a compatible version of the Matlab engine by using the [PyPI page for Matlab Engine API for Python](https://pypi.org/project/matlabengine): From the Release history tab, review the Required MathWorks Products section for each MATLAB engine release. (More information about how to install the Matlab Engine API for Python can be found at https://mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

**3. Add API credentials** <br>
Create an .env file, and provide your OpenAI API key as an enviroment variable
```
OPENAI_API_KEY=sk-...
```
(This is required for the multi-modal GPT-4o mini LLM, as well as for the speech-to-text Whisper model)

## 3. Quick Start

### As a Streamlit application
```
streamlit run main.py
```

### As an app from the command line
```
python app.py
```

## 4. Questions and Bugs
To report a potential bug, or to request a new feature, please open an issue.

## 5. License 
This code repository is licensed under the MIT License.
