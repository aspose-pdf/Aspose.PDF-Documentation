---
title: Mengonversi DICOM ke PDF 
linktitle: Mengonversi DICOM ke PDF
type: docs
weight: 250
url: /id/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Mengonversi gambar medis yang disimpan dalam format DICOM ke file PDF menggunakan Aspose.PDF untuk Android melalui Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar untuk menangani, menyimpan, mencetak, dan mentransmisikan informasi dalam pencitraan medis. Standar ini mencakup definisi format file dan protokol komunikasi jaringan.

Aspose.PDF untuk Java memungkinkan Anda untuk mengonversi file DICOM ke format PDF, lihat cuplikan kode berikut:

1. Muat gambar ke dalam stream
1. Inisialisasi [`Dokumen objek`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Muat file gambar DICOM contoh
1. Simpan dokumen PDF keluaran

```java
//    Mengonversi DICOM ke PDF
    public void convertDICOMtoPDF () {
        // Inisialisasi objek dokumen
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

        // Muat file gambar BMP contoh
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Simpan dokumen keluaran
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```