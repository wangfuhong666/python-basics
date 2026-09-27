import unicodedata
import sys


def ultra_clean_pdf_text():
    print("=" * 50)
    print("📢 请粘贴文本（支持多行），完成后：")
    print("Windows: Enter -> Ctrl+Z -> Enter")
    print("Mac/Linux: Enter -> Ctrl+D")
    print("=" * 50)

    try:
        raw_text = sys.stdin.read()
    except EOFError:
        raw_text = ""

    if not raw_text:
        return

    # 1. 第一步：Unicode 规范化，解决 ABC 不相邻的问题
    # 这一步会将全角字符转为标准半角，但核心是后续的过滤
    normalized_text = unicodedata.normalize('NFKC', raw_text)

    clean_chars = []

    for char in normalized_text:
        # 获取该字符的 Unicode 分类
        cat = unicodedata.category(char)

        # 过滤策略：
        # Z*: 所有形式的分隔符（空格、全角空格、换行、行分隔等）
        # C*: 控制字符、格式控制字符、私有区域字符（PDF里的乱码通常在这里）
        # M*: 组合标记（音标、重音等，PDF合并时有时会多出来）
        if cat.startswith('Z') or cat.startswith('C') or cat.startswith('M'):
            continue

        # 额外的保险：移除 Private Use Area (私有保留区字符，如 )
        if '\uE000' <= char <= '\uF8FF':
            continue

        # 如果不是空白且不是乱码，才保留
        clean_chars.append(char)

    result = "".join(clean_chars)

    print("\n" + "=" * 20 + " 极致清洗后的结果 " + "=" * 20)
    print(result)
    print("=" * 50)
    print(f"处理完成！最终长度: {len(result)}")


if __name__ == "__main__":
    ultra_clean_pdf_text()
