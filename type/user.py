import strawberry
import typing
from config.db import conn
from modles.index import users

@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str

@strawberry.type
class Query:
    @strawberry.field
    def select_user(self, info, id:int) -> User:
        return conn.execute(users.select().where(users.c.id == id)).first()
    @strawberry.field
    def select_all_users(self, info) -> typing.List[User]:
        return conn.execute(users.select()).fetchall()
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> bool:
        result = conn.execute(users.insert().values(name=name, email=email, password=password))
        return int(result.inserted_primary_key[0])
    def update_user(self, info, id: int, name: str, email: str, password: str) -> str:
        result = conn.execute(users.update().where(users.c.id == id).values(name=name, email=email, password=password))
        return str(result.rowcount) + 'row(s) affected'
    def delete_user(self, info, id) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0    