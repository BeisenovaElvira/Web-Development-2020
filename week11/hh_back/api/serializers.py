from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(default='')
    city = serializers.CharField(max_length=300)
    address = serializers.CharField(default='')

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('default'),
                                         city=validated_data.get('city'),
                                         address=validated_data.get('address'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        field = ('id', 'name', 'description', 'salary', 'company_id')


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'vacancies')
