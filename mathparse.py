from collections import OrderedDict

prefix = 'prefix'
infix = 'infix'

# store the verbs in an OrderedDict so that we can use the order for order of
# Operations later
mathverbs=OrderedDict();
mathverbs['multiply']= {'fix': prefix,'op': '*'}
mathverbs['divide '] = {'fix': prefix,'op': '/'}
                  # extra space so that it's not detected in "divided"
mathverbs['add']     = {'fix': prefix,'op': '+'}
mathverbs['subtract']= {'fix': prefix,'op': '-'}
mathverbs['times']   = {'fix': infix, 'op': '*'}
mathverbs['divided'] = {'fix': infix, 'op': '/'}
mathverbs['plus']    = {'fix': infix, 'op': '+'}
mathverbs['minus']   = {'fix': infix, 'op': '-'}

mathpreps = {'to',
             'by',
             'from'}

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


def text2int(textnum, numwords={}):
  if not numwords:
    units = [
      "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
      "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
      "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):    numwords[word] = (1, idx)
    for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

  current = result = 0
  for word in textnum.split():
    if word not in numwords:
      raise Exception("Illegal word: " + word)

    scale, increment = numwords[word]
    current = current * scale + increment
    if scale > 100:
      result += current
      current = 0

  return result + current


def parse_arith(sen):

  op1 = None
  try:
    op1 = text2int(sen)
  except:
    pass
  else:
    return {'verb':None, 'op1':str(op1), 'op2':None}

  if is_number(sen):
    return {'verb':None, 'op1':sen, 'op2':None}
    

  # find the verb in the sentence
  v = None
  for v in sen:
    if v in mathverbs: 
      break

  if v is None:
    return None

  # if it's a prefix verb, find the preposition and then parse
  if mathverbs[v]['fix'] is prefix:
    verb_pos = sen.find(v)

    # find the first space for the start of the first operand
    op1_pos = sen.find(' ',verb_pos) + 1


    # find the preposition
    p = None
    for p in mathpreps:
      if p in sen:
        break
    if p == None:
      return None

    prep_pos = sen.find(p)

    # find the first space after the preposition for the second operand
    op2_pos = sen.find(' ',prep_pos) + 1

    op1  =  sen[op1_pos:prep_pos-1]
    op2  =  sen[op2_pos:]

    if v is 'subract':
      temp = op1
      op1 = op2
      op2 = temp


  # if it's an infix verb, grab the operands from around the verb
  elif mathverbs[v]['fix'] is infix:
    verb_pos = sen.find(v)

    # find the first space after the verb for the second operand
    op2_pos = sen.find(' ',verb_pos) + 1
    if v is 'divided':
      op2_pos = sen.find(' ',op2_pos) + 1

    op1  =  sen[0:verb_pos-1]
    op2  =  sen[op2_pos:]
    
  # print mathverbs[v]
  # print v
  # print op1
  # print op2

  return {'verb':v, 'op1':op1, 'op2':op2}

# recursively parse an arithmatic string into numbers and symbols
def make_arith_string(sen):
  ret = ''
  if sen is None or len(sen) == 0:
    return None
  p = parse_arith(sen)
  if is_number(p['op1']) and p['verb'] is None:
    return p['op1']
  print p
  if mathverbs[p['verb']]['fix'] is prefix:
    ret += '('
  ret +=  make_arith_string(p['op1'])
  if mathverbs[p['verb']]['fix'] is prefix:
    ret += ')'
  ret += mathverbs[p['verb']]['op']
  if mathverbs[p['verb']]['fix'] is prefix:
    ret += '('
  ret +=  make_arith_string(p['op2'])
  if mathverbs[p['verb']]['fix'] is prefix:
    ret += ')'
  print ret
  return ret

  
