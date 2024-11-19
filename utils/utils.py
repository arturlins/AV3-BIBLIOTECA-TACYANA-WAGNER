def get_limited_input(prompt, max_length=100):
    while True:
        user_input = input(prompt)
        if len(user_input) <= max_length:
            return user_input
        else:
            print(f"Input exceeds {max_length} characters. Please try again.")