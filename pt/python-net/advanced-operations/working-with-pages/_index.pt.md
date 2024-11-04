---
title: Trabalhando com Páginas de PDF em Python
linktitle: Trabalhando com Páginas
type: docs
weight: 20
url: /python-net/working-with-pages/
description: Como adicionar páginas, adicionar cabeçalhos e rodapés, adicionar marcas d'água você pode saber nesta seção. Aspose.PDF para Python via .NET explica a você todos os detalhes sobre este tópico.
lastmod: "2023-04-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Páginas de PDF em Python",
    "alternativeHeadline": "Como trabalhar com Páginas de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, página pdf, adicionar página pdf, adicionar número de página, girar página, excluir página",
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
    "url": "/python-net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-pages/"
    },
    "dateModified": "2023-02-04",
    "description": "Como adicionar páginas, adicionar cabeçalhos e rodapés, adicionar marcas d'água você pode saber nesta seção. Aspose.PDF para Python via .NET explica a você todos os detalhes sobre este tópico."
}
</script>


**Aspose.PDF for Python via .NET** permite que você insira uma página em um documento PDF em qualquer local do arquivo, bem como adicione páginas ao final de um arquivo PDF. Esta seção mostra como adicionar páginas a um PDF sem o Acrobat Reader. Você pode adicionar texto ou imagens nos cabeçalhos e rodapés do seu arquivo PDF e escolher diferentes cabeçalhos em seu documento com a biblioteca Python da Aspose. Além disso, tente cortar páginas em um documento PDF programaticamente usando Python.

Esta seção ensina como adicionar marcas d'água em seu arquivo PDF usando a classe Artifact. Você verificará o exemplo de programação para esta tarefa. Adicione o número da página usando a classe [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/). Para adicionar um carimbo em seu documento, use as classes [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) e [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). Use a adição de uma marca d'água para criar imagens de fundo em seu arquivo PDF com **Aspose.PDF for Python via .NET**.


Você pode fazer o seguinte:

- [Adicionar Páginas](/pdf/python-net/add-pages/) - adicionar páginas no local desejado ou ao final de um arquivo PDF e excluir uma página do seu documento.
- [Mover Páginas](/pdf/python-net/move-pages/) - mover páginas de um documento para outro.
- [Excluir Páginas](/pdf/python-net/delete-pages/) - excluir página do seu arquivo PDF usando a coleção PageCollection.
- [Alterar Tamanho da Página](/pdf/python-net/change-page-size/) - você pode alterar o tamanho da página do PDF com um trecho de código usando a biblioteca Aspose.PDF.
- [Rotacionar Páginas](/pdf/python-net/rotate-pages/) - você pode alterar a orientação das páginas em um arquivo PDF existente.
- [Dividir Páginas](/pdf/python-net/split-document/) - você pode dividir arquivos PDF em um ou vários PDFs.
- [Adicionar Cabeçalhos e/ou Rodapés](/pdf/python-net/add-headers-and-footers-of-pdf-file/) - adicionar texto ou imagens nos cabeçalhos e rodapés do seu arquivo PDF.
- [Cortar Páginas](/pdf/python-net/crop-pages/) - você pode cortar páginas em um documento PDF programaticamente com diferentes Propriedades de Página.

- [Adicionar Marca d'água](/pdf/python-net/add-watermarks/) - adicionar marcas d'água no seu arquivo PDF com a Classe Artifact.
- [Adicionar Numeração de Página em Arquivo PDF](/pdf/python-net/add-page-number/) - A classe PageNumberStamp ajudará você a adicionar um número de página no seu arquivo PDF.
- [Adicionar Fundos](/pdf/python-net/add-backgrounds/) - imagens de fundo podem ser usadas para adicionar uma marca d'água.
- [Carimbar](/pdf/python-net/stamping/) - você pode usar a classe ImageStamp para adicionar um carimbo de imagem a um arquivo PDF e a classe TextStamp para adicionar um texto.
- [Obter e Definir Propriedades da Página](/pdf/python-net/get-and-set-page-properties/) - esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página do PDF, como cor, e definir propriedades da página.

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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>