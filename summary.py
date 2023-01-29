percentage = int(input("What will be the percentage of your summary (0-100): "))
text = "Some people believe that theatre began in ancient Greece, where myths and legends were narrated by a group of people called the Chorus, who chanted their lines to enthralled audiences. Then came the idea of including the dramatic impersonation of someone in the storyline, in other words acting, and an actor was introduced into the performance. Plots were made more complicated by the addition of a second or even third actor, although the scope for convincing acting was limited by the factthat the actors wore masks to represent the characters they were portraying. Greek plays were performed in honour of the Greek gods and took place during the major spring festival, when people flocked to the open-air hillside amphitheatres to be informed and entertained. At first, only tragedies were performed, but the introduction of comedy, with its often cruel satire of contemporary society, appealed to the ordinary people, thus increasing the popularity of drama. In Roman times, the public enjoyed a varied range of entertainment, often involving spectacular contests between gladiators and animals, which took place in massive, purpose-built arenas. Going to the theatre was also a popular feature of life, where the development of a secondary story, or sub-plot, made plays more sophisticated by enabling audiences to look at the lives of more than one set of characters in the same play. Later, throughout Europe, groups of street actors, often accompanied by acrobats and animals, moved from town to town, performing for a succession of appreciative audiences; towns were enlivened at the news of approaching players, and a great buzz ensued. Through time, permanent buildings for the production of plays were established, bringing audiences to the theatre rather than the other way round. It is estimated that in sixteenth-century London, for example, one in eight adults went to the theatre every week. Around the world, various forms of theatre evolved, like the shadow puppets of Malaysia, and Japanese Noh theatre in which actors sing and dance scenes from legends with an immense slowness and solemnity which is particularly moving. Today, theatre continues to attract people all over the world. Because plays are performed live, every performance is different. It is this dynamic nature of theatre which means that live performances are always better than films. Being gripped by the unfolding story of a play can be an excellent form of relaxation, and for many the experience of being transported into another setting or into someone else’s life – sometimes described as suspending disbelief – is fascinating. Moreover, theatre lovers enjoy marvelling at the skill of the actors, which is why theatre acting is much more challenging than acting in front of a camera. Empathising with the characters’ stories can make audiences relate them to their own lives and use them to help in making decisions or even solving problems. The cleansing emotional experience – or catharsis – brought about by watching drama can be good for mental health. This makes theatre a more satisfying emotional experience than cinema. A trip to the theatre can bring families together, for example during national holidays or celebrations, giving family members the opportunity to enjoy a common experience. Technological advances in recent times – such as in lighting and special effects – can make theatre a spectacle as well as a play. In future, technological developments will provide audiences with even more sensational and thrilling experiences. In addition, theatre sometimes offers the opportunity of being part of a tradition. An example of this is a play called The Mousetrap, the longest running play in the world, where the attraction is not just the drama itself, but also being part of a large, world-wide, ‘secret’ group who share the knowledge of the identity of the villain. And of course, theatre audiences, often without realising the fact, are part of an even longer tradition, one going back to those Greek choruses, thousands of years ago."
stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
             'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
             'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
             'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
             'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
             'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
             "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
             'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
             "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan',
             "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
             "wouldn't"]
sentences = text.split(".")
sentences = sentences[:-1]
content = []
for i,sentence in enumerate(sentences):
    lst = []
    lst.append(i)
    lst.append(sentence)
    stopWordsCount = 0
    words = sentence.split(" ")
    noOfWordsInSentence = len(words)
    for word in words:
        if word in stopWords:
            stopWordsCount += 1
    importanceWeightage = (noOfWordsInSentence - stopWordsCount) / noOfWordsInSentence
    lst.append(importanceWeightage)
    content.append(lst)
newContent = sorted(content, key = lambda x:x[-1],reverse = True)
noOfSentencesInSummary = int((percentage/100) * len(sentences))
summarySentences = newContent[:noOfSentencesInSummary]
finalSentences = sorted(summarySentences, key = lambda x:x[0])
file = open("Summary.txt","w")
for i in finalSentences:
    sentence = i[1] + "."
    file.write(sentence)
file.close()
