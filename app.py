from generate_response import generate_response

def main():
    print("Welcome to the RAG-based Text-to-SQL Application!")
    while True:
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_query)
        print("Response:", response)

if __name__ == "__main__":
    main()