from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from api.models import Project,Scenario,Templates,TestCase,TestSuit,ExecutionRecord
from api.data_type_parser import parser

class TemplateSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    method_display = serializers.CharField(source='get_method_display', read_only=True)

    def create(self, validated_data):
        headers={}
        for header in validated_data["header"]:
            headers.update({header["field"]:header["val"]})
        validated_data["header"]=headers
        template = Templates.objects.create(**validated_data)
        return template

    def update(self, instance, validated_data):
        headers = {}
        header_ = validated_data.get('header', instance.header)
        for header in header_:
            headers.update({header["field"]: header["val"]})
        instance.header = headers
        instance.name = validated_data.get('name',instance.name)
        instance.url = validated_data.get('url',instance.url)
        instance.method = validated_data.get('method',instance.method)
        instance.data = validated_data.get('data',instance.data)
        instance.statue = validated_data.get('statue',instance.statue)
        instance.linux_order_str = validated_data.get('linux_order_str',instance.linux_order_str)
        instance.process_name = validated_data.get('process_name',instance.process_name)
        instance.table_name = validated_data.get('table_name',instance.table_name)
        instance.save()
        return instance

    class Meta:
        model = Templates
        fields = "__all__"



class ScenarioSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    testcase = serializers.CharField(source='cases.case' , read_only=True)
    case_title = serializers.CharField(source='cases.case_title' , read_only=True)

    def create(self, validated_data):
        params={}
        for param in validated_data["parameter"]:
            param = parser(param)
            field = param["field"]+"@"+str(param["type"])
            params.update({field:param["val"]})
        validated_data["parameter"]=params

        expects = {}
        for expect in validated_data["validator"]:
            expect = parser(expect)
            expression = expect["expression"]+"@"+str(expect["mode"])+"@"+str(expect["type"])
            expects.update({expression: expect["val"]})
        validated_data["validator"] = expects

        scenario = Scenario.objects.create(**validated_data)
        return scenario

    def update(self, instance, validated_data):
        params = {}
        parameter_ = validated_data.get('parameter', instance.parameter)
        for param in parameter_:
            field = param["field"] + "@" + str(param["type"])
            params.update({field: param["val"]})
        instance.parameter = params

        vals = {}
        validator_ = validated_data.get('validator', instance.validator)
        for val in validator_:
            expression = val["expression"] + "@" + str(val["mode"]) +"@" + str(val["type"])
            vals.update({expression: val["val"]})
        instance.validator = vals

        instance.scenario = validated_data.get('scenario', instance.scenario)
        instance.cases = validated_data.get('cases', instance.cases)
        instance.statue = validated_data.get('statue', instance.statue)
        instance.save()
        return instance

    class Meta:
        model = Scenario
        fields = "__all__"


class TestCaseSerializer(serializers.ModelSerializer):
    case_scenario = ScenarioSerializer(many=True, read_only=True)
    casetemplate = serializers.SerializerMethodField()


    def get_casetemplate(self, obj):
        temp = TemplateSerializer(instance=obj.template)
        return temp.data

    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    module = serializers.CharField(source='testsuit.module', read_only=True)
    class_title = serializers.CharField(source='testsuit.class_title', read_only=True)

    class Meta:
        model = TestCase
        fields = "__all__"


class TestSuitSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    suit_case = TestCaseSerializer(many=True, read_only=True)
    projects = serializers.SerializerMethodField()

    def get_projects(self, obj):
        queryset = obj.project.all()
        projects = [row.name for row in queryset]
        return projects

    class Meta:
        model = TestSuit
        fields = "__all__"

    # def create(self, validated_data):
    #     validated_data["owner"] = self.context["request"].user
    #     return TestSuit.objects.create(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    testsuit_set = TestSuitSerializer(read_only=True, many=True)  # 根据project查询下面所有的suit

    class Meta:
        model = Project
        fields = "__all__"

    # def validate(self, attrs):
    #     from user.auther import Authenticator
    #     auth = Authenticator()
    #     user_obj, token = auth.authenticate(self.context["request"])
    #     print(user_obj, token)
    #     if not attrs.get("owner").user_id == user_obj.user_id:  # 通过context方法获取request对象
    #         raise ValidationError("所属者须和当前登录用户保持一致")
    #     return attrs

    # def create(self, validated_data):
    #     validated_data["owner"] = self.context["request"].user
    #     return ApiProject.objects.create(**validated_data)



class ExecutionRecordSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = ExecutionRecord
        fields = "__all__"
