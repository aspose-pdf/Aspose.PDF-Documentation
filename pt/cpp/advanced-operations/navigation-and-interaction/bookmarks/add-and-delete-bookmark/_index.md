---
title: Adicionar e Excluir um Marcador 
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: pt/cpp/add-and-delete-bookmark/
description: Este tópico explica como adicionar um marcador a um documento PDF com a biblioteca C++. Também é possível excluir todos ou determinados marcadores de um documento PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar um Marcador a um Documento PDF

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) do objeto Documento, que está na coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) à coleção Outlines.

O trecho de código a seguir mostra como adicionar um marcador em um documento PDF.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Crie um objeto de marcador

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Defina o número da página de destino

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Adicione um marcador na coleção de contornos do documento.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Salve o documento atualizado

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Adicionar um Marcador Filho ao Documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica com marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
2. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), definindo suas propriedades.
3. Adicione a OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) do objeto Document.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção Outlines do marcador pai.

Os seguintes trechos de código mostram como adicionar um marcador filho a um documento PDF.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abra o documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Crie um objeto de marcador pai

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Crie um objeto de marcador filho

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Adicione o marcador filho na coleção do marcador pai

pdfOutline->Add(pdfChildOutline);

// Adicione o marcador pai na coleção de contornos do documento.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Salvar saída

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## Excluir todos os Favoritos de um Documento PDF

Todos os favoritos em um PDF são mantidos na coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Este artigo explica como excluir todos os favoritos de um arquivo PDF.

Para excluir todos os favoritos de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. Salve o arquivo modificado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

Os seguintes trechos de código mostram como excluir todos os favoritos de um documento PDF.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// Excluir todos os favoritos

pdfDocument->get_Outlines()->Delete();


// Salvar arquivo atualizado

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```

## Excluir um Favorito em Particular de um Documento PDF

[Excluir Todos os Anexos do documento PDF](https://docs.aspose.com/pdf/cpp/working-with-attachments/) mostrou como excluir todos os anexos de um arquivo PDF. Também é possível remover apenas anexos específicos.

Para excluir um marcador específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). O método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) remove qualquer marcador com o título passado para o método.

Os seguintes trechos de código mostram como excluir um marcador específico do documento PDF.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// Excluir contorno específico por Título

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// Salvar arquivo atualizado

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```