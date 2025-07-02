import os
import sys

def main():
    # Use environment variable or command-line argument to determine build result
    status = os.getenv("BUILD_STATUS") or (sys.argv[1] if len(sys.argv) > 1 else "success")

    print(f"Requested build status: {status}")

    if status.lower() == "success":
        print("✅ Build succeeded!")
        sys.exit(0)
    else:
        print("❌ Build failed due to simulated error.")
        sys.exit(1)

if __name__ == "__main__":
    main()
