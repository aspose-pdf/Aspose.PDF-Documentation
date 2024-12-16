---
title: PdfFileMend Class
type: docs
weight: 20
url: /id/java/pdffilemend-class/
description: Bagian ini menjelaskan cara bekerja dengan Aspose.PDF Facades menggunakan Kelas PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Tampaknya bukan tugas yang sulit untuk memasukkan [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) ke dalam dokumen PDF, dengan syarat Anda memiliki versi asli yang dapat diedit dari dokumen ini. Misalkan Anda membuat dokumen, dan kemudian teringat bahwa Anda perlu menambahkan baris lain atau kita berbicara tentang volume dokumen yang lebih besar, dalam kedua kasus tersebut akan membantu Anda Aspose.PDF Facades. Mari kita pertimbangkan kemungkinan menambahkan teks dalam File PDF yang sudah ada dengan kelas [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## Tambahkan Teks dalam File PDF yang Ada (facades)

Kita dapat menambahkan teks dengan beberapa cara.
 Pertimbangkan yang pertama. Kami mengambil [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) dan menambahkannya ke Halaman. Setelah itu, kami menunjukkan koordinat sudut kiri bawah, dan kemudian kami menambahkan teks kami ke Halaman.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Selamat datang di Aspose!");

        mender.AddText(message, 1, 10, 750);

        // simpan file keluaran
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

Periksa bagaimana tampilannya:

![Tambahkan Teks](/pdf/id/net/images/add_text.png)

Cara kedua untuk menambahkan [FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext). Selain itu, kami menunjukkan sebuah persegi panjang di mana teks kami harus sesuai.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Selamat datang di Aspose! Selamat datang di Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // simpan file keluaran
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

Contoh ketiga memberikan kemampuan untuk Menambahkan Teks ke halaman tertentu. Dalam contoh kita, mari tambahkan keterangan pada halaman 1 dan 3 dari dokumen.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Welcome to Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // simpan file keluaran
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## Menambahkan Gambar dalam File PDF yang Ada (facades)

Pernahkah Anda mencoba menambahkan gambar ke file PDF yang ada?
 Kami yakin Anda tahu bahwa ini bukan tugas yang mudah. Mungkin Anda sedang mengisi formulir online dan Anda perlu melampirkan foto untuk identifikasi atau melampirkan foto Anda ke resume yang sudah ada. Sebelumnya, tugas semacam ini diselesaikan dengan membuat foto, melampirkannya ke dokumen, kemudian memindai dan mengirimkannya. Proses ini sangat merepotkan dan memakan waktu.

Menambahkan gambar dan teks dalam file PDF yang sudah ada adalah kebutuhan umum dan com.aspose.pdf.facades namespace memenuhi kebutuhan ini dengan sangat baik. Ini menyediakan kelas [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) yang memungkinkan Anda menambahkan gambar dalam file PDF.

Artikel ini akan menunjukkan kepada Anda cara menyisipkan gambar ke dalam PDF menggunakan com.aspose.pdf.facades. Ada juga beberapa opsi untuk menambahkan gambar ke PDF.

Sisipkan gambar ke dalam dokumen PDF dengan mengatur parameter dari persegi panjang.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // Muat gambar ke dalam stream
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // simpan file output
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Add Image](/pdf/id/net/images/add_image1.png)

Mari kita pertimbangkan cuplikan kode kedua. Dengan menggunakan variasi dari parameter kelas [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters), kita dapat memperoleh efek desain yang berbeda. Kami mencoba salah satu dari mereka.

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Memuat gambar ke dalam stream
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // menyimpan file keluaran
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Tambahkan Gambar](/pdf/id/net/images/add_image2.png)

Dalam cuplikan kode berikut, kita menggunakan [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). ImageFilterType menunjukkan jenis codec aliran yang akan digunakan untuk encoding, secara default Jpeg. jika Anda memuat gambar dari format PNG, maka akan disimpan dalam dokumen sebagai JPEG (atau dalam format lain yang telah saya tentukan).

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Muat gambar ke dalam stream
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // simpan file output
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


Pada cuplikan kode berikut, Anda dapat mencatat penggunaan metode [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) adalah sebuah bendera, yang menunjukkan apakah akan menerapkan sebuah masker pada gambar untuk mencapai transparansi dari gambar asli

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // Memuat gambar ke dalam aliran
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // menyimpan file keluaran
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```