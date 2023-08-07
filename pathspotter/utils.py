import os


def export_dir(local_dir, file_origin):
    file_path = os.path.dirname(file_origin)
    head_path = os.path.split(file_path)[0]
    head_path = os.path.split(head_path)[0]
    return os.path.join(head_path, local_dir)