from modules.engine import *

dis = make_discriminant(1, -2, -3) # Находим тип дискриминант из a: 1, b: -2, c: -3. Ссылочка на modules\engine.py.
print(make_general_solution(1, -2, dis)) # А вот и два икса, передаем ему тупл dis, который получили выше. Ссылка на modules\engine.py.