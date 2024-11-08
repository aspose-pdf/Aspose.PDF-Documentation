---
title: Ekstrak dan Simpan Lampiran
linktitle: Ekstrak dan Simpan Lampiran
type: docs
weight: 20
url: /id/java/extract-and-save-an-attachment/
description: Aspose.PDF untuk Java memungkinkan Anda mendapatkan semua lampiran dari dokumen PDF. Selain itu, Anda dapat mendapatkan lampiran individual dari dokumen Anda.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Lampiran Dari Dokumen PDF

Dengan Aspose.PDF, memungkinkan untuk mendapatkan semua lampiran dari dokumen PDF. Ini berguna baik ketika Anda ingin menyimpan dokumen secara terpisah dari PDF, atau jika Anda perlu menghapus lampiran dari PDF.

Berikut adalah potongan kode yang menunjukkan cara mendapatkan semua lampiran dari dokumen PDF.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Buka dokumen
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Dapatkan file tersemat tertentu
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Dapatkan properti file
  System.out.printf("Nama: - " + fileSpecification.getName());
  System.out.printf("\nDeskripsi: - " + fileSpecification.getDescription());
  System.out.printf("\nTipe Mime: - " + fileSpecification.getMIMEType());
  // Dapatkan lampiran dari file PDF
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Buat jalur untuk file dari pdf
   file.getParentFile().mkdirs();
   // Buat dan ekstrak file dari pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Tutup objek InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Tutup objek Document
  pdfDocument.dispose();
        
    }

```


## Dapatkan Informasi Lampiran

Seperti yang disebutkan dalam [Dapatkan Lampiran dari Dokumen PDF](/pdf/id/java/get-attachments-from-a-pdf-document/), informasi lampiran disimpan dalam objek [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), dikumpulkan bersama lampiran lainnya dalam koleksi EmbeddedFiles pada objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Objek [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) menyediakan metode yang mendapatkan informasi tentang lampiran, misalnya:

- getName() – mendapatkan nama file.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – mendapatkan deskripsi file.
- getMIMEType() – mendapatkan tipe MIME file.
- getParams() – informasi tentang parameter file, misalnya CheckSum, CreationDate, ModDate, dan Size.

Untuk mendapatkan parameter ini, pertama pastikan bahwa metode getParams() tidak mengembalikan null.

Anda dapat melakukan loop melalui semua lampiran dalam koleksi EmbeddedFiles menggunakan for loop, atau mendapatkan lampiran individual dengan menentukan nilai indeksnya.
 The following code snippet shows how to get information about a specific attachment.

```java
    public static void GetAttachmentInformation() {
  // Buka dokumen
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Dapatkan file tertanam tertentu
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Dapatkan properti file
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // Periksa apakah objek parameter berisi parameter
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```