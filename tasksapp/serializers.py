from tasksapp.models import HouseImage, House
from rest_framework import serializers


class ImagesSerialzier(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = ['id','house','image']



class MainSerializer(serializers.ModelSerializer):
    images= ImagesSerialzier(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000,allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = House
        fields = ['price','description','area','number_of_rooms','parking','pets','toilets','bathroom','images','uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        house = House.objects.create(**validated_data)
        for image in uploaded_images:
            transaction=HouseImage.objects.create(house=house, image=image )

        return house



