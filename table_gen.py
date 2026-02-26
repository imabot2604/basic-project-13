def make_table(headers, rows): return f"| {" | ".join(headers)} |"
if __name__ == "__main__":
    print(make_table(["ID", "Name"], ["1", "Test"]))
