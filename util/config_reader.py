def read_config(file_path):
    config = {}
    
    with open(file_path, 'r') as f:
        text = f.read()
        for line in text.splitlines():
            line = line.split('#', 1)[0]    # remove comments
            key, value = [x.strip() for x in line.split(':', 1)]
            config[key] = value
        return config
