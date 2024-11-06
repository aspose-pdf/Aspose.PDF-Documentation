---
title: Tambahkan watermark ke PDF 
linktitle: Tambahkan watermark
type: docs
weight: 90
url: id/php-java/add-watermarks/
description: Artikel ini menjelaskan fitur-fitur bekerja dengan artefak dan mendapatkan watermark dalam PDF menggunakan PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** memungkinkan penambahan watermark ke dokumen PDF Anda menggunakan Artifacts. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Sebuah watermark yang dibuat dengan Adobe Acrobat disebut sebagai artefak (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artefak dari spesifikasi PDF). Untuk bekerja dengan artefak, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Untuk mendapatkan semua artefak pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) memiliki properti Artifacts.
 ## Bekerja dengan Artifacts

Kelas [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) memiliki properti berikut:

**Artifact.Type** – mendapatkan tipe artifact (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilainya termasuk Background, Layout, Page, Pagination, dan Undefined).
**Artifact.Subtype** – mendapatkan subtype artifact (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilainya termasuk Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Harap dicatat bahwa watermark yang dibuat dengan Adobe Acrobat memiliki tipe Pagination dan subtype Watermark.

{{% /alert %}}

**Artifact.Contents** – Mendapatkan koleksi operator internal artifact. Tipe yang didukung adalah System.Collections.ICollection.
**Artifact.Form** – Mendapatkan XForm dari artifact (jika XForm digunakan). Artifacts watermark, header, dan footer mengandung XForm yang menunjukkan semua isi artifact.

**Artifact.Image** – Mendapatkan gambar dari artifact (jika ada gambar, jika tidak maka null).**Artifact.Text** – Mendapatkan teks dari sebuah artefak.  
**Artifact.Rectangle** – Mendapatkan posisi sebuah artefak pada halaman.  
**Artifact.Rotation** – Mendapatkan rotasi dari sebuah artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).  
**Artifact.Opacity** – Mendapatkan opasitas sebuah artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 sepenuhnya buram.

## Contoh Pemrograman: Mendapatkan Watermark

Cuplikan kode berikut menunjukkan cara mendapatkan setiap watermark pada halaman pertama dari sebuah file PDF dengan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```