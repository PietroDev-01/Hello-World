from enum import Enum

class EstadoTarefa(Enum):
    NOVA = "Nova"
    PRONTA = "Pronta"
    EXECUTADA = "Executada"
    SUSPENSA = "Suspensa"
    TERMINADA = "Terminada"

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.estado = EstadoTarefa.NOVA

    def mudar_estado(self, novo_estado):
        if isinstance(novo_estado, EstadoTarefa):
            self.estado = novo_estado
            print(f"Estado alterado para: {self.estado.value}")
        else:
            print("Estado inválido.")

    def visualizar_estado(self):
        print(f"Tarefa: {self.descricao}\nEstado atual: {self.estado.value}")

# Exemplo de uso
tarefa = Tarefa("Implementar sistema de login")

# Visualizar estado inicial
tarefa.visualizar_estado()

# Mudando o estado da tarefa
tarefa.mudar_estado(EstadoTarefa.PRONTA)
tarefa.mudar_estado(EstadoTarefa.EXECUTADA)
tarefa.mudar_estado(EstadoTarefa.SUSPENSA)
tarefa.mudar_estado(EstadoTarefa.TERMINADA)

# Visualizar estado final
tarefa.visualizar_estado()