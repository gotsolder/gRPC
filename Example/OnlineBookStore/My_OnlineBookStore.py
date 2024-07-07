# this is from the gRPC Udemy course.

import book_pb2

book = book_pb2.Book()
book.isbn = "978-0134685991"
book.title = "Effective Python"
# ...

serialized_book = book.SerializeToString()
print(f"serialized_book=<{serialized_book}>")

deserialize_book = book_pb2.Book()
deserialize_book.ParseFromString(serialized_book)

print(f"deserialize_book=<{deserialize_book}>")
