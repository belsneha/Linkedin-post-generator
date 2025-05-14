import json
import re
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException


def process_posts(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        enriched_posts = []
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, mode="w", encoding='utf-8') as outfile:
        json.dump(enriched_posts, outfile, indent=4)


def clean_and_load_json(raw_text):
    """
    Attempts to fix small JSON formatting issues (like a missing closing brace)
    and then loads it into a Python dict.
    """
    match = re.search(r'\{.*', raw_text, re.DOTALL)
    if not match:
        raise OutputParserException(f"Could not find JSON in output:\n{raw_text}")

    json_str = match.group(0).strip()

    # Fix unclosed JSON if needed
    open_braces = json_str.count('{')
    close_braces = json_str.count('}')
    if open_braces > close_braces:
        json_str += '}' * (open_braces - close_braces)

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise OutputParserException(f"Invalid JSON extracted:\n{json_str}") from e


def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish or Hindi (Hinglish means hindi + english)

    Only return a JSON object and nothing else.

    Here is the actual post on which you need to perform this task:  
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"post": post})
    raw_text = response.content.strip()

    return clean_and_load_json(raw_text)


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements:
    1. Tags are unified and merged to create a shorter list. 
       Example: "Jobseekers", "Job Hunting" -> "Job Search"
    2. Use title case for each unified tag (e.g., "Job Search")
    3. Output should be a JSON object with original tags mapped to unified tags. No explanation or preamble.

    Tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"tags": unique_tags_list})
    raw_text = response.content.strip()

    return clean_and_load_json(raw_text)


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
