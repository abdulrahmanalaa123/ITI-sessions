# entities in our database
- Students
- Instructors
- Courses (Price, Modules (videos list with file paths or source links))
- course category (either an enum or a seperate entity which idk what is the optimal yet)
- Cart
- Wishlist
- Notification System
- Learning progress (probably a relation between the courses and the student)
- Order,payments,orderlines
- cart items can be exported into order lines, etc.
- cart items
# relations
- Many students may buy courses
- Courses may have many instructors ( as a beginning we can start with forcing one instructor)
- The instructor is basically an account with student privelage and an instructor privelage in his own course
- User has only one cart and one wishlist
