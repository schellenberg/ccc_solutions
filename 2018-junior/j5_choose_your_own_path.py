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
    
    return len(visited_pages) == pages[0]
    
    
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
