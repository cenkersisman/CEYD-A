from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)
#print(word_vectors.wv.most_similar(positive=["kral","kadın"],negative=["erkek"]))
#print(word_vectors.wv.most_similar(positive=["doktor","kadın"],negative=["erkek"]))
print(word_vectors.wv.doesnt_match(["covid","hasta","migros","doktor"]))



#print(word_vectors.wv.most_similar(positive=["paris","ispanya"],negative=["fransa"]))
#print(word_vectors.wv.doesnt_match(["mars","ay","jüpiter","venüs"]))
#print(word_vectors.wv.similarity("istanbul", "başkent"))
#print(word_vectors.wv.most_similar(positive=["bugün","hava","kaç","derece"]))

"""
my_dict = dict({})
for idx, key in enumerate(word_vectors.wv.vocab):
    my_dict[key] = word_vectors.wv[key]
    # Or my_dict[key] = model.wv.get_vector(key)
    # Or my_dict[key] = model.wv.word_vec(key, use_norm=False)
"""
#print(word_vectors.wv.vocab.keys())
"""for i, word in enumerate(word_vectors.wv.vocab):
    if i == 10:
        break
    print(word)
"""

#print(word_vectors.wv.similarity("ankara", "başkent"))
#print(word_vectors.wv.most_similar(positive=['kral', 'erkek'], topn=1))
