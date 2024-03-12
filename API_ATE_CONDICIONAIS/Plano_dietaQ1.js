/**
    INgestão calórica:
Proteínas 4 calorias por 1g
Carboidratos 4 calorias por 1g
Gorduras 9 calorias por 1g

Necessidade Calórica Diária (Adultos em kcal) para Manter o Peso:
Homem → 662 – (9,53 x idade) + AF x (15,91 x peso ) + (539,6 x altura)
Mulher → 354 – (6,91 x idade) + AF x (9,36 x peso) + (726 x altura)

Onde:
idade em anos, peso em kg e altura em m
AF: Ritmo de Atividade Física (Em adultos):
Sexo/Perfil Homens                        MULHERES
             1,00 Sedendentário           1,00 Sedendentário
            1,11 Pouco Ativo               1,12 Pouco Ativo
           1,25 Ativo                      1,27 Ativo
          1,48 Muito Ativo                 1,45 Muito Ativo


 Receba:
Nome, sexo, idade, peso, altura, Perfil Atividade Física

 */

const { question } = require("readline-sync");


function main(){
    nome = question('QUAL O SEU NOME?: ').toLowerCase()
    sexo = question('QUAL O SEU SEXO?(M ou F): ').toLowerCase()
    idade = get_number('QUANTOS ANOS VOCE TEM?: ')
    peso = get_number('QUAL O SEU PESO, EM KG?: ')
    altura = get_number('QUAL SUA ALTURA, EM M?: ')
    atribuicao_pfa = question('QUAL SEU PERFIL DE ATIVIDADE FISICA (SEDENTARIO, POUCO ATIVO, ATIVO OU MUITO ATIVO)?: ').toLowerCase()

    pfa = pfa_relacao(atribuicao_pfa, sexo)
    calculo_necessidade = necessidade_calorica(sexo, idade, peso, altura, pfa)
    calculo_necessidade_enxuto = necessidade_calorica_calculo(sexo, idade, peso, altura, pfa)

    print(calculo_necessidade)

    //preguntas parte 2
    ganhar_ou_perder_peso = question('voce deseja GANHAR ou PERDER peso?(responda apenas com "ganhar" ou "perder"): ').toLowerCase()
    perder_ganhar = perder_ou_ganhar(ganhar_ou_perder_peso)
    kg = get_number(`quantos kg voce pretende ${perder_ganhar}?: `)
    semanas = get_number('e em quantas semanas voce pretende chegar a esse resultado?: ')
    //calculos basicos
    kcal = kg * 7700
    kilos_perdidos_por_semana = kg / semanas
    calorias_diarias = (kilos_perdidos_por_semana / 7) * 7700
    //função
    amenos_amais = ingerir_ou_nao(ganhar_ou_perder_peso)
    alerta = alertasaude(kilos_perdidos_por_semana, amenos_amais, nome)
    //
    dieta = calculo_necessidade_enxuto - calorias_diarias
    //nova dieta em calorias
    proteinas_dieta = Math.floor(dieta * 0.4)
    carboidratos_dieta = Math.floor(dieta * 0.4)
    gorduras_dieta = Math.floor(dieta * 0.2)
    //nova dieta em gramas
    gramas_proteina = Math.floor(proteinas_dieta / 4)
    gramas_carboidrato = Math.floor(carboidratos_dieta / 4)
    gramas_gordura = Math.floor(gorduras_dieta / 9)

    print(`---------------------------------------------------------------------------------------------------
    Caso você siga o plano de forma linear você deve ${perder_ganhar} ${kilos_perdidos_por_semana.toFixed(3)} kg por semana, isso corresponde a +- ${(kilos_perdidos_por_semana * 7700).toFixed(3)} Kcal semanais.
    A sua meta de calorias diárias para seu objetivo é de ${calorias_diarias.toFixed(2)} kcal ${amenos_amais} durante o dia pelas próximas ${semanas} semanas
    NOVA DIETA:
    ${gramas_proteina} g de proteinas diárias
    ${gramas_carboidrato} g de carboidratos diários
    ${gramas_gordura} g de gorduras diárias
    Pelas próximas ${semanas} semana(s)
    ${alerta}
    `)
}

function perder_ou_ganhar(ganhar_ou_perder_peso){
    if (ganhar_ou_perder_peso === 'ganhar'){
        return `ganhar`
    }else {
        return `perder`
    }
}

function pfa_relacao(atribuicao_pfa){
    if (atribuicao_pfa === 'sedentario' || atribuicao_pfa === 'sedentário'){
        return 1
    }else if (atribuicao_pfa === 'pouco ativo' && sexo === 'm'){
        return 1.11
    }else if (atribuicao_pfa === 'pouco ativo' && sexo === 'f'){
        return 1.12
    }else if (atribuicao_pfa === 'ativo' && sexo === 'm'){
        return 1.25
    }else if (atribuicao_pfa === 'ativo' && sexo === 'f'){
        return 1.27
    }else if (atribuicao_pfa === 'muito ativo' && sexo === 'm'){
        return 1.48
    }else if (atribuicao_pfa === 'muito ativo' && sexo === 'f'){
        return 1.45
    }
}

function alertasaude(kilos_perdidos_por_semana, amenos_amais, nome){
    if (kilos_perdidos_por_semana > 1){
        return (`Cuidado ${nome}!!!
        ${kilos_perdidos_por_semana} kg ${amenos_amais} por dia, pode comprometer sua saúde`)
    }else if (kilos_perdidos_por_semana <=1 ){
        return (`Fique em paz ${nome}!!!
        Eu sei que você vai conseguir atingir o objetivo se seguir a nova dieta e manter o ritmo de exercícios.`)
    }
}

function necessidade_calorica(sexo, idade, peso, altura, pfa){
    if (sexo === 'm'){
        const necessidade_calorica_homem = (9.53 * idade) + pfa * (15.91 * peso) + (539.6 * altura)
        return `
        sua necessidade calórica diária é de: ${necessidade_calorica_homem} kcal
        `
     }else if (sexo === 'f'){
        const necessidade_calorica_mulher = (6.91 * idade) + pfa * (9.36 * peso) + (726 * altura)
        return `
        sua necessidade calórica diária é de: ${necessidade_calorica_mulher} kcal
        `
     }else {
        return `
        por favor redigite qual o seu sexo, M para masculino ou F para feminino
        `
     }
}

function necessidade_calorica_calculo(sexo, idade, peso, altura, pfa){
    if (sexo === 'm'){
        const necessidade_calorica_homem = (9.53 * idade) + pfa * (15.91 * peso) + (539.6 * altura)
        return necessidade_calorica_homem
     }else if (sexo === 'f'){
        const necessidade_calorica_mulher = (6.91 * idade) + pfa * (9.36 * peso) + (726 * altura)
        return necessidade_calorica_mulher
}}


function ingerir_ou_nao(ganhar_ou_perder_peso){
    if (ganhar_ou_perder_peso === 'ganhar'){
        return `a mais`
    }else {
        return `a menos`
    }
}

main()

function print(imprimir){
    console.log(imprimir)
}

function get_number(mensagem){
    const n = Number(question(mensagem))
    return n 
}