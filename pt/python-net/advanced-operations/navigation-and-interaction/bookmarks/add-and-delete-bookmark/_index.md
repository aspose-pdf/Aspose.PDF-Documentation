---
title: Adicionar e Excluir um Marcador usando Python
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: pt/python-net/add-and-delete-bookmark/
description: Você pode adicionar um marcador a um documento PDF com Python. É possível excluir todos ou determinados marcadores de um documento PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar e Excluir um Marcador",
    "alternativeHeadline": "Como adicionar e excluir Marcador de PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, excluir marcador, adicionar marcador",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Você pode adicionar um marcador a um documento PDF com Python. É possível excluir todos ou determinados marcadores de um documento PDF."
}
</script>


## Adicionar um Marcador a um Documento PDF

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) do objeto Document, que está na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) à coleção Outlines.

O trecho de código a seguir mostra como adicionar um marcador em um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar um objeto de marcador
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Definir o número da página de destino
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Adicionar marcador na coleção de contornos do documento.
    document.outlines.append(outline)

    # Salvar saída
    document.save(output_pdf)
```


## Adicionar um Marcador Filho ao Documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica com marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
1. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definindo suas propriedades.
1. Adicione a OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) do objeto Documento.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção de contornos do marcador pai.

Os trechos de código a seguir mostram como adicionar um marcador filho a um documento PDF.

```python

    import aspose.pdf as ap

    # Abra o documento
    document = ap.Document(input_pdf)

    # Crie um objeto de marcador pai
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Crie um objeto de marcador filho
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Adicione o marcador filho na coleção do marcador pai
    outline.append(childOutline)
    # Adicione o marcador pai na coleção de contornos do documento.
    document.outlines.append(outline)

    # Salvar saída
    document.save(output_pdf)
```


## Excluir todos os Favoritos de um Documento PDF

Todos os favoritos em um PDF são mantidos na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Este artigo explica como excluir todos os favoritos de um arquivo PDF.

Para excluir todos os favoritos de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. Salve o arquivo modificado usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Os trechos de código a seguir mostram como excluir todos os favoritos de um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Excluir todos os favoritos
    document.outlines.delete()

    # Salvar arquivo atualizado
    document.save(output_pdf)

```

## Excluir um Favorito Específico de um Documento PDF

Para excluir um favorito específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). O método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) remove qualquer marcador com o título passado para o método.

Os trechos de código a seguir mostram como deletar um marcador específico do documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Deletar um marcador específico pelo Título
    document.outlines.delete("Child Outline")

    # Salvar arquivo atualizado
    document.save(output_pdf)