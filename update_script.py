import json
import os

def main():
    if not os.path.exists('payload.json'):
        return
        
    with open('payload.json', 'r', encoding='utf-8') as f:
        payload = json.load(f)
    
    action = payload.get('action')
    content = payload.get('data')

    # 逻辑：如果是更新代码，我们将内容追加到一个专门的更新日志中，
    # 或者你可以修改路径直接指向 src/app 里的某个组件
    if action == "update_code":
        update_path = "public/update_log.txt"
        os.makedirs(os.path.dirname(update_path), exist_ok=True)
        with open(update_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- New Update ---\n{content}\n")
        print(f"Successfully updated {update_path}")

if __name__ == "__main__":
    main()
