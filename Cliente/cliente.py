import socket
import cv2
import numpy as np


class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            self._method()
        except:
            print("Servidor não disponível")

    
    def _method(self):
        """
        Método que implementa as requisições do cliente
        """
        print("b")
        try:
            msg = ''
            while True:
                msg = input("Digite a operação (x para sair): ")
                if msg == '':
                    continue
                elif msg == 'x':
                    break
                self.__tcp.send(bytes(msg,'ascii'))
                resp = self.__tcp.recv(1024)
                print("= ",resp.decode('ascii'))
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)


class ClientePI(Cliente):
    """
    Classe Cliente - API Socket - Processamento de imagens
    """
    def __init__(self, server_ip, port):
        super().__init__(server_ip, port)
    
    def _plot(self, img):
        cv2.imshow('Imagem Processada', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def _method(self):
        """
        Método que implementa as requisições do cliente
        """
        try:
            caminho_imagem = ''
            while True:
                caminho_imagem = input("Digite o caminho da imagem: ")
                if caminho_imagem == '':
                    continue
                elif caminho_imagem == 'x':
                    break
                # leitura da imagem
                img = cv2.imread(caminho_imagem)

                # codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img) 
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')

                # Primeiro envia o tamanho da imagem
                self.__tcp.send(tamanho_da_imagem_codificado)

                # Envia então a imagem, a quantidade de byts recebidos pelo
                # cliente tem que ser a mesma enviada antes, para garantia de
                # estabilidade
                self.__tcp.send(img_bytes)

                resp_tam_imagem = self.__tcp.recv(1024)
                tam = int.from_bytes(resp_tam_imagem, 'big')

                resp_img = self.__tcp.recv(tam)
                
                img = cv2.imdecode(np.frombuffer(resp_img, np.uint8), cv2.IMREAD_COLOR)

                self._plot(img)
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)

