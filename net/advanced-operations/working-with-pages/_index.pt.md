---
title: Trabalhando com Páginas PDF em C#
linktitle: Trabalhando com Páginas
type: docs
weight: 20
url: /net/working-with-pages/
description: Como adicionar páginas, cabeçalhos e rodapés, adicionar marcas d'água você pode saber nesta seção. Aspose.PDF para .NET explica todos os detalhes sobre este tópico.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Páginas PDF em C#",
    "alternativeHeadline": "Como trabalhar com Páginas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, página pdf, adicionar página pdf, adicionar número de página, girar página, deletar página",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Como adicionar páginas, cabeçalhos e rodapés, adicionar marcas d'água você pode saber nesta seção. Aspose.PDF para .NET explica todos os detalhes sobre este tópico."
}
</script>
**Aspose.PDF para .NET** permite inserir uma página em um documento PDF em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF. Esta seção mostra como adicionar páginas a um PDF sem o Acrobat Reader.
Você pode adicionar texto ou imagens nos cabeçalhos e rodapés do seu arquivo PDF e escolher diferentes cabeçalhos em seu documento com a biblioteca C# da Aspose.
Também, tente recortar páginas em um documento PDF programaticamente usando C#.

Esta seção ensina como adicionar marcas d'água em seu arquivo PDF usando a classe Artifact. Você verificará o exemplo de programação para esta tarefa.
Adicione número de página usando a classe PageNumberStamp. Para adicionar um Carimbo em seu documento use as classes ImageStamp e TextStamp. Use a adição de uma marca d'água para criar imagens de fundo em seu arquivo PDF com **Aspose.PDF para .NET**.

Você é capaz de fazer o seguinte:

- [Adicionar Páginas](/pdf/net/add-pages/) - adicione páginas na localização desejada ou ao final de um arquivo PDF e exclua uma página do seu documento.
- [Mover Páginas](/pdf/net/move-pages/) - mova páginas de um documento para outro.
- [Mover Páginas](/pdf/net/move-pages/) - mover páginas de um documento para outro.
- [Excluir Páginas](/pdf/net/delete-pages/) - excluir página do seu arquivo PDF usando a coleção PageCollection.
- [Alterar Tamanho da Página](/pdf/net/change-page-size/) - você pode alterar o tamanho da página PDF com trecho de código usando a biblioteca Aspose.PDF.
- [Rotacionar Páginas](/pdf/net/rotate-pages/) - você pode alterar a orientação das páginas em um arquivo PDF existente.
- [Dividir Páginas](/pdf/net/split-document/) - você pode dividir arquivos PDF em um ou vários PDFs.
- [Adicionar Cabeçalhos e/ou Rodapés](/pdf/net/add-headers-and-footers-of-pdf-file/) - adicionar texto ou imagens nos cabeçalhos e rodapés do seu arquivo PDF.
- [Recortar Páginas](/pdf/net/crop-pages/) - você pode recortar páginas em um documento PDF programaticamente com diferentes Propriedades de Página.
- [Adicionar Marcas D'água](/pdf/net/add-watermarks/) - adicionar marcas d'água no seu arquivo PDF com a Classe Artifact.
- [Adicionar Numeração de Páginas no Arquivo PDF](/pdf/net/add-page-number/) - a classe PageNumberStamp ajudará você a adicionar um Número de Página no seu arquivo PDF.
- [Adicionar Numeração de Páginas em Arquivo PDF](/pdf/net/add-page-number/) - A classe PageNumberStamp ajudará você a adicionar um Número de Página no seu arquivo PDF.
- [Adicionar Fundos](/pdf/net/add-backgrounds/) - imagens de fundo podem ser usadas para adicionar uma marca d'água.
- [Carimbando](/pdf/net/stamping/) - você pode usar a classe ImageStamp para adicionar um carimbo de imagem a um arquivo PDF e a classe TextStamp para adicionar um texto.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

