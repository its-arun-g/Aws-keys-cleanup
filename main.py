import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from src.key_manager import disable_key, delete_key
from src.user_manager import delete_user


def process_items(items, action, object_type, profile, max_threads=10):
    """Process keys or users concurrently."""
    with ThreadPoolExecutor(max_threads) as executor:
        if object_type == "key":
            if action == "disable":
                futures = {
                    executor.submit(disable_key, profile, item): item for item in items
                }
            elif action == "delete":
                futures = {
                    executor.submit(delete_key, profile, item): item for item in items
                }
        elif object_type == "user" and action == "delete":
            futures = {
                executor.submit(delete_user, profile, item): item for item in items
            }
        else:
            raise ValueError(f"Unsupported object and action: {object_type}, {action}")

        for future in as_completed(futures):
            future.result()


def main():
    parser = argparse.ArgumentParser(description="Manage AWS access keys and users.")
    parser.add_argument(
        "--object",
        type=str,
        required=True,
        choices=["key", "user"],
        help="The object to manage (key or user).",
    )
    parser.add_argument(
        "--action",
        type=str,
        required=True,
        choices=["disable", "delete"],
        help="The action to perform (disable or delete).",
    )
    parser.add_argument(
        "--files-path",
        type=str,
        required=True,
        help="Path to the files containing access keys or usernames (newline-separated) with filename as account ID",
    )
    parser.add_argument(
        "--profile-name",
        type=str,
        required=True,
        help="Profile name existing in all accounts to be used for deletion",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=1,
        help="Number of threads to use for processing.",
    )

    args = parser.parse_args()

    for root, _, files in os.walk(args.files_path):
        for acc_file in files:
            items = []
            try:
                with open(os.path.join(root, acc_file), "r") as file:
                    items = [line.strip() for line in file if line.strip()]
            except FileNotFoundError:
                print(f"Error: File '{args.file}' not found.")
                return

            try:
                process_items(
                    items,
                    args.action,
                    args.object,
                    f"{acc_file.split('.')[0]}:{args.profile_name}",
                    max_threads=args.threads,
                )
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
