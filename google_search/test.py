from google import google
num_page =1
search_results = google.search('type:pdf django documentation 1.9..1.11 ', num_page)
print search_results[0].name