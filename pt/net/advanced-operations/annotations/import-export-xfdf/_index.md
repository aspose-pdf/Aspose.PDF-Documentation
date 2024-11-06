---
title: Importação e Exportação de Anotações para XFDF
linktitle: Importação e Exportação de Anotações para XFDF
type: docs
weight: 40
url: pt/net/import-export-xfdf/
description: Você pode importar e exportar anotações no formato XFDF com C# e a biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Importação e Exportação de Anotações para XFDF",
    "alternativeHeadline": "Métodos para importar e exportar dados de anotações para arquivos XFDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, importação exportação para XFDF",
    "wordcount": "302",
    "proficiencyLevel": "Iniciante",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode importar e exportar anotações no formato XFDF com C# e a biblioteca Aspose.PDF para .NET."
}
</script>
{{% alert color="primary" %}}

XFDF significa XML Forms Data Format. É um formato de arquivo baseado em XML. Esse formato de arquivo é usado para representar dados de formulário ou anotações contidas em um formulário PDF. O XFDF pode ser usado para diversos fins, mas no nosso caso, pode ser usado para enviar ou receber dados de formulário ou anotações para outros computadores ou servidores etc, ou pode ser usado para arquivar os dados do formulário ou anotações. Neste artigo, veremos como o Aspose.Pdf.Facades levou esse conceito em consideração e como podemos importar e exportar dados de anotações para arquivos XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** é um componente rico em recursos quando se trata de editar documentos PDF. Como sabemos que XFDF é um aspecto importante da manipulação de formulários PDF, o namespace Aspose.Pdf.Facades em Aspose.PDF for .NET considerou isso muito bem e forneceu métodos para importar e exportar dados de anotações para arquivos XFDF.

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contém dois métodos para trabalhar com importação e exportação de anotações para arquivo XFDF.
A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contém dois métodos para trabalhar com importação e exportação de anotações para o arquivo XFDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

O seguinte trecho de código mostra como exportar anotações para um arquivo XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // O caminho para o diretório de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// Importando anotações do arquivo XFDF
        /// Arquivo no Formato de Dados de Formulários XML (XFDF) criado pelo Adobe Acrobat, uma aplicação de autoria PDF;
        /// armazena descrições de elementos de formulário de página e seus valores, como os nomes e valores para
        /// campos de texto; usado para salvar dados de formulário que podem ser importados em um documento PDF.
        /// Você pode importar dados de anotação do arquivo XFDF para PDF usando
        /// o método ImportAnnotationsFromXfdf na classe PdfAnnotationEditor.
        /// </summary>

        public static void ExportAnnotationXFDF()
        {
            // Criar objeto PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // Vincular documento PDF ao Editor de Anotações
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));

            // Exportar anotações
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
O próximo trecho de código descreve como importar anotações para um arquivo XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // Cria objeto PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Cria um novo documento PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importa anotação
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Salva o PDF de saída
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Outra maneira de exportar/importar anotações de uma só vez

No código abaixo, um método ImportAnnotations permite importar anotações diretamente de outro documento PDF.

```csharp
        /// <summary>
        /// O método ImportAnnotations permite importar anotações diretamente de outro documento PDF
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // Cria objeto PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // Cria um novo documento PDF
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // O Editor de Anotações permite importar anotações de vários documentos PDF,
            // mas neste exemplo, usamos apenas um.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // Salva o PDF de saída
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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

