from aitextgen import aitextgen
from court_bot import generate_from_text

# load model
ai = aitextgen(model_folder="smaller_trained_model")

def random_gen(output_video='hello.mp4'):
    print('generating text')
    text = ai.generate_one(max_length=300, prompt='Phoenix:')
    print(text)
    generate_from_text(text, output_video)

if __name__ == '__main__':
    random_gen()
