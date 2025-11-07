from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def openai_filter(diff_stream: list[str]) -> bool:
    prompt = f"""
    Consider this list of git diffs between an HTML page at two different points in time. Are the differences significant enough to qualify as a divergence? 
    
    Return 'true' if it qualifies as a divergence, 'false' otherwise. Don't return anything else.
    
    
    {diff_stream}
    
    """

    # print(prompt)

    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text.lower() == "true".lower()
