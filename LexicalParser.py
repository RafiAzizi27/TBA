import streamlit as st
import string

st.title("Lexical Analyzer and Parser")
# Input
sentence = st.text_input("Masukkan kalimat: ")
tokens = sentence.lower().split()
tokens.append('EOS')

# Definisi Simbol
non_terminal = ['S', 'SU', 'VB', 'OB']
terminal = ['sorella', 'fratello', 'padre', 'madre', 'mangia', 'legge', 
            'giocca', 'carota', 'melanzane', 'giornale', 'libro', 'carte']

# Definisi Parse Table
parse_table = {}

parse_table[('S', 'sorella')] = ['SU', 'VB', 'OB']
parse_table[('S', 'fratello')] = ['SU', 'VB', 'OB']
parse_table[('S', 'padre')] = ['SU', 'VB', 'OB']
parse_table[('S', 'madre')] = ['SU', 'VB', 'OB']
parse_table[('S', 'mangia')] = ['error']
parse_table[('S', 'legge')] = ['error']
parse_table[('S', 'giocca')] = ['error']
parse_table[('S', 'carota')] = ['error']
parse_table[('S', 'melanzane')] = ['error']
parse_table[('S', 'giornale')] = ['error']
parse_table[('S', 'libro')] = ['error']
parse_table[('S', 'carte')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('SU', 'sorella')] = ['sorella']
parse_table[('SU', 'fratello')] = ['fratello']
parse_table[('SU', 'padre')] = ['padre']
parse_table[('SU', 'madre')] = ['madre']
parse_table[('SU', 'mangia')] = ['error']
parse_table[('SU', 'legge')] = ['error']
parse_table[('SU', 'giocca')] = ['error']
parse_table[('SU', 'carota')] = ['error']
parse_table[('SU', 'melanzane')] = ['error']
parse_table[('SU', 'giornale')] = ['error']
parse_table[('SU', 'libro')] = ['error']
parse_table[('SU', 'carte')] = ['error']
parse_table[('SU', 'EOS')] = ['error']

parse_table[('VB', 'sorella')] = ['error']
parse_table[('VB', 'fratello')] = ['error']
parse_table[('VB', 'padre')] = ['error']
parse_table[('VB', 'madre')] = ['error']
parse_table[('VB', 'mangia')] = ['mangia']
parse_table[('VB', 'legge')] = ['legge']
parse_table[('VB', 'giocca')] = ['giocca']
parse_table[('VB', 'carota')] = ['error']
parse_table[('VB', 'melanzane')] = ['error']
parse_table[('VB', 'giornale')] = ['error']
parse_table[('VB', 'libro')] = ['error']
parse_table[('VB', 'carte')] = ['error']
parse_table[('VB', 'EOS')] = ['error']

parse_table[('OB', 'sorella')] = ['error']
parse_table[('OB', 'fratello')] = ['error']
parse_table[('OB', 'padre')] = ['error']
parse_table[('OB', 'madre')] = ['error']
parse_table[('OB', 'mangia')] = ['error']
parse_table[('OB', 'legge')] = ['error']
parse_table[('OB', 'giocca')] = ['error']
parse_table[('OB', 'carota')] = ['carota']
parse_table[('OB', 'melanzane')] = ['melanzane']
parse_table[('OB', 'giornale')] = ['giornale']
parse_table[('OB', 'libro')] = ['libro']
parse_table[('OB', 'carte')] = ['carte']
parse_table[('OB', 'EOS')] = ['error']

# Inisiasi Stack
stack = []
stack.append('#')
stack.append('S')

# Inisiasi Pembacaan Input
idx_token = 0
symbol = tokens[idx_token]

st.text("=====PARSER=====")
# Parsing
while len(stack) > 0:
    top = stack[len(stack)-1]
    st.text(f'top = {top}')
    st.text(f'symbol = {symbol}')
    if top in terminal:
        st.text('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                st.text(f'isi stack: {stack}')
                stack.pop()
        else:
            st.text('error')
            break;
    elif top in non_terminal:
        st.text('top adalah simbol non terminal')
        if not (symbol in terminal):
            st.text('error')
            break;
        elif parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbolPush = parse_table[(top, symbol)]
            for i in range(len(symbolPush)-1,-1,-1):
                stack.append(symbolPush[i])
        else:
            st.text('error')
            break;
    else:
        st.text('error')
        break;
    st.text(f'isi stack: {stack}')

if symbol == 'EOS' and len(stack)==0:
    st.text(f'Input string {sentence} diterima, sesuai grammar')
else:
    st.text(f'Error, input string {sentence} tidak diterima, tidak sesuai grammar')

input_string = sentence.lower()+'#'

alphabet_list = list(string.ascii_lowercase)
state_list = []
for i in range(65):
    state = "q{}"
    state_list.append(state.format(i))

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = "error"
    transition_table[(state, '#')] = "error"
    transition_table[(state, ' ')] = "error"

# spasi sebelum string
transition_table[('q0',' ')] = 'q0'

# carota
transition_table[('q0','c')] ='q1'
transition_table[('q1','a')] ='q2'
transition_table[('q2','r')] ='q3'
transition_table[('q3','o')] ='q4'
transition_table[('q4','t')] ='q5'
transition_table[('q5','a')] ='q6'
transition_table[('q6','#')] ='accepted'
transition_table[('q6',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# carte
transition_table[('q0','c')] ='q1'
transition_table[('q1','a')] ='q2'
transition_table[('q2','r')] ='q3'
transition_table[('q3','t')] ='q8'
transition_table[('q8','e')] ='q10'
transition_table[('q10','#')] ='accepted'
transition_table[('q10',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# fratello
transition_table[('q0','f')] ='q11'
transition_table[('q11','r')] ='q12'
transition_table[('q12','a')] ='q13'
transition_table[('q13','t')] ='q14'
transition_table[('q14','e')] ='q15'
transition_table[('q15','l')] ='q16'
transition_table[('q16','l')] ='q17'
transition_table[('q17','o')] ='q18'
transition_table[('q18','#')] ='accepted'
transition_table[('q18',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# giornale
transition_table[('q0','g')] ='q19'
transition_table[('q19','i')] ='q20'
transition_table[('q20','o')] ='q21'
transition_table[('q21','r')] ='q22'
transition_table[('q22','n')] ='q23'
transition_table[('q23','a')] ='q24'
transition_table[('q24','l')] ='q25'
transition_table[('q25','e')] ='q26'
transition_table[('q26','#')] ='accepted'
transition_table[('q26',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# giocca
transition_table[('q0','g')] ='q19'
transition_table[('q19','i')] ='q20'
transition_table[('q20','o')] ='q21'
transition_table[('q21','c')] ='q27'
transition_table[('q27','c')] ='q28'
transition_table[('q28','a')] ='q29'
transition_table[('q29','#')] ='accepted'
transition_table[('q29',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# libro
transition_table[('q0','l')] ='q30'
transition_table[('q30','i')] ='q31'
transition_table[('q31','b')] ='q32'
transition_table[('q32','r')] ='q33'
transition_table[('q33','o')] ='q34'
transition_table[('q34','#')] ='accepted'
transition_table[('q34',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# legge
transition_table[('q0','l')] ='q30'
transition_table[('q30','e')] ='q35'
transition_table[('q35','g')] ='q36'
transition_table[('q36','g')] ='q37'
transition_table[('q37','e')] ='q38'
transition_table[('q38','#')] ='accepted'
transition_table[('q38',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# madre
transition_table[('q0','m')] ='q39'
transition_table[('q39','a')] ='q40'
transition_table[('q40','d')] ='q41'
transition_table[('q41','r')] ='q42'
transition_table[('q42','e')] ='q43'
transition_table[('q43','#')] ='accepted'
transition_table[('q43',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# melanzane
transition_table[('q0','m')] ='q39'
transition_table[('q39','e')] ='q44'
transition_table[('q44','l')] ='q45'
transition_table[('q45','a')] ='q46'
transition_table[('q46','n')] ='q47'
transition_table[('q47','z')] ='q48'
transition_table[('q48','a')] ='q49'
transition_table[('q49','n')] ='q50'
transition_table[('q50','e')] ='q51'
transition_table[('q51','#')] ='accepted'
transition_table[('q51',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# mangia
transition_table[('q0','m')] ='q39'
transition_table[('q39','a')] ='q40'
transition_table[('q40','n')] ='q52'
transition_table[('q52','g')] ='q53'
transition_table[('q53','i')] ='q54'
transition_table[('q54','a')] ='q55'
transition_table[('q55','#')] ='accepted'
transition_table[('q55',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# padre
transition_table[('q0','p')] ='q56'
transition_table[('q56','a')] ='q57'
transition_table[('q57','d')] ='q41'
transition_table[('q41','r')] ='q42'
transition_table[('q42','e')] ='q43'
transition_table[('q43','#')] ='accepted'
transition_table[('q43',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# sorella
transition_table[('q0','s')] ='q58'
transition_table[('q58','o')] ='q59'
transition_table[('q59','r')] ='q60'
transition_table[('q60','e')] ='q61'
transition_table[('q61','l')] ='q62'
transition_table[('q62','l')] ='q63'
transition_table[('q63','a')] ='q64'
transition_table[('q64','#')] ='accepted'
transition_table[('q64',' ')] ='q7'
transition_table[('q7','#')] ='accepted'
transition_table[('q7',' ')] ='q7'

# new word
transition_table[('q7','c')] ='q1'
transition_table[('q7','f')] ='q11'
transition_table[('q7','g')] ='q19'
transition_table[('q7','l')] ='q30'
transition_table[('q7','m')] ='q39'
transition_table[('q7','p')] ='q56'
transition_table[('q7','s')] ='q58'

st.text("=====ANALYZER=====")
# analyzer
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accepted':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'q7':
        st.text(f'current token: {current_token}, valid')
        current_token = ''
    if state == 'error':
        st.text('error')
        break
    idx_char = idx_char + 1

#conclusion
if state == 'accepted':
    st.text(f'semua token di input: {sentence}, valid')
st.text("Kesimpulan: ")
# Kesimpulan
if state == 'accepted' and symbol == 'EOS' and len(stack)==0:
    st.text(f"Kalimat {sentence} valid dan sesuai grammar")
elif state == 'accepted':
    st.text(f'Kalimat {sentence} valid tetapi tidak sesuai grammar')
else:
    st.text(f'Kalimat {sentence} tidak valid')