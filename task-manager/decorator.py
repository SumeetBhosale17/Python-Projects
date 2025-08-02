def log_actions(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper
