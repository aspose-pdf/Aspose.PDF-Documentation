---
title: Importar anotações no formato FDF para PDF via C#
linktitle: Importar anotações no formato FDF para PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/import-fdf/
description: Use os métodos existentes Form.ImportFdf() ou PdfAnnotationEditor.ImportAnnotationsFromFdf() para importar anotações no formato FDF para PDF com Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Importe anotações no formato FDF para arquivos PDF de forma contínua usando Aspose.PDF for .NET, aprimorando suas capacidades de gerenciamento de PDF. Com os métodos Form.ImportFdf() e PdfAnnotationEditor.ImportAnnotationsFromFdf(), você pode integrar facilmente dados de formulários e comentários de arquivos FDF leves em seus documentos PDF, simplificando os processos de envio de dados e anotações.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

FDF (Forms Data Format) é um formato de arquivo que armazena e transmite dados de formulários e anotações em documentos PDF. É uma versão leve do PDF que contém apenas os valores dos campos do formulário ou comentários, sem o conteúdo completo do arquivo PDF original. Os arquivos FDF são frequentemente usados ao enviar dados de formulários para um servidor ou ao trocar anotações sem precisar enviar o arquivo PDF inteiro. Eles podem ser importados de volta para um PDF para preencher campos de formulário ou aplicar comentários.

{{% /alert %}}

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfannotationeditor/) contém métodos para trabalhar com a importação de anotações de arquivos FDF. O método [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) fornece a funcionalidade para importar anotações de um documento FDF para um arquivo PDF.

Além disso, a [Classe Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/) inclui o método [Form.ImportFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/importfdf/) - importa o conteúdo dos campos do arquivo FDF e os coloca no novo PDF.

O seguinte trecho de código mostra como importar anotações no formato FDF para PDF com o método Form.ImportFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

O próximo trecho de código mostra como importar anotações no formato FDF para PDF com o método PdfAnnotationEditor.ImportAnnotationsFromFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```