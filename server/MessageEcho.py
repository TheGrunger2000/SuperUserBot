class MessageEcho:

    def __init__(self):
        self._answers_dict = {
            "Hello": "Dummy message",
            "How are you?": "How DARE you!",
            "Let's kill Java maybe?": "SURE!",
            "Maybe 4:20?": "Why not?",
            "What?": "Nothing...",
            "?": "Well...",
            "Oh really?": "Yeah... Why not?",
            "You're Asshole": "F...k you!!!",
            "Hard Bass?": "You're slave!",
            "Wrong!!!": "Maybe... bvhjdsabvhkdabv",
        }

    def run(self, message):
        try:
            answer = self._answers_dict[message]
        except KeyError:
            answer = "Nah, you're boring! Try again!"
        return answer
