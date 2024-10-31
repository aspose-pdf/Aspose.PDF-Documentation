---
title: Mengubah PDF ke BMP 
linktitle: Mengubah PDF ke BMP
type: docs
weight: 40
url: /androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: Artikel ini menjelaskan cara mengubah Halaman PDF ke gambar BMP, mengubah semua Halaman ke gambar BMP dan mengubah satu halaman PDF ke gambar BMP dengan Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Kelas [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) memungkinkan Anda untuk mengubah halaman PDF menjadi gambar <abbr title="Bitmap Image File">BMP</abbr>. Kelas ini menyediakan metode bernama [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) yang memungkinkan Anda untuk mengubah halaman tertentu dari file PDF ke format gambar BMP.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

Kelas BmpDevice memungkinkan Anda untuk mengubah halaman PDF menjadi gambar BMP.
 Kelas ini menyediakan metode bernama process(..) yang memungkinkan Anda untuk mengubah halaman tertentu dari file PDF menjadi gambar BMP.

## Mengonversi Halaman PDF ke Gambar BMP

Untuk mengonversi halaman PDF ke gambar BMP:

1. Buat objek dari kelas Document, untuk mendapatkan halaman tertentu yang ingin Anda konversi.
2. Panggil metode process(..) untuk mengonversi halaman ke BMP.

Cuplikan kode berikut menunjukkan kepada Anda cara mengonversi halaman tertentu ke gambar BMP.

```java
//Mengonversi PDF ke BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Buat objek stream untuk menyimpan gambar keluaran
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Buat objek Resolution
            Resolution resolution = new Resolution(300);

            // Buat objek BmpDevice dengan resolusi tertentu
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Konversi halaman tertentu dan simpan gambar ke stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Tutup stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Mengubah Semua Halaman PDF ke Gambar BMP

Untuk mengubah semua halaman file PDF ke format BMP, Anda perlu mengiterasi untuk mendapatkan setiap halaman individu dan mengonversinya ke format BMP. Cuplikan kode berikut menunjukkan kepada Anda cara menelusuri semua halaman file PDF dan mengonversinya ke BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop melalui semua halaman file PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Buat objek stream untuk menyimpan gambar keluaran
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Buat objek Resolution
            Resolution resolution = new Resolution(300);
            // Buat objek BmpDevice dengan resolusi tertentu
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Konversi halaman tertentu dan simpan gambar ke stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Tutup stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Konversi wilayah halaman tertentu ke Gambar (DOM)

Kita dapat mengonversi dokumen PDF ke berbagai format Gambar menggunakan objek perangkat gambar dari Aspose.PDF. Namun, terkadang ada kebutuhan untuk mengonversi wilayah halaman tertentu ke format Gambar. Kita dapat memenuhi kebutuhan ini dalam dua langkah. Pertama, potong halaman PDF ke wilayah yang diinginkan dan kemudian konversi ke gambar menggunakan objek perangkat Gambar yang diinginkan.

Cuplikan kode berikut menunjukkan kepada Anda cara mengonversi halaman PDF ke gambar.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Dapatkan persegi panjang dari wilayah halaman tertentu
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // setel nilai CropBox sesuai dengan persegi panjang wilayah halaman yang diinginkan
        document.getPages().get_Item(1).setCropBox(pageRect);
        // simpan dokumen yang telah dipotong ke stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // buka dokumen PDF yang telah dipotong dari stream dan konversi ke gambar
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Buat objek Resolusi
        Resolution resolution = new Resolution(300);
        // Buat perangkat BMP dengan atribut yang ditentukan
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Konversi halaman tertentu dan simpan gambar ke stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```