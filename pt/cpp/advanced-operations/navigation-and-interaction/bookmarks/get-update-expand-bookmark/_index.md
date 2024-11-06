---
title: Obter, Atualizar e Expandir um Favorito
linktitle: Obter, Atualizar e Expandir um Favorito
type: docs
weight: 20
url: pt/cpp/get-update-and-expand-bookmark/
description: A biblioteca Aspose.PDF para C++ permite que você obtenha? atualize em um arquivo PDF com o nosso.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Favoritos

A coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) contém todos os favoritos de um arquivo PDF. Este artigo explica como obter favoritos de um arquivo PDF e como obter em qual página um determinado favorito está.

Para obter os favoritos, percorra a coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) e obtenha cada favorito na OutlineItemCollection. O OutlineItemCollection fornece acesso a todos os atributos do marcador. O seguinte trecho de código mostra como obter marcadores do arquivo PDF.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Percorrer todos os marcadores

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"Título :- " + outlineItem->get_Title());


Console::WriteLine(u"É Itálico :- " + outlineItem->get_Italic());


Console::WriteLine(u"É Negrito :- " + outlineItem->get_Bold());


Console::WriteLine(u"Cor :- {0}", outlineItem->get_Color());

}
}
```

## Obtendo o Número da Página de um Marcador

Depois de adicionar um marcador, você pode descobrir em qual página ele está obtendo o número da página de destino associado ao objeto Bookmark.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Criar PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// Abrir arquivo PDF

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// Extrair marcadores

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"Título :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"Número da Página :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"Ação da Página :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## Atualizar Favoritos em um Documento PDF

Para atualizar um favorito em um arquivo PDF, primeiro, obtenha o favorito específico da coleção OutlineColletion do objeto Document especificando o índice do favorito. Uma vez que você tenha recuperado o favorito no objeto [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection), você pode atualizar suas propriedades e então salvar o arquivo PDF atualizado usando o método Save. Os snippets de código a seguir mostram como atualizar favoritos em um documento PDF.

```cpp
void UpdateBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obter um objeto de favorito

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// Atualizar o objeto de favorito

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// Definir a página alvo como 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Salvar saída

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Atualizar Marcadores Filhos em um Documento PDF

Para atualizar um marcador filho:

1. Recupere o marcador filho que você deseja atualizar do arquivo PDF, primeiro obtendo o marcador pai e depois o marcador filho usando os valores de índice apropriados.
1. Salve o arquivo PDF atualizado usando o método Save.

{{% alert color="primary" %}}

Obtenha um marcador da coleção OutlineCollection do objeto Document especificando o índice do marcador e, em seguida, obtenha o marcador filho especificando o índice deste marcador pai.

{{% /alert %}}

O trecho de código a seguir mostra como atualizar marcadores filhos em um documento PDF.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obter um objeto de marcador

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Obter objeto de marcador filho

auto childOutline = pdfOutline->idx_get(1);


// Atualizar o objeto de marcador

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// Defina a página de destino como 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Salvar saída

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Marcadores Expandido ao visualizar o documento

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) do objeto Document, que está na coleção [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). No entanto, podemos ter um requisito para que todos os marcadores sejam expandidos ao visualizar o arquivo PDF.

Para cumprir esse requisito, podemos definir o status de abertura para cada item de contorno/marcador como Aberto. O trecho de código a seguir mostra como definir o status de abertura para cada marcador como expandido em um documento PDF.

```cpp
void ExpandedBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// definir modo de visualização de página, ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos

doc->set_PageMode(PageMode::UseOutlines);

// imprimir contagem total de marcadores no arquivo PDF

Console::WriteLine(doc->get_Outlines()->get_Count());

// percorrer cada item de contorno na coleção de contornos do arquivo PDF

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {

// definir status de abertura para item de contorno

doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// salvar o arquivo PDF

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```