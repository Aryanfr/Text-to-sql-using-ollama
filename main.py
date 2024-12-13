from ollama_integration import run_ollama_to_generate_sql
from execute_sql import execute_sql_query
from generate_response import generate_response

def main(user_prompt, database_path):
    print("Processing your query...")
    
    # Step 1: Generate SQL query using LLaMA
    sql_query = run_ollama_to_generate_sql(user_prompt)
    if not sql_query:
        print("Failed to generate a SQL query. Please try again.")
        return
    
    print(f"Generated SQL Query: {sql_query}")
    
    # Step 2: Execute SQL query on the database
    results = execute_sql_query(database_path, sql_query)
    if results is None:
        print("Failed to execute the SQL query. Please check the database or query.")
        return
    
    # Step 3: Format and display the results
    response = generate_response(results)
    print(response)