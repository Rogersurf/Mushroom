import sys
from pathlib import Path

# Append the path to the Mushroom directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from Db import db_user_content
from recommendations import get_recommendations

BASE_PATH = Path("./Data/Models")

def test_recommendations():
    # Load the models
    le_username, _, reduced_matrix = db_user_content.load_models()

    # Sample usernames for testing
    test_usernames = ['user1', 'user2', 'user3', 'user_not_in_data']

    for username in test_usernames:
        print(f"Getting recommendations for {username}")
        recommendations = get_recommendations(username, le_username, reduced_matrix)
        print("Recommended items:", recommendations)
        print("-----")

# Call the test function
if __name__ == "__main__":
    test_recommendations()