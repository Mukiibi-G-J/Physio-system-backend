from rest_framework import serializers
from authentication.models import CustomUser as User
from django.contrib.auth import password_validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authentication.models import Department


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)


    class Meta:
        model = User
        fields = ['email', 'username','password', 'first_name', 'last_name', 'phone_number','department']

    def validate(self, attrs):
        print("attrs>",attrs)
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': ('Email is already in use')})
        #? check username is alphanumeric exmaple: john123
        #? usernames that are not alphanumeric look like this: john@123, john_123, john-123, john 123
        if not username.isalnum():
            raise serializers.ValidationError(
                {"error": "The username should only contain alphanumeric characters"})
            
        # check for password strength
        #? check if password is strong enough with django AUTTH_PASSWORD_VALIDATORS

        # if not password_validation.validate_password(password):
        #     raise serializers.ValidationError(
        #         {"password": "The password is not strong enough"})  
        
        return attrs
    

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        password = validated_data['password']
        department_name = validated_data['department']
        department_instance = Department.objects.get(name=department_name)
        
        # Set the department for the user instance
        instance.department = department_instance
        if password is not None:
            instance.set_password(validated_data['password'])
        
        instance.save()
        # the instance is the user object
        print("instamce>",instance)
        return instance
  


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['token', 'email']
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # Validate if user is verified
    
    def validate(self, attrs):
        #? Sturcture of attrs is: ([('email', 'k4@gmail.com'), ('password', '12345678')])
        #? get the user from the email
        email = attrs.get('email', '')
        self.user = User.objects.filter(email=email).first()
       #? chek if user is verified
        if self.user is None:
            raise serializers.ValidationError(
                {"error": "Invalid credentials please try again"})
        if not self.user.is_verified:
            raise serializers.ValidationError(
                {"error": "Please verify your email before login"})
        return super().validate(attrs)
     
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['department'] = user.department.name
        # ...

        return token    