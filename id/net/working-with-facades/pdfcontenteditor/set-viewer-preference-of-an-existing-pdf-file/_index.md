---
title: Atur Preferensi Penampil PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/set-viewer-preference-of-an-existing-pdf-file/
description: Bagian ini menunjukkan cara mengatur preferensi penampil dari file PDF yang ada menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Tingkatkan pengalaman pengguna dokumen PDF Anda dengan memanfaatkan fitur Atur Preferensi Penampil. Fungsionalitas ini memungkinkan pengembang untuk menyesuaikan mode tampilan, seperti memusatkan jendela, menyembunyikan bilah menu, dan mengaktifkan mode layar penuh, menggunakan kelas PdfContentEditor. Permudah presentasi dokumen dan pastikan tampilan optimal untuk audiens Anda dengan pengaturan yang disesuaikan ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "338",
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
    "url": "/net/set-viewer-preference-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-viewer-preference-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Atur Preferensi Penampil dari File PDF yang Ada

[ViewerPreference](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/viewerpreference) kelas mewakili mode tampilan file PDF; misalnya, memposisikan jendela dokumen di tengah layar, menyembunyikan bilah menu aplikasi penampil, dll.

Metode [ChangeViewerPreference](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) dalam kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk mengubah preferensi penampil. Untuk melakukan itu, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Setelah itu, Anda dapat memanggil metode [ChangeViewerPreference](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) untuk mengatur preferensi apa pun. Akhirnya, Anda harus menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save/index). Potongan kode berikut menunjukkan kepada Anda cara mengubah preferensi penampil dalam file PDF yang ada.

Sebagai contoh, kami menentukan parameter [CenterWindow](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) di mana kami memusatkan jendela, setelah menghapus bilah alat atas dengan [HideMenubar](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) dan dengan [PageModeUseNone](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) membuka mode layar penuh.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Change Viewer Preferences
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Change Viewer Preferences
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}