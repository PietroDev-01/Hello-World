import threading
import time

# Fluxo simples do sistema: Linhas 11 e 12 pegam os inputs do usuário --> Linha 44 e 45 criam as threads através da classe Thread, passando os argumentos para as funções --> Linhas 48 e 49 os threads são executados --> Após o thread_cancelamento ser executado as threads são finalizadas e o programa é terminado após a linha 55 ser imprimida.

# Funções: A função relogio pega horas e minutos do usuário e funciona "infinitamente" enquanto a bandeira de cancelamento, que está em outra função (executada em outro thread paralelo a esse), não for sinalizada (nesse caso apertar o enter faz com que a bandeira seja sinalizada). A função monitorar_cancelamento está ali justamente para realizar o "desligamento" da função relogio (por meio da sinalização da bandeira ela cancela a execução do laço de repetição, assim, finalizando o thread_relogio).

# Essa biblioteca threading até que é interresante *-*

# Leitura das horas e minutos iniciais
horas = int(input("Digite a hora inicial (0-23): "))
minutos = int(input("Digite o minuto inicial (0-59): "))

# Função para incrementar e mostrar o relógio em tempo real
def relogio(horas, minutos, stop_event):
    segundos = 0
    while not stop_event.is_set():  # Continua até que o evento de parada seja ativado

        # Formatação de horas, minutos e segundos
        print(f"\rRelógio: {horas:02}:{minutos:02}:{segundos:02}", end=" ")
        time.sleep(1)  # Espera 1 segundo para incrementar
        
        # Incrementa os segundos
        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
        if horas == 24:
            horas = 0

# Função para monitorar o comando de cancelamento
def monitorar_cancelamento(stop_event):
    input("\nPressione Enter para parar o relógio...\n")
    stop_event.set()  # Sinaliza para parar o relógio


# Criação do evento de parada
stop_event = threading.Event()

# Criação das threads
thread_relogio = threading.Thread(target=relogio, args=(horas, minutos, stop_event))
thread_cancelamento = threading.Thread(target=monitorar_cancelamento, args=(stop_event,))

# Iniciando as threads
thread_relogio.start()
thread_cancelamento.start()

# Aguardando finalização das threads
thread_relogio.join()
thread_cancelamento.join()

print("\nRelógio parado.")