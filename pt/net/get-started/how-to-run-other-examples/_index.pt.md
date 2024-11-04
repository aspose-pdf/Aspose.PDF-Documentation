---
title: Como executar outros exemplos
linktitle: Como executar outros exemplos
type: docs
weight: 50
url: /net/how-to-run-other-examples/    
description: Esta página demonstra diretrizes que serão úteis para os seguintes requisitos antes de baixar e executar os exemplos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Requisitos de Software

Por favor, certifique-se de atender aos seguintes requisitos antes de baixar e executar os exemplos.

1. Visual Studio 2010 ou superior
1. Gerenciador de Pacotes NuGet instalado no Visual Studio. Certifique-se de que a versão mais recente da API NuGet esteja instalada no Visual Studio. Para detalhes sobre como instalar o gerenciador de pacotes NuGet, consulte <https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools>
1. Vá para `Tools->Options->NuGet Package Manager->Package Sources` e certifique-se de que a opção **nuget.org** esteja marcada
1.
## Baixar do GitHub

Todos os exemplos do Aspose.PDF para .NET estão hospedados no [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-.NET).

- Você pode clonar o repositório usando seu cliente GitHub favorito ou baixar o arquivo ZIP [aqui](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/archive/master.zip).
- Extraia o conteúdo do arquivo ZIP para qualquer pasta em seu computador. Todos os exemplos estão localizados na pasta **Examples**.
- Existem dois arquivos de solução do Visual Studio, um para Console e outro para Aplicação Web.
- Os projetos são criados no Visual Studio 2013, mas os arquivos de solução são compatíveis com o Visual Studio 2010 SP1 e superior.
- Abra o arquivo de solução no Visual Studio e construa o projeto.
- Na primeira execução, as dependências serão automaticamente baixadas via NuGet.
- A pasta **Data** na pasta raiz de **Examples** contém arquivos de entrada que os exemplos em CSharp usam. É obrigatório que você baixe a pasta **Data** junto com o projeto de exemplos.
- Abra o arquivo *RunExamples.cs*, todos os exemplos são chamados a partir daqui.
- Abra o arquivo *RunExamples.cs*, todos os exemplos são chamados a partir daqui.
- Descomente os exemplos que deseja executar dentro do projeto.

Sinta-se à vontade para entrar em contato usando nossos Fóruns se tiver qualquer problema para configurar ou executar os exemplos.

## Contribuir

Se deseja adicionar ou melhorar um exemplo, incentivamos que contribua para o projeto. Todos os exemplos e projetos de demonstração neste repositório são de código aberto e podem ser usados livremente em suas próprias aplicações.

Para contribuir, você pode fazer um fork do repositório, editar o código-fonte e criar um pull request. Nós revisaremos as alterações e incluiremos no repositório se considerarmos úteis.
