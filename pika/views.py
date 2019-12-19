from django.shortcuts import render
import json
from django.http.response import JsonResponse, HttpResponse
from django.http import QueryDict, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Tree
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.conf import settings
from django.views import generic
from .forms import LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm
)


@ensure_csrf_cookie
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
    time = str(Tree.objects.filter(lighted=False).count())
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",
            "time" :time}
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

def posttest(request):
    if request.method == 'GET':
        return HttpResponse("you've http getted to this page")
    if request.method =='POST':
        print("posted")
        bb = ""
        for i in range(93):
            aa = hex2rgb(str(request.POST[str(i)]))
            ss = list(aa)
            for i in range(3):
               ss[i]=str(ss[i])
            for i in range(3):
                if (len(ss[i]))==1:
                    ss[i]="00"+str(ss[i])
                    break
                if (len(ss[i]))==2:
                    ss[i]="0"+str(ss[i])
            
            print(ss)
            #print("")
            #aaa = "".join(map(str,aa))
            #print(aaa)
            bb += "".join(map(str,ss))
            #bb += " "
        print(bb)
            #bb += "\r"
            #aa+=color
        #if len(aa)!=837:
            #return HttpResponse("data unproperly sent. please post it again.")
        #else:
        name = request.POST["name"]
        category = request.POST["category"]
        treedata = Tree(data=bb, name=name, look=category)
        treedata.save()
        print("record has created!")
        print(str(request.POST["name"]))
        print(str(request.POST["category"]))
        return HttpResponse(bb)

def esp(request):
    if request.method == "GET":
        if (Tree.objects.filter(lighted=False).order_by("date")):
            ss =  Tree.objects.filter(lighted=False).order_by("date").first()
            treedata = Tree(lighted=True)
            treedata.save()
            sss=""
            sss = ss.data
            #ssss=
            ww = ""
            n = 0
            for i in range(93):
                rr=""
                bb=""
                gg=""
                rr += sss[n]
                rr += sss[n+1]
                rr += sss[n+2]
                bb += sss[n+3]
                bb += sss[n+4]
                bb += sss[n+5]
                gg += sss[n+6]
                gg += sss[n+7]
                gg += sss[n+8]
                ww += gg
                ww += "\r"
                ww += rr
                ww += "\r"
                ww += bb

                n += 9
                ww += "\r"
            print(ss.name)

            #print((Tree.objects.filter(lighted=False).order_by("date").first()).data)
            return HttpResponse(ww)
        else:
            ss = Tree.objects.order_by("?").first()
            sss=""
            sss = ss.data
            for i in range(80):
                sss+=("00000000000000000000000000000000000000000000")
            #ssss=
            ww = ""
            n = 0
            for i in range(93):
                rr=""
                bb=""
                gg=""
                rr += sss[n]
                rr += sss[n+1]
                rr += sss[n+2]
                bb += sss[n+3]
                bb+= sss[n+4]
                bb+= sss[n+5]
                gg += sss[n+6]
                gg += sss[n+7]
                gg += sss[n+8]
                ww += gg
                ww += "\r"
                ww += rr
                ww += "\r"
                ww += bb

                n += 9
                ww += "\r"
            print(ss.date)
            return HttpResponse(ww)


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'pika/index.html'


User = get_user_model()





class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'pika/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('register/mail_template/create/subject.txt', context)
        message = render_to_string('register/mail_template/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('pika:user_create_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'pika/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'pika/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()