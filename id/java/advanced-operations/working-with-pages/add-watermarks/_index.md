---
title: Tambahkan watermark ke PDF
linktitle: Tambahkan watermark
type: docs
weight: 90
url: /id/java/add-watermarks/
description: Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan watermark dalam PDF secara pemrograman menggunakan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** memungkinkan menambahkan watermark ke dokumen PDF Anda menggunakan Artefak. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Watermark yang dibuat dengan Adobe Acrobat disebut sebagai artefak (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artefak dari spesifikasi PDF). Untuk bekerja dengan artefak, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Untuk mendapatkan semua artefak pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) memiliki properti Artefak.
 ## Bekerja dengan Artefak

Kelas [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) berisi properti-properti berikut:

**Artifact.Type** – mendapatkan jenis artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilainya termasuk Latar Belakang, Tata Letak, Halaman, Paginasi, dan Tidak Ditetapkan).
**Artifact.Subtype** – mendapatkan subtipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilainya termasuk Latar Belakang, Footer, Header, Tidak Ditetapkan, Watermark).

{{% alert color="primary" %}}

Harap dicatat bahwa watermark yang dibuat dengan Adobe Acrobat memiliki tipe Paginasi dan subtipe Watermark.

{{% /alert %}}

**Artifact.Contents** – Mendapatkan koleksi operator internal artefak. Jenis yang didukung adalah System.Collections.ICollection.
**Artifact.Form** – Mendapatkan XForm dari artefak (jika XForm digunakan). Artefak watermark, header, dan footer mengandung XForm yang menunjukkan semua isi artefak.

**Artifact.Image** – Mendapatkan gambar dari artefak (jika gambar ada, jika tidak maka null).**Artifact.Text** – Mendapatkan teks dari sebuah artefak.  
**Artifact.Rectangle** – Mendapatkan posisi sebuah artefak pada halaman.  
**Artifact.Rotation** – Mendapatkan rotasi sebuah artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).  
**Artifact.Opacity** – Mendapatkan opasitas sebuah artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 sepenuhnya buram.  

## Contoh Pemrograman: Mendapatkan Watermark

Cuplikan kode berikut menunjukkan cara mendapatkan setiap watermark pada halaman pertama dari file PDF dengan Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // Buka dokumen
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```