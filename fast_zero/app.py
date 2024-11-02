from fastapi import FastAPI

from http import HTTPStatus

from schemas import Message, UserSchema, UserPublic


app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema): 
    '''note que o cliente envia no modelo userschema,
     mas a resposta é userpublic, q n mostra sua senha'''
    return user
