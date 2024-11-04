---
title: Exemplo de Hello World usando a linguagem Python
linktitle: Exemplo de Hello World
type: docs
weight: 20
url: /python-cpp/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples "Hello, World!" usando Aspose.PDF para Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exemplo de Hello World usando a linguagem Python",
    "alternativeHeadline": "Exemplo Aspose.PDF Python (via C++)",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, Python, geração de documentos",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Este exemplo demonstra como criar um documento PDF simples usando Aspose.PDF para Python.",
    "articleBody": "Um caso de uso simples pode ajudar a demonstrar os recursos de uma linguagem de programação ou software. Isso é geralmente feito com um exemplo de "Hello World".\n\nAspose.PDF para Python via C++ é uma poderosa API de PDF que permite aos desenvolvedores criar, manipular e converter documentos PDF em suas aplicações Python. Ele suporta o trabalho com vários formatos de arquivo, como PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, mostraremos como criar um documento PDF com o texto "Hello World!" usando a API Aspose.PDF. Você precisa instalar o Aspose.PDF para Python via C++ em seu ambiente antes de executar o seguinte exemplo de código.\n1. Importe o módulo AsposePdfPython.\n2. Crie um novo objeto de documento PDF usando a função document_create.\n3. Obtenha a coleção de páginas do documento usando a função document_get_pages.\n4. Adicione uma nova página à coleção de páginas usando a função page_collection_add_page.\n5. Obtenha a coleção de parágrafos da página usando a função page_get_paragraphs.\n6. Crie um novo objeto de imagem usando a função image_create.\n7. Defina o nome do arquivo do objeto de imagem como "sample.jpg" usando a função image_set_file.\n8. Adicione o objeto de imagem à coleção de parágrafos usando a função paragraphs_add_image.\n9. Salve o documento em um arquivo chamado "document.pdf" usando a função document_save.\n10. Feche o manipulador de documentos usando a função close_handle."
}
</script>


Um caso de uso simples pode ajudar a demonstrar os recursos de uma linguagem de programação ou software. Isso geralmente é feito com um exemplo "Hello World".

Aspose.PDF para Python via C++ é uma poderosa API de PDF que permite aos desenvolvedores criar, manipular e converter documentos PDF em suas aplicações Python. Ele suporta trabalhar com vários formatos de arquivo, como PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, mostraremos como criar um documento PDF com o texto "Hello World!" usando a API Aspose.PDF. Você precisa instalar o Aspose.PDF para Python via C++ em seu ambiente antes de executar o exemplo de código a seguir.

1. Importe o módulo `AsposePdfPython`.
1. Crie um novo objeto de documento PDF usando a função `document_create`.
1. Obtenha a coleção de páginas do documento usando a função `document_get_pages`.
1. Adicione uma nova página à coleção de páginas usando a função `page_collection_add_page`.

1. Obtenha a coleção de parágrafos da página usando a função `page_get_paragraphs`.
1. Criando um novo objeto de imagem usando a função `image_create`.
1. Definindo o nome do arquivo do objeto de imagem para "sample.jpg" usando a função `image_set_file`.
1. Adicionando o objeto de imagem à coleção de parágrafos usando a função `paragraphs_add_image`.
1. Salvando o documento em um arquivo chamado "document.pdf" usando a função `document_save`.
1. Fechando o manipulador do documento usando a função `close_handle`.

O trecho de código a seguir é um programa Hello World que demonstra como o Aspose.PDF para Python via C++ funciona.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```