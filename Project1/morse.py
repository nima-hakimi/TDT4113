from GPIOSimulator_v1 import *
import time
GPIO = GPIOSimulator()
GPIO.setup(PIN_RED_LED_0, GPIO.OUT, GPIO.LOW)
GPIO.setup(PIN_BLUE_LED, GPIO.OUT, GPIO.LOW)

MORSE_CODE = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
              '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
              '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
              '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
              '---..': '8', '----.': '9', '-----': '0'}

T = 0.7
DOT_TIME = T
DASH_TIME = 3 * T
LETTER_PAUSE = 4.5 * T
WORD_PAUSE = 7 * T
FINISH_PAUSE = 14 * T


class MorseDecoder():
    def __init__(self):
        self.current_symbol = ""
        self.current_word = ""
        self.current_message = ""
        self.pushed_time = 0
        self.released_time = 0
        self.previous_signal = 0
        self.signalMap = {'0': 'dot', '1': 'dash', '2': 'end_symbol', '3': 'end_word', '4': 'finish'}

    def reset(self):
        self.current_symbol = ""
        self.current_word = ""
        self.current_message = ""

    def read_one_signal(self):
        pass

    def decoding_loop(self):
        while True:
            current_signal = GPIO.input(0)
            if (current_signal == GPIO.input(0)):
                # Space down
                if (current_signal == 1 and self.previous_signal == 0):
                    self.pushed_time = time.time()
                    self.previous_signal = 1
                    if (self.released_time != 0):
                        paused_time = self.pushed_time - self.released_time
                        if (paused_time < WORD_PAUSE and paused_time >= LETTER_PAUSE):
                            self.process_signal("2")
                        elif (paused_time < FINISH_PAUSE and paused_time >= WORD_PAUSE):
                            self.process_signal("3")
                            continue
                        elif (paused_time >= FINISH_PAUSE):
                            self.process_signal('4')
                            break
                        self.released_time = 0

                # Space up
                elif (current_signal == 0 and self.previous_signal == 1):
                    self.released_time = time.time()
                    hold_time = self.released_time - self.pushed_time
                    if (hold_time >= DOT_TIME and hold_time < DASH_TIME):
                        self.process_signal("0")
                    elif (hold_time >= DASH_TIME):
                        self.process_signal("1")
                    self.previous_signal = 0

        self.handle_reset()

    def process_signal(self, signal):
        signalType = self.signalMap[str(signal)]
        if (signalType == "dot"):
            GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
            self.update_current_symbol(".")
            GPIO.output(PIN_RED_LED_0, GPIO.LOW)
        elif (signalType == "dash"):
            GPIO.output(PIN_BLUE_LED, GPIO.HIGH)
            self.update_current_symbol('-')
            GPIO.output(PIN_BLUE_LED, GPIO.LOW)
        elif (signalType == "end_symbol"):
            self.handle_symbol_end()
        elif (signalType == "end_word"):
            self.handle_word_end()
        elif (signalType == 'finish'):
            self.show_message()
        else:
            raise("Something weird has happened with the signal")

    def update_current_symbol(self, signal):
        self.current_symbol += signal
        print(self.current_symbol)

    def update_current_word(self, symbol):
        self.current_word += symbol
    def handle_symbol_end(self):        print(self.current_word                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )

        if (self.current_symbol != ""):
            try:
                symbol = MORSE_CODE[self.current_symbol]
                self.update_current_word(symbol)
                self.current_symbol = ""
            except KeyError:
                print("invalid morse code!")
                self.current_symbol = ""

    def handle_word_end(self):
        self.handle_symbol_end()
        print(self.current_word)
        if (self.current_message == ''):
            self.current_message == self.current_word
        else:
            self.current_message += ' ' + self.current_word
        self.current_word = ""

    def handle_reset(self):
        GPIO.cleanup()

    def show_message(self):
        self.handle_word_end()
        print('Final message:', self.current_message)


def main():
    decoder = MorseDecoder()
    decoder.decoding_loop()


if __name__ == "__main__":
    main()
