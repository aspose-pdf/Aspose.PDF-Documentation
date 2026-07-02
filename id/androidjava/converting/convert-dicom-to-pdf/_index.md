---
title: Konversi DICOM ke PDF
linktitle: Konversi DICOM ke PDF
type: docs
weight: 250
url: /id/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Konversi gambar medis yang disimpan dalam format DICOM ke file PDF menggunakan Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar untuk menangani, menyimpan, mencetak, dan mengirimkan informasi dalam pencitraan medis. Ini mencakup definisi format file dan protokol komunikasi jaringan.

Aspsoe.PDF untuk Java memungkinkan Anda mengonversi file DICOM ke format PDF, lihat cuplikan kode berikut:

1. Muat gambar ke dalam stream
1. Inisialisasi [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Muat file gambar DICOM contoh
1. Simpan dokumen PDF keluaran

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

