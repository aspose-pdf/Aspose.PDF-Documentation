---
title: Bekerja dengan Operator
linktitle: Bekerja dengan Operator
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /id/net/working-with-operators/
description: Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Kelas operator menyediakan fitur hebat untuk manipulasi PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "Fitur Operator dalam Aspose.PDF for .NET meningkatkan kemampuan manipulasi PDF dengan memungkinkan pengguna untuk memanfaatkan kelas operator tertentu untuk tugas seperti menambahkan gambar dan menghapus grafik. Fungsionalitas ini menyederhanakan proses mendefinisikan elemen grafis dan statusnya dalam PDF, memberikan pengembang alat yang kuat untuk pengeditan dan pemrosesan dokumen yang lebih halus.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Kelas operator menyediakan fitur hebat untuk manipulasi PDF."
}
</script>

## Pengenalan Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan beberapa tindakan yang akan dilakukan, seperti melukis bentuk grafis di halaman. Kata kunci operator dibedakan dari objek bernama dengan tidak adanya karakter solidus awal (2Fh). Operator hanya berarti di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan dilukis di halaman. Detail lebih lanjut tentang operator PDF dapat ditemukan di [spesifikasi PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detail Implementasi

Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Contoh yang dipilih menambahkan gambar ke dalam file PDF untuk menggambarkan konsep tersebut. Untuk menambahkan gambar dalam file PDF, operator yang berbeda diperlukan. Contoh ini menggunakan [GSave](https://reference.aspose.com/pdf/id/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://reference.aspose.com/pdf/id/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://reference.aspose.com/pdf/id/net/aspose.pdf.ioperatorselector/visit/methods/14), dan [GRestore](https://reference.aspose.com/pdf/id/net/aspose.pdf.ioperatorselector/visit/methods/26).

- Operator **GSave** menyimpan status grafis saat ini dari PDF.
- Operator **ConcatenateMatrix** (matriks gabungan) digunakan untuk menentukan bagaimana gambar harus ditempatkan di halaman PDF.
- Operator **Do** menggambar gambar di halaman.
- Operator **GRestore** mengembalikan status grafis.

Untuk menambahkan gambar ke dalam file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document) dan buka dokumen PDF input.
1. Dapatkan halaman tertentu tempat gambar akan ditambahkan.
1. Tambahkan gambar ke dalam koleksi Sumber halaman.
1. Gunakan operator untuk menempatkan gambar di halaman:
   - Pertama, gunakan operator GSave untuk menyimpan status grafis saat ini.
   - Kemudian gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan ditempatkan.
   - Gunakan operator Do untuk menggambar gambar di halaman.
1. Terakhir, gunakan operator GRestore untuk menyimpan status grafis yang diperbarui.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan kode berikut menunjukkan cara menggunakan operator PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## Menggambar XForm di Halaman menggunakan Operator

Topik ini menunjukkan cara menggunakan operator GSave/GRestore, operator ContatenateMatrix untuk memposisikan xForm dan operator Do untuk menggambar xForm di halaman.

Kode di bawah ini membungkus konten yang ada dari file PDF dengan pasangan operator GSave/GRestore. Pendekatan ini membantu mendapatkan status grafis awal di akhir konten yang ada. Tanpa pendekatan ini, transformasi yang tidak diinginkan mungkin tetap ada di akhir rantai operator yang ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## Menghapus Objek Grafik menggunakan Kelas Operator

Kelas operator menyediakan fitur hebat untuk manipulasi PDF. Ketika file PDF berisi grafik yang tidak dapat dihapus menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor), kelas operator dapat digunakan untuk menghapusnya sebagai gantinya.

Potongan kode berikut menunjukkan cara menghapus grafik. Harap dicatat bahwa jika file PDF berisi label teks untuk grafik, mereka mungkin tetap ada di file PDF, menggunakan pendekatan ini. Oleh karena itu, cari operator grafik untuk metode alternatif untuk menghapus gambar semacam itu.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
      }
  }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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