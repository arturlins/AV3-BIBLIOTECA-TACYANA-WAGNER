from datetime import date
from services.admin_services import list_books, list_book_category, add_new_book, list_book_author, list_book_publisher, remove_book, list_books_simpler, add_book_author, remove_book_author
from services.students_services import rent_book
from services.users_services import login_worker
from utils.utils import get_book_id, list_books, list_books_authors_only

list_books()
#list_book_category()
#add_book_category()
#add_new_book()
#print(get_book_id())
#list_book_author()
#list_book_publisher()
#list_books_simpler()
#remove_book()
#print(date.today())
#login_worker()
#rent_book()
#add_book_author()
#remove_book_author()
#list_books_authors_only()