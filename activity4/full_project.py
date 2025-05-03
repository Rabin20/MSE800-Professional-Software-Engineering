import csv

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")


class CSVProcessor(FileProcessor):
    def process(self):
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                print(f"\nCSV File: {self.file_path}")
                print(f"Total rows: {len(rows)}")
                if rows:
                    print("Header:", rows[0])
                    print("First row:", rows[1] if len(rows) > 1 else "N/A")
        except Exception as e:
            print(f"Error reading CSV: {e}")


class TextProcessor(FileProcessor):
    def process(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                print(f"\nText File: {self.file_path}")
                print(f"Total lines: {len(lines)}")
                if lines:
                    print("First line:", lines[0].strip())
                    print("Last line:", lines[-1].strip())
        except Exception as e:
            print(f"Error reading TXT: {e}")


def main():
    print("Welcome to the File Processor Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Process CSV file")
        print("2. Process TXT file")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            file_path = input("Enter path to CSV file: ").strip()
            processor = CSVProcessor(file_path)
            processor.process()
        elif choice == '2':
            file_path = input("Enter path to TXT file: ").strip()
            processor = TextProcessor(file_path)
            processor.process()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
