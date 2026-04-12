from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Quiz, QuizAttempt


def quiz_list(request):
    quizzes = Quiz.objects.filter(is_active=True)
    return render(request, 'quiz/list.html', {'quizzes': quizzes})


def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, is_active=True)
    questions = quiz.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        score = 0
        total = questions.count()
        results = []

        for question in questions:
            selected_id = request.POST.get(f'question_{question.id}')
            correct_choice = question.choices.filter(is_correct=True).first()
            is_correct = False
            if selected_id and correct_choice:
                is_correct = str(correct_choice.id) == selected_id
                if is_correct:
                    score += 1

            results.append({
                'question': question,
                'selected_id': int(selected_id) if selected_id else None,
                'correct_choice': correct_choice,
                'is_correct': is_correct,
            })

        if not request.session.session_key:
            request.session.create()

        attempt = QuizAttempt.objects.create(
            session_key=request.session.session_key,
            quiz=quiz,
            score=score,
            total=total,
        )

        return render(request, 'quiz/result.html', {
            'quiz': quiz,
            'score': score,
            'total': total,
            'results': results,
            'percentage': round(score / total * 100) if total else 0,
        })

    return render(request, 'quiz/take.html', {
        'quiz': quiz,
        'questions': questions,
    })
