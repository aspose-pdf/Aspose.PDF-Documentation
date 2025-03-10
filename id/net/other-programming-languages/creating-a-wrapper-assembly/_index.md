---
title: Membuat Wrapper Assembly
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/creating-a-wrapper-assembly/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a Wrapper Assembly",
    "alternativeHeadline": "Simplify COM Interop with Wrapper Assemblies",
    "abstract": "Fitur Wrapper Assembly baru untuk Aspose.PDF for .NET memungkinkan pengembang untuk membuat antarmuka yang disederhanakan untuk berinteraksi dengan kelas, metode, dan properti Aspose.PDF dari kode yang tidak dikelola. Dengan mengenkapsulasi kompleksitas COM Interop, fungsionalitas ini memperlancar pengembangan proyek, membuatnya lebih mudah untuk mengelola dan memanfaatkan fungsionalitas PDF tanpa memerlukan keterampilan lanjutan dalam pemrograman .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "244",
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
    "url": "/net/creating-a-wrapper-assembly/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/creating-a-wrapper-assembly/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Jika Anda perlu menggunakan banyak kelas, metode, dan properti Aspose.PDF for .NET, pertimbangkan untuk membuat wrapper assembly (menggunakan C# atau bahasa pemrograman .NET lainnya). Wrapper assemblies membantu menghindari penggunaan Aspose.PDF for .NET secara langsung dari kode yang tidak dikelola.

Pendekatan yang baik adalah mengembangkan assembly .NET yang mereferensikan Aspose.PDF for .NET dan melakukan semua pekerjaan dengannya, dan hanya mengekspos seperangkat kelas dan metode minimal ke kode yang tidak dikelola. Aplikasi Anda kemudian harus bekerja hanya dengan pustaka wrapper Anda.

Mengurangi jumlah kelas dan metode yang perlu Anda panggil melalui COM Interop menyederhanakan proyek. Menggunakan kelas .NET melalui COM Interop sering kali memerlukan keterampilan lanjutan.

{{% /alert %}}

## Wrapper Aspose.PDF for .NET

```csharp
using System.Runtime.InteropServices;

namespace TextRetriever
{
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IRetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [ClassInterface(ClassInterfaceType.None)]
    [ComSourceInterfaces(typeof(IRetriever))]
    public class Retriever : IRetriever
    {
        public void SetLicense(string file)
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // Open PDF document
            using (var document = new Aspose.Pdf.Document(file))
            {
                // Create TextAbsorber object to extract text
                var absorber = new Aspose.Pdf.Text.TextAbsorber();

                // Accept the absorber for all document's pages
                document.Pages.Accept(absorber);

                // Get the extracted text
                string text = absorber.Text;

                return text;
            }
        }
    }
}
```