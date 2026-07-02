---
title: Konversi PDF ke BMP
linktitle: Konversi PDF ke BMP
type: docs
weight: 40
url: /id/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: Artikel ini menjelaskan cara mengonversi Halaman PDF ke gambar BMP, mengonversi semua Halaman ke gambar BMP, dan mengonversi satu halaman PDF menjadi gambar BMP dengan Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) kelas memungkinkan Anda mengonversi halaman PDF menjadi <abbr title="Bitmap Image File">BMP</abbr> gambar. Kelas ini menyediakan metode bernama [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) yang memungkinkan Anda mengonversi halaman tertentu dari file PDF ke format gambar Bmp.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

Kelas BmpDevice memungkinkan Anda mengonversi halaman PDF ke gambar BMP. Kelas ini menyediakan metode bernama process(..) yang memungkinkan Anda mengonversi halaman tertentu dari file PDF ke gambar BMP.

## Mengonversi Halaman PDF menjadi Gambar BMP

Untuk mengonversi halaman PDF menjadi gambar BMP:

1. Buat sebuah objek dari kelas Document, untuk mendapatkan halaman tertentu yang ingin Anda konversi.
1. Panggil metode process(..) untuk mengonversi halaman menjadi BMP.

Potongan kode berikut menunjukkan cara mengonversi halaman tertentu ke gambar BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Konversi Semua Halaman PDF ke Gambar BMP

Untuk mengonversi semua halaman file PDF ke format BMP, Anda perlu mengiterasi untuk mendapatkan masing-masing halaman secara individual dan mengonversinya ke format BMP. Potongan kode berikut menunjukkan cara menelusuri semua halaman file PDF dan mengonversinya ke BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## Konversi wilayah halaman tertentu menjadi Gambar (DOM)

Kami dapat mengonversi dokumen PDF ke berbagai format Image menggunakan objek perangkat image dari Aspose.PDF. Namun terkadang ada kebutuhan untuk mengonversi wilayah halaman tertentu ke format Image. Kami dapat memenuhi kebutuhan ini dalam dua langkah. Pertama, memotong halaman PDF ke wilayah yang diinginkan dan kemudian mengonversinya ke gambar menggunakan objek perangkat Image yang diinginkan.

Potongan kode berikut menunjukkan cara mengonversi halaman PDF menjadi gambar.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
