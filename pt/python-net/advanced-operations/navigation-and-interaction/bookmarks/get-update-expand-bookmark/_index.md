---
title: Obter, atualizar e expandir marcadores de PDF em Python
linktitle: Obter, atualizar e expandir um marcador
type: docs
weight: 20
url: /pt/python-net/get-update-and-expand-bookmark/
description: Saiba como recuperar, atualizar e expandir marcadores em documentos PDF usando Python.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como usar marcadores em PDF com Python
Abstract: Este artigo fornece um guia abrangente sobre como gerenciar marcadores dentro de um documento PDF usando a biblioteca Aspose.PDF em Python. Ele começa explicando como recuperar marcadores de um arquivo PDF através da `OutlineCollection`, que contém todos os marcadores, e detalha o acesso aos atributos dos marcadores via `OutlineItemCollection`. O artigo então descreve o processo de determinar o número da página associado a um marcador usando o `PdfBookmarkEditor`. Também explica como lidar com estruturas hierárquicas de marcadores, recuperando marcadores filhos dentro de cada `OutlineItemCollection`. Além disso, aborda a atualização das propriedades dos marcadores, demonstrando como modificar os atributos dos marcadores e salvar as alterações em um PDF. Por fim, o artigo trata da necessidade de expandir os marcadores ao visualizar um documento, mostrando como definir o status aberto de cada marcador para garantir que eles sejam expandidos por padrão. Trechos de código acompanham cada seção, fornecendo exemplos práticos de implementação dessas funcionalidades.
---

## Obter Marcadores

O [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) A coleção contém todos os marcadores de um arquivo PDF. Este artigo explica como obter marcadores de um arquivo PDF e como descobrir em qual página um marcador específico está.

Para obter os marcadores, percorra o [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção e obtenha cada marcador na OutlineItemCollection. O [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) fornece acesso a todos os atributos do marcador. O trecho de código a seguir mostra como obter marcadores do arquivo PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obtendo o número da página de um marcador

Depois de adicionar um marcador, você pode descobrir em qual página ele está obtendo o PageNumber de destino associado ao objeto Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Obter marcadores filhos de um documento PDF

Os marcadores podem ser organizados em uma estrutura hierárquica, com pais e filhos. Para obter todos os marcadores, percorra as coleções Outlines do objeto Document. No entanto, para obter também os marcadores filhos, percorra também todos os marcadores em cada [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto obtido no primeiro loop. Os trechos de código a seguir mostram como obter marcadores filhos de um documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Atualizar Marcadores em um Documento PDF

Para atualizar um marcador em um arquivo PDF, primeiro, obtenha o marcador específico da coleção OutlineColletion do objeto Document especificando o índice do marcador. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objeto, você pode atualizar suas propriedades e então salvar o arquivo PDF atualizado usando o método Save. Os trechos de código a seguir mostram como atualizar marcadores em um documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Marcadores expandidos ao visualizar o documento

Os marcadores são mantidos no objeto Document\u0027s [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) coleção, ela mesma no [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção. No entanto, podemos ter um requisito de que todos os marcadores estejam expandidos ao visualizar o arquivo PDF.

Para atender a esse requisito, podemos definir o status aberto para cada item de contorno/marcador como Aberto. O trecho de código a seguir mostra como definir o status aberto para cada marcador como expandido em um documento PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Tópicos Relacionados ao Marcador

- [Trabalhar com marcadores de PDF em Python](/pdf/pt/python-net/bookmarks/)
- [Adicionar e excluir marcadores de PDF em Python](/pdf/pt/python-net/add-and-delete-bookmark/)
- [Navegação e interação em PDF usando Python](/pdf/pt/python-net/navigation-and-interaction/)

