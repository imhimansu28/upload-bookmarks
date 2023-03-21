import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import BookmarkUploadForm
from .models import Bookmark


def bookmark(request):
    # Get page parameter from request.GET
    page_number = request.GET.get("page")
    page_size = 15
    bookmarks = Bookmark.objects.filter(user=request.user).order_by(
        "-created_at"
    )
    paginator = Paginator(bookmarks, page_size)
    bookmarks = paginator.get_page(page_number)
    context = {"bookmarks": bookmarks}
    return render(request, "bookmark-view.html", context)


@login_required
def bookmark_upload(request):
    if request.method == "POST":
        form = BookmarkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Load the JSON data from the uploaded file
            try:
                jsonfile = request.FILES["file"]
                data = json.load(jsonfile)

            except json.JSONDecodeError:
                messages.error(request, "File is not valid JSON")
                return redirect("bookmark:bookmark_import")
            # Create a Bookmark object for each item in the JSON data
            bookmarks = []
            for item in data:
                try:
                    bookmark = Bookmark(
                        user=request.user, title=item["title"], url=item["url"]
                    )
                    bookmarks.append(bookmark)
                except KeyError:
                    continue
            Bookmark.objects.bulk_create(bookmarks)

            messages.success(request, "Bookmarks imported successfully")
            return redirect("bookmark:bookmark")
    else:
        form = BookmarkUploadForm()
    return render(
        request, "bookmark-upload.html", {"form": form, "error": form.errors}
    )
