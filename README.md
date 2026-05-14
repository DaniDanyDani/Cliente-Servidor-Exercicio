# Cliente-Servidor-Exercicio
Sistema Cliente-Servidor de Detecção Facial para a disciplina ENE118-2026.1-A - INFORMÁTICA INDUSTRIAL

Objetivo:
Nesta atividade, você deverá aplicar os conceitos de programação em rede (sockets). O objetivo é evoluir a aplicação cliente-servidor vista em aula (calculadora remota) para um sistema capaz de realizar a detecção facial em imagens enviadas remotamente.

Descrição da Aplicação:

- Você deve desenvolver uma aplicação cliente-servidor em Python que atenda rigorosamente ao seguinte fluxo:
- Envio da Imagem: O cliente deverá carregar uma imagem a partir de seus arquivos locais e enviá-la, via socket, para o servidor.
- Processamento (Visão Computacional): O servidor receberá os bytes da imagem e aplicará uma técnica de detecção de faces. Caso uma ou mais faces sejam encontradas, o servidor deverá desenhar um retângulo azul ao redor de cada uma delas.
- Retorno dos Dados: Após a conclusão do processamento, o servidor deverá enviar a imagem processada de volta para o cliente.
- Exibição: O cliente deverá receber os dados, reconstruir a imagem processada e exibi-la na tela para o usuário.

Material de Apoio (Repositório da Disciplina):
Os códigos base para iniciar esta atividade encontram-se na pasta Python/Python 3/:

- Base de Comunicação: Consulte as pastas Cliente e Servidor para entender a estrutura de sockets já utilizada.
- Base de Visão Computacional: Estude o código na pasta ExemploProcessamentoImagem. Ele contém a lógica necessária para abrir imagens e realizar a detecção de faces utilizando a biblioteca OpenCV.

Requisitos Técnicos e Dicas Importantes:
- Protocolo de Comunicação: O envio de arquivos de mídia (como imagens) via rede requer controle sobre o fluxo de dados. Na comunicação entre cliente e servidor, o agente remetente deve enviar primeiro o tamanho da imagem (em bytes) antes de enviar o arquivo propriamente dito. Dessa forma, o agente receptor saberá exatamente a quantidade de dados que deve esperar no buffer para reconstruir a imagem sem erros.
- Codificação de Imagens: Analise o código dentro do exemplo ExemploProcessamentoImagem  sobre como converter uma matriz de imagem do OpenCV para um array de bytes antes de enviar pelo socket (ex: usando cv2.imencode), e como fazer o processo inverso ao receber (ex: usando cv2.imdecode e numpy).
- Tratamento de Exceções: Lembre-se de tratar os casos em que a conexão falha ou a imagem enviada é inválida.

Formato de Entrega (Git):
A entrega desta atividade deverá ser feita exclusivamente via Git.
- Crie um repositório para o seu projeto (certifique-se de dar as permissões de acesso necessárias ao professor, caso seja privado).
- O repositório deve conter os arquivos fonte da sua solução (ex: cliente.py, servidor.py) e um arquivo requirements.txt com as dependências do projeto.
- Lembre-se de configurar corretamente o seu .gitignore para não incluir arquivos desnecessários (como pastas de ambientes virtuais venv/ ou caches __pycache__/).
- Submeta o link do repositório na plataforma da disciplina até a data limite estipulada.