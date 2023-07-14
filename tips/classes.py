class User:
    def __init__(self, group: str, request: str) -> None:
        self.group = group
        self.request = request

def process_admin_request(user, request): print(user, request)
def process_manager_request(user, request): print(user, request)
def process_client_request(user, request): print(user, request)

user = User(group="admin", request="More money")

# if user.group == "admin":
#     process_admin_request(user, request)
# elif user.group == "manager":
#     process_manager_request(user, request)
# elif user.group == "client":
#     process_client_request(user, request)

group_to_process_method = {
        "admin": process_admin_request,
        "manager": process_manager_request,
        "client": process_client_request,
        }
group_to_process_method[user.group](user.group, user.request)
