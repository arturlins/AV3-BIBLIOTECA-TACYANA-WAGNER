from datetime import date
from services.admin_services import list_books, list_book_category, add_new_book, list_all_book_authors, list_book_publisher, remove_book, add_book_author, remove_book_author, edit_books_titles, edit_books_quantities
from services.students_services import rent_book
from services.users_services import login_worker
from utils.utils import get_book_id, list_books, list_books_authors_only, list_books_simpler, get_publisher_id, get_category_id, get_author_id

#list_books()
#list_book_category()
#add_book_category()
#add_new_book()
#print(get_book_id())
#list_all_book_authors()
#list_book_publisher()
#list_books_simpler()
#remove_book()
#print(date.today())
#login_worker()
#rent_book()
#add_book_author()
#remove_book_author()
#list_books_authors_only()
# print(get_book_id())
# print(get_publisher_id())
# print(get_category_id())
# print(get_author_id())
#edit_books_titles()
#print(get_books_ids_list())
edit_books_quantities()