---
title: Membuat PDF yang sesuai dengan PDF/3-A dan melampirkan faktur ZUGFeRD di C#
linktitle: Lampirkan ZUGFeRD ke PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/attach-zugferd/
description: Pelajari cara menghasilkan dokumen PDF dengan ZUGFeRD di Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Temukan fungsionalitas baru yang memungkinkan pengembang untuk menghasilkan dokumen PDF yang sesuai dengan PDF/A-3B dan melampirkan faktur ZUGFeRD dengan lancar menggunakan C#. Fitur ini menyederhanakan proses penyisipan metadata faktur dalam file PDF, memastikan pelestarian dokumen jangka panjang dan kepatuhan terhadap standar faktur elektronik",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Lampirkan ZUGFeRD ke PDF

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

Kami merekomendasikan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

* Tentukan variabel jalur yang menunjuk ke folder tempat file PDF input dan output berada.
* Buat objek dokumen dengan memuat file PDF yang ada (misalnya "ZUGFeRD-test.pdf") dari jalur.
* Buat objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) dengan memberikan jalur dan deskripsi file lain bernama "factur-x.xml", yang berisi metadata faktur yang sesuai dengan standar ZUGFeRD.
* Tambahkan properti ke objek spesifikasi file, seperti deskripsi, tipe MIME, dan hubungan AF. Hubungan AF menunjukkan bagaimana file yang disisipkan terkait dengan dokumen PDF. Dalam hal ini, diatur ke "Alternatif", yang berarti file yang disisipkan adalah representasi alternatif dari konten PDF.
* Tambahkan objek spesifikasi file ke koleksi file yang disisipkan dalam dokumen. Nama file harus ditentukan sesuai dengan standar ZUGFeRD, misalnya "factur-x.xml".
* Konversi dokumen ke format PDF/A-3B, subset dari PDF yang memastikan pelestarian jangka panjang dokumen elektronik. PDF/A-3B memungkinkan penyisipan file dalam format apa pun ke dalam dokumen PDF.
* Simpan dokumen yang telah dikonversi sebagai file PDF baru (misalnya "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

Metode konversi mengambil stream, format PDF, dan tindakan kesalahan konversi sebagai parameter. Parameter stream dapat digunakan untuk menyimpan log konversi. Parameter tindakan kesalahan konversi menentukan apa yang harus dilakukan jika terjadi kesalahan selama konversi. Dalam hal ini, diatur ke "Hapus", yang berarti bahwa elemen yang tidak sesuai dengan format PDF/A-3B akan dihapus dari dokumen.