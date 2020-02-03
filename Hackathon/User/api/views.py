from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


User = get_user_model()
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# Create your views here.
from django.core.mail import EmailMessage

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import(
RegistrationSerializer,
LoginSerializer
)
@api_view(['POST',])
#permission_classes = [AllowAny]
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        print("1")
        data={}
        if serializer.is_valid():
            print("1")
            account=serializer.save()
            print("1")
            data['status']=status.HTTP_201_CREATED
            data['response']="Succesfully created kindly confirm mail to activate the account "
            #token=Token.objects.create(user=account).key
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': account,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(account.pk)),
                'token':account_activation_token.make_token(account),
            })
            to_email = account.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
        else:
           # data=serializer.errors
            data['problem']='ddd'
        return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))

def activate(request, uidb64, token):
    context={}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
       # user.profile.email_confirmed = True
        user.save()
        #login(request, user)
        context['status']=status.HTTP_201_CREATED
    return Response(context)


@api_view(['POST',])
@permission_classes((AllowAny,))
def ObtainAuthTokenView(request):
    if request.method=='POST':
        serializer=LoginSerializer(data=request.data)
        context={}
        if serializer.is_valid(raise_exception=True):
            #serializer.save()
            usernam=serializer.validated_data['username']
            passwor=serializer.validated_data['password']
            account=authenticate(username=usernam ,password=passwor)
            if account:
                token=Token.objects.create(user=account)
                context['status']=200
                context['token'] = token.key
                context['Is_Organization']=account.Is_Organization
                context['Is_Candidate']=account.Is_Candidate
                context['Is_University']=account.Is_University
            else:
                context['response'] = 'Error'
                context['error_message'] = 'Invalid credentials'
        else:
            context['status']: 440
        return Response(context)
