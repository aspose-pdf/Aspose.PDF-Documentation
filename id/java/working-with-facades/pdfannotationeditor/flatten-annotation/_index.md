---
title: Flatten Annotation dari File PDF ke XFDF (facades)
type: docs
weight: 40
url: /id/java/flatten-annotation/
description: Bagian ini menjelaskan cara mengekspor anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Proses flattening berarti ketika anotasi dihapus dari dokumen, representasi visualnya tetap utuh. Anotasi yang telah diflatten masih terlihat tetapi tidak lagi dapat diedit oleh pengguna Anda atau oleh aplikasi Anda. Ini dapat digunakan, misalnya, untuk menerapkan anotasi secara permanen ke dokumen Anda atau untuk membuat anotasi terlihat oleh penonton yang sebaliknya tidak dapat menampilkan anotasi. Jika tidak ditentukan, ekspor akan menjaga semua anotasi seperti semula.

Ketika opsi ini dipilih, anotasi Anda akan disertakan dalam PDF yang diekspor sebagai anotasi standar PDF.

Periksa bagaimana metode [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) digunakan dalam cuplikan kode berikut.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfEditorKomentarPdf();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new PengaturanPerataan();
        flattenSettings.setApplyRedactions(true); // Menerapkan penyuntingan
        flattenSettings.setCallEvents(false); // Menonaktifkan acara panggilan
        flattenSettings.setHideButtons(true); // Menyembunyikan tombol
        flattenSettings.setUpdateAppearances(true); // Memperbarui tampilan
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf"); // Menyimpan file PDF
    }
```