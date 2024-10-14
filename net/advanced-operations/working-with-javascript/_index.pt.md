---
title: Trabalhando com JavaScript
type: docs
url: /net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com JavaScript",
    "alternativeHeadline": "Como trabalhar com JavaScript em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, javascript em pdf",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## Adicionando JavaScript (DOM)

### O que é Acrobat JavaScript?

Acrobat JavaScript é uma linguagem baseada no núcleo da versão 1.5 do JavaScript da ISO-16262, anteriormente conhecida como ECMAScript, uma linguagem de script orientada a objetos desenvolvida pela Netscape Communications. O JavaScript foi criado para transferir o processamento de páginas da Web de um servidor para um cliente em aplicações baseadas na Web. O Acrobat JavaScript implementa extensões, na forma de novos objetos e seus métodos e propriedades correspondentes, à linguagem JavaScript. Esses objetos específicos do Acrobat permitem que um desenvolvedor gerencie a segurança do documento, comunique-se com um banco de dados, manipule anexos de arquivo, manipule um arquivo PDF para que ele se comporte como um formulário interativo e habilitado para a web, entre outros. Como os objetos específicos do Acrobat são adicionados em cima do JavaScript core, você ainda tem acesso às suas classes padrão, incluindo Math, String, Date, Array e RegExp.

### Acrobat JavaScript vs HTML (Web) JavaScript

Os documentos PDF têm grande versatilidade, pois podem ser exibidos tanto dentro do software Acrobat quanto em um navegador Web.
Os documentos PDF têm grande versatilidade, pois podem ser exibidos tanto no software Acrobat quanto em um navegador da Web.

- O JavaScript do Acrobat não tem acesso a objetos dentro de uma página HTML. Da mesma forma, o JavaScript HTML não pode acessar objetos dentro de um arquivo PDF.
- O JavaScript HTML é capaz de manipular objetos como Window. O JavaScript do Acrobat não pode acessar este objeto específico, mas pode manipular objetos específicos do PDF.

Você pode adicionar JavaScript tanto no nível do documento quanto no nível da página usando [Aspose.PDF for .NET](/pdf/net/). Para adicionar JavaScript:

### Adicionando JavaScript à Ação do Documento ou da Página

1. Declare e instancie um objeto JavascriptAction com a declaração de JavaScript desejada como argumento do construtor.
1. Atribua o objeto JavascriptAction à ação desejada do documento ou página PDF.

O exemplo abaixo aplica o OpenAction a um documento específico.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **Adicionando/Removendo JavaScript no Nível do Documento**
### **Adicionando/Removendo JavaScript no Nível do Documento**

Uma nova propriedade chamada JavaScript é adicionada na classe Documento, que possui tipo de coleção JavaScript e fornece acesso aos cenários de JavaScript por sua chave. Esta propriedade é usada para adicionar JavaScript no nível do Documento. A coleção JavaScript possui as seguintes propriedades e métodos:

- string this(string key) – Obtém ou define o JavaScript pelo seu nome
- IList Keys – fornece uma lista de chaves existentes na coleção JavaScript
- bool Remove(string key) – remove o JavaScript pela sua chave.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


