from pathlib import Path
import re
from re import Match
from typing import Callable


def transform_file_text(file_path, transform_function):
    p = Path(file_path)
    old_text = p.read_text()
    new_text = transform_function(old_text)
    p.write_text(new_text)

def replace_line_in_text(text, original_line, new_line):
    lines = text.splitlines()
    bad_line_number = next(i for i, line in enumerate(lines) if line == original_line)
    lines[bad_line_number] = new_line
    return "\n".join(lines)

def replace_line_in_file(file_path, original_line, new_line):
    transform_file_text(file_path, lambda t: replace_line_in_text(t, original_line, new_line))

def modify_regex_matches(regex: re.Pattern[str], text: str, transform: Callable[[Match[str]], str]) -> str:
    prev_match_end = 0
    prev_match: Match[str] | None = None
    modified_text = ""
    for match in regex.finditer(text):
        match_start = match.start(0)
        match_end = match.end(0)
        modified_text += text[prev_match_end: match_start]
        modified_text += transform(match)
        prev_match_end = match_end
    modified_text += text[prev_match_end:] # copy text from last matcher till end
    return modified_text
