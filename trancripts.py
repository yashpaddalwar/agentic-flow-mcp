# import re
# from mcp.server.fastmcp import FastMCP
# from youtube_transcript_api import YouTubeTranscriptApi

# mcp = FastMCP("youtube_transcript")

# @mcp.tool()
# def get_youtube_transcript(url: str) -> dict:
#     """Fetches transcript from a given YouTube URL."""
#     video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
#     if not video_id_match:
#         return {"error": "Invalid YouTube URL"}

#     video_id = video_id_match.group(1)

#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript_text = "\n".join([entry["text"] for entry in transcript])
#         return {"transcript": transcript_text}
#     except Exception as e:
#         return {"error": str(e)}

# if __name__ == "__main__":
#     mcp.run(transport="stdio")

# from youtube_transcript_api import YouTubeTranscriptApi
# video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
# if not video_id_match:
#     return {"error": "Invalid YouTube URL"}

# video_id = video_id_match.group(1)

# try:
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     transcript_text = "\n".join([entry["text"] for entry in transcript])
#     # return {"transcript": transcript_text}
#     print(transcript_text)
# except Exception as e:
#     # return {"error": str(e)}
#     print

from duckduckgo_search import DDGS

def search_duckduckgo(query: str, max_results=5) -> str:
    """Search DuckDuckGo for a query and return results."""
    results_final = ""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        for i, result in enumerate(results, 1):
            results_final += f"{i}. {result['title']}\n{result['href']}\n{result['body']}\n"
    return results_final

print(search_duckduckgo("is manmohan singh alive", max_results=3))