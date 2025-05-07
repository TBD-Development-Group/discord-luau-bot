import re

def beautify_lua(code: str) -> str:
    # Fix basic things like no semicolons, spacing, etc.
    code = re.sub(r';', '', code)
    code = re.sub(r'\s*([=+-/*<>])\s*', r' \1 ', code)
    code = re.sub(r'\s+', ' ', code)
    code = re.sub(r'end', '\nend\n', code)
    code = re.sub(r'then', ' then\n', code)
    return code.strip()
