import random

def choose_word():
    # List kata yang bisa dipilih
    words = [
      'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
      'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
      'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
      'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
      'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
    ]
    # Memilih kata secara acak dari list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Membuat string dengan karakter _ untuk huruf yang belum ditebak
    # dan huruf jika sudah ditebak
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += '_'
    return displayed

def draw_hangman(incorrect_attempts):
    stages = [  # Hangman stages
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        '''
    ]
    return stages[incorrect_attempts]

def hangman():
    # Mengatur permainan
    word = choose_word()
    guessed_letters = []
    attempts = 6
    incorrect_attempts = 0

    print("Selamat datang di Hangman!")

    while True:
        print(draw_hangman(incorrect_attempts))
        print("\nKata:", display_word(word, guessed_letters))
        print("Sisa kesempatan:", attempts)
        guess = input("Tebak huruf: ").lower()

        if guess in guessed_letters:
            print("Anda sudah menebak huruf itu sebelumnya.")
            continue
        elif guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print(draw_hangman(incorrect_attempts))
                print("Selamat! Anda berhasil menebak kata '{}'!".format(word))
                break
        else:
            print("Huruf '{}' tidak ada dalam kata.".format(guess))
            guessed_letters.append(guess)
            attempts -= 1
            incorrect_attempts += 1
            if attempts == 0:
                print(draw_hangman(incorrect_attempts))
                print("Anda kehabisan kesempatan. Kata yang benar adalah '{}'.".format(word))
                break

    play_again = input("Ingin bermain lagi? (ya/tidak): ").lower()
    if play_again == 'ya':
        hangman()
    else:
        print("Terima kasih telah bermain!")

if __name__ == "__main__":
    hangman()
