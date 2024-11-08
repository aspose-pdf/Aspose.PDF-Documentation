---
title: Imprimir PDF em aplicação WPF
linktitle: Imprimir documento PDF em aplicação WPF
type: docs
weight: 50
url: /pt/net/print-pdf-document-in-wpf-application/
description: Imprimir documentos PDF de uma aplicação WPF usando C#. Este exemplo de código mostra como imprimir documentos PDF de uma aplicação WPF usando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Imprimir PDF em aplicação WPF",
    "alternativeHeadline": "Como imprimir PDF em aplicação WPF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, pdf em aplicação WPF",
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
    "url": "/net/print-pdf-document-in-wpf-application/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-pdf-document-in-wpf-application/"
    },
    "dateModified": "2022-02-04",
    "description": "Imprimir documentos PDF de uma aplicação WPF usando C#. Este exemplo de código mostra como imprimir documentos PDF de uma aplicação WPF usando C#."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Impressão direta

A biblioteca Aspose.PDF tem a capacidade de converter arquivos PDF para XPS. Podemos usar essa função para organizar a impressão de documentos.
Vamos considerar o exemplo para impressão direta:

```csharp
    private void Print_OnClick(object sender, RoutedEventArgs e)
    {
        var openFileDialog = new OpenFileDialog
        {
            Filter = "Documentos PDF|*.pdf"
        };
        openFileDialog.ShowDialog();

        Aspose.Pdf.Document document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        var package = Package.Open(memoryStream);

        //Criar URI para o pacote Xps
        //Qualquer Uri será na verdade adequado aqui. Ele atua como um substituto para o
        //Uri do pacote dentro do PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Adicionar pacote ao PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();

        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator, "Um documento fixo");
            else
                throw new NullReferenceException();
        }
        PackageStore.RemovePackage(packageUri);
        xpsDoc.Close();

    }
```
Neste caso, seguiremos estas etapas:

1. Abrir arquivo PDF usando OpenFileDialog
1. Converter PDF para XPS e armazenar em um objeto MemoryStream
1. Associar o objeto MemoryStream com o pacote Xps
1. Adicionar o pacote ao Armazenamento de Pacotes
1. Criar um XpsDocument baseado no pacote
1. Obter uma instância da sequência FixedDocumentSequence
1. Enviar esta sequência para a impressora usando PrintDialog

## Visualizar e imprimir documento

Em muitos casos, os usuários querem ver o documento antes de imprimir. Para implementar uma visualização, podemos usar uma classe DocViewer.
A maioria das etapas para implementar essa abordagem é semelhante ao exemplo anterior.

```csharp
private void OpenFile_OnClick(object sender, RoutedEventArgs e)
{
    var openFileDialog = new OpenFileDialog
    {
        Filter = "Documentos PDF|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        var document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        var package = Package.Open(memoryStream);

        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Adicionar pacote ao Armazenamento de Pacotes
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        DocViewer.Document = xpsDoc.GetFixedDocumentSequence();
        xpsDoc.Close();
    };
}
```

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

