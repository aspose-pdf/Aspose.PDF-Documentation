---
title: Menjustifikasi Teks dalam Field Textbox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/justify-text-in-a-textbox-field/
description: Artikel ini menunjukkan kepada Anda cara Menjustifikasi Teks dalam Field Textbox menggunakan Kelas Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "Fitur ini memungkinkan pengguna untuk menjustifikasi teks dalam field textbox di dokumen PDF menggunakan kelas FormEditor dari namespace Aspose.Pdf.Facades. Dengan memanfaatkan opsi AlignJustified, pengguna dapat mencapai penyelarasan teks yang menarik secara visual sambil mempertahankan fungsionalitas, meskipun penyelarasan yang dijustifikasi tidak didukung selama input aktif. Ini meningkatkan presentasi data formulir dalam file PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Dalam artikel ini, kami akan menunjukkan kepada Anda cara menjustifikasi teks dalam field textbox di file PDF.

{{% /alert %}}

## Detail implementasi

Kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dalam [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) menawarkan kemampuan untuk menghias field formulir PDF. Sekarang, jika kebutuhan Anda adalah untuk menjustifikasi teks dalam field textbox, Anda dapat dengan mudah mencapainya menggunakan nilai [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) dari enumerasi [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) dan memanggil metode [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). Dalam contoh di bawah ini, pertama-tama kita akan mengisi Field Textbox menggunakan metode [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) dari kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Setelah itu kita akan menggunakan kelas FormEditor untuk menjustifikasi Teks dalam Field Textbox. Potongan kode berikut menunjukkan kepada Anda cara menjustifikasi teks dalam Field Textbox.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
Harap dicatat bahwa penyelarasan yang dijustifikasi tidak didukung oleh PDF, oleh karena itu teks akan diselaraskan ke kiri saat Anda memasukkan teks dalam Field Textbox. Namun, ketika field tidak aktif, teks akan dijustifikasi.