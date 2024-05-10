import re

from validate_docbr import CPF


class ClienteValidators:
    """ Classe para validações de dados do modelo de clientes """

    @staticmethod
    def cpf_valid(numero_cpf):
        """ Valida se o CPF é válido """
        return CPF().validate(numero_cpf)

    @staticmethod
    def nome_valid(nome):
        """ Valida se o nome é alfanumérico """
        return nome.isalpha()

    @staticmethod
    def rg_numeric(rg):
        """ Valida se o RG possui apenas números """
        return rg.isdigit()

    @staticmethod
    def rg_valid(rg):
        """ Valida se o RG tem 11 dígitos """
        return len(rg) == 11

    @staticmethod
    def celular_format(celular):
        """ Valida se o formato do celular é 11 99999-9999 """
        expressao = r'[\d]{2} [\d]{5}-[\d]{4}'

        return re.findall(expressao, celular)
