from model.model import BottomUpModel

def main():
    alice = BottomUpModel()
    print("ALICE Model ready! Type 'exit' to quit.")

    while True:
        user_input = input("Du: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        alice.learn(user_input)
        response = alice.respond(user_input)
        print("ALICE:", response)

if __name__ == '__main__':
    main()
