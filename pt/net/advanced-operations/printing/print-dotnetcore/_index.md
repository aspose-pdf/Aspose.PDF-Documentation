---
title: Como imprimir arquivo PDF em .NET Core
linktitle: Imprimindo PDF em .NET Core
type: docs
weight: 40
url: /pt/net/print-dotnetcore/
description: Esta página explica como converter um documento PDF em XPS em .NET Core e adicioná-lo como um trabalho na fila da impressora local.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Como imprimir arquivo PDF em .NET Core",
    "alternativeHeadline": "Imprimir arquivo PDF em .NET Core",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, pdf em .NET Core",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página explica como converter um documento PDF em XPS e adicioná-lo como um trabalho na fila da impressora local."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## **Imprimir documento Pdf em .NET Core**

A biblioteca Aspose.PDF nos permite converter arquivos PDF para XPS. Esta função pode ser útil para organizar a impressão de documentos. Vamos dar uma olhada em um exemplo usando a impressora padrão:

```csharp
class Program
{
    static void Main()
    {
        // Crie a thread secundária e passe o método de impressão para
        // o parâmetro delegado ThreadStart do construtor.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // Configure a thread que usará PrintQueue.AddJob para um único thread.
        printingThread.SetApartmentState(ApartmentState.STA);

        // Inicie a thread de impressão. O método passado para o construtor
        // da Thread será executado.
        printingThread.Start();
    }//fim Main

    private static void PrintPDF(string pdfFileName)
    {
        // Crie o servidor de impressão e a fila de impressão.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // Imprima o arquivo Xps fornecendo validação XPS e notificações de progresso.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0} não pôde ser adicionado à fila de impressão.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\tNão é um arquivo XPS válido. Use a ferramenta de conformidade isXPS para depurá-lo.");
            }
            Console.WriteLine("\tContinuando com o próximo arquivo XPS.\n");
        }
    }
}//fim da classe Program
```
Neste exemplo, convertemos um documento PDF em XPS e o adicionamos como um trabalho à fila da impressora local.

```json
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
```

