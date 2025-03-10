---
title: Menggabungkan file PDF menggunakan .NET 5
linktitle: Cara menggabungkan PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /id/net/how-to-concatenate-pdf-files-in-different-ways/
description: Artikel ini menjelaskan cara-cara yang mungkin untuk menggabungkan sejumlah file PDF yang ada menjadi satu file PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Gabungkan beberapa file PDF menjadi satu dokumen secara mulus dengan fungsionalitas baru di Aspose.PDF for .NET. Fitur ini memungkinkan pengembang untuk menggabungkan sejumlah PDF melalui panggilan metode sederhana, meningkatkan produktivitas dalam manajemen dan manipulasi PDF. Integrasikan kemampuan ini dengan mudah ke dalam berbagai aplikasi .NET, termasuk aplikasi ASP.NET dan Windows, dengan pendekatan yang fleksibel yang memenuhi berbagai kebutuhan",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Artikel ini menjelaskan bagaimana Anda dapat [Menggabungkan](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) beberapa Dokumen PDF menjadi Satu Dokumen PDF dengan bantuan Komponen [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) membuat pekerjaan ini seperti sepotong kue.

{{% /alert %}}

Yang perlu Anda lakukan adalah memanggil metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dan semua file PDF input Anda akan digabungkan bersama dan satu file PDF akan dihasilkan. Mari kita buat aplikasi untuk berlatih penggabungan file PDF. Kita akan membuat aplikasi menggunakan Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET dapat digunakan dalam jenis aplikasi apa pun yang berjalan di .NET Framework baik itu aplikasi web ASP.NET atau Aplikasi Windows

{{% /alert %}}

## Cara Menggabungkan File PDF dengan Cara yang Berbeda

Dalam formulir, terdapat tiga Kotak Teks (textBox1, textBox2, textBox3) yang memiliki Label Tautan masing-masing (linkLabel1, linkLabel2, linkLabel3) untuk menjelajahi file PDF. Dengan mengklik Label Tautan "Browse", Dialog File Input (inputFileDialog1) akan muncul yang memungkinkan kita memilih file PDF (yang akan digabungkan).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

Tampilan aplikasi formulir windows ditunjukkan untuk demonstrasi kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) untuk Penggabungan File PDF.

![Menggabungkan File PDF](how-to-concatenate-pdf-files-in-different-ways_1.png)

Setelah kita memilih file PDF dan mengklik tombol OK. Nama file lengkap dengan jalur ditugaskan ke Kotak Teks terkait.

![Pilih file PDF](how-to-concatenate-pdf-files-in-different-ways_2.png)

Demikian pula, kita dapat memilih dua atau tiga File PDF Input untuk digabungkan seperti yang ditunjukkan di bawah ini:

![Pilih dua atau tiga File PDF Input](how-to-concatenate-pdf-files-in-different-ways_3.png)

Kotak Teks terakhir (textBox4) akan mengambil Jalur Tujuan dari file PDF output dengan namanya di mana file output ini akan dibuat.

![Jalur Tujuan dari file PDF output](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Metode Concatenate](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Metode Concatenate()

Metode Concatenate() dapat digunakan dengan tiga cara. Mari kita lihat lebih dekat masing-masing dari mereka:

### Pendekatan 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Pendekatan ini baik hanya jika Anda perlu menggabungkan hanya dua file PDF. Dua argumen pertama (firstInputFile dan secInputFile) memberikan nama file lengkap dengan jalur penyimpanan dari dua file PDF input yang akan digabungkan. Argumen ketiga (outputFile) memberikan nama file yang diinginkan dengan jalur dari file PDF output.

![Menggabungkan dua PDF menggunakan Nama File](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Pendekatan 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

Mirip dengan pendekatan di atas, pendekatan ini juga memungkinkan penggabungan dua file PDF. Dua argumen pertama (firstInputStream dan secInputStream) memberikan dua file PDF input sebagai Stream (stream adalah array bit/byte) yang akan digabungkan. Argumen ketiga (outputStream) memberikan representasi stream dari file PDF output yang diinginkan.

![Menggabungkan dua PDF menggunakan Stream File](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### Pendekatan 3

- Concatenate(Stream inputStreams[], Stream outputStream)

Jika Anda ingin menggabungkan lebih dari dua file PDF maka pendekatan ini akan menjadi pilihan utama Anda. Argumen pertama (inputStreams[]) memberikan file PDF input dalam bentuk Array Stream yang akan digabungkan. Argumen kedua (outputStream) memberikan representasi stream dari file PDF output yang diinginkan.

![Menggabungkan beberapa PDF menggunakan Array Stream](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```