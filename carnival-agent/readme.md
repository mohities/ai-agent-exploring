# Create virtual environment on mac
python3 -m venv venv ( for mac or python3 -m venv venv)
source venv/bin/activate  
# On Windows: venv\Scripts\activate

# install necessary packages
pip install openai python-dotenv

#  Create project structure
mkdir -p src/agent src/tools tests


# Create the environment file with -  .env extension

# Run the query in interactive mode
python3 -c "from src.agent.carnival_agent import CarnivalAgent; a = CarnivalAgent(); a.start_conversation()" (Use python3 on mac)
