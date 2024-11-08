---
title: Impressão de PDF no .NET Framework
linktitle: Impressão de PDF no .NET Framework
type: docs
weight: 10
url: /pt/net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: Você pode imprimir arquivos PDF na impressora padrão usando as configurações de impressora e página com C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impressão de PDF no .NET Framework",
    "alternativeHeadline": "Como imprimir PDF no .NET Framework",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, pdf no .NET Framework",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode imprimir arquivos PDF na impressora padrão usando as configurações de impressora e página com C#."
}
</script>
## **Imprimir Arquivo Pdf em C# - Imprimir Arquivo PDF para Impressora Padrão Usando Configurações de Impressora e de Página**

Este artigo descreve como imprimir um arquivo PDF para a impressora padrão usando configurações de impressora e de página em C#.

A classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) permite que você imprima um arquivo PDF na impressora padrão. Você precisa criar um objeto PdfViewer e abrir o PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Para especificar diferentes configurações de impressão, use as classes `PageSettings` e `PrinterSettings`. Finalmente, chame o método [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) para imprimir o PDF na impressora padrão. O seguinte trecho de código mostra como imprimir PDF para a impressora padrão com configurações de impressora e de página.

```csharp
public static void SimplePrint()
{
    // Criar objeto PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Abrir arquivo PDF de entrada
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Definir atributos para impressão
    viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
    viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada
    viewer.PrintPageDialog = false;   // Não exibir o diálogo de número de página ao imprimir

    // Criar objetos para configurações de impressora e de página e PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Definir nome da impressora
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Definir tamanho da página (se necessário)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Definir margens da página (se necessário)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimir documento usando configurações de impressora e de página
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Fechar o arquivo PDF após a impressão
    viewer.Close();
}
```
Para exibir um diálogo de impressão, tente usar o seguinte trecho de código:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // O código de impressão do documento vai aqui
    // Imprimir documento usando configurações de impressora e página
    viewer.PrintDocumentWithSettings(pgs, ps);
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

