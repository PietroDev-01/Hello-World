const { question } = require("readline-sync")

function main(){
Nome_Usuario = question('NOME: ')
Idade_Usuario = get_number('IDADE: ')

Minutos_atividade = get_number('Minutos de Atividade que voce fara: ')
//Alterei 10% do tempo de atividade em moderada para atribuir a "ATIVIDADE MÁXIMA"
Atividade_moderada = Minutos_atividade * 0.4
Atividade_leve = Minutos_atividade * 0.2
Atividade_dificil = Minutos_atividade * 0.1
Atividade_muito_leve = Minutos_atividade * 0.2
Atividade_Máxima = Minutos_atividade * 0.1

FCM = 220 - Idade_Usuario

Muito_leve_max = FCM * 0.6
Muito_leve_min = FCM * 0.5

Leve_min = Muito_leve_max
Leve_max = FCM * 0.7

Moderada_min = Leve_max
Moderada_max = FCM * 0.8

Dificil_min = Moderada_max
Dificil_max = FCM * 0.9

Maxima_min = Dificil_max
Maxima_max = FCM * 1


print(` --------------------------------------------------------------------------------------------------------------
Plano de Atividade Física 
${Atividade_muito_leve} Minutos Mantendo o grau de atividade em "Muito Leve" (ENTRE ${Muito_leve_min.toFixed(1)} BPM E ${Muito_leve_max.toFixed(1)} BPM)
${Atividade_leve} Minutos Mantendo o grau de atividade em "Leve" (ENTRE ${Leve_min.toFixed(1)} BPM E ${Leve_max.toFixed(1)} BPM)
${Atividade_moderada} Minutos Mantendo o grau de atividade em "Moderada" (ENTRE ${Moderada_min.toFixed(1)} BPM E ${Moderada_max.toFixed(1)} BPM)
${Atividade_dificil} Minutos Mantendo o grau de atividade em "Difícil" (ENTRE ${Dificil_min.toFixed(1)} BPM E ${Dificil_max.toFixed(1)} BPM)
${Atividade_Máxima} Minutos Mantendo o grau de atividade em "Máxima" (ENTRE ${Maxima_min.toFixed(1)} BPM E ${Maxima_max} BPM)

`)

}

main()

function print(imprimir){
    console.log(imprimir)
}

function get_number(mensagem){
    const n = Number(question(mensagem))
    return n 
}