# MINHA SOLUÇÃO

# def titulo():
#     print('1 - ADICIONAR TAREFA | 2 - LISTAR TAREFAS')
#     print('3 - DESFAZER | 4 - REFAZER | 5 - SAIR')
#     e = input('\n\tESCOLHA UMA OPÇÃO ACIMA: ')
#     return e
#
#
# def adiciona_tarefa():
#     tarefas.append(input('\tINFORME A TAREFA: '))
#     return tarefas
#
#
# def lista_tarefas(lista):
#     if len(lista) == 0:
#         print('ADICIONE TAREFAS ANTES DE LISTAR.')
#         return
#     else:
#         for tarefa in lista:
#             print(tarefa)
#
#
# def desfazer(lista):
#     if len(lista) > 0:
#         auxiliar.append(lista[-1])
#         lista.pop()
#         return lista
#     else:
#         print('NÃO EXISTE NENHUMA AÇÃO PARA DESFAZER')
#
#
# def refazer(lista):
#     if len(auxiliar) > 0:
#         lista.append(auxiliar[-1])
#         auxiliar.pop()
#     else:
#         print('NÃO EXISTE NENHUMA AÇÃO PARA REFAZER')
#
#
# auxiliar = []
# tarefas = []
# while True:
#     escolha = titulo()
#     if escolha == '1':
#        adiciona_tarefa()
#     elif escolha == '2':
#         lista_tarefas(tarefas)
#     elif escolha == '3':
#         desfazer(tarefas)
#     elif escolha == '4':
#         refazer(tarefas)
#     elif escolha == '5':
#         break
#     else:
#         print('INFORME UMA OPÇÃO VÁLIDA.')

# SOLUCÇÃO DO PROFESSOR

"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
