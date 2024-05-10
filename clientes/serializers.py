from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import ClienteValidators


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, attrs):
        if not ClienteValidators.cpf_valid(attrs['cpf']):
            raise serializers.ValidationError({
                'cpf': 'O CPF informado não é valido.'
            })

        if not ClienteValidators.nome_valid(attrs['nome']):
            raise serializers.ValidationError({
                'nome': 'O nome não deve incluir números.'
            })

        if not ClienteValidators.rg_numeric(attrs['rg']):
            raise serializers.ValidationError({
                'rg': 'O RG só pode conter números.'
            })

        if not ClienteValidators.rg_valid(attrs['rg']):
            raise serializers.ValidationError({
                'rg': 'O RG deve conter 11 dígitos.'
            })

        if not ClienteValidators.celular_format(attrs['celular']):
            raise serializers.ValidationError({
                'celular': 'O celular deve estar no formato 11 98765-1234.'
            })

        return attrs
