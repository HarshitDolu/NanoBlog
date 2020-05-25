from django.shortcuts import render,HttpResponse,render,redirect
from .models import Post,blogcomment
from django.contrib import messages
# Create your views here.
#from blog.templatetags import extras
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request, slug):
    article=Post.objects.filter(slug=slug).first()
    comments=blogcomment.objects.filter(post=article,parent=None)
    replies = blogcomment.objects.filter(post=article).exclude(parent=None)
    repdict={}
    for reply in replies:
        if reply.parent.sno not in repdict.keys():
            repdict[reply.parent.sno]=[reply]
        else:
            repdict[reply.parent.sno].append(reply)
    context={'article':article,'comments':comments,'user':request.user,'repdict':repdict}
    return render(request,'blog/blogPost.html',context)


def postcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postsno=request.POST.get("postsno")
        post=Post.objects.get(sno=postsno)
        parentsno=request.POST.get('parentsno')
        if parentsno=="":
            comm = blogcomment(comment=comment, user=user, post=post)
            comm.save()
            messages.success(request, "comment posted")
        else:
            parent=blogcomment.objects.get(sno=parentsno)
            comm = blogcomment(comment=comment, user=user, post=post,parent=parent)





            comm.save()
            messages.success(request,"reply posted")
    return redirect(f"/blog/{post.slug}")



