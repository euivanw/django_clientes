from rest_framework import serializers

from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve conter 11 dígitos.')
        return cpf

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome não deve incluir números.')
        return nome

    def validate_rg(self, rg):
        if len(rg) != 11:
            raise serializers.ValidationError('O RG deve conter 11 dígitos.')
        return rg

    def validate_celular(self, celular):
        if not celular.isdigit():
            raise serializers.ValidationError('O celular só pode conter números.')
        if len(celular) != 11:
            raise serializers.ValidationError('O celular deve conter 11 dígitos.')
        return celular
