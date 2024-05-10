class ClienteValidators:

    @staticmethod
    def cpf_numeric(cpf):
        return cpf.isdigit()

    @staticmethod
    def cpf_valid(cpf):
        return len(cpf) == 11

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
    def celular_numeric(celular):
        return celular.isdigit()

    @staticmethod
    def celular_valid(celular):
        return len(celular) == 11
