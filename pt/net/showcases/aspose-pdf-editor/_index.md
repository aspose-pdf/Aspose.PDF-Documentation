---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/aspose-pdf-editor/
description: Aspose.PDF for .NET demonstra que o Editor PDF baseado em HTML5 é um editor de PDF baseado na web de código aberto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF Editor",
    "alternativeHeadline": "HTML5 PDF Editor: Create, Edit, and Convert PDF Online",
    "abstract": "O Editor Aspose.PDF for .NET é uma ferramenta robusta de edição de PDF baseada na web e de código aberto para .NET que permite aos usuários criar, editar e converter documentos PDF de forma contínua dentro de suas aplicações web. Com funcionalidades avançadas, como mesclar arquivos, preencher campos de formulário e suportar múltiplos formatos, oferece uma interface simplificada projetada para gerenciamento eficiente de documentos e uma experiência do usuário aprimorada.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3488",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/aspose-pdf-editor/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-editor/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## O que é o Editor PDF Html5 da Aspose.PDF for .NET?

O Editor PDF HTML5 da Aspose.PDF for .NET é um editor de PDF baseado na web de código aberto que permite aos usuários criar, editar e converter arquivos PDF online, e os usuários podem facilmente incorporar o editor em suas próprias aplicações web para visualização e edição de arquivos PDF. O Editor PDF HTML5 é desenvolvido usando HTML5, jQuery Ajax, ASP.NET, Bootstrap e o backend é alimentado por Aspose.PDF for .NET. A interface do usuário do editor é mantida muito simples para fácil compreensão e aprimoramento das funcionalidades conforme as necessidades do usuário.

![Imagem](../images/aspose-pdf-editor.png)

## Recursos

Ele suporta os seguintes recursos:

- Criar novos arquivos PDF.
- Carregar e visualizar arquivos PDF.
- Carregar arquivos PDF e de imagem do Dropbox.
- Exportar arquivo PDF para diferentes formatos de arquivo.
- Anexar ou mesclar arquivos PDF.
- Inserir novas páginas.
- Excluir páginas.
- Mover páginas no arquivo PDF.
- Inserir texto no PDF.
- Destacar texto no PDF.
- Rotacionar texto inserido no PDF.
- Pesquisar texto no PDF.
- Substituir texto no PDF.
- Inserir imagens.
- Redimensionar assinatura e imagens.
- Arrastar e posicionar itens inseridos.
- Carregar arquivos PDF com campos de formulário.
- Preencher campos de formulário usando o Editor.
- Salvar e exportar PDF com dados de campos de formulário.
- Destacar campos de formulário necessários.
- Adicionar anexos a arquivos PDF.
- Carregar anexos do arquivo PDF de entrada.
- Baixar os arquivos de anexo.
- Remover os arquivos de anexo.
- Assinar PDF usando desenho à mão livre.

## Requisitos do Sistema

Como o Editor PDF HTML5 é uma aplicação web .NET desenvolvida usando ASP.NET, C#, HTML5, jQuery, Javascript. Você precisará do seguinte ambiente de sistema para configurar o Editor PDF HTML5 em sua máquina.

- Visual Studio 2010 (ou superior).
- .NET Framework 3.5 (ou superior).
- Aspose.PDF for .NET.
- jQuery 2.0.3.
- Bootstrap 3.2.0.

Você pode usar qualquer um dos seguintes navegadores para executar a aplicação em sua máquina:

- Mozilla Firefox (recomendado).
- Internet Explorer (versão 9 ou posterior).
- Google Chrome.
- Apple Safari.

## Suporte

Nós, da Aspose, garantimos fornecer o melhor suporte possível aos nossos clientes/usuários para suas dúvidas de qualquer natureza, ou seja, técnicas ou de vendas. Por favor, use os links abaixo para qualquer dúvida relacionada a licenças e vendas ou técnica.

## Guia do Desenvolvedor do Editor PDF

### Criar Novos Arquivos PDF

Além de editar documentos PDF existentes, o Editor PDF Html5 também suporta a criação de novos arquivos PDF do zero, o que você pode fazer usando a opção Criar Novo Arquivo na barra de menu. Usando esse recurso, você pode criar um PDF em branco no editor, adicionar algum texto/imagens a ele e salvá-lo em qualquer formato desejado. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Criar Novo Arquivo" é clicado na página**

Quando você clica no item de menu "Criar Novo Arquivo", o método onNewFileClicked é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método CreateNewFile.**

Veja a aba Editor.js abaixo para o código-fonte do método onNewFileClicked, que chama o método CreateNewFile no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método CreateNewFile. Ele limpa quaisquer dados existentes sobre o arquivo carregado anteriormente usando o método ResetData.

**Criação de novo arquivo PDF usando Aspose.PDF for .NET**

Após limpar os dados usando o método ResetData, o método CreateNewFile cria um novo arquivo PDF usando a classe Document de Aspose.PDF for .NET. Como você pode ver na aba abaixo, o objeto Document está gerando um arquivo com uma página vazia. Depois que o arquivo é gerado no servidor, o arquivo é convertido em imagem usando o método ImageConverter para ser carregado no canvas.

**Carregando o arquivo resultante no canvas.**

Depois que o arquivo é convertido em imagem no lado do servidor, o controle é retornado ao método onNewFileClicked no Editor.js. O método onNewFileClicked redefine todas as coleções do lado do cliente e carrega o arquivo de imagem gerado no canvas usando o método resetData.

### Exportando PDF para Diferentes Formatos de Arquivo

O Editor PDF HTML5 suporta a exportação de arquivos PDF para diferentes formatos de arquivo, o que você pode fazer usando a opção Exportar Arquivo na barra de menu. Usando esse recurso, você pode exportar o arquivo PDF para o formato desejado. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Exportar Arquivo" é clicado na página.**

Quando você clica no item de menu "Exportar Arquivo", você pode escolher o formato de exportação na lista. Após selecionar o formato de exportação, o método "ExportFile" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método btnFileExport_Click**

Veja a aba Editor.js abaixo para o código-fonte do método "ExportFile". Ele envia uma solicitação ao método do servidor btnFileExport_Click com o parâmetro de formato de arquivo no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Com base no parâmetro de formato de arquivo passado para btnFileExport_Click, o arquivo PDF é convertido usando o método Save do objeto Aspose.PDF Document.

**Exportar arquivo para download no navegador do cliente**

Depois que o arquivo é gerado no servidor, o controle é retornado ao método ExportFile no Editor.js, de onde o arquivo é enviado ao navegador para o usuário baixar usando o método ExportToBrowser.

### Anexando ou Mesclando Arquivos PDF

O Editor PDF Html5 suporta a anexação ou mesclagem de arquivos PDF, o que você pode fazer usando a opção Anexar Arquivo na barra de menu. Usando esse recurso, você pode anexar o arquivo PDF ao seu arquivo de entrada. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Anexar Arquivo" é clicado na página.**

Quando você clica no item de menu "Anexar Arquivo", você pode fazer o upload do arquivo usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação ao servidor para o método ProcessRequest**

Veja a aba Editor.js abaixo para o código-fonte do método "fileSelected". O arquivo é enviado ao servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Com base no parâmetro de formulário passado, o arquivo a ser anexado é salvo no servidor e o método "AppendFile" é chamado. O método AppendFile anexa o arquivo carregado usando Aspose.PDF for .NET, converte o arquivo resultante em imagem e retorna o controle ao método "fileSelected" no Editor.js.

**Atualizar o conteúdo do canvas após anexar o arquivo**

Depois que o arquivo é gerado no servidor, o controle é retornado ao método "fileSelected" no Editor.js, que atualiza o conteúdo do editor.

### Carregar Arquivo PDF Local

O Editor PDF HTML5 suporta o upload de arquivo PDF da máquina local usando a opção Abrir do Computador na barra de menu. Usando esse recurso, você pode abrir um arquivo PDF existente e realizar edições no seu arquivo PDF. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Abrir do Computador" é clicado na página.**

Quando você clica no item de menu "Abrir do Computador", você pode fazer o upload do arquivo de entrada usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação ao servidor para o método ProcessRequest**

Veja a aba Editor.js abaixo para o código-fonte do método "fileSelected". O arquivo é enviado ao servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Com base no parâmetro de formulário passado, o arquivo a ser carregado é salvo no servidor, os dados são redefinidos usando o método "ResetData" e o método "ImageConverter" é chamado. O método ImageConverter converte o arquivo carregado em imagens usando Aspose.PDF for .NET e retorna o controle ao método "fileSelected" no Editor.js.

**Atualizar o conteúdo do canvas após carregar o arquivo**

Depois que o arquivo é gerado no servidor, o controle é retornado ao método "fileSelected" no Editor.js, que atualiza o conteúdo do editor, ou seja, redefine o canvas, carrega o arquivo recém-carregado.

### Adicionando Página no Arquivo PDF

Usando o Editor PDF Html5, você pode adicionar novas páginas em arquivos PDF usando a opção Adicionar Página na barra de menu. Usando esse recurso, você pode adicionar uma página em branco ao seu arquivo PDF. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Adicionar Página" é clicado na página**

Quando você clica no item de menu "Adicionar Página", o método "AddPage" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método AddPage_Click.**

Veja a aba Editor.js abaixo para o código-fonte do método AddPage, que chama o método AddPage_Click no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método AddPage_Click. Ele adiciona uma nova página vazia no arquivo PDF usando a classe Aspose.Pdf.Document. Após adicionar a página ao arquivo PDF, ele converte a página em imagem para ser exibida no editor. O controle é então retornado ao arquivo Editor.js, que atualiza a numeração das páginas no método AddPage.

### Excluindo Página do Arquivo PDF

Usando o Editor PDF Html5, você pode excluir uma página de arquivos PDF usando a opção Excluir Página na barra de menu. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Excluir Página" é clicado na página**

Quando você clica no item de menu "Excluir Página", o método DeletePage é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método DeletePage_Click.**

Veja a aba Editor.js abaixo para o código-fonte do método DeletePage, que chama o método DeletePage_Click no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método DeletePage_Click. Ele exclui a página selecionada do arquivo PDF usando o método Delete da coleção Aspose.Pdf.Document.Page.

**Atualizando o conteúdo da edição**

Após excluir a página do arquivo PDF, o controle é então retornado ao método DeletePage no arquivo Editor.js, que atualiza a numeração das páginas, remove quaisquer coleções associadas à página excluída usando o método updateIndexesDelete.

### Mover Páginas no Arquivo PDF

Usando o Editor PDF Html5, você pode mover páginas em arquivos PDF usando a opção Mover Página na barra de menu. Assim que você pressionar o item de menu Mover Página, será apresentada uma caixa de diálogo de entrada para especificar a nova localização da página selecionada. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Mover Página" é clicado na página**

Quando você clica no item de menu "Mover Página", uma caixa de diálogo de entrada é exibida para obter a nova localização da página selecionada. Após fornecer o número da página e pressionar o botão "Mover", o método "Move" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método MovePages.**

Veja a aba Editor.js abaixo para o código-fonte do método Move, que chama o método MovePage e passa os detalhes como mover de, mover para, lista de páginas para o método MovePages no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método MovePages. Ele usa a coleção Aspose.Pdf.Document.Pages para mover as páginas.

**Atualizando o conteúdo da edição**

Após mover a página, o controle é então retornado ao método MovePage no arquivo Editor.js, que atualiza os índices das páginas e as informações relacionadas a diferentes coleções no editor usando o método MoveUpdate.

### Inserindo Texto no Arquivo PDF

Usando o Editor PDF Html5, você pode inserir texto em arquivos PDF usando a opção Modo de Texto na barra de menu. Assim que você selecionar o item de menu Modo de Texto e clicar em qualquer local no editor onde deseja adicionar o texto, será apresentada uma caixa de diálogo de entrada para inserir e formatar seu texto desejado, conforme mostrado abaixo:

Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Modo de Texto" é selecionado na página**

Quando você seleciona o item de menu "Modo de Texto" e clica no local desejado no editor para inserir texto no arquivo PDF, uma caixa de diálogo de entrada é exibida para obter o texto que você precisa inserir na página. Após fornecer o texto e pressionar o botão "OK", o método "saveTextFromArea" é chamado no arquivo Editor.js.

**Javascript - Obter o texto de entrada da caixa de diálogo de entrada e mostrar no editor.**

Veja a aba Editor.js abaixo para o código-fonte do método saveTextFromArea, que obtém o texto da caixa de diálogo de entrada e o exibe no editor. Além disso, ele salva os dados na coleção de formas, que é usada posteriormente no lado do servidor para inserir texto no arquivo PDF. Você pode verificar o código-fonte do método saveFile, que é chamado quando o arquivo é salvo.

**Método web ASP.NET lida com solicitações do servidor**

Como mencionado acima, o texto será realmente inserido em nosso arquivo PDF de origem quando realizarmos a operação de salvar, que usa o método GetTextStamp para criar o carimbo de texto a ser inserido no arquivo PDF. Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método GetTextStamp. Ele usa a classe Aspose.Pdf.TextStamp para inserir o texto no arquivo PDF.

### Destacar Texto no Arquivo PDF

Usando o Editor PDF Html5, você pode destacar texto em arquivos PDF usando a opção Modo de Destaque na barra de menu. Assim que você selecionar o item de menu Modo de Destaque, poderá destacar qualquer texto e área usando a ferramenta de destaque retangular. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Modo de Destaque" é selecionado na página**

Quando você seleciona o item de menu "Modo de Destaque", pode desenhar um destaque retangular em torno de qualquer texto ou item no seu arquivo PDF. A implementação desse processo pode ser vista no método "tools.rect" no arquivo Editor.js.

**Javascript - Desenhar retângulo de destaque no editor.**

Veja a aba Editor.js abaixo para o código-fonte do método tool.rect, que permite ao usuário desenhar um retângulo de destaque em qualquer local no editor. Além disso, ele salva os dados na coleção de formas, que é usada posteriormente no lado do servidor para inserir o destaque no arquivo PDF de origem. Você pode verificar o código-fonte do método saveFile, que é chamado quando o arquivo é salvo.

**Método web ASP.NET lida com solicitações do servidor**

Como mencionado acima, o destaque é realmente inserido em nosso arquivo PDF de origem quando realizamos a operação de salvar, que usa o método GetImageStamp para inserir o carimbo de imagem no arquivo PDF de origem na localização especificada no editor. Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método GetImageStamp. Ele usa a classe Aspose.Pdf.ImageStamp para inserir o retângulo de destaque no arquivo PDF.

### Pesquisar Texto no Arquivo PDF

Usando o Editor PDF Html5, você pode pesquisar texto em arquivos PDF usando a opção Pesquisar Texto na barra de menu. Assim que você clicar no item de menu Pesquisar Texto, será apresentada uma caixa de diálogo para inserir o texto a ser pesquisado, conforme mostrado abaixo:

Ao fornecer o texto e pressionar pesquisar, todas as instâncias da palavra pesquisada serão destacadas, conforme mostrado abaixo:

**HTML - O item de menu "Pesquisar Texto" é clicado na página**

Quando você clica no item de menu "Pesquisar Texto", é apresentada uma caixa de diálogo de entrada para inserir o texto que deseja pesquisar. Após inserir o texto e pressionar o botão de pesquisa, o método "Move" é chamado, que verifica se a operação de mover página foi realizada ou se a operação de pesquisa foi realizada e, em seguida, chama o método performSearch no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método SearchData**

Veja a aba Editor.js abaixo para o código-fonte do método performSearch, que obtém o texto de entrada e uma solicitação ao método do servidor SearchData no arquivo _CanvasSave.aspx.cs_.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba _Canvas.aspx.cs_ abaixo. Usando o texto de entrada passado do método performSearch, o método SearchData usa a classe Aspose.Pdf.Text.TextFragmentAbsorber para pesquisar todas as instâncias do texto de entrada em nosso arquivo PDF de origem e a classe System.Drawing.Brush para desenhar o destaque contra o texto pesquisado. Uma vez que os dados são pesquisados, o arquivo resultante é novamente convertido em imagem e carregado no editor.

### Substituindo Texto no Arquivo PDF

Usando o Editor PDF Html5, você pode substituir o texto existente em arquivos PDF usando a opção Substituir Texto na barra de menu. Assim que você clicar no item de menu Substituir Texto, será apresentada uma caixa de diálogo para inserir o texto a ser pesquisado e substituído.

**HTML - O item de menu "Substituir Texto" é clicado na página**

Quando você clica no item de menu "Substituir Texto", é apresentada uma caixa de diálogo de entrada para inserir o texto a ser pesquisado e substituído. Após inserir o texto e pressionar o botão Substituir, o método "ReplaceText" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método ReplaceText**

Veja a aba Editor.js abaixo para o código-fonte do método ReplaceText, que obtém o texto de entrada da caixa de diálogo de texto de entrada e uma solicitação ao método do servidor ReplaceText no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. O método ReplaceText usa a classe Aspose.Pdf.Text.TextFragmentAbsorber para pesquisar todas as instâncias do texto a ser substituído em nosso arquivo PDF de origem e substitui todas as instâncias pelo texto substituto. Uma vez que o texto é substituído, o arquivo resultante é novamente convertido em imagem e carregado no editor.

### Carregando Arquivo PDF com Campos de Formulário

Usando o Editor PDF Html5, você pode carregar e trabalhar com um arquivo PDF contendo campos de formulário. Assim que o arquivo com campos de formulário é carregado no editor, todos os campos de formulário são carregados para edição. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Abrir do Computador" é clicado na página.**

Quando você clica no item de menu "Abrir do Computador", você pode fazer o upload do arquivo de entrada contendo os campos de formulário usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação ao servidor para o método ProcessRequest**

O arquivo é enviado ao servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Com base no parâmetro de formulário passado, o arquivo a ser carregado é salvo no servidor, o método ImageConverter converte o arquivo carregado em imagens e o método "CheckFields" é chamado, que usa a classe Aspose.Pdf.InteractiveFeatures.Forms para verificar todos os campos de formulário e coletar as informações sobre os campos, ou seja, FieldType, Localização, etc., e retorna a coleção de campos de volta ao método ImageConverter. O método ImageConverter retorna o controle de volta ao método "fileSelected" no Editor.js.

**Carregando campos de formulário no canvas**

Veja a aba Editor.js abaixo, o método manageFields no Editor.js é usado para gerar todos os campos no canvas com base nas informações enviadas de volta do lado do servidor. Ele desenha controles de campo HTML usando o tipo e a informação de localização do lado do servidor para o canvas.

### Destacando Campos de Formulário Necessários

Usando o Editor PDF Html5, você pode destacar os campos de formulário necessários no editor. Assim que o arquivo com campos de formulário é carregado no editor, todos os campos de formulário necessários são destacados para ajudar os usuários na edição. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

**HTML - O item de menu "Abrir do Computador" é clicado na página.**

Quando você clica no item de menu "Abrir do Computador", você pode fazer o upload do arquivo de entrada contendo os campos de formulário usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação ao servidor para o método ProcessRequest**

O arquivo é enviado ao servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Com base no parâmetro de formulário passado, o arquivo a ser carregado é salvo no servidor, o método ImageConverter converte o arquivo carregado em imagens e o método "CheckFields" é chamado, que usa a classe Aspose.Pdf.InteractiveFeatures.Forms para verificar todos os campos de formulário e coletar as informações sobre os campos, ou seja, FieldType, Localização, etc. Após obter os detalhes de todos os campos de formulário, obtemos a informação se um campo de formulário é um campo de formulário necessário usando o método Aspose.Pdf.Facades.IsRequiredField e retorna a coleção de campos de volta ao método ImageConverter. O método ImageConverter retorna o controle de volta ao método "fileSelected" no Editor.js.

**Carregando campos de formulário no canvas**

Veja a aba Editor.js abaixo, o método manageFields no Editor.js é usado para gerar todos os campos no canvas com base nas informações enviadas de volta do lado do servidor. Ele desenha controles de campo HTML usando o tipo e a informação de localização do lado do servidor para o canvas. Se um determinado campo for necessário, ele usa o div (chamado de wrapper) ao redor do controle e altera a propriedade de cor de fundo do div para mostrá-lo como um campo necessário destacado.