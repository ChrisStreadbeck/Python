html = ['<h1>', 'Some Content', '</h1>']
html2 = ['<h1>', 'Some Content', 'more', '</h1>']


def scraper(the_scraped):
  new_list = the_scraped[1:-1]
  return new_list


print(scraper(html))
print(scraper(html2))

#works, but should use globbing

#one, two, three = [1, 2, 3]
#one == 1, 2 == 2, 3 == 3
#if you have more that three values in the list you can assign them to parts of a variable
#one, *two, three = [1, 2, 3, 4, 5]
#one == [1], two == [2, 3, 4], three == [5]

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


print(remove_first_and_last(html))
print(remove_first_and_last(html2))