---
title: Konversi PDF ke JPG
linktitle: Konversi PDF ke JPG
type: docs
weight: 10
url: /id/androidjava/convert-pdf-to-jpg/
description:  Halaman ini menjelaskan cara mengonversi Halaman PDF ke gambar JPEG, mengonversi semua dan halaman tunggal ke gambar JPEG dengan Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Konversi Halaman PDF ke Gambar JPG

Kelas JpegDevice memungkinkan Anda mengonversi halaman PDF ke gambar JPEG. Kelas ini menyediakan metode bernama process(..) yang memungkinkan Anda mengonversi halaman tertentu dari file PDF ke gambar JPEG.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Konversi satu halaman PDF ke gambar JPG

Aspose.PDF for Android via Java memungkinkan Anda mengonversi satu halaman ke format Jpeg.

Untuk mengonversi hanya satu halaman menjadi gambar JPEG:

1. Buat sebuah objek dari kelas Document untuk mendapatkan halaman yang ingin Anda konversi.
1. Panggil metode process(..) untuk mengonversi halaman menjadi gambar JPEG.

Potongan kode berikut menunjukkan langkah-langkah untuk mengonversi halaman pertama PDF ke format Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Konversi semua halaman PDF ke gambar JPG

Aspose.PDF for Android via Java memungkinkan Anda mengonversi semua halaman dalam file PDF menjadi gambar:

1. Lakukan perulangan pada semua halaman dalam file.
1. Konversi tiap halaman secara terpisah:
    - Buat objek dari kelas Document untuk memuat dokumen PDF.
    - Dapatkan halaman yang ingin Anda konversi.
    - Panggil metode Process untuk mengonversi halaman ke Jpeg.

Potongan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi gambar Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
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
            JpegDevice JpegDevice = new JpegDevice(resolution);

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

## Konversi halaman PDF tertentu ke gambar JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
