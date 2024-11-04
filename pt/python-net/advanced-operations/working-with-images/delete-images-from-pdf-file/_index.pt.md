---
title: Excluir Imagens de Arquivo PDF usando Python
linktitle: Excluir Imagens
type: docs
weight: 20
url: /python-net/delete-images-from-pdf-file/
description: Esta seção explica como excluir imagens de um arquivo PDF usando Aspose.PDF para Python via .NET.
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Excluir Imagens de Arquivo PDF usando Python",
    "alternativeHeadline": "Como remover Imagens de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, excluir, remover imagem de pdf",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "Esta seção explica como excluir imagens de um arquivo PDF usando Aspose.PDF para Python via .NET."
}
</script>


Existem muitas razões para remover todas ou imagens específicas de PDFs.

Às vezes, um arquivo PDF pode conter imagens importantes que precisam ser removidas para proteger a privacidade ou impedir o acesso não autorizado a certas informações.

Remover imagens indesejadas ou redundantes pode ajudar a reduzir o tamanho do arquivo, facilitando o compartilhamento ou armazenamento dos PDFs.

Se necessário, você pode reduzir o número de páginas removendo todas as imagens do documento. Além disso, excluir imagens do documento ajudará a preparar o PDF para compressão ou extração de informações de texto.

**Aspose.PDF for Python via .NET** irá ajudá-lo com esta tarefa.

## Excluir Imagens de Arquivo PDF

Para excluir uma imagem de um arquivo PDF:

1. Abra o Documento PDF existente.
1. Exclua uma imagem específica.
1. Salve o arquivo PDF atualizado.

O trecho de código a seguir mostra como excluir uma imagem de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Abra o documento
    document = ap.Document(input_file)

    # Exclua uma imagem específica
    document.pages[2].resources.images.delete(1)

    # Salve o arquivo PDF atualizado
    document.save(output_pdf)
```


## Excluir todas as imagens do PDF de entrada

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_file)

    # Excluir todas as imagens em todas as páginas
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # Salvar arquivo PDF atualizado
    document.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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