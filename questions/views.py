from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category, Question


def redirect_by_role(user):
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')
    return redirect('student_dashboard')


# ════════════════════════════════════════════════════════════════════════════
#  CATEGORIES
# ════════════════════════════════════════════════════════════════════════════

@login_required
def categories_list(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    categories = Category.objects.prefetch_related('questions').all()
    return render(request, 'questions/categories/index.html', {'categories': categories})


@login_required
def category_create(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    if request.method == 'POST':
        name        = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if not name:
            messages.error(request, 'Category name is required.')
            return render(request, 'questions/categories/create.html')

        if Category.objects.filter(name__iexact=name).exists():
            messages.error(request, 'A category with this name already exists.')
            return render(request, 'questions/categories/create.html')

        Category.objects.create(name=name, description=description)
        messages.success(request, 'Category created successfully.')
        return redirect('categories_list')

    return render(request, 'questions/categories/create.html')


@login_required
def category_edit(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        name        = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if not name:
            messages.error(request, 'Category name is required.')
            return render(request, 'questions/categories/edit.html', {'category': category})

        if Category.objects.filter(name__iexact=name).exclude(pk=pk).exists():
            messages.error(request, 'A category with this name already exists.')
            return render(request, 'questions/categories/edit.html', {'category': category})

        category.name        = name
        category.description = description
        category.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('categories_list')

    return render(request, 'questions/categories/edit.html', {'category': category})


@login_required
def category_delete(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    category = get_object_or_404(Category, pk=pk)
    # Questions with this category will have category set to NULL (SET_NULL)
    category.delete()
    messages.success(request, 'Category deleted. Its questions are now uncategorised.')
    return redirect('categories_list')


# ════════════════════════════════════════════════════════════════════════════
#  QUESTIONS
# ════════════════════════════════════════════════════════════════════════════

@login_required
def questions_list(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    category_id = request.GET.get('category')
    q_type      = request.GET.get('type')

    questions  = Question.objects.select_related('category').all()
    categories = Category.objects.all()

    if category_id:
        questions = questions.filter(category_id=category_id)
    if q_type in ('scored', 'open'):
        questions = questions.filter(type=q_type)

    return render(request, 'questions/questions/index.html', {
        'questions':          questions,
        'categories':         categories,
        'selected_category':  category_id,
        'selected_type':      q_type,
    })


@login_required
def question_create(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    categories = Category.objects.all()

    if request.method == 'POST':
        text        = request.POST.get('text', '').strip()
        q_type      = request.POST.get('type', 'scored')
        category_id = request.POST.get('category_id', '')

        if not text:
            messages.error(request, 'Question text is required.')
            return render(request, 'questions/questions/create.html', {'categories': categories})

        if q_type not in ('scored', 'open'):
            q_type = 'scored'

        category = None
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                pass

        Question.objects.create(text=text, type=q_type, category=category)
        messages.success(request, 'Question created successfully.')
        return redirect('questions_list')

    return render(request, 'questions/questions/create.html', {'categories': categories})


@login_required
def question_edit(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    question   = get_object_or_404(Question, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        text        = request.POST.get('text', '').strip()
        q_type      = request.POST.get('type', 'scored')
        category_id = request.POST.get('category_id', '')

        if not text:
            messages.error(request, 'Question text is required.')
            return render(request, 'questions/questions/edit.html', {
                'question': question, 'categories': categories
            })

        if q_type not in ('scored', 'open'):
            q_type = 'scored'

        category = None
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                pass

        question.text     = text
        question.type     = q_type
        question.category = category
        question.save()
        messages.success(request, 'Question updated successfully.')
        return redirect('questions_list')

    return render(request, 'questions/questions/edit.html', {
        'question': question, 'categories': categories
    })


@login_required
def question_toggle(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    question          = get_object_or_404(Question, pk=pk)
    question.is_active = not question.is_active
    question.save()
    status = 'activated' if question.is_active else 'deactivated'
    messages.success(request, f'Question {status} successfully.')
    return redirect('questions_list')


@login_required
def question_delete(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    question = get_object_or_404(Question, pk=pk)
    question.delete()
    messages.success(request, 'Question deleted successfully.')
    return redirect('questions_list')
