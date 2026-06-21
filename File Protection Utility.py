import base64

print("1. Protect File Content")
print("2. Restore File Content")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    content = input("Enter file content: ")

    protected_content = base64.b64encode(content.encode()).decode()

    print("\nProtected Content:")
    print(protected_content)

elif choice == "2":
    protected_content = input("Enter protected content: ")

    try:
        original_content = base64.b64decode(protected_content.encode()).decode()

        print("\nRestored Content:")
        print(original_content)

    except:
        print("Invalid protected content.")

else:
    print("Invalid choice.")