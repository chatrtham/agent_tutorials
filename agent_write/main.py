import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from dotenv import load_dotenv
from graph import create_workflow

# Load environment variables from .env file
load_dotenv()


# Create the workflow
app = create_workflow(LLM)

# test instruction
# test_instruction = "Write a 5000 words, current and up to date 100% unique guide for my intermittent fasting for women over 50 cookbook on \u201cSnacks\u201d with humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively."
title = title = input("Enter the title: ")
test_instruction = f"""เขียนบทความยาว SEO เรื่อง \"{title}\"
    """


# Run the workflow
inputs = {"initial_prompt": test_instruction,  
          "num_steps": 0,
          "llm_name": title}
output = app.invoke(inputs)

print(output['final_doc'])