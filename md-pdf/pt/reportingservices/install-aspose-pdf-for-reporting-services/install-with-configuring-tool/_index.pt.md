---
title: Instalar com a Ferramenta de Configuração
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

Aspose.Pdf para Ferramenta de Configuração do Reporting Services pode ajudá-lo a configurar a extensão Aspose.Pdf para Reporting Services para qualquer uma das versões suportadas do Report Server (RS). Atualmente, suporta RS2016, RS2017, RS2019, RS2022 e Power BI Report Server. A Ferramenta de Configuração requer o .NET Framework 4.8.

Se você deseja instalar a extensão e registrá-la no Report Server, selecione o tipo de ação 'Register'. Para desregistrar e desinstalar a extensão, selecione o tipo de ação 'Unregister'.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**Os seguintes passos descrevem como usá-la em detalhes:**

1. Insira ou procure o caminho do arquivo DLL para a extensão Aspose.Pdf para Reporting Services;
1. Selecione o tipo de ação correspondente: Register ou Unregister;
1. Selecione a aba correspondente à versão do Report Server que você deseja configurar. Certifique-se de que selecionou o arquivo DLL destinado à sua versão do RS. Se a versão solicitada do produto não estiver instalada na máquina, a ferramenta de configuração irá informá-lo com dicas. Se você estiver configurando a extensão para a instância nomeada RS2016 (não a padrão 'MSSQLSERVER'), por favor, insira o nome da instância personalizada e, em seguida, pressione o botão 'Atualizar'.
1. Certifique-se de que os caminhos e nomes dos arquivos de configuração mostrados nas caixas de texto inferiores estão corretos. Se não estiverem, você pode pressionar o botão 'Atualizar' para tentar encontrar a instância do RS novamente, ou pode localizá-los manualmente.
1. Pressione o botão 'Config'. A ferramenta agora tentará fazer a configuração solicitada e informará se a configuração foi bem-sucedida ou não.