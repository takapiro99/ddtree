from django.shortcuts import render
import json
from django.http.response import JsonResponse, HttpResponse
from django.http import QueryDict, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Tree

@ensure_csrf_cookie
# Create your views here.
#index
#tree
#about
#post
#waitinglist

def tree(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"tree.html",params)

def about(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"about.html",params)

def post(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"post.html",params)

def waitinglist(request):
    print(str(Tree.objects.all().count()) +"trees have been posted since.")
    print(str(Tree.objects.filter(lighted=False).count())+" trees are not lighted yet.")
    loook=[]
    wlist = Tree.objects.filter(lighted=False).order_by('date')[:10]
    print(wlist[0],wlist[1])
    for i in range(10):
        if wlist[i]==1:
            a="かわいい"
        if wlist[i]==2:
            a="かっこいい"
        if wlist[i]==3:
            a="おもしろい"
        if wlist[i]==4:
            a="おしゃれ"
        if wlist[i]==5:
            a="映え"
        if wlist[i]==6:
            a="文字"
        
    #question = get_object_or_404(Question, pk=question_id)
    
    print(type(wlist))
    print(wlist)
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",
            "wlist": wlist,
            "loook": loook,}
    print(loook)
    return render(request,"waitinglist.html",params)




def index(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",
        }
        return render(request, "index.html", params)
    else:
        return HttpResponse("please get to this page")


def table(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "posttest",
        }
        return render(request, "table.html", params)

def canvas(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "posttest",
        }
        return render(request, "canvasing.html", params)

def posttest(request):
    if request.method == 'GET':
        return HttpResponse("you've http getted to this page")
    if request.method =='POST':
        
        print("posted")
        aa = "<style>body{margin:100px;}</style>"
        aa+="your data is :<br><small>"
        aa=""
        for i in range(len(request.POST)-1):
            aaa = request.POST[str(i)]
            color = aaa.replace("rgb","")
            color = aaa.replace("#","0x")
            aa+="\r"
            aa+=color
        if len(aa)!=837:
            return HttpResponse("data unproperly sent. please post it again.")
        else:
            treedata = Tree(data=aa, name="testname", look=2)
            treedata.save()
            print("record has created!")
            return HttpResponse(aa)





def posted(request):
    if request.method =="POST":
        a="aa"
        
        params={a:1}
        return render(request, "done.html", params)

def esp(request):
    if request.method == "GET":
        #params={a:1,b:2}
        #ret={"1":"#ffff00","2":"#ffa500"}
        ret=""
        for j in range(93):
        #    ret+="#00ff00"
        #    ret+='\r'            
            ret+="000"
            ret+='\r'            
            ret+="255"
            ret+='\r'
            ret+="000"
            ret+='\r'
            j += 1
        #ret="#ff0000"+"\r"+"#123456"+"\r"+"#098123"+"\r"+"#098654"
        return  HttpResponse(ret)   

def stats(request):
    if request.method == "GET":
        return render(request, "stats.html")



