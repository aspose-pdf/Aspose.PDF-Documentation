---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
weight: 10
url: pt/net/aspose-pdf-editor/
description: Aspose.PDF for .NET demonstra que o HTML5 PDF Editor é um editor de PDF baseado na web e de código aberto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## O que é o Html5 PDF Editor por Aspose.PDF para .NET?

O HTML5 PDF Editor por Aspose.PDF para .NET é um editor de PDF baseado na web e de código aberto que permite aos usuários criar, editar e converter arquivos PDF online. Os usuários podem facilmente incorporar o editor em suas próprias aplicações web para visualização e edição de arquivos PDF. O HTML5 PDF Editor é desenvolvido usando HTML5, jQuery Ajax, ASP.NET, Bootstrap e o backend é alimentado por Aspose.PDF para .NET. A interface do usuário do editor é mantida muito simples para fácil entendimento e melhoria das funcionalidades conforme as necessidades dos usuários.

![Image](../images/aspose-pdf-editor.png)

## Recursos

Atualmente, ele suporta os seguintes recursos:

- Criar novos arquivos PDF
- Carregar e visualizar arquivos PDF
- Carregar arquivos PDF e de imagem do Dropbox
- Carregar arquivos PDF e de imagem do Dropbox
- Exportar arquivo PDF para diferentes formatos de arquivo
- Anexar ou Mesclar arquivos PDF
- Inserir Novas Páginas
- Excluir Páginas
- Mover Páginas no arquivo PDF
- Inserir Texto no PDF
- Destacar Texto no PDF
- Rotacionar Texto Inserido no PDF
- Pesquisar Texto no PDF
- Substituir Texto no PDF
- Inserir Imagens
- Redimensionar Assinatura e Imagens
- Arrastar e Posicionar itens inseridos
- Carregar arquivos PDF com campos de formulário
- Preencher campos de formulário usando o Editor
- Salvar e Exportar PDF com dados dos campos de formulário
- Destacar campos de formulário necessários
- Adicionar Anexos aos Arquivos PDF
- Carregar Anexos do arquivo PDF de entrada
- Baixar os arquivos de Anexo
- Remover os arquivos de Anexo
- Assinar PDF usando Desenho à Mão Livre

## Requisitos do Sistema

Como o Editor de PDF HTML5 é uma aplicação Web .NET desenvolvida usando ASP.NET, C#, HTML5, jQuery, Javascript, você precisará do seguinte ambiente de sistema para configurar o Editor de PDF HTML5 em seu final.

- Visual Studio 2010 (ou superior)
- .NET Framework 3.5 (ou superior)
- Aspose.PDF para .NET
- Aspose.PDF para .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

Você pode usar qualquer um dos seguintes navegadores para executar a aplicação no seu fim:

- Mozilla Firefox (recomendado)
- Internet Explorer (versão 9 ou posterior)
- Google Chrome
- Apple Safari

## Suporte

Nós, na Aspose, nos certificamos de fornecer o melhor suporte possível aos nossos clientes / usuários para suas consultas de qualquer natureza, seja técnica ou de vendas. Por favor, use os links abaixo para qualquer consulta relacionada a licença e vendas ou consulta técnica.

# Guia do Desenvolvedor do Editor de PDF

## Criar Novos Arquivos PDF

Além de editar documentos PDF existentes, o Editor de PDF Html5 também suporta a criação de novos arquivos PDF do zero, o que você pode fazer usando a opção Criar Novo Arquivo da barra de menu. Usando esse recurso, você pode criar um PDF em branco no editor, adicionar algum texto/imagens a ele e salvar no formato desejado. Na próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

### Como funciona?

**HTML - o item de menu "Criar Novo Arquivo" é clicado na página**

Quando você clica no item de menu "Criar Novo Arquivo", o método onNewFileClicked é chamado no arquivo Editor.js.
Quando você clica no item de menu "Criar Novo Arquivo", o método onNewFileClicked é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax ao servidor para o método CreateNewFile.**

Veja a aba Editor.js abaixo para o código fonte do método onNewFileClicked, ele chama o método CreateNewFile no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código fonte do método CreateNewFile. Ele limpa quaisquer dados existentes referentes ao arquivo previamente carregado usando o método ResetData.

**Criação de novo arquivo PDF usando Aspose.PDF para .NET**

Após limpar os dados usando o método ResetData, o método CreateNewFile cria um novo arquivo PDF usando a classe Document do Aspose.PDF para .NET.
Como você pode ver na aba abaixo, o objeto Document está gerando um arquivo com uma página vazia. Depois que o arquivo é gerado no servidor, o arquivo é convertido para imagem usando o método ImageConverter para ser carregado na tela.

**Carregando o arquivo resultante na tela.**

Depois que o arquivo é convertido para imagem no lado do servidor, o controle retorna para o método onNewFileClicked no Editor.js.
Após o arquivo ser convertido em imagem no lado do servidor, o controle é devolvido ao método onNewFileClicked no Editor.js.

## Exportação de PDF para Diferentes Formatos de Arquivo

O Editor PDF HTML5 suporta a exportação de arquivo PDF para diferentes formatos de arquivo, o que você pode fazer usando a opção Exportar Arquivo na barra de menu. Usando esse recurso, você pode exportar o arquivo PDF para o formato desejado. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

### Como funciona?

**HTML - O item de menu "Exportar Arquivo" é clicado na página.**

Quando você clica no item de menu "Exportar Arquivo", você pode escolher o formato de exportação da lista. Após selecionar o formato de exportação, o método "ExportFile" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação de servidor Ajax para o método btnFileExport_Click**

Veja a aba Editor.js abaixo para o código fonte do método "ExportFile". Ele envia uma solicitação ao método de servidor btnFileExport_Click com o parâmetro de formato de arquivo no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo.
Veja a aba Canvas.aspx.cs abaixo.

**Exportar arquivo para download no navegador do cliente**

Após o arquivo ser gerado no servidor, o controle é retornado para o método ExportFile em Editor.js de onde o arquivo é enviado para o navegador para o usuário baixar usando o método ExportToBrowser.

## Anexando ou Mesclando Arquivos PDF

O Editor PDF Html5 suporta a anexação ou mesclagem de arquivos PDF, que você pode fazer usando a opção Anexar Arquivo da barra de menu. Usando esse recurso, você pode anexar o arquivo PDF ao seu arquivo de entrada. Na próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

### Como funciona?

**HTML - O item de menu "Anexar Arquivo" é clicado na página.**

Quando você clica no item de menu "Anexar Arquivo", você pode fazer o upload do arquivo usando o diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação de servidor para o método ProcessRequest**

Veja a aba Editor.js abaixo para o código fonte do método "fileSelected".
**O método web do ASP.NET trata das solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Baseado no parâmetro do formulário passado, o arquivo a ser anexado é salvo no servidor e o método "AppendFile" é chamado. O método AppendFile anexa o arquivo enviado usando Aspose.PDF para .NET, converte o arquivo resultante em imagem e retorna o controle para o método "fileSelected" no Editor.js

**Atualizar o conteúdo da tela após anexar o arquivo**

Após o arquivo ser gerado no servidor, o controle é retornado para o método "fileSeleceted" no Editor.js, que atualiza o conteúdo do editor.

## Carregar Arquivo PDF Local

O editor de PDF HTML5 suporta o carregamento de arquivo PDF da máquina local usando a opção Abrir Do Computador da barra de menu. Usando esse recurso, você pode abrir um arquivo PDF existente e realizar a edição no seu arquivo PDF. Na próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

### Como funciona?

**HTML - O item de menu "Abrir Do Computador" é clicado na página.**
**HTML - "Abrir do Computador" é clicado na página.**

Quando você clica em "Abrir do Computador", pode fazer upload do arquivo usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação ao servidor para o método ProcessRequest**

Veja a aba Editor.js abaixo para o código fonte do método "fileSelected". O arquivo é postado no servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo. Baseado no parâmetro de formulário passado, o arquivo a ser carregado é salvo no servidor, reinicia os dados usando o método "ResetData" e o método "ImageConverter" é chamado. O método ImageConverter, converte o arquivo carregado em imagens usando Aspose.PDF para .NET e retorna o controle para o método "fileSelected" no Editor.js.

**Atualizar o conteúdo da tela após o upload do arquivo**

Após o arquivo ser gerado no servidor, o controle é retornado para o método "fileSelected" no Editor.js, que atualiza o conteúdo do editor.
Depois que o arquivo é gerado no servidor, o controle é devolvido ao método "fileSeleceted" em Editor.js que atualiza o conteúdo do editor.

## Adicionando Página em Arquivo PDF

Usando o Editor PDF Html5, você pode adicionar novas páginas em arquivos PDF usando a opção Adicionar Página na barra de menu. Com esse recurso, você pode adicionar uma página em branco ao seu arquivo PDF. Na próxima seção, discutiremos os detalhes técnicos por trás desse recurso.

### Como funciona?

**HTML - O item de menu "Adicionar Página" é clicado na página**

Quando você clica no item de menu "Adicionar Página", o método "AddPage" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax para o servidor para o método AddPage_Click.**

Veja a aba Editor.js abaixo para o código fonte do método AddPage, ele chama o método AddPage_Click no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET que lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código fonte do método AddPage_Click.
## Excluindo Página de um Arquivo PDF

Usando o Html5 PDF Editor, você pode excluir uma página de arquivos PDF usando a opção Excluir Página na barra de menu. Na próxima seção, discutiremos os detalhes técnicos por trás deste recurso.

### Como funciona?

**HTML - O item de menu "Excluir Página" é clicado na página**

Quando você clica no item de menu "Excluir Página", o método DeletePage é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação Ajax para o servidor para o método DeletePage_Click.**

Veja a aba Editor.js abaixo para o código fonte do método DeletePage, ele chama o método DeletePage_Click no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código fonte do método DeletePage_Click. Ele exclui a página selecionada do arquivo PDF usando o método Delete da coleção Aspose.PDF.Document.Page.

**Atualizando o conteúdo de edição**

Após excluir a página do arquivo PDF, o controle é então retornado ao método DeletePage no arquivo Editor.js, que atualiza a numeração das páginas, remove quaisquer coleções associadas à página excluída usando o método updateIndexesDelete.
Após deletar a página do arquivo PDF, o controle é então retornado para o método DeletePage no arquivo Editor.js, que atualiza a numeração das páginas e remove quaisquer coleções associadas à página deletada usando o método updateIndexesDelete.

## Mover Páginas no Arquivo PDF

Usando o Editor de PDF Html5, você pode mover páginas em arquivos PDF usando a opção Mover Página na barra de menu. Uma vez que você pressiona o item de menu Mover Página, é apresentado um diálogo de entrada para especificar a nova localização da página selecionada. Na nossa próxima seção, discutiremos os detalhes técnicos por trás desta funcionalidade.

### Como funciona?

**HTML - O item de menu "Mover Página" é clicado na página**

Quando você clica no item de menu "Mover Página", um diálogo de entrada é mostrado para obter a nova localização da página selecionada. Após fornecer o número da página e pressionar o botão "Mover", o método "Move" é chamado no arquivo Editor.js.

**jQuery - Enviar requisição Ajax ao servidor para o método MovePages.**

Veja a aba Editor.js abaixo para o código fonte do método Move, que chama o método MovePage e passa detalhes como mover de, mover para, lista de páginas para o método MovePages no arquivo CanvasSave.aspx.cs.
Veja a aba Editor.js abaixo para o código-fonte do método Move, que chama o método MovePage e passa os detalhes como mover de, mover para, lista de páginas para o método MovePages no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações do servidor**

Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método MovePages. Ele usa a coleção Aspose.PDF.Document.Pages para mover as páginas.

**Atualizando conteúdo de edição**

Após mover a página, o controle é então retornado ao método MovePage no arquivo Editor.js que atualiza os índices das páginas e informações relacionadas a diferentes coleções no editor usando o método MoveUpdate.

## Inserindo Texto em Arquivo PDF

Usando o Editor de PDF Html5, você pode inserir texto em arquivos PDF usando a opção Modo Texto da barra de menu. Uma vez que você seleciona o item do menu Modo Texto e clica em qualquer local no editor onde você deseja adicionar o texto, é apresentada uma caixa de diálogo de entrada para inserir e formatar o texto desejado conforme mostrado abaixo:

Na nossa próxima seção, discutiremos os detalhes técnicos por trás dessa funcionalidade.
Na nossa próxima seção, discutiremos os detalhes técnicos por trás desta funcionalidade.

### Como funciona?

**HTML - O item de menu "Modo Texto" é selecionado na página**

Quando você seleciona o item de menu "Modo Texto" e clica no local desejado no editor para inserir texto no arquivo PDF, é exibido um diálogo de entrada para obter o texto que você precisa inserir na página. Após fornecer o texto e pressionar o botão "OK", o método "saveTextFromArea" é chamado no arquivo Editor.js.

**Javascript - Obter o texto de entrada do diálogo de entrada e mostrar no editor.**

Veja a aba Editor.js abaixo para o código fonte do método saveTextFromArea, que obtém o texto do diálogo de entrada e o mostra no editor. Além disso, ele salva os dados na coleção de formas que é posteriormente usada no lado do servidor para inserir texto no arquivo PDF. Você pode verificar o código fonte do método saveFile que é chamado quando o arquivo é salvo.

**Método web ASP.NET lida com solicitações do servidor**

Como mencionado acima, o texto será realmente inserido no nosso arquivo PDF fonte quando realizarmos a operação de salvar que usa o método GetTextStamp para criar o carimbo de texto para inserir no arquivo PDF.
Como mencionado acima, o texto será inserido em nosso arquivo PDF fonte quando realizarmos a operação de salvar, que utiliza o método GetTextStamp para criar a marcação de texto a ser inserida no arquivo PDF.

## Destacar Texto em Arquivo PDF

Usando o Editor de PDF Html5, você pode destacar textos em arquivos PDF utilizando a opção Modo de Destaque no menu. Ao selecionar o item de menu Modo de Destaque, você pode destacar qualquer texto e área usando a ferramenta de destaque retangular. Na próxima seção, discutiremos os detalhes técnicos por trás dessa funcionalidade.

### Como funciona?

**HTML - O item de menu "Modo de Destaque" é selecionado na página**

Quando você seleciona o item de menu "Modo de Destaque", você pode desenhar um destaque retangular em torno de qualquer texto ou item no seu arquivo PDF. A implementação deste processo pode ser vista no método "tools.rect" no arquivo Editor.js.

**Javascript - Desenhar retângulo de destaque no editor.**

Veja a aba Editor.js abaixo para o código fonte do método tool.rect, que permite ao usuário desenhar um retângulo de destaque em qualquer localização no editor.
Veja a aba Editor.js abaixo para o código-fonte do método tool.rect, que permite ao usuário desenhar um retângulo de destaque em qualquer local no editor.

**Método web ASP.NET lida com solicitações do servidor**

Como mencionado acima, o destaque é realmente inserido em nosso arquivo PDF fonte quando realizamos a operação de salvar que usa o método GetImageStamp para inserir o carimbo de imagem no arquivo PDF fonte na localização especificada no editor. Veja a aba Canvas.aspx.cs abaixo com o código-fonte do método GetImageStamp. Ele usa a classe Aspose.PDF.ImageStamp para inserir o retângulo de destaque no arquivo PDF.

## Buscando Texto no Arquivo PDF

Usando o Editor de PDF Html5, você pode buscar texto em arquivos PDF usando a opção Buscar Texto da barra de menu. Uma vez que você clicar no item de menu Buscar Texto, será apresentada uma caixa de diálogo para inserir o texto a ser buscado como mostrado abaixo:

Ao fornecer o texto e pressionar buscar, todas as instâncias da palavra buscada serão destacadas como mostrado abaixo:

### Como funciona?

**HTML - item de menu "Buscar Texto" é clicado na página**
**HTML - O item de menu "Buscar Texto" é clicado na página**

Ao clicar no item de menu "Buscar Texto", é apresentada uma caixa de diálogo de entrada para inserir o texto que deseja buscar. Após inserir o texto e pressionar o botão de busca, o método "Mover" é chamado, que verifica se a operação de mudança de página é realizada ou se a operação de busca é realizada e então chama o método performSearch no arquivo Editor.js.

**jQuery - Enviar requisição Ajax ao servidor para o método SearchData**

Veja a aba Editor.js abaixo para o código fonte do método performSearch, que obtém o texto de entrada e uma requisição ao método do servidor SearchData no arquivo _CanvasSave.aspx.cs_.

**Método web ASP.NET que lida com requisições ao servidor**

Veja a aba _Canvas.aspx.cs_ abaixo.
Veja a aba _Canvas.aspx.cs_ abaixo.

## Substituindo Texto em Arquivo PDF

Usando o Editor de PDF Html5, você pode substituir o texto existente em arquivos PDF usando a opção Substituir Texto da barra de menu. Uma vez que você clique no item de menu Substituir Texto, será apresentada uma caixa de diálogo para inserir o texto a ser pesquisado e substituído.

### Como funciona?

**HTML - Item de menu "Substituir Texto" é clicado na página**

Quando você clica no item de menu "Substituir Texto", é apresentada uma caixa de diálogo de entrada para inserir o texto a ser pesquisado e substituído. Após inserir o texto e pressionar o botão Substituir, o método "ReplaceText" é chamado no arquivo Editor.js.

**jQuery - Enviar solicitação de servidor Ajax para o método ReplaceText**

Veja a aba Editor.js abaixo para o código fonte do método ReplaceText, que obtém o texto de entrada da caixa de diálogo de texto de entrada e uma solicitação ao método do servidor ReplaceText no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com solicitações de servidor**

Veja a aba Canvas.aspx.cs abaixo.
## Carregando Arquivo PDF com Campos de Formulário

Usando Html5 PDF Editor, você pode carregar e trabalhar com um arquivo PDF que contém campos de formulário. Uma vez que o arquivo com campos de formulário é carregado no editor, todos os campos de formulário são carregados para edição. Na próxima seção, discutiremos os detalhes técnicos por trás dessa funcionalidade.

### Como funciona?

**HTML - O item de menu "Abrir do Computador" é clicado na página.**

Quando você clica no item de menu "Abrir do Computador", você pode fazer o upload do arquivo de entrada contendo os campos de formulário usando a caixa de diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Enviar pedido ao servidor para o método ProcessRequest**

O arquivo é postado para o servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET lida com pedidos do servidor**

Veja a aba Canvas.aspx.cs abaixo.
**Carregando campos de formulário no canvas**

Veja a aba Canvas.aspx.cs abaixo.

Veja a aba Editor.js abaixo, o método manageFields em Editor.js é usado para gerar todos os campos no canvas com base nas informações enviadas pelo lado do servidor. Ele desenha controles de campo HTML usando as informações de tipo e localização do lado do servidor para o canvas.

## Destacando Campos de Formulário Obrigatórios

Usando Html5 PDF Editor, você pode destacar os campos de formulário obrigatórios no editor. Uma vez que o arquivo com campos de formulário é carregado no editor, todos os campos de formulário obrigatórios são destacados para os usuários auxiliarem na edição. Na nossa próxima seção, discutiremos os detalhes técnicos por trás dessa funcionalidade.

### Como funciona?

**HTML - O item de menu "Abrir do Computador" é clicado na página.**

Quando você clica no item de menu "Abrir do Computador", você pode fazer o upload do arquivo de entrada contendo os campos de formulário usando o diálogo de upload de arquivo. Após o arquivo ser carregado, o método "fileSelected" é chamado no arquivo Editor.js.

**jQuery - Envie solicitação ao servidor para o método ProcessRequest**
**jQuery - Envio de requisição de servidor para o método ProcessRequest**

O arquivo é enviado para o servidor e o método "ProcessRequest" é chamado no arquivo CanvasSave.aspx.cs.

**Método web ASP.NET manipula requisições do servidor**

Veja a aba Canvas.aspx.cs abaixo. Baseado no parâmetro de formulário passado, o arquivo a ser carregado é salvo no servidor, o método ImageConverter, converte o arquivo carregado em imagens e o método "CheckFields" é chamado, o qual utiliza a classe Aspose.PDF.InteractiveFeatures.Forms para verificar todos os campos do formulário e coletar informações sobre os campos, como Tipo de Campo, Localização, etc. Após obter os detalhes de todos os campos do formulário, obtemos a informação se um campo de formulário é necessário usando o método Aspose.PDF.Facades.IsRequiredField e retorna a coleção de campos de volta para o método ImageConverter. O método ImageConverter devolve o controle para o método "fileSelected" no Editor.js

**Carregamento de campos de formulário no canvas**

Veja a aba Editor.js abaixo, o método manageFields no Editor.js é usado para gerar todos os campos no canvas baseado nas informações enviadas de volta do lado do servidor.
Veja a aba Editor.js abaixo, o método manageFields em Editor.js é usado para gerar todos os campos na tela com base nas informações enviadas de volta do servidor.
