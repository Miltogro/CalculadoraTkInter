import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
janela = ctk.CTk()
janela.title("Calculadora")
janela.iconbitmap('iconecalc.ico')
janela.minsize(290, 400)
janela.maxsize(290, 400)
font1 = ('Arial',40,'bold')
font2 = ('Arial',25,'bold')
font3 = ('Arial',15,'bold')

printar = ""

def show(valor):
    global printar
    printar += valor
    saida.insert(0, valor)

def clear():
    saida.delete(0)

def clearAll(): #APAGA TUDO DA SAIDA E LIMPA "PRINTAR"
    global printar
    saida.delete(0, 'end')
    printar = ""

def calcular():
    global printar
    try:
        resultado = eval(printar)
    except Exception: #LIMPA A SAÍDA E PRINTA O ERRO DEPOIS LIMPA "PRINTAR"
        saida.delete(0, 'end')
        saida.insert(0, "ERRO")
        printar = ""
    else: #LIMPA A SAÍDA E INSERE O RESULTADO, ATUALIZA A STR PRINTAR COM O RESULTADO
        saida.delete(0, 'end')
        saida.insert(0, resultado)
        printar = str(resultado)

saida = ctk.CTkEntry(janela, placeholder_text='', width=270, height= 100, font=font1)
saida.place(x=10, y=10)

botaoCA = ctk.CTkButton(janela, text='AC', width=60, height=25, command=clearAll, font=font3, fg_color='#b5520b')
botaoCA.place(x=220, y=120)

botaoClear = ctk.CTkButton(janela, text='C', width=60, height=25, command=clear, font=font3, fg_color='#b5520b')
botaoClear.place(x=220, y=155)

botao0 = ctk.CTkButton(janela, text='0', width=60, height=60, font=font2, command=lambda:show('0'), fg_color='#000000')
botao0.place(x=80, y=330)

botao1 = ctk.CTkButton(janela, text='1', width=60, height=60, font=font2, command=lambda:show('1'), fg_color='#000000')
botao1.place(x=150, y=260)

botao2 = ctk.CTkButton(janela, text='2', width=60, height=60, font=font2, command=lambda:show('2'), fg_color='#000000')
botao2.place(x=80, y=260)

botao3 = ctk.CTkButton(janela, text='3', width=60, height=60, font=font2, command=lambda:show('3'), fg_color='#000000')
botao3.place(x=10, y=260)

botao4 = ctk.CTkButton(janela, text='4', width=60, height=60, font=font2, command=lambda:show('4'), fg_color='#000000')
botao4.place(x=150, y=190)

botao5 = ctk.CTkButton(janela, text='5', width=60, height=60, font=font2, command=lambda:show('5'), fg_color='#000000')
botao5.place(x=80, y=190)

botao6 = ctk.CTkButton(janela, text='6', width=60, height=60, font=font2, command=lambda:show('6'), fg_color='#000000')
botao6.place(x=10, y=190)

botao7 = ctk.CTkButton(janela, text='7', width=60, height=60, font=font2, command=lambda:show('7'), fg_color='#000000')
botao7.place(x=150, y=120)

botao8 = ctk.CTkButton(janela, text='8', width=60, height=60, font=font2, command=lambda:show('8'), fg_color='#000000')
botao8.place(x=80, y=120)

botao9 = ctk.CTkButton(janela, text='9', width=60, height=60, font=font2, command=lambda:show('9'), fg_color='#000000')
botao9.place(x=10, y=120)

botaoIgual = ctk.CTkButton(janela, text='=', width=130, height=60, font=font2, command=calcular, fg_color='#b5520b')
botaoIgual.place(x=150, y=330)

botaoPonto = ctk.CTkButton(janela, text='.', width=60, height=60, font=font2, command=lambda:show('.'), fg_color='#b5520b')
botaoPonto.place(x=10, y=330)

botaoDividir = ctk.CTkButton(janela, text='/', width=25, height=25, font=font3, command=lambda:show('/'), fg_color='#b5520b')
botaoDividir.place(x=220, y=190)

botaoPorcento = ctk.CTkButton(janela, text='%', width=25, height=25, font=font3, command=lambda:show('%'), fg_color='#b5520b')
botaoPorcento.place(x=255, y=190)

botaoVezes = ctk.CTkButton(janela, text='x', width=60, height=25, font=font3, command=lambda:show('*'), fg_color='#b5520b')
botaoVezes.place(x=220, y=225)

botaoMais = ctk.CTkButton(janela, text='+', width=60, height=25, font=font3, command=lambda:show('+'), fg_color='#b5520b')
botaoMais.place(x=220, y=260)

botaoMenos = ctk.CTkButton(janela, text='-', width=60, height=25, font=font3, command=lambda:show('-'), fg_color='#b5520b')
botaoMenos.place(x=220, y=295)


janela.mainloop()