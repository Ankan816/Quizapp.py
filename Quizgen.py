import tkinter as tk
from tkinter import messagebox


class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "Who invented Java Programming?",
                "options": [" James Gosling", "Guido van Rossum", "Dennis Richie", "Bjarne Stroustrup"],
                "correct_option": 0
            },
            {
                "question": "Which component is used to compile, debug and execute the java programs?",
                "options": ["JRE",
                            "JRE", " JVM",
                            "JIT"],
                "correct_option": 1
            },
            {
                "question": "  Which one of the following is not a Java feature?",
                "options": ["Object-oriented", "Use of pointers", "Portable", "Dynamic and Extensible"],
                "correct_option": 1
            },
            {
                "question": "Which of the following is not an OOPS concept in Java?",
                "options": ["Polymorphism", " Compilation", " Inheritance", "Encapsulation"],
                "correct_option": 1
            }
        ]

        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.option_var = tk.IntVar()
        self.option_var.set(-1)

        self.option_radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.option_var, value=i)
            self.option_radio_buttons.append(rb)
            rb.pack(anchor="w", padx=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.load_next_question()

    def load_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_radio_buttons[i].config(text=option)
            self.option_var.set(-1)
            self.result_label.config(text="")
        else:
            self.show_final_results()

    def submit_answer(self):
        if self.option_var.get() == -1:
            self.result_label.config(text="Please select an option.")
            return

        question = self.questions[self.current_question_index]
        correct_option = question["correct_option"]
        user_option = self.option_var.get()

        if user_option == correct_option:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            correct_answer = question["options"][correct_option]
            self.result_label.config(text=f"Incorrect. Correct answer: {correct_answer}", fg="red")

        self.current_question_index += 1
        self.load_next_question()

    def show_final_results(self):
        message = f"Quiz completed!\nYour final score: {self.score}/{len(self.questions)}"
        if self.score == len(self.questions):
            message += "\nCongratulations! You got all the questions right!"
        else:
            message += "\nKeep practicing and try again!"
        messagebox.showinfo("Final Results", message)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.current_question_index = 0
            self.load_next_question()
        else:
            self.root.quit()


def main():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()