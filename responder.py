import mathparse
import insultgen
import wikistuff
import test3
import random
import classifier

end_text = 'Okay, so long!'
born_list = ['born', 'birth', 'birthday']
death_list = ['die', 'died', 'death']
math_words = ['solve', 'calculate']


def respond_math(text) :
  text = text.replace('?','')
  try:
    math = mathparse.make_arith_string(text)
  except:
    return test3.solver(text)
  return test3.solver(math)


def respond_question(text, valence):
    t = text.lower().split()
    if t[0] == 'when':
      #get the name
      name = text[text.find(' ')+1:] #skip over "when"
      name = name[text.find(' '):] #skip over verb
      name = name[:name.rfind(' ')]
      url = "http://en.wikipedia.org/wiki/" + name.replace(' ','_')
      #print url

      if any(word in text for word in born_list):
        try:
          ret = wikistuff.findTheBirth(url)
        except:
          return "Oops, I couldn't find that person."
        return 'They were born on '+ret
      if any(word in text for word in death_list):
        try:
          ret = wikistuff.findTheDeath(url)
        except:
          return "Oops, I couldn't find that person."
        return 'They died on '+ret
      return name

    if t[0] == 'who' and (t[1] == 'is' or t[1] == 'was'):
      #get the name
      name = text[text.find(' ')+1:] #skip over "when"
      name = name[text.find(' '):] #skip over verb
      if '?' in name:
        name = name[:name.rfind('?')]
      try:
        ret = wikistuff.getInfo(name)
      except:
        return "Oops, I couldn't find that person."
      return ret

    if t[0] == 'what' and t[1] == 'is':
      math = ' '.join(t[2:])
      return respond_math(math)
      
    if valence == 'pos' :
        return random.choice(["I wish I knew.",
                              "I'm not sure how to answer that.",
                              "Can't quite understand your question there, friend.",
                              "Could you repeat that, and go slow this time."])
    else :
        return random.choice(["That's a tough question.",
                              "Hard to know...",
                              "Hmm, I'll need to think about that one for a while. I'll get back to you.",
                              "Oh, you must think you're pretty clever, asking that."])

def respond_other(text, valence) :
    return ":P  Well, what next?"

def respond_statement(text, valence) :
    if valence == 'pos' :
        return random.choice(["Great!  Tell me more.",
                              "Wow, that's really interesting.",
                              "Awesome!",
                              "Man, that's pretty cool."])
    else :
        g = insultgen.insultgen()
        return g.generateInsult()

def respond_bye(text, valence) :
    return end_text

def respond_greet(text, valence) :
    return random.choice(["Hey there!",
                          "Hi, friend!",
                          "Hello!",
                          "Howdy!",
                          "Greetings, fellow human!"])

def respond_reject(text, valence) :
    if valence == 'pos' :
        return random.choice(["Well, if you insist!",
                              "Yeah, I didn't really like that either.",
                              "Yeah, it sucked.",
                              "Alright, if you say do."])
    else :
        g = insultgen.insultgen()
        return g.generateInsult()

def respond_emphasis(text, valence) :
    if valence == 'pos' :
        return random.choice(['!!!',
                              'Wow!',
                              'Holy cow!',
                              'Gadzooks!',
                              'Good golly gosh!'])
    else :
        g = insultgen.insultgen()
        return g.generateInsult()


responses = {'Accept': respond_other,
             'Bye': respond_bye,
             'Clarify': respond_other,
             'Continuer': respond_other,
             'Emotion': respond_other,
             'Emphasis': respond_emphasis,
             'Greet': respond_greet,
             'nAnswer': respond_other,
             'Other': respond_other,
             'Reject': respond_reject,
             'Statement': respond_statement,
             'System': respond_other,
             'whQuestion': respond_question,
             'yAnswer': respond_other,
             'ynQuestion': respond_question}


def respond(text) :  
    if any(word in text.lower() for word in math_words):
      # strip opening word
      math = text[text.find(' ')+1:]
      return respond_math(math)
    elif any(word in text.lower() for word in mathparse.mathverbs):
      return respond_math(text)
    act = classifier.expt3.classify(text)
    valence = classifier.expt1.classify(text)
    # print act
    return responses[act](text, valence)
