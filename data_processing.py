from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pandas import *

# import nltk
# 
import csv
import sys
 
def main():
    stop_words = stopwords.words('english')

    custom_stop_words = ["n't","im","bc",'.',',',"'ve","'m",'(', '``',"''", ')',"'s","ive",'#','&',';',"'ll",'*','’','?','!','”','-','...','..','%','+',"dont",'“']
    # print(stop_words)

    # reading CSV file
    args = sys.argv
    file_name = args[1]
    data = read_csv(file_name)

    output_f = file_name.split('.')
    print(output_f[0])
    output_f = output_f[0].split('/')
    print(output_f)
    output_f = output_f[-1]
    output_f = output_f+"_clean.csv"
    output_folder = "Reddit_post_clean/"
    output_f = output_folder+output_f
    
    # inFile = open(args[1],'r')
    
    posts = data['post'].tolist()
    tokenized_post = []
    main_post = []
    for post in posts:
        # print(stream)
        word_tokens = word_tokenize(post)
        tokenized_post.append(word_tokens)
        # print(word_tokens)
        filtered_sentence = []
        for w in word_tokens:
            if w.lower() not in stop_words and w.lower() not in custom_stop_words:
                if "," in w.lower():
                    print(w.lower())
                    filtered_sentence.append(w.lower().replace(",",""))
                else:
                    filtered_sentence.append(w.lower())
            
        main_post.append(filtered_sentence)
        # main_post.append(" ".join(filtered_sentence))
        
    print(len(tokenized_post))
    print(len(main_post))

    # print(main_post[0])

    all_post = []

    for post in main_post:
        full_sentence = " ".join(post)
        # print(full_sentence)
        all_post.append(full_sentence)
    # all_post
    # print(all_post[0])

    # f1 = open('posts_clean.csv', 'w')
    f1 = open(output_f,'w')
    f1.write('post')
    f1.write('\n')

    for post in all_post:

        # write the header
        f1.write(post)
        f1.write('\n')

        
    print(len(all_post))

if __name__ == "__main__":
    main()

