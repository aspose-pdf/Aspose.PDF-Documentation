---
title: Convert PDF to JPG 
linktitle: Convert PDF to JPG
type: docs
weight: 10
url: /id/androidjava/convert-pdf-to-jpg/
description: Halaman ini menjelaskan cara mengonversi halaman PDF ke gambar JPEG, mengonversi semua dan halaman tunggal ke gambar JPEG dengan Aspose.PDF untuk Android melalui Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengonversi Halaman PDF ke Gambar JPG

Kelas JpegDevice memungkinkan Anda untuk mengonversi halaman PDF ke gambar JPEG. Kelas ini menyediakan metode bernama process(..) yang memungkinkan Anda untuk mengonversi halaman tertentu dari file PDF ke gambar JPEG.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Mengonversi halaman PDF tunggal ke gambar JPG

Aspose.PDF untuk Android melalui Java memungkinkan Anda untuk mengonversi satu halaman ke format Jpeg.

Untuk mengonversi hanya satu halaman ke gambar JPEG:

1. Buat objek dari kelas Dokumen untuk mendapatkan halaman yang ingin Anda konversi.
1. Panggil metode process(..) untuk mengkonversi halaman ke gambar JPEG.

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengkonversi halaman pertama PDF ke format Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Buat objek stream untuk menyimpan gambar keluaran
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Buat objek Resolusi
            Resolution resolution = new Resolution(300);

            // Buat objek JpegDevice dengan resolusi tertentu
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Konversi halaman tertentu dan simpan gambar ke stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Tutup stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Ubah semua halaman PDF ke gambar JPG

Aspose.PDF untuk Android melalui Java memungkinkan Anda mengubah semua halaman dalam file PDF menjadi gambar:

1. Loop melalui semua halaman dalam file.
1. Ubah setiap halaman secara individual:
    - Buat objek dari kelas Document untuk memuat dokumen PDF.
    - Dapatkan halaman yang ingin Anda ubah.
    - Panggil metode Process untuk mengubah halaman menjadi Jpeg.

Cuplikan kode berikut menunjukkan cara mengubah semua halaman PDF menjadi gambar Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop melalui semua halaman file PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Buat objek stream untuk menyimpan gambar keluaran
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Buat objek Resolution
            Resolution resolution = new Resolution(300);
            // Buat objek JpegDevice dengan resolusi tertentu
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Ubah halaman tertentu dan simpan gambar ke stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

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


## Mengubah halaman PDF tertentu menjadi gambar JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Dapatkan persegi panjang dari area halaman tertentu
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // setel nilai CropBox sesuai dengan persegi panjang dari area halaman yang diinginkan
        document.getPages().get_Item(1).setCropBox(pageRect);
        // simpan dokumen yang dipotong ke dalam aliran
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // buka dokumen PDF yang dipotong dari aliran dan ubah menjadi gambar
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Buat objek Resolusi
        Resolution resolution = new Resolution(300);
        // Buat perangkat Jpeg dengan atribut yang ditentukan
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Konversi halaman tertentu dan simpan gambar ke aliran
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```