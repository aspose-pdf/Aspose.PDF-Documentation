---
title: Flatten Annotation dari PDF ke XFDF
type: docs
weight: 40
url: /net/flatten-annotation/
description: Bagian ini menjelaskan cara mengekspor anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Proses perataan berarti ketika sebuah anotasi dihapus dari dokumen, representasi visualnya tetap utuh. Sebuah anotasi yang diratakan masih terlihat tetapi tidak lagi dapat diedit oleh pengguna Anda atau oleh aplikasi Anda. Ini dapat digunakan, misalnya, untuk menerapkan anotasi secara permanen ke dokumen Anda atau untuk membuat anotasi terlihat oleh pemirsa yang sebaliknya tidak dapat menampilkan anotasi. Jika tidak ditentukan, ekspor akan mempertahankan semua anotasi seperti apa adanya.

Ketika opsi ini dipilih, anotasi Anda akan disertakan dalam PDF yang diekspor sebagai anotasi standar PDF.

Periksa bagaimana metode [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) digunakan dalam potongan kode berikut.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```