import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.key_manager  import disable_key, delete_key
from src.user_manager import delete_user

def process_items(items, action, object_type, max_threads=10):
    """Process keys or users concurrently."""
    results = []
    with ThreadPoolExecutor(max_threads) as executor:
        if object_type == "key":
            if action == "disable":
                futures = {executor.submit(disable_key, item): item for item in items}
            elif action == "delete":
                futures = {executor.submit(delete_key, item): item for item in items}
        elif object_type == "user" and action == "delete":
            futures = {executor.submit(delete_user, item): item for item in items}
        else:
            raise ValueError(f"Unsupported object and action: {object_type}, {action}")
        
        for future in as_completed(futures):
            results.append(future.result())
    return results

def main():
    parser = argparse.ArgumentParser(description="Manage AWS access keys and users.")
    parser.add_argument("--object", type=str, required=True, choices=["key", "user"], help="The object to manage (key or user).")
    parser.add_argument("--action", type=str, required=True, choices=["disable", "delete"], help="The action to perform (disable or delete).")
    parser.add_argument("--file", type=str, required=True, help="Path to the file containing access keys or usernames (newline-separated).")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use for processing.")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, "r") as file:
            items = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        return
    
    try:
        results = process_items(items, args.action, args.object, max_threads=args.threads)
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
