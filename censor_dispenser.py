# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# task 2
def find_replace(text, censored_term):
    ''' Difference between my function & the solution:
        the solution doesn't redact if spaces occur in the search term
        while mine does. Also, the solution performed the search term
        replacement letter-by-letter and mine performed it as a whole. '''
    redacted_text = text.replace(censored_term, len(censored_term) * '*')
    return redacted_text

# print(find_replace(email_one, 'learning algorithm'))

# task 3
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena"]

def multi_find_replace(text, censored_terms):
    ''' Difference between my function & the solution:
        same as task 2 above - accounting for spaces in the search terms
        and searching letter-by-letter rather than singly '''
    for term in censored_terms:
        text = text.replace(term, len(term) * '*')
    return text

# print(multi_find_replace(email_two, proprietary_terms))

# task 4
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

def negative_find_replace(text, negative_terms):
    ''' Difference between my function & the solution:
        the solution converted the text string to a list before the search
        and then joined the list to convert it back to a whole string. I
        dealt with the string throughout the function. The solution removes
        carriage returns (new lines) and punctuation, presumably to improve
        the search for keywords. However, the text that is returned from the
        function is unformatted while my function returns the email text as
        it originally appears. The solution, when performing the searches,
        looks for each word from the text in the keyword lists. My function
        does the opposite; it looks for each keyword in the text since there
        are fewer keywords than words in the text (i.e. fewer cycles through
        a for loop. The solution rebuilt the code created in task 3 in
        this function while mine just called the function already created '''
    neg_count = 0
    for term in negative_terms:
        neg_count += text.count(term) 
        if neg_count >= 2:
           text = text.replace(term, len(term) * '*')
    return text
        
    
# print(negative_find_replace(multi_find_replace(email_three, proprietary_terms), negative_words))

# task 5
all_words = proprietary_terms + negative_words
print(all_words)
def fore_aft_find_replace(text, search_terms):
    ''' Difference between my function & the solution:
        Same as task four as regards carriage returns (new lines) and
        punctuation. My function converted the text to a list like the
        solution did in this task as well as task 4. '''
    email_list = list(text.split(' '))
    index = 0
    for term in search_terms:
        if term in email_list:
            count = email_list.count(term)
            for i in range(count):
                index = email_list.index(term)
                email_list[index] =  len(term) * '*'
                email_list[index - 1] = len(term) * '*'
                email_list[index + 1] = len(term) * '*'

    listToStr = ' '.join([str(elem) for elem in email_list])
    return listToStr

print(fore_aft_find_replace(email_four, all_words))

# I give myself a B grade on this project. The solution addressed details
# that mine didn't. Overall, my project reproduced the desired results
# with far fewer lines of code than the solution.

