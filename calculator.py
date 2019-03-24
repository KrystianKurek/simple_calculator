import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import math


# Constants defining basic operations
ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4


class Calculator(tk.Tk):
    """Class that inherits from tk.Tk."""
    def __init__(self):
        # Create instance of a window
        super(Calculator, self).__init__()
        self.title("Simple calculator")
        self.resizable(False, False)
        self.create_widgets()

        # Set some helpful variables to start values
        self.first_number = None
        self.second_number = None
        self.operation = None
        self.answer = None

    def create_widgets(self):
        """Create buttons and text box."""
        self.digits_text_box = ttk.Entry(self, width=50)
        self.digits_text_box.grid(column=0, row=0, columnspan=4)

        answer_button = ttk.Button(self, text="Ans", command=self.ans)
        answer_button.grid(column=0, row=2)

        clear_button = ttk.Button(self, text="C", command=self.clear)
        clear_button.grid(column=1, row=2)

        backspace_button = ttk.Button(self, text="Backspace", width=24, command=self.backspace)
        backspace_button.grid(column=2, row=2, columnspan=2)

        logarithm_button = ttk.Button(self, text="log", command=lambda: self.one_argument_function_count(math.log2))
        logarithm_button.grid(column=0, row=3)

        inverse_number_button = ttk.Button(self, text="1/x", command=lambda: self.one_argument_function_count(lambda x: 1/x))
        inverse_number_button.grid(column=1, row=3)

        square_root_button = ttk.Button(self, text="√", command=lambda: self.one_argument_function_count(math.sqrt))
        square_root_button.grid(column=2, row=3)

        divide_button = ttk.Button(self, text="/", command=lambda: self.set_operation(DIVIDE))
        divide_button.grid(column=3, row=3)

        multiply_button = ttk.Button(self, text="x", command=lambda: self.set_operation(MULTIPLY))
        multiply_button.grid(column=3, row=4)

        subtract_button = ttk.Button(self, text="-", command=lambda: self.set_operation(SUBTRACT))
        subtract_button.grid(column=3, row=5)

        add_button = ttk.Button(self, text="+", command=lambda: self.set_operation(ADD))
        add_button.grid(column=3, row=6)

        equals_button = ttk.Button(self, text="=", command=self.equals)
        equals_button.grid(column=3, row=7)

        sign_button = ttk.Button(self, text="+/-", command=self.sign)
        sign_button.grid(column=0, row=7)

        dot_button = ttk.Button(self, text=".", command=lambda: self.insert_char('.'))
        dot_button.grid(column=2, row=7)

        buttons = [ttk.Button(self, text=str(i), command=lambda char=str(i): self.insert_char(char)) for i in range(0, 10)]
        buttons[0].grid(column=1, row=7)
        buttons[1].grid(column=0, row=6)
        buttons[2].grid(column=1, row=6)
        buttons[3].grid(column=2, row=6)
        buttons[4].grid(column=0, row=5)
        buttons[5].grid(column=1, row=5)
        buttons[6].grid(column=2, row=5)
        buttons[7].grid(column=0, row=4)
        buttons[8].grid(column=1, row=4)
        buttons[9].grid(column=2, row=4)

    def one_argument_function_count(self, function):
        """Count value given certain function.
        :param function: function that counts the value
        """
        self.first_number = self.digits_text_box.get()
        try:
            self.answer = function(float(self.first_number))
        except ValueError:
            if len(self.first_number) == 0:
                msg.showerror('Error!', 'You have to type something first!')
            else:
                msg.showerror('Error!', 'Invalid argument!')
        except ZeroDivisionError:
            msg.showerror('Error!', 'You can\'t divide by 0!')
        else:
            self.show_answer()
        finally:
            self.reset()

    def ans(self):
        """Print answer to the textbox."""
        if self.answer:
            self.show_answer()

    def reset(self):
        """Set first_number, second_number and operation to None."""
        self.first_number = None
        self.second_number = None
        self.operation = None

    def clear(self):
        """Clear textbox, set answer to None and perform reset() function."""
        self.digits_text_box.delete(0, tk.END)
        self.reset()
        self.answer = None

    def backspace(self):
        """Delete the last char in textbox."""
        self.digits_text_box.delete(len(self.digits_text_box.get())-1, tk.END)

    def insert_char(self, char):
        """
        Insert given char at the end of textbox.
        :param char: char to be inserted
        """
        self.digits_text_box.insert(tk.END, char)

    def get_first_number(self):
        """Read first_number from textbox or show error message."""
        try:
            self.first_number = float(self.digits_text_box.get())
            self.digits_text_box.delete(0, tk.END)
        except ValueError:
            msg.showerror('Error!', 'You have to type something first!')

    def get_second_number(self):
        """Read second_number from textbox or show error message."""
        try:
            self.second_number = float(self.digits_text_box.get())
            self.digits_text_box.delete(0, tk.END)
        except ValueError:
            msg.showerror('Error!', 'You have to type something first!')

    def set_operation(self, operation):
        """
        Set operation to this one given in argument and read first_number.
        :param operation: operation to be set
        """
        self.get_first_number()
        self.operation = operation

    def sign(self):
        """Change number's sign to the opposite."""
        entry_text = self.digits_text_box.get()
        if len(entry_text) == 0:
            return
        if entry_text[0] == "+":
            self.digits_text_box.delete(0, 1)
            self.digits_text_box.insert(0, "-")
        elif entry_text[0] == "-":
            self.digits_text_box.delete(0, 1)
        else:
            self.digits_text_box.insert(0, "-")

    def equals(self):
        """If possible count answer, if not show error message."""
        try:
            self.second_number = float(self.digits_text_box.get())
            self.digits_text_box.delete(0, tk.END)
        except ValueError:
            msg.showerror('Error!', 'You have to type something first!')
        else:
            if self.operation == DIVIDE:
                try:
                    self.answer = self.first_number / self.second_number
                except ZeroDivisionError:
                    msg.showerror('Error', 'You can\'t divide by 0!')
                else:
                    self.show_answer()
            else:
                if self.operation == ADD:
                    self.answer = self.first_number + self.second_number
                elif self.operation == SUBTRACT:
                    self.answer = self.first_number - self.second_number
                elif self.operation == MULTIPLY:
                    self.answer = self.first_number * self.second_number
                self.show_answer()

    def show_answer(self):
        """Print answer to the textbox."""
        self.digits_text_box.delete(0, tk.END)
        if self.answer is None:
            return
        elif str(self.answer)[-2:] == ".0":
            self.digits_text_box.insert(0, str(self.answer)[:-2])
        else:
            self.digits_text_box.insert(0, str(self.answer))


if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
