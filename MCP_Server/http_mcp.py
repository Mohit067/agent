from fastmcp import FastMCP
from litellm import completion

mcp = FastMCP("MyServer")

@mcp.tool
def summarize_text(text: str):
    """
    summarize_text takes a string input and generates a concise summary in three lines.
    It uses a language model to process the input text and produce a summary.
    """
    # prompt = f"Summarize this in 3 lines:\n{text}"

    response = completion(
        model="groq/openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
              "content": "You are a TEXT SUMMARIZER, you will get a text as an input and you have to summarize that peice of text."
            },
            {
                "role": "user",
                "content": f"SUMMARIZE THIS in three lines: {text}"
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Start an HTTP server on port 8000
    mcp.run(transport="http", host="127.0.0.1", port=8002)