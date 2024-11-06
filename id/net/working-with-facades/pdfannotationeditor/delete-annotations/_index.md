---
title: Hapus Anotasi (fasad)
type: docs
weight: 10
url: id/net/delete-annotations/
description: Bagian ini menjelaskan cara menghapus anotasi dengan Aspose.PDF Facades menggunakan Kelas PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hapus Semua Anotasi dari File PDF yang Ada

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) memungkinkan Anda menghapus semua anotasi dari file PDF yang ada. First off, create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method to delete all the annotations from the file, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.

```csharp
   public static void DeleteAllAnnotations()
        {
            // Buka dokumen
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // Hapus semua anotasi
            annotationEditor.DeleteAnnotations();
            // Simpan PDF yang diperbarui
        }   
    
```
## Delete All Annotations by Specified Type

Anda dapat menggunakan kelas [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) untuk menghapus semua anotasi, berdasarkan jenis anotasi yang ditentukan, dari file PDF yang ada. Untuk melakukan itu, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations), dengan parameter string, untuk menghapus semua anotasi dari file; parameter string mewakili jenis anotasi yang akan dihapus. Terakhir, gunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan cara menghapus semua anotasi berdasarkan jenis anotasi tertentu.

```csharp
    public static void DeleteAnnotation()
        {
            // Buka dokumen
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("Silakan masukkan nomor:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Simpan PDF yang telah diperbarui
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```