---
title: Generate Thumbnail Images from PDF
linktitle: Generate Thumbnail Images
type: docs
weight: 110
url: /net/generate-thumbnail-images-from-pdf-documents/
description: Esta seção descreve como gerar imagens em miniatura a partir de documentos PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "How to generate Thumbnail Images from PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, generate thumbnail Images",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção descreve como gerar imagens em miniatura a partir de documentos PDF"
}
</script>
{{% alert color="primary" %}}

O SDK do Adobe Acrobat é um conjunto de ferramentas que ajudam você a desenvolver software que interage com a tecnologia Acrobat. O SDK contém arquivos de cabeçalho, bibliotecas de tipos, utilitários simples, código de exemplo e documentação.

Usando o SDK do Acrobat, você pode desenvolver software que se integra ao Acrobat e ao Adobe Reader de várias maneiras:

- **JavaScript** — Escreva scripts, seja em um documento PDF individual ou externamente, para estender a funcionalidade do Acrobat ou do Adobe Reader.
- **Plug-ins** — Crie plug-ins que são vinculados dinamicamente e estendem a funcionalidade do Acrobat ou do Adobe Reader.
- **Comunicação interaplicativos** — Escreva um processo de aplicativo separado que usa comunicação interaplicativos (IAC) para controlar a funcionalidade do Acrobat. DDE e OLE são suportados no Microsoft® Windows®, e eventos da Apple/AppleScript no Mac OS®. IAC não está disponível no UNIX®.

O Aspose.PDF para .NET oferece muitas das mesmas funcionalidades, libertando-o da dependência da Automação do Adobe Acrobat.
Aspose.PDF para .NET oferece muitas das mesmas funcionalidades, libertando-o da dependência da Automação do Adobe Acrobat.

{{% /alert %}}

## Desenvolvendo Aplicativo usando a API de Comunicação Interaplicativa do Acrobat

Pense na API do Acrobat como tendo duas camadas distintas que usam objetos de Comunicação Interaplicativa (IAC) do Acrobat:

- A camada da aplicação Acrobat (AV). A camada AV permite controlar como o documento é visualizado. Por exemplo, a visualização de um objeto de documento reside na camada associada ao Acrobat.
- A camada de documento portátil (PD). A camada PD fornece acesso às informações dentro de um documento, como uma página. A partir da camada PD, você pode realizar manipulações básicas de documentos PDF, como excluir, mover ou substituir páginas, além de alterar atributos de anotação. Você também pode imprimir páginas PDF, selecionar texto, acessar texto manipulado e criar ou excluir miniaturas.

Como nosso objetivo é converter páginas PDF em imagens de miniaturas, estamos focando mais no IAC.
À medida que nosso objetivo é converter páginas PDF em imagens em miniatura, estamos focando mais em IAC.

### Abordagem Acrobat

Para gerar as imagens em miniatura para cada documento, utilizamos o Adobe Acrobat 7.0 SDK e o Microsoft .NET 2.0 Framework.

O [Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combinado com a versão completa do Adobe Acrobat expõe uma biblioteca COM de objetos (infelizmente, o Adobe Reader gratuito não expõe as interfaces COM) que pode ser usada para manipular e acessar informações de PDF. Usando esses objetos COM via COM Interop, carregue o documento PDF, obtenha a primeira página e renderize essa página para a área de transferência. Em seguida, com o .NET Framework, copie isso para um bitmap, escale e combine a imagem e salve o resultado como um arquivo GIF ou PNG.

Uma vez que o Adobe Acrobat esteja instalado, use o regedit.exe e procure em HKEY_CLASSES_ROOT pela entrada chamada AcroExch.PDDoc.

**O registro mostrando a entrada AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Abordagem Aspose.PDF para .NET

Aspose.PDF para .NET oferece suporte extensivo para lidar com documentos PDF. Também suporta a capacidade de converter as páginas de documentos PDF em uma variedade de formatos de imagem. A funcionalidade descrita acima pode ser facilmente alcançada usando Aspose.PDF para .NET.

Aspose.PDF tem benefícios distintos:

- Você não precisa ter o Adobe Acrobat instalado em seu sistema para trabalhar com arquivos PDF.
- Usar Aspose.PDF para .NET é simples e fácil de entender em comparação com a Automação do Acrobat.

Se precisarmos converter páginas PDF em JPEGs, o namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) fornece uma classe chamada [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) para renderizar páginas PDF em imagens JPEG.
Se precisarmos converter páginas de PDF em JPEGs, o namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) fornece uma classe chamada [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) para renderizar páginas de PDF em imagens JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- Obrigado ao CodeProject por [Gerar Imagem em Miniatura a partir de documento PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Obrigado ao Acrobat pela [Referência do SDK do Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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


