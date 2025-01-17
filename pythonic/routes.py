from pythonic.models import User, Lesson, Course
from flask import render_template, url_for, flash, redirect, request, session,jsonify,abort
from pythonic.forms import (
    NewCourseForm,
    NewLessonForm,
    RegistrationForm,
    LoginForm,
    UpdateProfileForm,
)
from pythonic import app, bcrypt, db
from pythonic.utils import save_picture, save_video
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
    login_required,
)

from werkzeug.utils import secure_filename


@app.route("/")
@app.route("/home")
def home():
    lessons = Lesson.query.all()
    courses = Course.query.all()
    return render_template("home.html", lessons=lessons, courses=courses)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            fname=form.fname.data,
            lname=form.lname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard", active_tab=None)


@app.route("/dashboard/profile", methods=["GET", "POST"])
@login_required
def profile():
    profile_form = UpdateProfileForm()
    if profile_form.validate_on_submit():
        if profile_form.picture.data:
            picture_file = save_picture(
                profile_form.picture.data, "static/user_pics", output_size=(150, 150)
            )
            current_user.image_file = picture_file
        current_user.username = profile_form.username.data
        current_user.email = profile_form.email.data
        current_user.bio = profile_form.bio.data
        db.session.commit()
        flash("Your profile has been updated", "success")
        return redirect(url_for("profile"))
    elif request.method == "GET":
        profile_form.username.data = current_user.username
        profile_form.email.data = current_user.email
        profile_form.bio.data = current_user.bio
    image_file = url_for("static", filename=f"user_pics/{current_user.image_file}")
    return render_template(
        "profile.html",
        title="Profile",
        profile_form=profile_form,
        image_file=image_file,
        active_tab="profile",
    )





@app.route("/dashboard/new_lesson", methods=["GET", "POST"])
@login_required
def new_lesson():
    new_lesson_form = NewLessonForm()
    new_course_form = NewCourseForm()

    form = ""
    flag = session.pop("flag", False)

    # تحديد نوع النموذج المرسل
    if "content" in request.form:
        form = "new_lesson_form"
    elif "description" in request.form:
        form = "new_course_form"

    # معالجة نموذج إضافة درس جديد
    if form == "new_lesson_form" and new_lesson_form.validate_on_submit():
        thumbnail_file = None
        video_file = None

        if new_lesson_form.thumbnail.data:
            try:
                thumbnail_file = save_picture(
                    new_lesson_form.thumbnail.data, "static/lesson_thumbnails"
                )
            except ValueError as e:
                flash(e.message, 'error')
                return redirect(url_for('new_lesson'))

        if new_lesson_form.video.data:
            try:
                video_file = save_video(
                    new_lesson_form.video.data, "pythonic/static/lesson_videos"
                )
            except ValueError as e:
                flash(e.message, 'error')
                return redirect(url_for('new_lesson'))

        lesson_slug = str(new_lesson_form.slug.data).replace(" ", "-")
        course = new_lesson_form.course.data
        lesson = Lesson(
            title=new_lesson_form.title.data,
            content=new_lesson_form.content.data,
            slug=lesson_slug,
            author=current_user,  # حفظ المستخدم الحالي
            course_name=course,
            thumbnail=thumbnail_file,
            video=video_file,
        )
        db.session.add(lesson)
        db.session.commit()
        flash("Your lesson has been created!", "success")
        return redirect(url_for("home"))

    # معالجة نموذج إضافة كورس جديد
    elif form == "new_course_form" and new_course_form.validate_on_submit():
        if new_course_form.icon.data:
            picture_file = save_picture(
                new_course_form.icon.data, "static/course_icons", output_size=(150, 150)
            )
        course_title = str(new_course_form.title.data).replace(" ", "-")
        course = Course(
            title=course_title,
            description=new_course_form.description.data,
            icon=picture_file,
        )
        db.session.add(course)
        db.session.commit()
        session["flag"] = True
        flash("New Course has been created!", "success")
        return redirect(url_for("dashboard"))

    # جلب أول 6 كورسات فقط من قاعدة البيانات
    courses = Course.query.limit(6).all()

    # تحديد النافذة المنبثقة التي ستظهر
    modal = None if flag else "newCourse"

    return render_template(
        "new_lesson.html",
        title="New Lesson",
        new_lesson_form=new_lesson_form,
        new_course_form=new_course_form,
        active_tab="new_lesson",
        modal=modal,
        courses=courses,  # تمرير الكورسات إلى القالب
    )

@app.route("/<string:course>/<string:lesson_slug>")
def lesson(course, lesson_slug):
    # أولاً نحصل على الكورس
    course_obj = Course.query.filter_by(title=course).first_or_404()
    
    # ثم نحصل على الدرس باستخدام الكورس والسلاج
    lesson = Lesson.query.filter_by(
        slug=lesson_slug,
        course_id=course_obj.id
    ).first_or_404()
    
    # نحصل على الدرس السابق والتالي
    previous_lesson = Lesson.query.filter(
        Lesson.course_id == lesson.course_id,
        Lesson.id < lesson.id
    ).order_by(Lesson.id.desc()).first()
    
    next_lesson = Lesson.query.filter(
        Lesson.course_id == lesson.course_id,
        Lesson.id > lesson.id
    ).order_by(Lesson.id.asc()).first()

    return render_template(
        "lesson.html",
        lesson=lesson,
        previous_lesson=previous_lesson,
        next_lesson=next_lesson
    )






@app.route("/<string:course_title>")
def course(course_title):
    course = Course.query.filter_by(title=course_title).first()
    course_id = course.id if course else None
    course = Course.query.get_or_404(course_id)
    return render_template(
        "course.html",
        title=course.title,
        course=course,
    )


@app.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("courses.html", title="Courses", courses=courses)



@app.route("/dashboard/user_lessons", methods=["GET", "POST"])
@login_required
def user_lessons():
    return render_template(
        "user_lessons.html", title="Your Lessons", active_tab="user_lessons"
    )


@app.route("/lesson/<lesson_id>/delete", methods=["POST"])
def delete_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if lesson.author != current_user:
        abort(403)
    db.session.delete(lesson)
    db.session.commit()
    flash("Your lesson has been deleted!", "success")
    return redirect(url_for("user_lessons"))
