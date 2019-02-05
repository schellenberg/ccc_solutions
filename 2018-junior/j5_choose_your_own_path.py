# j5 - choose your own path (2018)

# first element of list contains number of pages,
# rest of the pages contain a sublist of all reachable pages from that page

def are_all_pages_reachable(pages):
    visited_pages = []
    still_need_to_visit = [1]
    while len(still_need_to_visit) > 0:
        current_page = still_need_to_visit.pop()
        visited_pages.append(current_page)
        if len(pages[current_page]) > 1:
            for possible_page in pages[current_page]:
                if possible_page not in visited_pages and possible_page not in still_need_to_visit and possible_page != 0:
                    still_need_to_visit.append(possible_page)
        else:
            possible_page = pages[current_page][0]
            if possible_page not in visited_pages and possible_page not in still_need_to_visit and possible_page != 0:
                still_need_to_visit.append(possible_page)
    
    if len(visited_pages) == pages[0]:
        return "Y"
    else:
        return "N"
    

def breadth_first_shortest_path(pages):
    # populate with first level from page 1
    levels = []
    levels.append(extract_pages_to_include(pages[1]))
    
    current_depth = 0
    still_searching = True
    while still_searching:
        pages_to_visit = []
        for page in levels[current_depth]:
            linked_pages = extract_pages_to_include(pages[page])
            for possible_page in linked_pages:
                if possible_page not in pages_to_visit:
                    pages_to_visit.append(possible_page)
        levels.append(pages_to_visit)
    
        #check if we've found a path out!
        if 0 in levels[-1]:
            still_searching = False
        else:
            current_depth += 1
    
    return len(levels)
            

def extract_pages_to_include(page_data):
    if page_data[0] == 0:
        return [0]
    else:
        return page_data[1:]
        

def load_book():
    pages = []

    pages.append( int(input()) )

    for i in range(pages[0]):
        this_page = input()
        info = this_page.split()
        current_page = []
        for item in info:
            current_page.append(int(item))
        pages.append(current_page)

    return pages


######################################################
pages = load_book()
#print(pages)
print(are_all_pages_reachable(pages))
print(breadth_first_shortest_path(pages))