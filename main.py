#!/usr/bin/env python
import openai
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from crews.hotel_manager.hotel_manager import hotel_manager
from openai import OpenAI
from pydub import AudioSegment
from pydub.utils import make_chunks




import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class Transcript(BaseModel):
    transcript: str = ""


class audio_transcriber(Flow[Transcript]):

    @start()
    def transcrbing_audio(self):
        print("Audio: ")
        path = "C:\\Users\\mpooj\\OneDrive\\Desktop\\gen_ai\\hotel_management\\src\\hotel_management\\crews\\hotel_manager\\output.mp3"

        #If Audio file less than 25 MB use the below code
        with open(path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"  # Options: "text", "verbose_json", "srt"
        )

        self.transcript = transcription
        print(f"Transcription: {self.transcript}")

        #If audio file is more than 25MB use the below code
        """
        chunk_length_ms = 60000
        chunks = make_chunks(audio, chunk_length_ms)
        
        
        full_transcribe = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.mp3"
            chunk.export(chunk_path, format="mp3")
            
            with open(chunk_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                   model = "whisper-1",
                   file = audio_file 
                )
                full_transcribe += transcription.text + " "
         
        self.state.transcript = full_transcribe
        print(f"Transcription: {self.state.transcript}")

        """
         

    @listen(transcrbing_audio)
    def input_transcribe(self):
        print("Input to the crew")
        
        result = (
            hotel_manager()
            .crew()
            .kickoff(inputs={"transcript": self.transcript})
        )



def kickoff():
    audio = audio_transcriber()
    audio.kickoff()





if __name__ == "__main__":
    kickoff()
