---
title: Menghasilkan Gambar Mini dari Dokumen PDF
linktitle: Menghasilkan Gambar Mini
type: docs
weight: 100
url: /java/generate-thumbnail-images-from-pdf-documents/
description: Bagian ini menjelaskan cara menghasilkan gambar mini dari dokumen PDF menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
---

## Pendekatan Aspose.PDF untuk Java

Aspose.PDF untuk Java menyediakan dukungan yang luas untuk menangani dokumen PDF. Ini juga mendukung kemampuan untuk mengonversi halaman dokumen PDF ke berbagai format gambar. Fungsionalitas yang dijelaskan di atas dapat dengan mudah dicapai menggunakan Aspose.PDF untuk Java.

Aspose.PDF memiliki manfaat yang berbeda:

- Anda tidak perlu menginstal Adobe Acrobat di sistem Anda untuk bekerja dengan file PDF.
- Menggunakan Aspose.PDF untuk Java adalah sederhana dan mudah dipahami dibandingkan dengan Otomatisasi Acrobat.

Jika kita perlu mengonversi halaman PDF menjadi JPEG, namespace [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) menyediakan kelas bernama [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) untuk merender halaman PDF menjadi gambar JPEG.
 Silakan lihat cuplikan kode berikut.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // Ambil nama semua file PDF di direktori tertentu
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Kesalahan saat membaca direktori
        }

        // Iterasi melalui semua entri file dalam array
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Buka dokumen
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Buat objek Resolusi
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Konversi halaman tertentu dan simpan gambar ke stream
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Tutup stream
                imageStream.close();
            }
        }

    }
}
```