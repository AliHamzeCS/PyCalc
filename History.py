import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, 'history.json')

def load_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            history = json.load(file)

        return history

    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE , 'w') as file :
        json.dump(history, file , indent=4)
        
def clear_history(history):
    history.clear()
    save_history(history)
    
def add_history(operation, result):
    history = load_history()
    
    history.append({
        "operation": operation,
        "result": result
    })
    
    save_history(history)
    
def view_history():
    history = load_history()

    if not history:
        print("History is empty.")
        return

    print("\n========== HISTORY ==========\n")

    for index, item in enumerate(history, start=1):
        print(f"{index}. {item['operation']} = {item['result']}")


