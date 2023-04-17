import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 10, "normal"), background=THEME_COLOR,
                           fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question will be right in here::.",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=image_true, highlightthickness=0, padx=50, pady=50, command=self.press_check)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, padx=50, pady=50, command=self.press_cross)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.button_false.config(state=DISABLED)
            self.button_true.config(state=DISABLED)

    def press_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_cross(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.quiz.score += 1
            self.label.config(text=f"Score: {self.quiz.score}", font=("Arial", 10, "normal"), background=THEME_COLOR,
                           fg="white")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
