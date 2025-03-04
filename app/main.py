from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str) -> None:
    customer_objs = []
    for cust_dict in customers:
        c=Customer(name=cust_dict["name"], food=cust_dict["food"])
        CinemaBar.sell_product(product=c.food, customer=c)
        customer_objs.append(c)
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj)
