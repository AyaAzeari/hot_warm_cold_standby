import time
import shutil

SOURCE = "/Users/ayaazeari/cybersecurity/DB/orders.db"
DESTINATION = "/Users/ayaazeari/cybersecurity/Backups/hot/orders.db"

def hot_standby():
    print("Hot standby is running...")
    try:
        while True:
            shutil.copy(SOURCE, DESTINATION)
            print(f"Hot backup synchronized at {time.ctime()}")
            # 1 sec before the next backup
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nHot standby stopped.")
    except FileNotFoundError:
        print(f"Error: Source file {SOURCE} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    hot_standby()
