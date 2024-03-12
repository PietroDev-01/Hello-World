/**
Valor base hora/aula na Universidade
Nome Professor
Horas semanais
Qualificação (E, M ou D)
Tempo de experiência docente (meses)
Quantidade Filhos menores de 6 anos
Valor Plano de Saúde (R$)

 */

const { question } = require("readline-sync")

function main(){
    nome_professor = question('Nome Professor: ')
    const valor_base_hora = get_number('Valor hora por aula: ')
    const horas_semanais = get_number('Horas semanais de aula: ')
    qualificacao = question('Sua qualificacao ("E" para especializacao, "M" para mestrado e "D" para doutorado): ').toLowerCase()
    const tempo_docencia = get_number('seu tempo de docencia em meses: ')
    const quantidade_filhos = get_number('seu tempo de docencia em meses: ')
    const valor_plano_de_saude = get_number('seu tempo de docencia em meses: ')

    por20 = 20/100
    por30 = 30/100
    por50 = 50/100
    por5 = 5/100

    salario_hora_aula = valor_base_hora * horas_semanais
    docencia_incremento = calculo_docencia_salario (salario_hora_aula, tempo_docencia, por20, por30, por50)
    tempo_expericencia = calculo_tempo_expericencia (tempo_docencia, docencia_incremento)
}

function calculo_docencia_salario (salario_hora_aula, tempo_docencia, por20, por30, por50){
    if (tempo_docencia === 'e'){
        novo_e = salario_hora_aula * por20
        novo_salario_e = salario_hora_aula + novo
        return novo_salario_e
    }else if (tempo_docencia === 'm'){
        novo_m = salario_hora_aula * por30
        novo_salario_m = salario_hora_aula + novo
        return novo_salario_m
    }else if(tempo_docencia === 'd'){
        novo_d = salario_hora_aula * por50
        novo_salario_d = salario_hora_aula + novo
        return novo_salario_d
    }
}

function calculo_tempo_expericencia (tempo_docencia, docencia_incremento, valor_base_hora, por5){
    incremento_hora = (tempo_docencia / 6)
    docencia_incremento / valor_base_hora
    //a terminar
}

function print(imprimir){
    console.log(imprimir)
}

function get_number(mensagem){
    const n = Number(question(mensagem))
    return n 
}

main()