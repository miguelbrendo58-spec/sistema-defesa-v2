import time

print("v2.0 - Sistema iniciado")

#CONFIGURAÇÕES
MAX_TENTATIVAS = 3
TEMPO_BLOQUEIO = 300

tentativas_falhas = {}
bloqueios = {}

print(f"Memorias criadas: {tentativas_falhas}, {bloqueios}")

def verficar_bloqueio(ip):
    if ip in bloqueios:
        tempo_restante = bloqueios[ip] - time.time()

        if tempo_restante > 0:
            print(f"[BLOQUEADO] {ip} ainda bloqueado por {int(tempo_restante)}s")
            return True
        else:
            print(f"[LIBERADO] {ip} foi liberado!")
            del bloqueios[ip]
            tentativas_falhas[ip] = 0
            return False
    return False

def registrar_falha(ip):
    tentativas_falhas[ip] = tentativas_falhas.get(ip, 0) + 1

    print(f"Tentativa falha de {ip} - {tentativas_falhas[ip]}/{MAX_TENTATIVAS}")

    if tentativas_falhas[ip] >= MAX_TENTATIVAS:
        bloqueios[ip] = time.time() + TEMPO_BLOQUEIO
        print(f"!!! IP {ip} BLOQUEADO por {TEMPO_BLOQUEIO}s")
        tentativas_falhas[ip] = 0

if __name__ == "__main__":
    ip_teste = "192.168.1.10"

    for i in range(6):
        print(f"\n --- Tentativa {i+1}---")
        if not  verficar_bloqueio(ip_teste):
            registrar_falha(ip_teste)
        time.sleep(1)




