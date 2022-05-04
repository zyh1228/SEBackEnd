from os import path

from seBackEnd.settings import OBJ_COVER_FOLDER, OBJ_MODEL_FOLDER


def upload_obj_cover_dir(instance=None, filename=None):

    if hasattr(instance, 'file_dir_id'):
        file_dir_id = instance.file_dir_id
        return path.join(OBJ_COVER_FOLDER, file_dir_id, filename)

    return filename


def upload_obj_model_dir(instance=None, filename=None):

    if hasattr(instance, 'file_dir_id'):
        file_dir_id = instance.file_dir_id
        return path.join(OBJ_MODEL_FOLDER, file_dir_id, filename)

    return filename
