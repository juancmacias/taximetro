# Pasar de audio a texto con la librería SpeechRecognition
 
import speech_recognition
 
# Inicializar el reconocedor de voz, Recognizer
UserVoiceRecognizer = speech_recognition.Recognizer()
#print("\033[2J\033[1;1f")
# siempre escuchando
def escuchar():
    while (1):
        try:
            # El micrófono del usuario se utiliza como fuente de entrada de voz.
            with speech_recognition.Microphone() as UserVoiceInputSource:
                UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
                # Esperando a que el usuario hable
                UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
                # Convertir la entrada de voz del usuario en texto
                # El idioma se establece en español
                UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput, language='es-ES', show_all=False)
                # Convertir el texto a minúsculas
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
                # Imprimir el texto convertido
                #print(UserVoiceInput_converted_to_Text)
                return UserVoiceInput_converted_to_Text
        except KeyboardInterrupt:
            print('El programa se cerró por el usuario')
            exit(0)
        
        except speech_recognition.UnknownValueError:
            print("No se ha entendido lo que has dicho")