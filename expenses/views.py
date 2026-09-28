from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from .models import Expense
from .forms import ExpenseForm


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(
        user=request.user
    ).order_by("-date", "-created_at")

    total_expense = expenses.aggregate(
        total=Sum("amount")
    )["total"] or 0

    expense_count = expenses.count()

    average_expense = (
        float(total_expense) / expense_count
        if expense_count > 0
        else 0
    )

    category_data = (
        expenses
        .values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    category_labels = [
        item["category"]
        for item in category_data
    ]

    category_values = [
        float(item["total"])
        for item in category_data
    ]

    monthly_data = (
        expenses
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )

    monthly_labels = [
        item["month"].strftime("%b %Y")
        for item in monthly_data
    ]

    monthly_values = [
        float(item["total"])
        for item in monthly_data
    ]

    context = {
        "expenses": expenses[:8],
        "total_expense": total_expense,
        "expense_count": expense_count,
        "average_expense": round(average_expense, 2),
        "category_labels": category_labels,
        "category_values": category_values,
        "monthly_labels": monthly_labels,
        "monthly_values": monthly_values,
    }

    return render(request, "dashboard.html", context)


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(
                request,
                "Expense added successfully!"
            )
            return redirect("dashboard")
    else:
        form = ExpenseForm()

    return render(
        request,
        "add_expense.html",
        {"form": form},
    )


@login_required
def edit_expense(request, id):
    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user,
    )

    if request.method == "POST":
        form = ExpenseForm(
            request.POST,
            instance=expense,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Expense updated successfully!"
            )
            return redirect("dashboard")
    else:
        form = ExpenseForm(instance=expense)

    return render(
        request,
        "edit_expense.html",
        {
            "form": form,
            "expense": expense,
        },
    )


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user,
    )
    expense.delete()

    messages.success(
        request,
        "Expense deleted successfully!"
    )

    return redirect("dashboard")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Account created successfully!"
            )

            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(
        request,
        "register.html",
        {"form": form},
    )


def user_logout(request):
    logout(request)
    return redirect("login")
