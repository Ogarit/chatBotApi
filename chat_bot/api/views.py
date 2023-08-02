from rest_framework.decorators import api_view
from rest_framework.response import Response
from googletrans import Translator
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from torch import ones_like, long
from random import choice


class Tranformers:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

        self.chat_history = []

    def chat_response(self, statements):
        while True:
            try:
                self.chat_history.append('I:' + statements)
                history = ' '.join(self.chat_history)

                input_ids = self.tokenizer.encode(history, return_tensors="pt", padding=True)

                attention_mask = ones_like(input_ids, dtype=long)

                outputs = self.model.generate(input_ids=input_ids, attention_mask=attention_mask, max_new_tokens=1000,
                                              num_beams=100, num_return_sequences=100)

                responses = list(map(lambda x: self.tokenizer.decode(x, skip_special_tokens=True), outputs))

                response = choice(responses)

                self.chat_history.append('You:' + response)

                return response

            except IndexError:
                self.chat_history = []


generator = Tranformers()
translator = Translator()


def translate(statements, lang):
    return translator.translate(statements, dest=lang).text


@api_view(['POST'])
def view_post(request):
    text = request.data.get('text')
    text = translate(text.replace('.', '.') + '.', 'en')

    response = {
        'response': translate(generator.chat_response(text), 'pt').replace('.', '. ')
        .replace('!', '! ').replace('?', '? ').replace(',', ', ')
    }

    return Response(response)
