---
title: Obter, Atualizar e Expandir um Marcador usando Python
linktitle: Obter, Atualizar e Expandir um Marcador
type: docs
weight: 20
url: /pt/python-net/get-update-and-expand-bookmark/
description: Este artigo descreve como usar marcadores em um arquivo PDF com nossa biblioteca Aspose.PDF para Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como usar marcadores em PDF com Python
Abstract: Este artigo oferece um guia abrangente sobre como gerenciar marcadores dentro de um documento PDF usando a biblioteca Aspose.PDF em Python. Ele começa explicando como recuperar marcadores de um arquivo PDF por meio da `OutlineCollection`, que contém todos os marcadores, e detalha o acesso aos atributos dos marcadores via `OutlineItemCollection`. O artigo então descreve o processo de determinar o número da página associado a um marcador usando o `PdfBookmarkEditor`. Também explica como lidar com estruturas hierárquicas de marcadores ao recuperar marcadores filhos dentro de cada `OutlineItemCollection`. Além disso, cobre a atualização de propriedades dos marcadores, demonstrando como modificar atributos de marcadores e salvar as alterações em um PDF. Por fim, o artigo aborda a necessidade de expandir marcadores ao visualizar um documento, mostrando como definir o status aberto de cada marcador para garantir que eles sejam expandidos por padrão. Trechos de código acompanham cada seção, fornecendo exemplos práticos de implementação dessas funcionalidades.
---

## Obter Marcadores

O objeto [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) da [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) contém todos os marcadores de um arquivo PDF. Este artigo explica como obter marcadores de um arquivo PDF e como descobrir em qual página está um marcador específico.

Para obter os marcadores, percorra a coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) e obtenha cada marcador na OutlineItemCollection. A [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) fornece acesso a todos os atributos do marcador. O trecho de código a seguir mostra como obter marcadores do arquivo PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obtendo o Número da Página de um Marcador

Depois de adicionar um marcador, você pode descobrir em qual página ele está obtendo o número da página de destino associado ao objeto Bookmark.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## Obter Marcadores Filhos de um Documento PDF

Os marcadores podem ser organizados em uma estrutura hierárquica, com pais e filhos. Para obter todos os marcadores, percorra as coleções Outlines do objeto Documento. No entanto, para obter também os marcadores filhos, percorra também todos os marcadores em cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtido no primeiro loop. Os trechos de código a seguir mostram como obter marcadores filhos de um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
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
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Atualizar Marcadores em um Documento PDF

Para atualizar um marcador em um arquivo PDF, primeiro obtenha o marcador específico da coleção OutlineColletion do objeto Document, especificando o índice do marcador. Depois de recuperar o marcador no objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), você pode atualizar suas propriedades e então salvar o arquivo PDF atualizado usando o método Save. Os trechos de código a seguir mostram como atualizar marcadores em um documento PDF.

```python

    import aspose.pdf as ap

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

## Marcadores Expandidos ao Visualizar o Documento

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) do objeto Document, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). No entanto, pode haver a necessidade de que todos os marcadores estejam expandidos ao visualizar o arquivo PDF.

Para atender a esse requisito, podemos definir o status aberto para cada item de contorno/marcador como Open. O trecho de código a seguir mostra como definir o status aberto de cada marcador como expandido em um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


