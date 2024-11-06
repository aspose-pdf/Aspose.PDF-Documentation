---
title: Bekerja dengan Portofolio dalam PDF
linktitle: Portofolio
type: docs
weight: 40
url: id/net/portfolio/
description: Cara Membuat Portofolio PDF dengan C#. Anda harus menggunakan Berkas Excel Microsoft, dokumen Word, dan berkas gambar untuk membuat Portofolio PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Portofolio dalam PDF",
    "alternativeHeadline": "Membuat Portofolio dalam dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf dalam pdf",
    "keywords": "pdf, c#, portofolio",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "Cara Membuat Portofolio PDF dengan C#. Anda harus menggunakan Berkas Excel Microsoft, dokumen Word, dan berkas gambar untuk membuat Portofolio PDF."
}
</script>
## Cara Membuat PDF Portfolio

Aspose.PDF memungkinkan pembuatan dokumen PDF Portfolio menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Tambahkan file ke dalam objek Document.Collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Setelah file telah ditambahkan, gunakan metode Save dari kelas Document untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat PDF Portfolio.

Kode di bawah ini menghasilkan portofolio berikut.

Kode snippet berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

### PDF Portfolio yang dibuat dengan Aspose.PDF

![PDF Portfolio yang dibuat dengan Aspose.PDF untuk .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Instansiasi Objek Dokumen
Document doc = new Document();

// Instansiasi objek Koleksi dokumen
doc.Collection = new Collection();

// Dapatkan File untuk ditambahkan ke Portfolio
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Berikan deskripsi file
excel.Description = "File Excel";
word.Description = "File Word";
image.Description = "File Gambar";

// Tambahkan file ke koleksi dokumen
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// Simpan dokumen Portfolio
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## Ekstrak file dari PDF Portfolio

PDF Portfolio memungkinkan Anda untuk menggabungkan konten dari berbagai sumber (misalnya, file PDF, Word, Excel, JPEG) ke dalam satu wadah terpadu. File asli tetap mempertahankan identitas individu mereka tetapi disusun menjadi file PDF Portfolio. Pengguna dapat membuka, membaca, mengedit, dan memformat setiap file komponen secara independen dari file komponen lainnya.

Aspose.PDF memungkinkan pembuatan dokumen PDF Portfolio menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ini juga menawarkan kemampuan untuk mengekstrak file dari PDF portfolio.

Potongan kode berikut menunjukkan langkah-langkah untuk mengekstrak file dari PDF portfolio.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Muat PDF Portfolio sumber
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Dapatkan koleksi file yang tertanam
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Iterasi melalui file individu dari Portfolio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Dapatkan lampiran dan tulis ke file atau aliran
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Simpan file yang diekstrak ke lokasi tertentu
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Tutup objek aliran
    fileStream.Close();
}
```
![Mengekstrak file dari Portofolio PDF](working-with-pdf-portfolio_2.jpg)

## Menghapus File dari Portofolio PDF

Untuk menghapus file dari portofolio PDF, coba gunakan baris kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Memuat Portofolio PDF sumber
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
```

