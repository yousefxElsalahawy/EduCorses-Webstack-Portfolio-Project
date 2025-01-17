import secrets
from PIL import Image
import os
from pythonic import app

def save_video(form_video, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_video.filename)
    
    if not f_ext:
        raise ValueError("Invalid file extension for video")
    
    video_fn = random_hex + f_ext
    video_path = os.path.join(os.getcwd(), folder, video_fn)

    # إنشاء المجلد إذا لم يكن موجودًا
    os.makedirs(os.path.dirname(video_path), exist_ok=True)
    
    form_video.save(video_path)
    return video_fn

    
def save_picture(form_picture, path, output_size=None):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    
    if not f_ext:
        raise ValueError("Invalid file extension for picture")
    
    picture_name = random_hex + f_ext
    picture_path = os.path.join(app.root_path, path, picture_name)

    # إنشاء المجلد إذا لم يكن موجودًا
    os.makedirs(os.path.dirname(picture_path), exist_ok=True)
    
    i = Image.open(form_picture)
    if output_size:
        i.thumbnail(output_size)
    i.save(picture_path)
    return picture_name

def get_previous_next_lesson(lesson):
    course = lesson.course_name
    for lsn in course.lessons:
        if lsn.title == lesson.title:
            index = course.lessons.index(lsn)
            previous_lesson = course.lessons[index - 1] if index > 0 else None
            next_lesson = (
                course.lessons[index + 1] if index < len(course.lessons) - 1 else None
            )
            break
    return previous_lesson, next_lesson
