from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=340, height=480)

        # Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250)

        self.card = self.canvas.create_text(
            150,
            125,
            width=280,
            text="QUESTION",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.true_img, command=self.correct)
        self.correct_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, command=self.false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.card, text=q_text)
        else:
            self.canvas.itemconfig(self.card, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



