# import os
# import asyncio
# from google.adk.sessions import InMemorySessionService
# from google.adk.runners import Runner
# from google.adk.agents import LlmAgent  # Correct import for LLM agent
# from google.adk.models.lite_llm import LiteLlm  # For Ollama integration
# from google.genai import types  # For creating message Content/Parts

# # --- Constants ---
# APP_NAME = "my_ollama_adk_app"
# USER_ID = "user_dev_1"
# SESSION_ID = "session_main_1"

# # --- Agent Definition ---
# root_agent = LlmAgent(
#     name="my_ollama_agent",
#     model=LiteLlm(model="ollama/llama3.1"),  # Local Ollama model
#     description="A basic assistant powered by a local Llama 3.1 model.",
#     instruction="You are a friendly and helpful assistant. Answer user questions clearly and concisely based on your knowledge."
# )

# print(f"Agent '{root_agent.name}' defined with Ollama's llama3.1 model.")

# # --- Session and Runner Setup ---
# session_service = InMemorySessionService()
# print("Session Service created.")

# session = session_service.create_session(
#     app_name=APP_NAME,
#     user_id=USER_ID,
#     session_id=SESSION_ID
# )
# print(f"Session '{SESSION_ID}' created.")

# runner = Runner(
#     agent=root_agent,
#     app_name=APP_NAME,
#     session_service=session_service
# )
# print(f"Runner created for agent '{root_agent.name}'.")

# # --- Interaction Logic ---
# async def run_conversation():
#     """Runs an interactive loop to chat with the agent."""
#     print("\n--- Starting Conversation (type 'quit' to exit) ---")
#     while True:
#         try:
#             user_query = input("You: ")
#             if user_query.lower() == 'quit':
#                 print("Exiting conversation.")
#                 break

#             # Prepare the user message in ADK format
#             content = types.Content(role='user', parts=[types.Part(text=user_query)])

#             final_response_text = "Agent did not produce a final response."

#             # Use run_async to process the message and get events
#             async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
#                 if event.is_final_response():
#                     if event.content and event.content.parts:
#                         final_response_text = event.content.parts[0].text
#                     break

#             print(f"Agent: {final_response_text}")

#         except Exception as e:
#             print(f"An error occurred: {e}")

# # --- Run the Application ---
# if __name__ == "__main__":
#     # Check dependencies
#     try:
#         import litellm
#     except ImportError:
#         print("Error: Missing litellm. Please run:")
#         print("pip install litellm")
#         exit()

#     # Ensure Ollama is running
#     try:
#         import subprocess
#         subprocess.run(["ollama", "list"], check=True, capture_output=True)
#     except subprocess.CalledProcessError:
#         print("Error: Ollama not running or llama3.1 not installed. Run:")
#         print("ollama serve")
#         print("ollama pull llama3.1")
#         exit()

#     # Run the async conversation loop
#     try:
#         asyncio.run(run_conversation())
#     except RuntimeError as e:
#         if "cannot be called from a running event loop" in str(e):
#             print("\nCannot start a new event loop. If in a Jupyter Notebook, run:")
#             print("await run_conversation()")
#         else:
#             raise e
        
#============================================================================

# from google.adk.models.lite_llm import LiteLlm 
# from google.adk.agents import LlmAgent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService

# APP_NAME = "my_ollama_adk_app"
# USER_ID = "user_dev_1"
# SESSION_ID = "session_main_1"

# session_service = InMemorySessionService()

# root_agent = LlmAgent(
#     name="my_ollama_agent",
#     model=LiteLlm(model="ollama/llama3.1"),  # Local Ollama model
#     description="A basic assistant powered by a local Llama 3.1 model.",
#     instruction="You are a friendly and helpful assistant. Answer user questions clearly and concisely based on your knowledge."
# )

# session = session_service.create_session(
#     app_name=APP_NAME,
#     user_id=USER_ID,
#     session_id=SESSION_ID
# )

# runner = Runner(
#     agent=root_agent,
#     app_name=APP_NAME,
#     session_service=session_service
# )


#============

# adk/agent.py
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
root_agent = LlmAgent(
    name="my_ollama_agent",
    model=LiteLlm(model="ollama/llama3.1"),
    instruction="You are a friendly assistant. Answer clearly and use session history if relevant.",
    description="A basic Ollama-based agent."
)