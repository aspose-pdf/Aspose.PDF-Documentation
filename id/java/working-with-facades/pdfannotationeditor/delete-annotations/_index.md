---
title: Hapus Anotasi (fasad)
type: docs
weight: 10
url: /id/java/delete-annotations/
description: Bagian ini menjelaskan cara menghapus anotasi dengan Aspose.PDF Facades menggunakan Kelas PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Anda dapat menggunakan kelas [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) untuk menghapus anotasi, berdasarkan jenis anotasi yang ditentukan, dari file PDF yang ada.
 Untuk melakukan itu, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) dan mengikat file PDF input menggunakan metode bindPdf. Setelah itu, panggil metode [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) dengan parameter string, untuk menghapus semua anotasi dari file; parameter string mewakili jenis anotasi yang akan dihapus. Terakhir, gunakan metode save untuk menyimpan file PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan kepada Anda cara menghapus anotasi berdasarkan jenis anotasi yang ditentukan.

```java
public static void DeleteAnnotation() {
        // Buka dokumen
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Silakan masukkan nomor:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Simpan PDF yang telah diperbarui
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) memungkinkan Anda menghapus semua anotasi dari file PDF yang ada.

Pertama-tama, buat [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) dan ikat file PDF input menggunakan metode BindPdf.

Setelah itu, panggil metode [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) untuk menghapus semua anotasi dari file, dan kemudian gunakan metode Save untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan cara menghapus semua anotasi dari file PDF.

```java
public static void DeleteAllAnnotations() {
    // Buka dokumen
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Hapus semua anotasi
    annotationEditor.deleteAnnotations();
    // Simpan PDF yang diperbarui
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```