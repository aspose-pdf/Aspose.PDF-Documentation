---
title: Mengonversi PDF ke Microsoft PowerPoint 
linktitle: Mengonversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF memungkinkan Anda mengonversi PDF ke format PowerPoint menggunakan Java. Salah satu caranya adalah dengan mengonversi PDF ke PPTX dengan Slide sebagai Gambar.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF untuk Java** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX. Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Dalam Aspose.PDF untuk Java, kami telah memperkenalkan fitur untuk mengubah dokumen PDF menjadi format PPTX. Selama konversi ini, setiap halaman dari file PDF diubah menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke PPTX, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya, daripada dirender sebagai gambar.
 Silakan dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama PptxSaveOptions. Sebuah objek dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) diberikan sebagai argumen kedua ke metode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Periksa cuplikan kode berikut untuk menyelesaikan tugas Anda dengan konversi PDF ke format PowerPoint:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Muat dokumen PDF
        Document document = new Document(documentFileName);

        // Instansiasi PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Simpan keluaran dalam format PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## Mengonversi PDF ke PPTX dengan Slide sebagai Gambar

Jika Anda perlu mengonversi PDF yang dapat dicari ke PPTX sebagai gambar alih-alih teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Untuk mencapai ini, atur properti SlidesAsImages dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) ke 'true' seperti yang ditunjukkan dalam contoh kode berikut.

Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF ke format PPTX Slide sebagai Gambar.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // Memuat dokumen PDF
    Document document = new Document(documentFileName);
    // Membuat instance PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // Menyimpan output dalam format PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Tampilkan Kemajuan di Konsol dengan Aspose.PDF untuk Java terlihat seperti ini:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Konversi PDF ke PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Muat dokumen PDF
        Document document = new Document(documentFileName);

        // Instansiasi objek PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Tentukan Pengelola Kemajuan Khusus
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // Simpan keluaran dalam format PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## Detail Kemajuan Konversi PPTX

Aspose.PDF untuk Java memungkinkan Anda melacak kemajuan konversi PDF ke PPTX. Kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) menyediakan properti [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) yang dapat ditetapkan ke metode kustom untuk melacak kemajuan konversi seperti yang ditunjukkan dalam contoh kode berikut.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - Kemajuan konversi : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - Halaman hasil %s dari %d tata letak dibuat.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - Halaman hasil %d dari %d diekspor.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - Halaman sumber %d dari %d dianalisis.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**Cobalah mengonversi PDF ke PowerPoint secara online**

Aspose.PDF untuk Java mempersembahkan aplikasi online gratis ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}