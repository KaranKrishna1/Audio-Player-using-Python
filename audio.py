import pygame
import time

def play_audio(file_path):
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        print(f"Playing audio: {file_path}")

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    audio_file = ""
    play_audio(audio_file)
