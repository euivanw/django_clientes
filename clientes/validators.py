import re


class ClienteValidators:
    @staticmethod
    def cpf_numeric(cpf):
        return cpf.isdigit()

    @staticmethod
    def cpf_valid(cpf):
        return len(cpf) >= 11

    @staticmethod
    def nome_valid(nome):
        return nome.isalpha()

    @staticmethod
    def rg_numeric(rg):
        return rg.isdigit()

    @staticmethod
    def rg_valid(rg):
        return len(rg) == 11

    @staticmethod
    def celular_format(celular):
        """ Valida se o formato do celular é 11 99999-9999 """
        expressao = r'[\d]{2} [\d]{5}-[\d]{4}'

        return re.findall(expressao, celular)
