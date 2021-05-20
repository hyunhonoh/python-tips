## python code tip

### 괄호안의 공백을 유지하고 공백으로 나누기

https://stackoverflow.com/questions/42070323/split-on-spaces-not-inside-parentheses-in-python


```python
def parenthesis_split(sentence,separator=" ",lparen="(",rparen=")"):
    nb_brackets=0
    sentence = sentence.strip(separator) # get rid of leading/trailing seps

    l=[0]
    for i,c in enumerate(sentence):
        if c==lparen:
            nb_brackets+=1
        elif c==rparen:
            nb_brackets-=1
        elif c==separator and nb_brackets==0:
            l.append(i)
        # handle malformed string
        if nb_brackets<0:
            raise Exception("Syntax error")

    l.append(len(sentence))
    # handle missing closing parentheses
    if nb_brackets>0:
        raise Exception("Syntax error")


    return([sentence[i:j].strip(separator) for i,j in zip(l,l[1:])])

print(parenthesis_split("blah (blah2 (blah3))|blah4 blah5"))
```


### 한자 찾기
- https://www.epubguide.net/118

```
([一-龥豈-龎]+)
```

