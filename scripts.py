import random

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Lesson,
    Commendation
)


def create_commendation(diary, subject):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    lesson, lesson_date, teacher = find_lesson(subject)
    random_commendation = random.choice(commendations)
    created_commendation = Commendation.objects.create(
        schoolkid=diary,
        teacher=teacher,
        subject=lesson,
        created=lesson_date,
        text=random_commendation
    )


def get_class_name(diary):
    year_of_study = diary.year_of_study
    group_letter = diary.group_letter
    return year_of_study, group_letter


def fix_marks(diary):
    child_diary = Mark.objects.filter(schoolkid=diary)
    marks = Mark.objects.filter(schoolkid=diary, points__lt=4).update(points=5)


def remove_chastisements(diary):
    chastisements = Chastisement.objects.filter(schoolkid=diary)
    chastisements.delete()


def find_lesson(subject):
    try:
        year_of_study, group_letter = get_class_name(diary)
        lessons = Lesson.objects.filter(
            group_letter__contains=group_letter,
            year_of_study__contains=year_of_study,
            subject__title=subject
        ).order_by('date')
        first_lesson = lessons.first()
        if first_lesson:
            lesson = first_lesson.subject
            lesson_date = first_lesson.date
            teacher = first_lesson.teacher
            return lesson, lesson_date, teacher
    except Schoolkid.DoesNotExist:
        raise Http404('Проверьте правильность ввода')


def get_diary(name):
    try:
        diary = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        raise Http404('Проверьте правильность ввода')
    return diary






