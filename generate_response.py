import re
from ollama_integration import run_ollama
from execute_sql import execute_sql_query

def extract_sql_from_response(response):
    """
    Extract the SQL query from the LLaMA model's response using regex.
    """
    try:
        sql_match = re.search(r"(SELECT|INSERT|UPDATE|DELETE)[\s\S]*?;", response, re.IGNORECASE)
        if sql_match:
            return sql_match.group(0).strip()
        return None
    except Exception as e:
        print("Error during SQL extraction:", e)
        return None

def generate_response(user_input):
    # Refine prompt for SQL-only generation
    sql_prompt = f"Generate only a valid SQL query for this request: {user_input}"
    generated_response = run_ollama(sql_prompt)

    if generated_response:
        print("LLaMA Response:", generated_response)

        # Extract SQL query
        generated_sql = extract_sql_from_response(generated_response)
        if not generated_sql:
            return "Failed to extract SQL query from the response."

        print("Generated SQL Query:", generated_sql)

        # Execute the extracted SQL query
        result = execute_sql_query(generated_sql)
        if result:
            return result
        else:
            return "Failed to execute the SQL query. Please check the database or query."
    else:
        return "Failed to generate SQL query. Please try again."