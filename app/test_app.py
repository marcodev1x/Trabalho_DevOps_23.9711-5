import unittest
import json
import random
from app import app, db, Aluno

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        pass

    def test_add_aluno(self):
        ra_aleatorio = str(random.randint(100000, 999999))

        data = {"nome": "João", "ra": ra_aleatorio}
        response = self.client.post('/alunos', data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        aluno = Aluno.query.filter_by(ra=ra_aleatorio).first()
        self.assertIsNotNone(aluno)
        self.assertEqual(aluno.nome, "João")
        self.assertEqual(aluno.ra, ra_aleatorio)

if __name__ == '__main__':
    unittest.main()
