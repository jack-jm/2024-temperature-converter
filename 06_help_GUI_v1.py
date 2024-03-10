from tkinter import *


class Converter:

  def __init__(self):
    # common font for all buttons
    # Arial, size 14, bold, with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"

    # Set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    self.to_help_button = Button(self.button_frame,
                                 text="Help / Info",
                                 bg="#CC6600",
                                 fg=button_fg,
                                 font=button_font, width=12,
                                 command=self.to_help)
    self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

  @staticmethod
  def to_help():
    DisplayHelp()


class DisplayHelp:

  def __init__(self):
    print("you pressed help")



  def check_temp(self, min_value):

    has_error = "no"
    error = "Please enter a number that is more " \
            "than {}".format(min_value)

    # check that user has entered a valid number

    response = self.temp_entry.get()

    try:
        response = float(response)

        if response < min_value:
          has_error = "yes"

    except ValueError:
      has_error = "yes"

    # Sets var_has_error so that entry box and
    # labels can be correctly formatted by formatting function
    if has_error == "yes":
      self.var_has_error.set("yes")
      self.var_feedback.set(error)
      return "invalid"

    # If we have no errors
    else:
      # set to 'no' in case of previous errors
      self.var_has_error.set("no")

      # return number to be
      # converted and enable history button
      self.to_history_button.config(state=NORMAL)
      return response

  @staticmethod
  def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)

  # check temperature is valid and convert it
  def temp_convert(self, min_val): 
    to_convert = self.check_temp(min_val)
    deg_sign = u'\N{DEGREE SIGN}'
    set_feedback = "yes"
    answer = ""
    from_to = ""

    if to_convert == "invalid":
      set_feedback = "no"

    # Convert to Celsius
    elif min_val == -459:
      # do calculation
      answer = (float(to_convert) - 32) * 5 / 9
      from_to = "{} F{} is {} C{}"

    # convert to Fahrenheit
    else:
      answer = float(to_convert) * 1.8 + 32
      from_to = "{} C{} is {} F{}"

    if set_feedback == "yes":
      to_convert = self.round_ans(to_convert)
      answer = self.round_ans(answer)

      # create user output and add to calculation history
      feedback = from_to.format(to_convert, deg_sign,
                                answer, deg_sign)
      self.var_feedback.set(feedback)

      self.all_calculations.append(feedback)

    self.output_answer()

  # Shows user output and clears entry widget
  # ready for next calculation
  def output_answer(self):
    output = self.var_feedback.get()
    has_errors = self.var_has_error.get()

    if has_errors == "yes":
      # red text, pink entry box
      self.temp_error.config(fg="#9C0000")
      self.temp_entry.config(bg="#F3CECC")

    else:
      self.temp_error.config(fg="#004C00")
      self.temp_entry.config(bg="#FFFFFF")

    self.temp_error.config(text=output)


# main routine
if __name__  == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()
