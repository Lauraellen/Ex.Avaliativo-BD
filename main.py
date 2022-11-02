# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://34.201.73.28:7687', user='neo4j', password='airplane-hoists-dye')

# Questão 01
# A
def getTeacher(pessoa):
    return db.execute_query('match (t:Teacher{name: $name}) return t.ano_nasc, t.cpf', {'name': pessoa['name']})

person = {
    'name': 'Renzo',
}
wj(getTeacher(person), '1A')

# B
def getTeacherStartsWith(letter):
    return db.execute_query('match (t:Teacher) where t.name starts with $letter return t.name, t.cpf', {'letter': letter['startsWith']})

letter = {
    'startsWith': 'M',
}
wj(getTeacherStartsWith(letter), '1B')

# C

#wj(aux, '1C')

# D

#wj(aux, '1D')

# Questão 02
# A

#wj(aux, '2A')

# B

#wj(aux, '2B')

# C

#wj(aux, '2C')

# D

#wj(aux, '2D')

# Questão 03
# A

# B

# C

# D

