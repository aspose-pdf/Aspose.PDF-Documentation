---
title: Dapatkan informasi file PDF - fasad
type: docs
weight: 10
url: /id/java/get-pdf-information/
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF dengan Aspose.PDF Facades menggunakan Kelas PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Untuk mendapatkan informasi khusus untuk file PDF, Anda perlu membuat objek dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Setelah itu, Anda dapat mendapatkan nilai dari properti individu seperti Subjek, Judul, Kata Kunci, dan Pembuat, dll.

Cuplikan kode berikut menunjukkan cara mendapatkan informasi file PDF.

```java
public static void GetPdfInfo()
    {
        // Buka dokumen
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Dapatkan informasi PDF
        System.out.println("Subjek: " + fileInfo.getSubject());
        System.out.println("Judul: " + fileInfo.getTitle());
        System.out.println("Kata Kunci: " + fileInfo.getKeywords());
        System.out.println("Pembuat: " + fileInfo.getCreator());
        System.out.println("Tanggal Pembuatan: " + fileInfo.getCreationDate());
        System.out.println("Tanggal Modifikasi: " + fileInfo.getModDate());
        // Menemukan apakah ini PDF yang valid dan juga terenkripsi
        System.out.println("Apakah PDF Valid: " + fileInfo.isPdfFile());
        System.out.println("Apakah Terenkripsi: " + fileInfo.isEncrypted());

        System.out.println("Lebar halaman:" +fileInfo.getPageWidth(1));
    }
```


## Dapatkan Info Meta

Untuk mendapatkan informasi, kita menggunakan metode [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). Dengan 'Hashtable' kita mendapatkan semua nilai yang mungkin.

```java
public static void GetMetaInfo()
    {        
        // Buat instance dari objek PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Ambil semua atribut kustom yang ada
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // dapatkan kunci
            String key = enumerator.nextElement();  
            // cetak kunci dan nilai yang sesuai dengan kunci tersebut
            System.out.println(key + ": " + hTable.get(key));
        }

        // Ambil satu atribut kustom
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```