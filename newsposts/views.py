from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsPost


def get_newsposts(request):
    """
    Create a view that will return a list of Posts that were publisehd prior to 'now'
    and render them to the newsposts.html template
    """

    posts = NewsPost.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')
    return render(request, 'newsposts.html', {'posts': posts})


def news_detail(request, pk):
    """
    Create a view that return a single Post based in the post ID
    and render it to the 'articepost.html' template.
    or return a 404 error if the post is not found
    """
    print(pk)
    post = get_object_or_404(NewsPost, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'articlepost.html', {'post': post})

