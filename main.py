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
class TeacherCrud(object):

    def __init__(self):
        self.db = db

    def create(self, teacher):
        return self.db.execute_query('create (t:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) return t',
                                     {'name': teacher['name'], 'ano_nasc': teacher['ano_nasc'], 'cpf': teacher['cpf']})

    def read(self, name):
        return self.db.execute_query('match (t:Teacher{name: $name}) return t',
                                     {'name': name['name']})

    def delete(self, name):
        return self.db.execute_query('match (t:Teacher{name: $name}) delete t',
                                     {'name': name['name']})

    def update(self, name, newCpf):
        return self.db.execute_query('match (t:Teacher{name: $name}) set t.cpf = $cpf return t',
                                     {'name': name, 'cpf': newCpf})
# B
teacherCrud = TeacherCrud()

teacher = {
    'name': 'Chris Lima',
    'ano_nasc': 1956,
    'cpf': '189.052.396-66'
}

wj(teacherCrud.create(teacher), '3A-CREATE')

# C
teacher = {
    'name': 'Chris Lima',
}
wj(teacherCrud.read(teacher), '3A-READ')

# D
name = 'Chris Lima'
newCpf = '162.052.777-77'
wj(teacherCrud.update(name, newCpf), '3A-UPDATE')





