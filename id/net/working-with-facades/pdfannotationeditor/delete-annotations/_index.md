---
title: Hapus Anotasi (facades)
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/delete-annotations/
description: Bagian ini menjelaskan cara menghapus anotasi dengan Aspose.PDF Facades menggunakan Kelas PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Annotations (facades)",
    "alternativeHeadline": "Effortlessly Remove Specific PDF Annotations with Ease",
    "abstract": "Fitur Aspose.PDF for .NET Facades memungkinkan pengguna untuk secara efisien menghapus anotasi dari file PDF yang ada menggunakan kelas PdfAnnotationEditor. Dengan kemampuan untuk menghapus semua anotasi atau menargetkan jenis anotasi tertentu, pengguna dapat memperlancar pengeditan dokumen dan meningkatkan kemampuan manajemen PDF mereka. Fungsionalitas ini menyederhanakan proses pemeliharaan dokumen PDF yang bersih dan fokus dengan menyediakan metode yang jelas untuk penghapusan anotasi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "427",
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
    "url": "/net/delete-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Hapus Semua Anotasi dari File PDF yang Ada

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) memungkinkan Anda menghapus semua anotasi dari file PDF yang ada. Pertama, buat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) dan ikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) untuk menghapus semua anotasi dari file, dan kemudian gunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan cara menghapus semua anotasi dari file PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

        // Delete all annoations
        annotationEditor.DeleteAnnotations();

        // Save PDF document
        annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

    // Delete all annoations
    annotationEditor.DeleteAnnotations();

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Semua Anotasi berdasarkan Tipe yang Ditentukan

Anda dapat menggunakan kelas [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) untuk menghapus semua anotasi, berdasarkan tipe anotasi yang ditentukan, dari file PDF yang ada. Untuk melakukan itu, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations), dengan parameter string, untuk menghapus semua anotasi dari file; parameter string mewakili tipe anotasi yang akan dihapus. Akhirnya, gunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan cara menghapus semua anotasi berdasarkan tipe anotasi yang ditentukan.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Collect all annotation types from all pages
        var annotationTypes = new List<string>();
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            // If page has no annotations, skip it
            if (page.Annotations == null)
            {
                continue;
            }

            // Retrieve each annotation type from the page
            IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
            annotationTypes.AddRange(pageAnnotationTypes);
        }

        // Make the list of annotation types distinct
        annotationTypes = annotationTypes.Distinct().ToList();

        // Display each annotation type to the user
        int index;
        for (index = 0; index < annotationTypes.Count; index++)
        {
            Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
        }

        // Prompt user to choose the annotation type to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine()) - 1;

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotations(annotationTypes[index]);

            // Save PDF document
            annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Collect all annotation types from all pages
    var annotationTypes = new List<string>();
    foreach (Aspose.Pdf.Page page in document.Pages)
    {
        // If page has no annotations, skip it
        if (page.Annotations == null)
        {
            continue;
        }

        // Retrieve each annotation type from the page
        IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
        annotationTypes.AddRange(pageAnnotationTypes);
    }

    // Make the list of annotation types distinct
    annotationTypes = annotationTypes.Distinct().ToList();

    // Display each annotation type to the user
    int index;
    for (index = 0; index < annotationTypes.Count; index++)
    {
        Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
    }

    // Prompt user to choose the annotation type to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine()) - 1;

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotations(annotationTypes[index]);

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Anotasi berdasarkan Nama yang Ditentukan

Anda dapat menggunakan kelas [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) untuk menghapus anotasi tertentu, berdasarkan **nama unik**-nya, dari file PDF yang ada. Untuk melakukan itu, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotation), dengan menyertakan nama anotasi yang akan dihapus. Akhirnya, gunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan cara menghapus anotasi berdasarkan namanya.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Display the list of annotations in the first page (adjust as needed for multiple pages)
        int index;
        for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
        {
            Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
        }

        // Prompt the user to enter the index of the annotation to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine());

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Save PDF document
            annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Display the list of annotations in the first page (adjust as needed for multiple pages)
    int index;
    for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
    {
        Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
    }

    // Prompt the user to enter the index of the annotation to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine());

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}