from django_filters import rest_framework as filters
from api.models import Project,Scenario,Templates,TestCase,TestSuit,ExecutionRecord


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    statue = filters.NumberFilter(field_name="statue")
    class Meta:
        model = Project  # 模型名
        fields = ["name","statue"]

class TestSuitFilter(filters.FilterSet):
    module = filters.CharFilter(field_name="module", lookup_expr='icontains')
    statue = filters.NumberFilter(field_name="statue")
    project = filters.NumberFilter(field_name="project")
    class Meta:
        model = TestSuit
        fields = ["module","statue","project"]

class TestCaseFilter(filters.FilterSet):
    case = filters.CharFilter(field_name="case", lookup_expr='icontains')
    statue = filters.NumberFilter(field_name="statue")
    testsuit = filters.NumberFilter(field_name="testsuit")
    priority = filters.NumberFilter(field_name="priority")

    class Meta:
        model = TestCase
        fields = ["case","statue","priority","testsuit"]

class TemplateFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    method = filters.NumberFilter(field_name="method")
    start = filters.DateTimeFilter(field_name="create_time",lookup_expr="gte")
    end = filters.DateTimeFilter(field_name="create_time",lookup_expr="lte")
    class Meta:
        model = Templates
        fields = ["name","method","start","end"]

class ScenarioFilter(filters.FilterSet):
    cases = filters.CharFilter(field_name="cases")
    scenario = filters.CharFilter(field_name="scenario", lookup_expr='icontains')
    statue = filters.NumberFilter(field_name="statue")
    class Meta:
        model = Scenario
        fields = ["cases","scenario","statue"]

class ExecutionRecordFilter(filters.FilterSet):
    remark = filters.CharFilter(field_name="remark", lookup_expr='icontains')
    person = filters.CharFilter(field_name="person", lookup_expr='icontains')
    type = filters.NumberFilter(field_name="type")
    statue = filters.NumberFilter(field_name="statue")
    start = filters.DateTimeFilter(field_name="create_time",lookup_expr="gte")
    end = filters.DateTimeFilter(field_name="create_time",lookup_expr="lte")
    class Meta:
        model = ExecutionRecord
        fields = ["remark","type","statue"]

