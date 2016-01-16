#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
import os

#---------------------------------------------------
# Criado por: Wolfterro
# Versão: 1.0.0 - Python 2.x
# Data: 16/01/2016
#---------------------------------------------------

# Versão do programa
#===================
versao_programa = "1.0.0"

# Verificação da pasta 'Cadastros', onde será armazenado os cadastros
#====================================================================
verificar_pasta_cadastros = os.path.exists("Cadastros")

if verificar_pasta_cadastros == False:
    os.system("mkdir Cadastros")
    os.chdir("Cadastros")
else:
    os.chdir("Cadastros")

# Classe principal para cadastramento
#====================================
class Cadastro(object):
    
    # Resgatando a data atual
    #========================
    ano_atual = time.strftime("%Y")
    mes_atual = time.strftime("%m")
    dia_atual = time.strftime("%d")

    hora_atual = time.strftime("%H")
    minuto_atual = time.strftime("%M")
    segundo_atual = time.strftime("%S")
    
    # Método de inicialização da classe
    #==================================
    def __init__(self, nome, sobrenome, ano_nascimento, sexo, estado_civil, endereco, telefone, celular1, celular2, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.endereco = endereco
        self.telefone = telefone
        self.celular1 = celular1
        self.celular2 = celular2
        self.email = email
    
    # Imprimindo as informações na tela e retornando para escrita
    #============================================================
    def print_info(self):
        print "\nFicha de " + self.nome + " " + self.sobrenome + ":"
        print "=============================="
        
        return "Nome: " + self.nome + "\n" + \
                "Sobrenome: " + self.sobrenome + "\n" + \
                "Ano de nascimento: " + str(self.ano_nascimento) + "\n" + \
                "Idade: " + str(int(Cadastro.ano_atual) - self.ano_nascimento) + "\n" + \
                "Sexo: " + self.sexo + "\n" + \
                "Estado civil: " + self.estado_civil + "\n" + \
                "Endereço: " + self.endereco + "\n" + \
                "Telefone: " + self.telefone + "\n" + \
                "Celular (principal): " + self.celular1 + "\n" + \
                "Celular (adicional): " + self.celular2 + "\n" + \
                "E-mail: " + self.email
          
#=================================================================

# Método de inicialização do Programa
#====================================
def Inicializar_Programa():

    print "\nCadastramento 2016 - Versão " + versao_programa
    print "================================="
    print "\n* Este é um programa simples que mostra processos básicos de um cadastramento."
    print "* Este programa NÃO É RECOMENDADO para tarefas profissionais e trabalhos importantes."
    print "* Este programa é puramente 'educacional', desenvolvido para Linux em linguagem Python."
    print "* Durante o cadastramento, nomes e sobrenomes SÃO OBRIGATÓRIOS e NÃO PODEM POSSUIR espaços!"
    print "* Para cancelar um processo de cadastramento, use o comando 'CTRL + C', encerrando o programa.\n"

    print "Menu do programa:"
    print "=================\n"

    print "(1) Realizar cadastramento"
    print "(2) Listar cadastramentos\n"

    menu_escolha = raw_input("Qual operação deseja realizar (qualquer outra tecla para sair): ")

    if menu_escolha == "1":
        Cadastramento()
    elif menu_escolha == "2":
        Verificar_Cadastros()
    else:
        print "\nObrigado por utilizar Cadastramento 2016!"
        print "Saindo do programa...\n"
        os.system("sleep 3")
#=================================================================

# Método de cadastramento
#========================
def Cadastramento():

    # Processo de cadastramento
    #==========================
    print "\nRealizando cadastramento"
    print "========================\n"

    cadastrar_nome = raw_input("Qual é o seu nome: ")
    cadastrar_sobrenome = raw_input("Qual é o seu sobrenome: ")
    cadastrar_ano_nascimento = int(raw_input("Em que ano você nasceu: "))
    cadastrar_sexo = raw_input("Você é do sexo Feminino ou Masculino: ")
    cadastrar_estado_civil = raw_input("Qual é o seu estado civil: ")
    cadastrar_endereco = raw_input("Qual é o seu endereço: ")
    cadastrar_telefone = raw_input("Seu número de telefone (fixo): ")
    cadastrar_celular1 = raw_input("Seu número de celular (principal): ")
    cadastrar_celular2 = raw_input("Seu número de celular (adicional):")
    cadastrar_email = raw_input("Qual é o seu e-mail (opcional): ")

    # Verificação de espaços e campos vazios no nome e sobrenome
    #===========================================================
    cadastro_espaco = False

    if ' ' in cadastrar_nome:
        cadastro_espaco = True
    elif ' ' in cadastrar_sobrenome:
        cadastro_espaco = True

    if cadastrar_nome == "":
        cadastro_espaco = True
    elif cadastrar_sobrenome == "":
        cadastro_espaco = True

    if cadastro_espaco == False:

        cadastrado = Cadastro(cadastrar_nome, cadastrar_sobrenome, cadastrar_ano_nascimento, cadastrar_sexo, cadastrar_estado_civil, cadastrar_endereco, cadastrar_telefone, cadastrar_celular1, cadastrar_celular2, cadastrar_email)
        cadastrado_info = cadastrado.print_info()
        print cadastrado_info

        confirmar_cadastro = raw_input("\nAs informações estão corretas? [S/n]: ")
        confirmar_cadastro = confirmar_cadastro.upper()

        # Processo de salvamento de cadastro
        #===================================
        if confirmar_cadastro == "S":

            os.system("touch " + cadastrar_nome + "_" + cadastrar_sobrenome + "_-_" + Cadastro.hora_atual + ":" + Cadastro.minuto_atual + ":" + Cadastro.segundo_atual + "_-_" + Cadastro.dia_atual + "-" + Cadastro.mes_atual + "-" + Cadastro.ano_atual + ".txt")

            arquivo_cadastro = open(cadastrar_nome + "_" + cadastrar_sobrenome + "_-_" + Cadastro.hora_atual + ":" + Cadastro.minuto_atual + ":" + Cadastro.segundo_atual + "_-_" + Cadastro.dia_atual + "-" + Cadastro.mes_atual + "-" + Cadastro.ano_atual + ".txt", "w")
            arquivo_cadastro.write(str(cadastrado_info))

            arquivo_cadastro.close()

            print "\nCadastramento realizado com sucesso!\n"
            os.system("sleep 3")

        else:
            os.system("clear")
            Cadastramento()
    else:
        print "\nErro! Nome ou sobrenome possui espaços ou campo vazio!"
        print "Reiniciando cadastramento (ou pressione 'CTRL + C' para encerrar)..."
        os.system("sleep 5")
        os.system("clear")
        Cadastramento()

#=================================================================

# Método de verificação de cadastro
#==================================
def Verificar_Cadastros():

    listar_pasta_cadastros = os.listdir(".")

    print "\nListando cadastros existentes:"
    print "=============================="

    for lista_cadastrados in listar_pasta_cadastros:
        lista_cadastrados = lista_cadastrados.replace("_", " ").replace(" - ", " == ").replace("-", "/").replace(".txt", "")
        print lista_cadastrados

    print ""

# Inicializando Programa
#=======================
Inicializar_Programa()