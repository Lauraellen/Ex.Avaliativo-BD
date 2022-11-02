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
def getAllTheCities():
    return db.execute_query('match (c:City) return c.name')
wj(getAllTheCities(), '1C')

# D
def getSchools():
    return db.execute_query('match (s:School) where s.number >= 150 and s.number <= 550 return s.name, s.address, s.number')
wj(getSchools(), '1D')

# Questão 02
# A
def getYoungestOlderTeach():
    return db.execute_query('match (t:Teacher)  return max(t.ano_nasc) as professorMaisNovo, min(t.ano_nasc) as professorMaisVelho')
wj(getYoungestOlderTeach(), '2A')

# B
def getAvgPopulations():
    return db.execute_query('match (c:City) return avg(c.population)')
wj(getAvgPopulations(), '2B')

# C
def getCity(cep):
    return db.execute_query('match (c:City) where c.cep = $cep return replace(c.name, "a", "A") as cityName', {'cep': cep['cep']})

cep = {
    'cep': '37540-000',
}
wj(getCity(cep), '2C')

# D
def getSubstring():
    return db.execute_query('match (t:Teacher) return substring(t.name, 3, 1)')
wj(getSubstring(), '2D')

# Questão 03
# A

# B

# C

# D

