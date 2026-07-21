import re

def parse_chat(text):
    pattern = re.compile(
        r'^\[(.*?)\]\s([^:]+):\s?(.*)$',
        re.MULTILINE
    )

    matches = list(pattern.finditer(text))
    messages = []

    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        extra = text[start:end].strip()

        msg = m.group(3).strip()

        # Detect WhatsApp reply
        if i > 0 and msg == messages[-1]["message"] and extra:
            msg = extra

        elif extra:
            msg += "\n" + extra

        messages.append({
            "time": m.group(1),
            "sender": m.group(2),
            "message": msg
        })

    return messages


