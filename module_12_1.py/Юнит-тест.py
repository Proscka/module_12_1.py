import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0


    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("a")
        for i in range (10,5):
            runner.walk()
            self.assertEqual(runner.distance, 50)


    def test_run(self):
        runner = Runner("a")
        for i in range(10,10):
            runner.run()
            self.assertEqual(runner.distance, 100)


    def test_challenge(self):
        runner = Runner("a")
        runner = Runner("b")
        for i in range(10):
            runner.run()
        for i in range(10):
            runner.walk()
            self.assertNotEqual(runner.distance, 100)
            self.assertNotEqual(runner.distance, 50)

if __name__ == "__main__":
    unittest.main()