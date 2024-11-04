---
title: Obter, Atualizar e Expandir um Marcador usando Python
linktitle: Obter, Atualizar e Expandir um Marcador
type: docs
weight: 20
url: /python-net/get-update-and-expand-bookmark/
description: Este artigo descreve como usar marcadores em um arquivo PDF com nossa biblioteca Aspose.PDF para Python.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obter, Atualizar e Expandir um Marcador com Python",
    "alternativeHeadline": "Como obter Marcadores de um arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, obter marcadores",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Este artigo descreve como usar marcadores em um arquivo PDF com nossa biblioteca Aspose.PDF para Python."
}
</script>


## Obter Favoritos

A coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contém todos os favoritos de um arquivo PDF. Este artigo explica como obter os favoritos de um arquivo PDF, e como identificar em qual página um determinado favorito está.

Para obter os favoritos, percorra a coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) e obtenha cada favorito na OutlineItemCollection. A [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) fornece acesso a todos os atributos do favorito. O trecho de código a seguir mostra como obter favoritos do arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Percorrer todos os favoritos
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

    # Criar PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Abrir arquivo PDF
    bookmarkEditor.bind_pdf(input_pdf)
    # Extrair marcadores
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Título:", bookmark.title)
        print(str_level_seprator, "Número da Página:", bookmark.page_number)
        print(str_level_seprator, "Ação da Página:", bookmark.action)
```

## Obter Marcadores Filhos de um Documento PDF

Os marcadores podem ser organizados em uma estrutura hierárquica, com pais e filhos.
 Para obter todos os marcadores, faça um loop através das coleções de Outlines do objeto Document. No entanto, para obter também os marcadores filhos, faça um loop através de todos os marcadores em cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtido no primeiro loop. Os seguintes trechos de código mostram como obter marcadores filhos de um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Fazer loop através de todos os marcadores
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Marcadores Filhos")
            # Existem marcadores filhos, então faça um loop através deles também
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Atualizar Favoritos em um Documento PDF

Para atualizar um favorito em um arquivo PDF, primeiro obtenha o favorito específico da coleção OutlineCollection do objeto Document, especificando o índice do favorito. Uma vez que você tenha recuperado o favorito no objeto [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), você pode atualizar suas propriedades e, em seguida, salvar o arquivo PDF atualizado usando o método Save. Os fragmentos de código a seguir mostram como atualizar favoritos em um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obter um objeto de favorito
    outline = document.outlines[1]

    # Obter objeto de favorito filho
    child_outline = outline[1]
    child_outline.title = "Outline Atualizado"
    child_outline.italic = True
    child_outline.bold = True

    # Salvar saída
    document.save(output_pdf)
```

## Favoritos Expandidos ao visualizar o documento

Os favoritos são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) do objeto Document, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 No entanto, podemos ter um requisito para que todos os marcadores sejam expandidos ao visualizar o arquivo PDF.

Para cumprir esse requisito, podemos definir o status de abertura para cada item de contorno/marcador como Aberto. O trecho de código a seguir mostra como definir o status de abertura para cada marcador como expandido em um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Definir modo de visualização da página, ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Percorrer cada item de contorno na coleção de contornos do arquivo PDF
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Definir status de abertura para o item de contorno
        item.open = True

    # Salvar saída
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>