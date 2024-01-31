from openai import OpenAI
import yaml

secrets = yaml.safe_load(open("secrets.yml"))
client = OpenAI(api_key=secrets["openai_api_key"])


def lecture_notes(transcription):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a student taking notes on a lecture transcript. Make your notes structured and helpful.",
            },
            {
                "role": "user",
                "content": str(transcription),
            },
        ],
        model="gpt-3.5-turbo-1106",
        max_tokens=4096,
    )
    return response.choices[0].message.content


def lecture_summarize(notes):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a student who is creating a paragraph summary for this week's lecture notes. Make your summary concise and informative.",
            },
            {
                "role": "user",
                "content": str("\n\n".join(notes)),
            },
        ],
        model="gpt-4-turbo-preview",
        max_tokens=4096,
    )
    return response.choices[0].message.content


def summarize(transcripts: list[str]) -> str:
    notes = []
    for t in transcripts:
        notes.append(lecture_notes(t))

    return lecture_summarize(notes)
