import json
from pathlib import Path

# Method 1: Using json.load() with file object
def read_json_method1(file_path: str) -> dict:
    """Read JSON file using json.load() with file object"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# Method 2: Using json.loads() with file.read()
def read_json_method2(file_path: str) -> dict:
    """Read JSON file using json.loads() with file.read()"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        data = json.loads(content)
    return data


# Method 3: Using pathlib (modern Python approach)
def read_json_method3(file_path: str) -> dict:
    """Read JSON file using pathlib"""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_json(file_path: str, data: dict | list, indent: int = 2, ensure_ascii: bool = False) -> bool:
    """Write data to a JSON file. Creates the file if it doesn't exist.
    
    Args:
        file_path: Path to the JSON file
        data: Dictionary or list to write as JSON
        indent: Number of spaces for indentation (default: 2)
        ensure_ascii: If True, escape non-ASCII characters (default: False)
        
    Returns:
        True if successful, False otherwise
        
    Raises:
        TypeError: If data is not JSON serializable
        OSError: If file cannot be written
    """
    try:
        path = Path(file_path)
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
        return True
    except (TypeError, OSError) as e:
        print(f"Error writing JSON file: {e}")
        return False


def overwrite_json(file_path: str, data: dict | list, indent: int = 2, ensure_ascii: bool = False) -> bool:
    """Overwrite an existing JSON file with new data.
    
    Args:
        file_path: Path to the JSON file
        data: Dictionary or list to write as JSON
        indent: Number of spaces for indentation (default: 2)
        ensure_ascii: If True, escape non-ASCII characters (default: False)
        
    Returns:
        True if successful, False if file doesn't exist or write failed
        
    Raises:
        TypeError: If data is not JSON serializable
        OSError: If file cannot be written
    """
    path = Path(file_path)
    if not path.exists():
        print(f"File '{file_path}' does not exist. Use write_json() to create a new file.")
        return False
    
    try:
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
        return True
    except (TypeError, OSError) as e:
        print(f"Error overwriting JSON file: {e}")
        return False 

# Example usage
if __name__ == "__main__":
    # Path to the sample JSON file
    json_file = "sample.json"
    
    # Method 1: Recommended approach
    print("=== Method 1: json.load() ===")
    data1 = read_json_method1(json_file)
    print(f"Total questions: {data1['metadata']['total_questions']}")
    print(f"First question: {data1['interview_questions'][0]['question']}")
    print()
    
    # Method 2: Alternative approach
    print("=== Method 2: json.loads() ===")
    data2 = read_json_method2(json_file)
    print(f"Categories: {', '.join(data2['metadata']['categories'])}")
    print()
    
    # Method 3: Using pathlib
    print("=== Method 3: pathlib ===")
    data3 = read_json_method3(json_file)
    print(f"Difficulty levels: {', '.join(data3['metadata']['difficulty_levels'])}")
    print()
    
    # Accessing nested data
    print("=== All Questions ===")
    for question in data1['interview_questions']:
        print(f"Q{question['id']}: {question['question']} ({question['category']} - {question['difficulty']})")
    
    # Writing JSON back to file (example)
    print("\n=== Writing JSON ===")
    output_data = {
        "message": "This is a sample output",
        "timestamp": "2024-01-01T12:00:00"
    }
    
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
    print("Written to output.json")
