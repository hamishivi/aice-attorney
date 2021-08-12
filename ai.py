from aitextgen import aitextgen

ai = aitextgen(model="EleutherAI/gpt-neo-125M", to_gpu=True)

ai.train('all_data.txt',
         line_by_line=True,
         from_cache=False,
         num_steps=3000,
         generate_every=1000,
         save_every=1000,
         save_gdrive=False,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1, 
         )

text = ai.generate_one()

print('output:')
print(text)