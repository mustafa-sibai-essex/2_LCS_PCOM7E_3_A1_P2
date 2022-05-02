class User():
    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str

    def __init__(self,
                 id,
                 first_name,
                 last_name,
                 phone_number,
                 email):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
