---
title: Simpan Dokumen PDF
linktitle: Simpan
type: docs
weight: 30
url: id/java/save-pdf-document/
description: Pelajari cara menyimpan file PDF dengan pustaka Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Simpan dokumen PDF ke sistem file

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem file menggunakan metode Save dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Ketika Anda tidak memberikan jenis format (opsi), maka dokumen disimpan dalam format Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## Simpan dokumen PDF ke stream

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke stream dengan menggunakan overload dari metode Save.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Simpan dokumen PDF dalam aplikasi Web

Untuk menyimpan dokumen dalam aplikasi Web, Anda dapat menggunakan cara yang diusulkan di atas. Selain itu, kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memiliki metode Save yang overload.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // dapatkan file Anda sebagai InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // salin ke OutputStream respons
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Error writing file to output stream. Filename was '{}'", fileName, ex);
    //         throw new RuntimeException("IOError writing file to output stream");
    //     }
    // }
```


Untuk penjelasan lebih rinci, silakan ikuti ke bagian [Showcase]().

## Simpan format PDF/A atau PDF/X

PDF/A adalah versi ISO-standar dari Portable Document Format (PDF) untuk digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik. PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti penghubungan font (sebagai lawan dari penyematan font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font yang disematkan, dan antarmuka pengguna untuk membaca anotasi yang disematkan.

PDF/X adalah subset dari standar ISO PDF. Tujuan dari PDF/X adalah untuk memfasilitasi pertukaran grafik, dan oleh karena itu memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku untuk file PDF standar.

Dalam kedua kasus, metode Save digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan metode Convert.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```