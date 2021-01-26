from rest_framework.fields import CharField, UUIDField
from rest_framework.serializers import Serializer

from restdoctor.rest_framework.resources import ResourceViewSet
from restdoctor.rest_framework.viewsets import ModelViewSet, ListModelViewSet


class DefaultSerializer(Serializer):
    default_field = CharField()


class AnotherSerializer(Serializer):
    another_field = CharField()


class CreateSerializer(Serializer):
    create_field = CharField()


class ListSerializer(Serializer):
    list_field = CharField()

class ListFilterSerialiser(Serializer):
    filter_uuid_field = UUIDField(required=False)
    filter_field = CharField(allow_null=True, help_text='Help text')

class SerializerClassMapViewSet(ModelViewSet):
    serializer_class_map = {
        'default': DefaultSerializer,
        'list': {
            'response': ListSerializer,
        },
        'create': {
            'response': CreateSerializer,
        },
    }


class DefaultViewSet(ModelViewSet):
    serializer_class = DefaultSerializer


class AnotherViewSet(ModelViewSet):
    serializer_class = AnotherSerializer


class ViewSetWithTags(ModelViewSet):
    schema_tags = ['tag1', 'tag2']
    serializer_class = DefaultSerializer


class ListViewSetWithRequestSerializer(ListModelViewSet):
    pagination_class = None
    schema_tags = ['tag']
    serializer_class_map = {
        'default': DefaultSerializer,
        'list': {
            'request': ListFilterSerialiser,
        }
    }


class DefaultAnotherResourceViewSet(ResourceViewSet):
    default_discriminative_value = 'default'
    resource_views_map = {
        'default': DefaultViewSet,
        'another': AnotherViewSet,
    }
