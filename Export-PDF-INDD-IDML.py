from pyautogui import *
import pyautogui
import keyboard
import time
import pygame

time.sleep(2)

error = False

# This script does:
# 1. Generate a pdf file with the previously used configuration
# 2. Generate a .indd file
# 3. Generate a .idml file

# Define function for key press
def press_key(keys):
    keyboard.press_and_release(keys)

def play_mp3(file_path):
    # Initialize Pygame
    pygame.init()

    # Load the MP3 file
    pygame.mixer.music.load(file_path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.quit()

def find_export_pdf_1():
    try:
        return pyautogui.locateOnScreen('imgs/export-pdf-1.png', grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f"Erro ao encontrar janela de exportar pdf do Windows: {e}")
        return False

def find_export_pdf_2():
    try:
        return pyautogui.locateOnScreen('imgs/export-pdf-2.png', grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f"Erro ao encontrar janela de exportar pdf do InDesign: {e}")
        return False

def find_save_as_idml():
    try:
        return pyautogui.locateOnScreen('imgs/save-as-idml-1.png', grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f"Erro ao encontrar janela de salvar idml do InDesign: {e}")
        return False

def find_missing_fonts_window():
    try:
        # Call print_middle to get the coordinates
        x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height = print_middle()

        return pyautogui.locateOnScreen('imgs/missing-fonts.png', region=(x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height), grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f'Janela "Missing fonts" não encontrada. {e}')
        return False

def find_missing_links_window():
    try:
        # Call print_middle to get the coordinates
        x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height = print_middle()

        return pyautogui.locateOnScreen('imgs/missing-links.png', region=(x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height), grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f'Janela "Missing links" não encontrada. {e}')
        return False

def find_replace_file_window():
    try:
        # Call print_middle to get the coordinates
        x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height = print_middle()

        return pyautogui.locateOnScreen('imgs/replace-file-window.png', region=(x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height), confidence=0.8) 
    except Exception as e:
        print(f"Erro ao encontrar janela de substituição de arquivo. {e}")
        return False

def find_new_file_button():
    try:
        # Call print_right to get the coordinates
        x_pixel_width, y_pixel_height = print_right()

        return pyautogui.locateOnScreen('imgs/new-file.png', region=(0, 0, x_pixel_width, y_pixel_height), confidence=0.8) 
    except Exception as e:
        print(f"find_new_file_button() {e}")
        return False  

def find_export_file():
    try:
        # Call print_left to get the coordinates
        x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height = print_left()

        return pyautogui.locateOnScreen('imgs/exporting.png', region=(x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height), grayscale=True, confidence=0.8) 
    except Exception as e:
        print(f"Continuando para o próximo passo. {e}")
        return False

def find_generating_pdf():
    try:
        return pyautogui.locateOnScreen('imgs/exporting-interactive.png', confidence=0.95) 
    except Exception as e:
        print(f"Continuando para o próximo passo. {e}")
        return False  

def print_middle():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Area of the screen in percentage
    x_start = 0.34
    y_start = 0
    x_finish = 0.66
    y_finish = 1

    # Transforming percentage in int value
    x_pixel_start = int(x_start * screen_width)
    y_pixel_start = int(y_start * screen_height)
    x_pixel_finish = int(x_finish * screen_width)
    y_pixel_finish = int(y_finish * screen_height)

    # Get the width and height of the print area
    x_pixel_width = x_pixel_finish - x_pixel_start
    y_pixel_height = y_pixel_finish - y_pixel_start

    return x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height

def print_right():
    # Doing this to cut the work of looking through the screen in half
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Area of the screen in percentage
    x_finish = 0.5
    y_finish = 1

    # Transforming percentage in int value
    x_pixel_width = int(x_finish * screen_width)
    y_pixel_height = int(y_finish * screen_height)

    return x_pixel_width, y_pixel_height

def print_left():
    # Doing this to cut the work of looking through the screen in half
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Area of the screen in percentage
    x_start = 0.5
    y_start = 0
    x_finish = 1
    y_finish = 1

    # Transforming percentage in int value
    x_pixel_start = int(x_start * screen_width)
    y_pixel_start = int(y_start * screen_height)
    x_pixel_finish = int(x_finish * screen_width)
    y_pixel_finish = int(y_finish * screen_height)

    # Get the width and height of the print area
    x_pixel_width = x_pixel_finish - x_pixel_start
    y_pixel_height = y_pixel_finish - y_pixel_start

    return x_pixel_start, y_pixel_start, x_pixel_width, y_pixel_height

# Get the screen width and height
screen_width, screen_height = pyautogui.size()
x_percentage = 0.04
y_percentage = 0.14

x_pixel = int(x_percentage * screen_width)
y_pixel = int(y_percentage * screen_height)

# Main loop, if Q is not pressed the loop continue
while keyboard.is_pressed('q') == False:
    if find_new_file_button() != False:
        print("Arquivos salvos.")
        play_mp3('sounds/among-us-task-complete.mp3')
        break
    # Press the keys Ctrl+0
    press_key('ctrl+0')

    # Wait a bit
    time.sleep(0.2)

    # Start exporting the pdf ---------------------------------------------------------------------------
    # Close any open window
    for _ in range(3):
        press_key('esc')

    # Press the keys Ctrl+E 
    press_key('ctrl+e')

    # Wait maximum of 15 sec for Ctrl+E to appear
    counter = 0
    while find_export_pdf_1() == False and counter < 16:
        # If Ctrl+E does not appear in 15 sec then close the program
        if counter == 15:
            print("Falha no ctrl+E, fechando o programa.")
            play_mp3('sounds/windows-xp-error-sound.mp3')
            break
        else:
            print("Falha no ctrl+E, tentando de novo. Fechando o programa em: ", 15 - counter)
            time.sleep(1)
            counter += 1

    # Check if the Ctrl+E is present
    if find_export_pdf_1() != False:
        # Press Enter on the windows export window
        press_key('enter')

        # Wait a bit
        time.sleep(0.4)
    else:
        print("Falha no ctrl+E, fechando o programa.")
        play_mp3('sounds/windows-xp-error-sound.mp3')
        break

    # Check if "want to replace file" windows appear
    if find_replace_file_window() != False:
        # Choose "yes" to replace
        print("Substituindo arquivo que já existe.")
        # Press Left Arrow key
        press_key('left')

        # Press Enter
        press_key('enter')
    else:
        print("Não foi encontrada a janela de confirmação de substituição de arquivo.")
    
    # Wait a bit
    time.sleep(0.2)

    # Wait 15 sec for InDesign export window to appear
    counter = 0
    while find_export_pdf_2() == False and counter < 16:
        # If InDesign export window does not appear in 5 sec then close the program
        if counter == 15:
            print("Falha na janela de exportação do InDesign. Fechando o programa.")
            play_mp3('sounds/windows-xp-error-sound.mp3')
            break
        else:
            print("Falha na janela de exportação do InDesign. Fechando o programa em:", 15 - counter)
            time.sleep(1)
            counter += 1
    
    # Press Enter on the InDesign export window
    press_key('enter')

    # Wait a bit
    time.sleep(0.6)

    # Check if something is missing
    # Checks if fonts are missing
    if find_missing_fonts_window() != False:
        print("Fontes faltando. Fechando o programa.")
        play_mp3('sounds/windows-xp-error-sound.mp3')
        break
    
    # Wait a bit
    time.sleep(0.6)

    # Checks if links are missing
    if find_missing_links_window() != False:
        print("Links faltando. Fechando o programa.")
        play_mp3('sounds/windows-xp-error-sound.mp3')
        break
    
    # Wait a bit
    time.sleep(0.5)

    # Wait until the export finishes
    counter = 0
    while find_export_file() != False or find_generating_pdf() != False:
        # If InDesign export window does not appear in 5 sec then close the program
        print("Esperando salvar.")

        # Wait a bit
        time.sleep(2)

    print("PDF exportado com sucesso.")
    # Finish exporting the pdf ---------------------------------------------------------------------------

    # Start exporting the indd ---------------------------------------------------------------------------
    # Close any open window
    for _ in range(3):
        press_key('esc')

    # Press the keys Ctrl+S
    press_key('ctrl+s')
    time.sleep(1)
    print("INDD exportado com sucesso.")
    # Finish exporting the indd --------------------------------------------------------------------------

    # Start exporting the idml ---------------------------------------------------------------------------
    # Close any open window
    for _ in range(3):
        press_key('esc')

    # Press the keys Ctrl+Shift+S
    press_key('ctrl+shift+s')

    # Wait 5 sec for Ctrl+Shift+S to appear
    counter = 0
    while find_save_as_idml() == False and counter < 16:
        # If Ctrl+Shift+S does not appear in 5 sec then close the program
        if counter == 15:
            print("Falha no Ctrl+Shift+S, fechando o programa.")
            play_mp3('sounds/windows-xp-error-sound.mp3')
            break
        else:
            print('Falha na janela de "Save As" do InDesign. Fechando o programa em: ', 15 - counter)
            time.sleep(1)
            counter += 1

    if find_save_as_idml() != False:
        # Press the key Tab
        press_key('tab')
            
        #Press Right Arrow key three times
        press_key('right')
        press_key('right')
        press_key('right')

        # Press Enter 
        press_key('enter')

        # Wait a bit
        time.sleep(0.1)

        # Press Enter 
        press_key('enter')

        # Wait a bit
        time.sleep(0.4)

    # Check if "want to replace file" windows appear
    if find_replace_file_window() != False:
        # Choose "yes" to replace
        # Press Left Arrow key
        press_key('left')

        # Press Enter
        press_key('enter')

    # Wait a bit
    time.sleep(0.5)

    # Wait until the export finishes
    counter = 0
    while find_export_file() != False or find_generating_pdf() != False:
        # If InDesign export window does not appear in 5 sec then close the program
        print("Esperando salvar.")

        # Wait a bit
        time.sleep(2)

    print("IDML exportado com sucesso.")
    # Finish exporting the idml --------------------------------------------------------------------------
    # Close any open window
    for _ in range(3):
        press_key('esc')

    # Closing the file in InDesign
    # Press the keys Ctrl+W
    press_key('ctrl+w')

    # Wait a bit
    time.sleep(3)