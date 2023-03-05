# @app.get('/')
# def ping():
#     return 'pong'
#
#
# @app.get(path='/hello',
#          tags=['hello'],
#          name='печатает хелло ворлд',
#          description='Возвращает типикал обучалку',
#          )
# def hello():
#     return {'msg': 'Hello world'}
#
#
# @app.get('/print')
# def pring_something(s: str = Query(default='Трава', title='Строка поиска',
#                                    min_length=5, max_length=64, deprecated=True)):
#     return {'msg': f'Печатаю что-та {s}'}
#
#
# @app.get('/printer/{smt}')
# def printer(smt: int = Path(include_in_schema=False)):
#     return {'msg': f'Печатаю что-та {smt}'}

def func(arr: int):
    pass

