from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=300, default='')
    city = serializers.CharField(max_length=300)
    address = serializers.CharField(default='')

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         city=validated_data.get('city'),
                                         address=validated_data.get('address'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=300, default='name')
    description = serializers.CharField(default='')
    salary = serializers.FloatField(default=1000)
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        #  field = ('id', 'name', 'description', 'salary', 'company_id')
        fields = '__all__'


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'vacancies')
