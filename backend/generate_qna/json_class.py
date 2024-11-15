class BaseModel:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question_text, options):
        question = {
            "question_text": question_text,
            "options": options
        }
        self.questions.append(question)

    def format_questions_for_prompt(self):
        prompt = f"Quiz Title: {self.title}\n"
        for idx, question in enumerate(self.questions, start=1):
            prompt += f"\nQ{idx}: {question['question_text']}\n"
            for opt_idx, option in enumerate(question['options'], start=1):
                prompt += f"  {opt_idx}. {option}\n"
        return prompt
    
class QuestionModel(BaseModel):
    def __init__(self, title):
        super().__init__(title)

    def add_question(self, question_text, options):
        super().add_question(question_text, options)

    def display(self):
        print(f"Quiz Title: {self.title}")
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQ{idx}: {question['question_text']}")
            for opt_idx, option in enumerate(question['options'], start=1):
                print(f"  {opt_idx}. {option}")
