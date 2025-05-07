import re
from beautifier import beautify_lua

# Anti-beautify bypass header
BYPASS_HEADER = '''\
local newcclosure = newcclosure or function(a) return a end
local old_pcall = pcall
pcall = newcclosure(function(...)
    local results = {old_pcall(...)}
    local first = results[1]
    if type(first) == "boolean" and first == false then
        local second = results[2]
        if type(second) == "string" then
            results[2] = (second:gsub(":(%d+)([:\\r\\n])", ":1%2"))
        end
    end
    return unpack(results)
end)

'''

def modify_luau_script(content: str) -> str:
    # Beautify first
    content = beautify_lua(content)

    # Then inject warn at ~= #{} => %1[%2] = %3
    pattern = r"~=\s*#\{\}"
    matches = list(re.finditer(pattern, content))

    if not matches:
        return BYPASS_HEADER + content + "\n-- [!] No ~= #{} pattern found."

    for match in matches:
        start = match.end()
        eq_pattern = r"(%w+)%[(%w+)%]%s*=%s*(%w+)"
        eq_matches = list(re.finditer(eq_pattern, content[start:]))

        if eq_matches:
            last_match = eq_matches[-1]
            inject_index = start + last_match.end()
            varname = last_match.group(3)
            content = content[:inject_index] + f"\nwarn({varname})" + content[inject_index:]

    return BYPASS_HEADER + content
