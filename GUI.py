import PySimpleGUI as sg  # import a GUI framework
from formulas import *  # import functions that return data on readability indexes

sg.theme('DarkPurple4')  # return 2007 by choosing stylish pinkish dark theme

# window layout
layout = [[sg.Text('Enter your text:'), sg.Multiline(size=(100, 10), key='-IN-')],  # input window
          [sg.Output(size=(100, 5))],  # space for printed output
          [sg.Button('Calculate Flesch score'), sg.Button('Calculate Gunning fog index'),
           sg.Button('Calculate Coleman-Liau index')],
          [sg.Button('Calculate Dale-Chall score (English texts only)'),
           sg.Button('Calculate Automated Readability Index')]]  # buttons launching corresponding calculations

window = sg.Window('Readability calculator', layout, size=(600, 350))

while True:
    event, values = window.read()
    try:
        # close window when the exit button pressed
        if event in (sg.WINDOW_CLOSED, 'WIN_CLOSED'):
            break

        # error message when input is empty
        if values['-IN-'] is None or values['-IN-'] == '':
            print('Error! Please, make sure that your input is not an empty string and contains textual '
                  'data in English or Russian language and try again.\n')

        # error message when input is too short
        if 0 < word_count(values['-IN-']) < 100:
            print('Error! The text is too short, please, enter a piece of text '
                  'consisting of no less than 100 words.\n')

        # associate buttons with corresponding functions
        else:
            if event == 'Calculate Flesch score':
                text = values['-IN-']
                print(flesch_index_data(flesch_index(text)))
            elif event == 'Calculate Gunning fog index':
                text = values['-IN-']
                print(gunning_fog_data(gunning_fog_index(text)))
            elif event == 'Calculate Coleman-Liau index':
                text = values['-IN-']
                print(cl_data(c_l_index(text)))
            elif event == 'Calculate Dale-Chall score (English texts only)':
                text = values['-IN-']
                print(dale_chall_data(dale_chall_index(text)))
            elif event == 'Calculate Automated Readability Index':
                text = values['-IN-']
                print(automated_readability_data(automated_readability_index(text)))
    # prevent the program from crashing in case of other errors
    except:
        print('Error! Please, make sure that your input is not an empty string and contains textual '
              'data in English or Russian language and try again.\n')
window.close()
