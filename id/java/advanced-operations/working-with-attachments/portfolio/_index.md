---
title: Bekerja dengan Portofolio dalam Dokumen PDF
linktitle: Portofolio
type: docs
weight: 40
url: /id/java/portfolio/
description: Cara Membuat Portofolio PDF dengan Java. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Pertama, mari kita pahami **Apa itu format file Portofolio PDF?**

Sebagai contoh, ambil file Portofolio PDF yang berisi presentasi Word, Excel, PowerPoint, dll, sebagai lampiran. Di sini setiap lampiran menjaga format dokumen aslinya, tetapi diintegrasikan atau disusun menjadi satu file Portofolio PDF. Anda tentu saja dapat membuka, membaca, atau mengedit masing-masing file individu dari Portofolio PDF seolah-olah file tersebut berada di drive atau folder. Selain itu, seperti dokumen PDF biasa, Anda juga dapat menerapkan watermark, mengatur kata sandi, dan izin keamanan seperti kemampuan untuk melihat, mencetak, atau membuat perubahan pada lampiran dari Portofolio PDF.

Kita dapat menempatkan atau menyusun file asli, dalam tipe atau format aslinya sebagai lampiran, ke dalam file Portofolio PDF.

## Cara Membuat Portofolio PDF

Aspose.PDF memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Tambahkan file ke dalam objek Document.Collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Ketika file telah ditambahkan, gunakan metode Save dari kelas Document untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.

Kode di bawah ini menghasilkan portofolio berikut.

### Portofolio PDF yang dibuat dengan Aspose.PDF

![Portofolio PDF yang dibuat dengan Aspose.PDF untuk Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Memperkenalkan Objek Document
        Document pdfDocument = new Document();

        // Memperkenalkan objek Collection dokumen
        pdfDocument.setCollection(new Collection());

        // Mendapatkan File untuk ditambahkan ke Portofolio
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // Menyediakan deskripsi file
        excel.setDescription ("File Excel");
        word.setDescription ("File Word");
        image.setDescription ("File Gambar");

        // Menambahkan file ke koleksi dokumen
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // Menyimpan dokumen Portofolio
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## Ekstrak file dari PDF Portfolio

PDF Portofolio memungkinkan Anda untuk menggabungkan konten dari berbagai sumber (misalnya, file PDF, Word, Excel, JPEG) ke dalam satu wadah yang terintegrasi. File asli mempertahankan identitas individual mereka tetapi dirakit menjadi file PDF Portofolio. Pengguna dapat membuka, membaca, mengedit, dan memformat setiap file komponen secara independen dari file komponen lainnya.

Aspose.PDF memungkinkan pembuatan dokumen PDF Portofolio menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Ini juga menawarkan kemampuan untuk mengekstrak file dari PDF portofolio.

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengekstrak file dari PDF portofolio.

![Ekstrak file dari PDF Portfolio](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // Dapatkan koleksi file tersemat
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // Iterasi melalui file individual dari Portofolio
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## Hapus File dari PDF Portfolio

Untuk menghapus/menghapus file dari PDF portfolio, coba gunakan baris kode berikut.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // Muat PDF Portfolio sumber
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```