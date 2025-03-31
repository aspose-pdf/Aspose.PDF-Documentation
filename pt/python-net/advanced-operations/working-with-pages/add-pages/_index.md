---
title: Adicionar Páginas em PDF com Python
linktitle: Adicionar Páginas
type: docs
weight: 10
url: /pt/python-net/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página no local desejado em um arquivo PDF. Aprenda a mover, remover (excluir) páginas de um arquivo PDF usando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Páginas em PDF com Python",
    "alternativeHeadline": "Como adicionar Páginas em documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, adicionar página pdf, inserir página pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo ensina como inserir (adicionar) uma página no local desejado em um arquivo PDF. Aprenda a mover, remover (excluir) páginas de um arquivo PDF usando Python."
}
</script>


Aspose.PDF para Python via .NET API fornece total flexibilidade para trabalhar com páginas em um documento PDF usando Python. Ele mantém todas as páginas de um documento PDF em [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) que pode ser usada para trabalhar com páginas PDF. Aspose.PDF para Python via .NET permite que você insira uma página em um documento PDF em qualquer local no arquivo, bem como adicione páginas ao final de um arquivo PDF. Esta seção mostra como adicionar páginas a um PDF usando Python.

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para Python via .NET permite que você insira uma página em um documento PDF em qualquer local no arquivo, bem como adicione páginas ao final de um arquivo PDF.

### Inserir Página Vazia em um Arquivo PDF no Local Desejado

Para inserir uma página vazia em um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de entrada.

1. Chame o método [insert](https://reference.aspose.com/pdf/pt/net/aspose.pdf/pagecollection/methods/insert) da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) com o índice especificado.
1. Salve o PDF de saída usando o método [save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/save/methods/4).

O trecho de código a seguir mostra como inserir uma página em um arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Inserir uma página vazia em um PDF
    document.pages.insert(2)
    # Salvar arquivo de saída
    document.save(output_pdf)
```

### Adicionar uma Página Vazia no Final de um Arquivo PDF

Às vezes, você quer garantir que um documento termine em uma página vazia. Este tópico explica como inserir uma página vazia no final do documento PDF.

Para inserir uma página vazia no final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de entrada.

1. Chame o método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) sem nenhum parâmetro.
1. Salve o PDF de saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O trecho de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Inserir uma página vazia no final de um arquivo PDF
    document.pages.add()

    # Salvar arquivo de saída
    document.save(output_pdf)