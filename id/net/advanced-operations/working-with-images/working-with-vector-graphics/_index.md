---
title: Bekerja dengan Grafik Vektor
linktitle: Bekerja dengan Grafik Vektor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /id/net/working-with-vector-graphics/
description: Artikel ini menjelaskan fitur-fitur bekerja dengan alat GraphicsAbsorber menggunakan C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics in PDF",
    "alternativeHeadline": "Programmatically manipulate PDF vector graphics",
    "abstract": "Manipulasi grafik vektor dalam dokumen PDF secara programatis menggunakan kelas GraphicsAbsorber yang baru. Perpustakaan C# Aspose.PDF for .NET memungkinkan kontrol yang tepat atas elemen grafis, memungkinkan tindakan seperti memindahkan, menghapus, dan menambahkan grafik untuk meningkatkan visual PDF. Alat ini menawarkan metode manipulasi individu dan massal untuk kinerja optimal",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "GraphicsAbsorber, Vector Graphics, PDF Manipulation, C# library, Aspose.PDF, Move Graphics, Remove Graphics, Add Graphics, PDF Vector Graphics",
    "wordcount": "967",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "Bagian ini menjelaskan fitur-fitur bekerja dengan file PDF GraphicsAbsorber menggunakan perpustakaan C#."
}
</script>

Dalam bab ini, kita akan menjelajahi cara menggunakan kelas `GraphicsAbsorber` yang kuat untuk berinteraksi dengan grafik vektor dalam dokumen PDF. Apakah Anda perlu memindahkan, menghapus, atau menambahkan grafik, panduan ini akan menunjukkan cara melakukan tugas-tugas ini secara efektif. Mari kita mulai!

## Pendahuluan<a name="introduction"></a>

Grafik vektor adalah komponen penting dari banyak dokumen PDF, digunakan untuk merepresentasikan gambar, bentuk, dan elemen grafis lainnya. Aspose.PDF menyediakan kelas `GraphicsAbsorber`, yang memungkinkan pengembang untuk mengakses dan memanipulasi grafik ini secara programatis. Dengan menggunakan metode `Visit` dari `GraphicsAbsorber`, Anda dapat mengekstrak grafik vektor dari halaman tertentu dan melakukan berbagai operasi, seperti memindahkan, menghapus, atau menyalinnya ke halaman lain.

## 1. Mengekstrak Grafik dengan `GraphicsAbsorber`<a name="extracting-graphics"></a>

Langkah pertama dalam bekerja dengan grafik vektor adalah mengekstraknya dari dokumen PDF. Berikut adalah cara melakukannya menggunakan kelas `GraphicsAbsorber`:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}

```

### Penjelasan:

1. **Buat Objek Dokumen**: Sebuah objek `Document` baru diinstansiasi dengan jalur ke file PDF target.
2. **Buat Instance dari `GraphicsAbsorber`**: Kelas ini menangkap semua elemen grafik dari halaman tertentu.
3. **Metode Visit**: Metode `Visit` dipanggil pada halaman pertama, memungkinkan `GraphicsAbsorber` untuk menyerap grafik vektor.
4. **Iterasi Melalui Elemen yang Diekstrak**: Kode melakukan loop melalui setiap elemen yang diekstrak, mencetak informasi seperti nomor halaman, posisi, dan jumlah operator gambar yang terlibat.

## 2. Memindahkan Grafik<a name="moving-graphics"></a>

Setelah Anda mengekstrak grafik, Anda dapat memindahkannya ke posisi yang berbeda di halaman yang sama. Berikut adalah cara mencapainya:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Move graphics by shifting their X and Y coordinates
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "MoveGraphics_out.pdf");
        }
    }
}
```

### Poin Kunci:

- **SuppressUpdate**: Metode ini sementara menangguhkan pembaruan untuk meningkatkan kinerja saat melakukan beberapa perubahan.
- **ResumeUpdate**: Metode ini melanjutkan pembaruan dan menerapkan perubahan yang dilakukan pada posisi grafik.
- **Penempatan Elemen**: Posisi setiap grafik disesuaikan dengan mengubah koordinat `X` dan `Y`-nya.

## 3. Menghapus Grafik<a name="removing-graphics"></a>

Ada skenario di mana Anda mungkin ingin menghapus grafik tertentu dari sebuah halaman. Aspose.PDF menawarkan dua metode untuk mencapai ini:

### Metode 1: Menggunakan Batasan Persegi Panjang

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suppress updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove those inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                if (rectangle.Contains(element.Position))
                {
                    element.Remove(); // Remove the graphic element
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### Metode 2: Menggunakan Koleksi Elemen yang Dihapus

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection to store the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Iterate through the extracted elements and add those inside the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the graphics elements from the page
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### Penjelasan:

- **Batasan Persegi Panjang**: Tentukan area persegi panjang untuk menentukan grafik mana yang akan dihapus.
- **Suppress dan Resume Updates**: Pastikan penghapusan yang efisien tanpa rendering sementara.

## 4. Menambahkan Grafik ke Halaman Lain<a name="adding-graphics"></a>

Grafik yang diserap dari satu halaman dapat ditambahkan ke halaman lain dalam dokumen yang sama. Berikut adalah dua metode untuk mencapainya:

### Metode 1: Menambahkan Grafik Secara Individu

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### Metode 2: Menambahkan Grafik sebagai Koleksi

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics elements to the second page at once
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### Poin Kunci:

- **SuppressUpdate dan ResumeUpdate**: Metode ini membantu dalam mempertahankan kinerja saat melakukan perubahan massal.
- **AddOnPage vs. AddGraphics**: Gunakan `AddOnPage` untuk penambahan individu dan `AddGraphics` untuk penambahan massal.

## Kesimpulan

Dalam bab ini, kita menjelajahi cara menggunakan kelas `GraphicsAbsorber` untuk mengekstrak, memindahkan, menghapus, dan menambahkan grafik vektor dalam dokumen PDF menggunakan Aspose.PDF. Dengan menguasai teknik-teknik ini, Anda dapat secara signifikan meningkatkan presentasi visual PDF Anda dan membuat dokumen yang dinamis dan menarik secara visual.

Silakan bereksperimen dengan contoh kode dan sesuaikan dengan kasus penggunaan spesifik Anda. Selamat coding!

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