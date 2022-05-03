from os import path

from seBackEnd.settings import OBJ_MODEL_FOLDER


def upload_dir(instance, filename):
    from objModel.models import ObjModel
    if isinstance(instance, ObjModel):
        file_dir_id = instance.file_dir_id
        return path.join(OBJ_MODEL_FOLDER, file_dir_id, filename)

    return filename
