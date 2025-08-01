import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            # Normalize keys to lowercase
            return [{'name': v.get('name') or v.get('Name', ''), 'time': v.get('time') or v.get('Time', '')} for v in data]
    except FileNotFoundError:
        return []

def safe_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):  # FIXED: loop variable name
        print(f"{index}. {video['name']}, Duration: {video['time']}")  # FIXED: consistent key access
    print("*" * 70)
    print("\n")

def add_videos(videos):
    name = input('Enter Video Name: ')
    time = input('Enter input time: ')
    videos.append({'name': name, 'time': time})  # FIXED: consistent keys
    safe_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    try:
        index = int(input('Enter the video number to be updated: '))
        if 1 <= index <= len(videos):
            name = input('Enter the new video name: ')
            time = input('Enter the new time: ')
            videos[index - 1] = {'name': name, 'time': time}
            safe_data_helper(videos)
        else:
            print("Invalid index selected")
    except ValueError:
        print("Please enter a valid number.")

def deleat_videos(videos):  # Kept name as-is (your original spelling)
    list_all_videos(videos)
    try:
        index = int(input('Enter a video number to be deleted: '))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            safe_data_helper(videos)
        else:
            print("Invalid video index selected")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | choose an option")
        print("1. List all YouTube Video")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Deleat a YouTube video")
        print("5. Exit the app")
        choise = input("Enter your choise: ")
        # print(videos)  # Optional: remove debug print

        match choise:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                deleat_videos(videos)
            case "5":
                break
            case _:
                print("Sorry you have entered some wrong input")

if __name__ == "__main__":
    main()
