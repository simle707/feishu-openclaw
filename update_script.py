import json
import os
import sys

def main():
    # 1. 确认文件是否存在
    if not os.path.exists('payload.json'):
        print("❌ 错误：找不到 payload.json 文件")
        return

    with open('payload.json', 'r', encoding='utf-8') as f:
        try:
            payload = json.load(f)
            # 打印收到的所有数据，方便在 Actions 日志里查看
            print(f"DEBUG: 收到 payload 数据 -> {payload}")
        except Exception as e:
            print(f"❌ 错误：JSON 解析失败 -> {e}")
            return

    # 2. 提取变量（注意 Key 必须和 Dify JSON 里的 key 完全一致）
    action = payload.get('action')
    content = payload.get('data')

    print(f"DEBUG: 解析出的 action -> {action}")
    print(f"DEBUG: 解析出的 content -> {content}")

    # 3. 执行写入逻辑（去掉 if 判断，强行写入一个 debug 文件测试）
    debug_path = "action_debug.txt"
    with open(debug_path, "w", encoding="utf-8") as f:
        f.write(f"Action: {action}\nContent: {content}")
    print(f"✅ 已强行创建测试文件: {debug_path}")

    # 4. 原有的业务逻辑
    if action == "update_code":
        log_path = "public/update_log.txt"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- New Update ---\n{content}\n")
        print(f"✅ 成功追加内容到: {log_path}")
    else:
        print(f"⚠️ 跳过写入：action 匹配失败（收到的 action 是 '{action}'，预期是 'update_code'）")

if __name__ == "__main__":
    main()
