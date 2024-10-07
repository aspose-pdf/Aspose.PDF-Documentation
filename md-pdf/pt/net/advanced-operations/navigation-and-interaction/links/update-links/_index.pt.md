---
title: Atualizar Links em PDF
linktitle: Atualizar Links
type: docs
weight: 20
url: /net/update-links/
description: Atualizar links em PDF programaticamente. Este guia é sobre como atualizar links em PDF na linguagem C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Atualizar Links em PDF",
    "alternativeHeadline": "Como atualizar Links em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, atualizar link em pdf",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Atualizar links em PDF programaticamente. Este guia é sobre como atualizar links em PDF na linguagem C#."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Atualizar Links em Arquivo PDF

Conforme discutido em Adicionar Hiperlink em um Arquivo PDF, a classe [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) possibilita a adição de links em um arquivo PDF. Há também uma classe similar usada para obter links existentes dentro de arquivos PDF. Use isso se você precisar atualizar um link existente. Para atualizar um link existente:

1. Carregue um arquivo PDF.
1. Vá para uma página específica no arquivo PDF.
1. Especifique o destino do link usando a propriedade Destination do objeto [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. A página de destino é especificada usando o construtor [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### Definir Destino do Link para uma Página no Mesmo Documento

O seguinte trecho de código mostra como atualizar um link em um arquivo PDF e definir seu alvo para a segunda página do documento.
O seguinte trecho de código mostra como atualizar um link em um arquivo PDF e definir seu destino para a segunda página do documento.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Carregar o arquivo PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// Obter a primeira anotação de link da primeira página do documento
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modificação do link: alterar destino do link
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// Especificar o destino para o objeto de link
// O primeiro parâmetro é o objeto do documento, o segundo é o número da página de destino.
// O 5º argumento é o fator de zoom ao exibir a página respectiva. Ao usar 2, a página será exibida com zoom de 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// Salvar o documento com o link atualizado
doc.Save(dataDir);
```
### Definir Destino do Link para um Endereço Web

Para atualizar o hiperlink de modo que aponte para um endereço web, instancie o objeto [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) e passe-o para a propriedade Action da LinkAnnotation. O seguinte trecho de código mostra como atualizar um link em um arquivo PDF e definir seu alvo para um endereço web.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Carregar o arquivo PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// Obter a primeira anotação de link da primeira página do documento
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modificação do link: alterar a ação do link e definir o alvo como endereço web
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// Salvar o documento com o link atualizado
doc.Save(dataDir);
```
### Definir Destino do Link para Outro Arquivo PDF

O seguinte trecho de código mostra como atualizar um link em um arquivo PDF e definir seu destino para outro arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Carregar o arquivo PDF
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// Próxima linha atualiza destino, não atualizar arquivo
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// Próxima linha atualiza arquivo
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// Salvar o documento com link atualizado
document.Save(dataDir);
```

### Atualizar Cor do Texto de LinkAnnotation

A anotação de link não contém texto.
A anotação de link não contém texto.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Carregar o arquivo PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // Procurar o texto sob a anotação
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // Mudar a cor do texto.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// Salvar o documento com o link atualizado
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
```

