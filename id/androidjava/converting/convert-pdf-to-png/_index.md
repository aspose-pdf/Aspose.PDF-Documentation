---
title: Konversi PDF ke PNG
linktitle: Konversi PDF ke PNG
type: docs
weight: 20
url: /id/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: Halaman ini menjelaskan cara mengonversi Halaman PDF ke gambar PNG, mengonversi semua dan halaman tunggal ke gambar PNG dengan Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gunakan perpustakaan **Aspose.PDF for Android via Java** untuk mengonversi Halaman PDF menjadi <abbr title="Portable Network Graphics">PNG</abbr> Gambar dengan cara yang dapat diakses dan nyaman.

Kelas PngDevice memungkinkan Anda mengonversi halaman PDF menjadi gambar PNG. Kelas ini menyediakan metode bernama Process yang memungkinkan Anda mengonversi halaman tertentu dari file PDF ke format gambar PNG.

## Konversi Halaman PDF ke Gambar PNG

Untuk mengonversi semua halaman dalam file PDF menjadi file PNG, iterasikan melalui setiap halaman dan konversi masing-masing ke format PNG. Potongan kode berikut menunjukkan cara menelusuri semua halaman dalam file PDF dan mengonversi masing-masing menjadi gambar PNG.

{{% alert color="primary" %}} 

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Konversi satu halaman PDF menjadi gambar PNG

Berikan indeks halaman sebagai argumen ke metode Process(..).
Potongan kode berikut menunjukkan langkah-langkah untuk mengonversi halaman pertama PDF ke format PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Konversi semua halaman PDF ke gambar PNG

Aspose.PDF for Android via Java menunjukkan cara mengonversi semua halaman dalam file PDF menjadi gambar:

1. Lakukan perulangan pada semua halaman dalam file.
1. Konversi tiap halaman secara terpisah:
    1. Buat objek dari kelas Document untuk memuat dokumen PDF.
    1. Dapatkan halaman yang ingin Anda konversi.
    1. Panggil metode Process untuk mengonversi halaman menjadi PNG.

Potongan kode berikut menunjukkan cara mengonversi semua halaman PDF ke gambar PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
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

## Konversi halaman PDF tertentu ke gambar PNG

Aspose.PDF for Android via Java menunjukkan cara mengonversi halaman tertentu ke format PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
