import sys
sys.path.append('objection_engine/')
# You can also import the components like this
from objection_engine import anim
from objection_engine.beans.comment import Comment
from objection_engine.beans.comment_bridge import CommentBridge
from objection_engine.constants import Character
import re
import random
from collections import Counter
from typing import Dict

# mock objects required for library
class MockCharacter:
    def __init__(self, name):
        self.name = name

class MockComment:
    def __init__(self, username: str, text: str, score: int = 0):
        self.author = MockCharacter(username)
        self.body = text
        self.score = score

# if they have a sprite, use it!
all_characters = [
        Character.PHOENIX,
        Character.EDGEWORTH,
        Character.GODOT,
        Character.FRANZISKA,
        Character.JUDGE,
        Character.LARRY,
        Character.MAYA,
        Character.KARMA,
        Character.PAYNE,
        Character.MAGGEY,
        Character.PEARL,
        Character.LOTTA,
        Character.GUMSHOE,
        Character.GROSSBERG,
    ]
# use a smaller selection for non-important chars.
side_characters = [
        Character.LARRY,
        Character.MAYA,
        Character.PAYNE,
        Character.MAGGEY,
        Character.PEARL,
        Character.LOTTA,
        Character.GUMSHOE,
        Character.GROSSBERG,
    ]
used_chars = {}
def get_char(character: str) -> str:
    if character in used_chars:
        return used_chars[character]
    for char in all_characters:
        if char.lower() == character.lower():
            used_chars[character] = char
            return char
    char = random.choice([char for char in side_characters if char not in used_chars])
    used_chars[character] = char
    return char


def generate_from_text(text, output_video):
    # load text and work it out
    lines = text.split('\n')

    char_pat = re.compile(r'^[a-zA-Z\?]*:?\s*$')
    # construct comments
    comments = []
    used_chars = {}
    current_comment = ''
    current_character = ''
    score = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if char_pat.match(line):
            if current_comment:
                comments.append(Comment(text_content=current_comment, user_name=current_character, score=score))
                comments[-1].character = get_char(current_character)
                score = 0
            current_character = line.split(':')[0]
            current_comment = ''
        elif line.lower() == 'objection!':
            # an objection! flush the previous comment, since the next line needs to start with an objection
            if current_comment:
                comments.append(Comment(text_content=current_comment, user_name=current_character, score=score))
                comments[-1].character = get_char(current_character)
                current_comment = ''
            # append the current line with objection tag.
            score = 1
        else:
            current_comment += line
    if current_character and current_comment:
        comments.append(Comment(text_content=current_comment, user_name=current_character, score=score))
        comments[-1].character = get_char(current_character)

    # selecting character
    thread = []
    for comment in comments:
        thread.append(CommentBridge(comment))

    anim.comments_to_scene(thread, name_music = 'PWR', output_filename=output_video)

if __name__ == '__main__':
    generate_from_text(open('test_data.txt', 'r').read(), 'hello.mp4')