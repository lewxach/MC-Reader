def read_session_lock(file_path):
    try:
        with open(file_path, 'rb') as f:
            lock_data = f.read()
            print(f"Session lock data: {lock_data}")
    except Exception as e:
        print(f"Error reading session.lock file {file_path}: {e}")