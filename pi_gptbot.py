from voice_module import speak, listen
from ai_module import ask_gpt
from camera_module import capture_frame, show_frame
from face_module import train_faces, recognize_face
import cv2

def main():
    speak("Hello! PiGPTBot is ready.")

    # Train faces once at startup
    label_map = train_faces()

    while True:
        speak("Say something:")
        command = listen().lower()

        if command in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        elif "who is here" in command or "recognize face" in command:
            frame = capture_frame()
            show_frame(frame)
            results = recognize_face(frame, label_map)
            if results:
                for name, confidence, (x, y, w, h) in results:
                    if confidence:
                        speak(f"I see {name} with {int(confidence)} confidence")
                    else:
                        speak("I see an unknown person")
            else:
                speak("No faces detected.")
        else:
            # Use GPT for general questions
            answer = ask_gpt(command)
            print("GPT:", answer)
            speak(answer)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
