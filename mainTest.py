from main import helloWorld

def testHelloWorld():
    assert helloWorld() == "Hello World"
    print("PASSEDD")
    
if __name__ == "__main__":
    testHelloWorld()