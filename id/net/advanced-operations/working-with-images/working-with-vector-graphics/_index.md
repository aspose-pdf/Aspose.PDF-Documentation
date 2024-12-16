---
title: Bekerja dengan Grafik Vektor
linktitle: Bekerja dengan Grafik Vektor
type: docs
weight: 120
url: /id/net/working-with-vector-graphics/
description: Artikel ini menjelaskan fitur-fitur dari bekerja dengan alat GraphicsAbsorber menggunakan C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan GraphicsAbsorber",
    "alternativeHeadline": "Cara mendapatkan posisi gambar dalam file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, GraphicsAbsorber dalam pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan fitur-fitur dari bekerja dengan file PDF GraphicsAbsorber menggunakan perpustakaan C#."
}
</script>
Dalam bab ini, kita akan menjelajahi cara menggunakan kelas `GraphicsAbsorber` yang kuat untuk berinteraksi dengan grafik vektor dalam dokumen PDF. Apakah Anda perlu memindahkan, menghapus, atau menambah grafik, panduan ini akan menunjukkan kepada Anda cara melakukan tugas-tugas tersebut dengan efektif. Mari kita mulai!

## Pendahuluan<a name="introduction"></a>

Grafik vektor adalah komponen penting dari banyak dokumen PDF, digunakan untuk merepresentasikan gambar, bentuk, dan elemen grafis lainnya. Aspose.PDF menyediakan kelas `GraphicsAbsorber`, yang memungkinkan pengembang untuk mengakses dan memanipulasi grafik ini secara programatik. Dengan menggunakan metode `Visit` dari `GraphicsAbsorber`, Anda dapat mengekstrak grafik vektor dari halaman yang ditentukan dan melakukan berbagai operasi, seperti memindahkan, menghapus, atau menyalinnya ke halaman lain.

## 1. Mengekstrak Grafik dengan `GraphicsAbsorber`<a name="extracting-graphics"></a>

Langkah pertama dalam bekerja dengan grafik vektor adalah mengekstraknya dari dokumen PDF. Berikut cara melakukannya menggunakan kelas `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // Langkah 1: Buat objek Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Langkah 2: Buat instansi dari GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // Pilih halaman pertama dari dokumen.
    var page = document.Pages[1];

    // Langkah 3: Gunakan metode `Visit` untuk mengekstrak grafik dari halaman.
    graphicsAbsorber.Visit(page);

    // Tampilkan informasi tentang elemen yang diekstrak.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"Nomor Halaman: {element.SourcePage.Number}");
        Console.WriteLine($"Posisi: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"Jumlah Operator: {element.Operators.Count}");
    }
}
```
### Penjelasan:

1. **Membuat Objek Dokumen**: Sebuah objek `Document` baru diinstansiasi dengan path ke file PDF target.
2. **Membuat Instansi dari `GraphicsAbsorber`**: Kelas ini menangkap semua elemen grafis dari halaman yang ditentukan.
3. **Metode Visit**: Metode `Visit` dipanggil di halaman pertama, memungkinkan `GraphicsAbsorber` untuk menyerap grafis vektor.
4. **Iterasi Melalui Elemen yang Diekstrak**: Kode melakukan looping melalui setiap elemen yang diekstrak, mencetak informasi seperti nomor halaman, posisi, dan jumlah operator gambar yang terlibat.

## 2. Memindahkan Grafik<a name="moving-graphics"></a>

Setelah Anda mengekstrak grafik, Anda dapat memindahkannya ke posisi yang berbeda di halaman yang sama. Berikut cara untuk mencapainya:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // Sementara menangguhkan pembaruan untuk meningkatkan kinerja.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // Memindahkan grafik dengan menggeser koordinat X dan Y-nya.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // Melanjutkan pembaruan dan menerapkan perubahan.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Poin Utama:

- **SuppressUpdate**: Metode ini sementara menangguhkan pembaruan untuk meningkatkan kinerja saat melakukan beberapa perubahan.
- **ResumeUpdate**: Metode ini melanjutkan pembaruan dan menerapkan perubahan yang dibuat pada posisi grafis.
- **Penempatan Elemen**: Posisi setiap grafis diatur dengan mengubah koordinat `X` dan `Y` nya.

## 3. Menghapus Grafis<a name="removing-graphics"></a>

Terdapat skenario di mana Anda mungkin ingin menghapus grafis tertentu dari halaman. Aspose.PDF menawarkan dua metode untuk mencapainya:

### Metode 1: Menggunakan Batas Persegi Panjang

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // Periksa apakah posisi grafis berada dalam persegi panjang.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Hapus elemen grafis.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Metode 2: Menggunakan Kumpulan Elemen yang Dihapus

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Penjelasan:

- **Batasan Persegi Panjang**: Mendefinisikan area persegi panjang untuk menentukan grafik apa yang akan dihapus.
- **Menekan dan Melanjutkan Pembaruan**: Memastikan penghapusan efisien tanpa rendering sementara.

## 4. Menambahkan Grafik ke Halaman Lain<a name="adding-graphics"></a>

Grafik yang diserap dari satu halaman dapat ditambahkan ke halaman lain dalam dokumen yang sama.
Grafik yang terserap dari satu halaman dapat ditambahkan ke halaman lain dalam dokumen yang sama.

### Metode 1: Menambahkan Grafik Secara Individual

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // Menambahkan setiap elemen grafis ke halaman kedua.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Metode 2: Menambahkan Grafik sebagai Koleksi

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // Menambahkan semua grafik sekaligus.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Poin Kunci:

- **SuppressUpdate dan ResumeUpdate**: Metode ini membantu dalam menjaga kinerja saat melakukan perubahan massal.
- **AddOnPage vs. AddGraphics**: Gunakan `AddOnPage` untuk penambahan individu dan `AddGraphics` untuk penambahan massal.

## Kesimpulan

Dalam bab ini, kita telah mengeksplorasi cara menggunakan kelas `GraphicsAbsorber` untuk mengekstrak, memindahkan, menghapus, dan menambahkan grafis vektor dalam dokumen PDF menggunakan Aspose.PDF. Dengan menguasai teknik-teknik ini, Anda dapat secara signifikan meningkatkan presentasi visual PDF Anda dan menciptakan dokumen yang dinamis dan menarik secara visual.

Jangan ragu untuk bereksperimen dengan contoh kode dan menyesuaikannya dengan kasus penggunaan spesifik Anda. Selamat coding!

