from rest_framework import serializers
from api.models import User, UserProfile, Task




class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """
    Task serializer.
    """
    class Meta:
        """
        Task fields to serialize.
        """
        model = Task
        fields = ('url', 'owner', 'title', 'description', 'completed', 'task_picture')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    UserProfile serializer.
    """
    class Meta:
        """
        UserProfile fields to serialize.
        """
        model = UserProfile
        fields = ('profile_picture', 'profile_banner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer, can use UserProfile serializer to get all informations about an user.
    """
    # Serialize profile field with UserProfileSerializer
    profile = UserProfileSerializer(required=True)
    tasks = TaskSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        """
        User fields to serialize
        """
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile', 'tasks')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        On user creation (Override default create method)
        """
        # Set profile_data to profile
        profile_data = validated_data.pop('profile')
        tasks_data = validated_data.pop('tasks')
        # Set password to password
        password = validated_data.pop('password')
        # Set user to all fields in userModel
        user = User(**validated_data)
        # Hash password and save it.
        user.set_password(password)
        user.save()
        # Create UserProfile according to User
        UserProfile.objects.create(user=user, **profile_data)
        Task.objects.create(owner=user, **tasks_data)

        return user

    def update(self, instance, validated_data):
        """
        On user update (Override default update method)
        """
        # Get profile_data
        profile_data = validated_data.pop('profile')
        tasks_data = validated_data.pop('tasks')
        # Get UserProfile instance
        profile = instance.profile
        tasks = instance.tasks

        # Update User fields
        # Previous data = (New validated data)
        instance.email = validated_data.get('email', instance.email)
        # Save updated User
        instance.save()

        # Update UserProfile fields
        # Previous data = (New validated data)
        profile.profile_picture = profile_data.get('profile_picture', profile.profile_picture)
        profile.profile_banner = profile_data.get('profile_banner', profile.profile_banner)
        # Tasks update
        tasks.title = tasks_data.get('title', tasks.title)
        tasks.description = tasks_data.get('description', tasks.description)
        tasks.completed = tasks_data.get('completed', tasks.completed)
        tasks.task_picture =  tasks_data.get('task_picture', tasks.task_picture)
        
        # Save updated UserProfile
        profile.save()

        return instance