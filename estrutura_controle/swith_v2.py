def get_dia_semana(dia):
    dias = {
        1:"Domingo",
        2:"Seginda",
        3:"Terça",
        4:"Quarta",
        5:"Quinta",
        6:"Sexta",
        7:"Sabado" 
        }

    return dias.get(dia, "** inválid0 **")

def fim_semana(dia):

    if dia == 7 or dia == 1:
        return f'{get_dia_semana(dia)} é fim de semana'
    else:
        return f'{get_dia_semana(dia)} é dia de semana'
        
if __name__== "__main__":
    for dia in range(0,9):
        print(f'{dia}: {fim_semana(dia)}')
