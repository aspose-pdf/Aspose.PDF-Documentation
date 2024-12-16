---
title: Inserir uma Imagem em uma Célula de Tabela em PDF
type: docs
weight: 20
url: /pt/java/inserir-uma-imagem-em-uma-celula-de-tabela-em-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Tabelas são elementos importantes para exibir dados. Elas fornecem um formato apresentável para a representação de dados. Tabelas são frequentemente usadas para exibir informações numéricas. A API Aspose.PDF fornece uma classe, Table, que oferece a capacidade de criar tabelas em um arquivo PDF.

Em vez de criar uma tabela simples, você pode definir diferentes opções de formatação, por exemplo, o estilo da borda da tabela, informações de margem, alinhamento, cor de fundo, largura da coluna, informações do título, o valor das linhas a serem repetidas em cada página e muito mais.

{{% /alert %}}

## Abordagem Aspose.PDF

De acordo com nosso DOM (Modelo de Objeto de Documento), um documento é composto de Páginas.
 Uma página contém um ou mais parágrafos, e um parágrafo pode ser uma imagem, texto, um campo de formulário, um título, uma caixa flutuante, gráfico, anexo ou uma tabela. Uma tabela, por sua vez, tem uma coleção de linhas e cada linha tem uma coleção de células. Uma célula é uma coleção de parágrafos.

Portanto, de acordo com nosso DOM, uma célula de tabela pode conter qualquer um dos elementos de parágrafo especificados acima, incluindo imagens.

## Entendendo a Largura da Célula

É necessário ter um entendimento claro da largura da célula, especialmente ao exibir uma imagem na célula da tabela, para que a largura da imagem seja fixa na largura de uma célula, garantindo que ela seja exibida corretamente. A largura de uma imagem pode ser definida usando o método setFixedWidth() da classe Image.

## Exemplo de Código

```java

 String dataDir = "C:\\temp\\";

//Instanciar um objeto Document chamando seu construtor vazio

Document pdfDocument = new Document();

//Criar uma página no objeto Document

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//Instanciar um objeto tabela

Table table = new Table();

//Adicionar a tabela na coleção de parágrafos da página desejada

page.getParagraphs().add(table);

//Definir as larguras das colunas da tabela

table.setColumnWidths("100 100 120");



//Definir a borda da tabela usando outro objeto BorderInfo personalizado

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//Criar um objeto imagem na página

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//Definir o caminho do arquivo de imagem

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//Criar linhas na tabela e depois células nas linhas

Row row1 = table.getRows().add();

row1.getCells().add("Texto de exemplo na célula");

// Adicionar a célula que contém a imagem

Cell cell2 = row1.getCells().add();

//Adicionar a imagem à célula da tabela

cell2.getParagraphs().add(img1);



row1.getCells().add("Célula anterior com imagem");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//Salvar o documento

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```