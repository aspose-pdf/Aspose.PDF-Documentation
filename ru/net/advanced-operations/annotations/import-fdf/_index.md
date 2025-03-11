---
title: Импорт аннотаций формата FDF в PDF через C#
linktitle: Импорт аннотаций формата FDF в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/import-fdf/
description: Используйте существующие методы Form.ImportFdf() или добавьте PdfAnnotationEditor.ImportAnnotationsFromFdf(), чтобы импортировать аннотации формата FDF в PDF с помощью Aspose.PDF for .NET.
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
    "abstract": "Импортируйте аннотации формата FDF в файлы PDF без проблем с помощью Aspose.PDF для .NET, расширяя возможности управления PDF-документами. С помощью методов Form.ImportFdf() и PdfAnnotationEditor.ImportAnnotationsFromFdf() вы можете легко интегрировать данные форм и комментарии из облегчённых FDF-файлов в ваши PDF-документы, оптимизируя процессы отправки данных и создания аннотаций",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

FDF (формат данных форм) — это формат файла, который хранит и передаёт данные форм и аннотации в документах PDF. Это облегчённая версия PDF, которая содержит только значения полей форм или комментарии, без полного содержимого исходного файла PDF. Файлы FDF часто используются при отправке данных формы на сервер или при обмене аннотациями без необходимости отправлять весь файл PDF. Их можно импортировать обратно в PDF для заполнения полей форм или применения комментариев.

{{% /alert %}}

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/) содержит метод для работы с импортом аннотаций из файла FDF. Метод [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) обеспечивает возможность импорта аннотаций из документа FDF в файл PDF.

Также класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/) включает метод [Form.ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/importfdf/), который импортирует содержимое полей из файла FDF и помещает их в новый PDF.

Следующий фрагмент кода показывает, как импортировать аннотации формата FDF в PDF с помощью метода Form.ImportFdf():

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

Следующий фрагмент кода демонстрирует, как импортировать аннотации формата FDF в PDF с помощью метода PdfAnnotationEditor.ImportAnnotationsFromFdf():

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