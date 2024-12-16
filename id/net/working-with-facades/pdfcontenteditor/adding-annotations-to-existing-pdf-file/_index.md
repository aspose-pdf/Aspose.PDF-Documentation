---
title: Menambahkan Anotasi ke file PDF yang ada
type: docs
weight: 80
url: /id/net/adding-annotations-to-existing-pdf-file/
description: Bagian ini menjelaskan bagaimana menambahkan Anotasi ke file PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menambahkan Anotasi Teks Bebas dalam File PDF yang Ada (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk menambahkan anotasi dari berbagai jenis dalam file PDF yang ada. Anda dapat menggunakan metode yang sesuai untuk menambahkan anotasi tertentu. Misalnya, dalam cuplikan kode berikut, kami telah menggunakan metode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) untuk menambahkan anotasi tipe [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Setiap jenis anotasi dapat ditambahkan ke file PDF dengan cara yang sama. First of all, you need to create an object of type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kedua, Anda harus membuat objek Rectangle untuk menentukan area anotasi.

Setelah itu, Anda dapat memanggil metode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) untuk menambahkan anotasi [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), dan kemudian menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) untuk menyimpan file PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan anotasi teks bebas dalam file PDF.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## Menambahkan Anotasi Teks dalam Berkas PDF yang Ada (facades)

Dalam contoh ini juga, Anda perlu membuat objek dari tipe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat berkas PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kedua, Anda harus membuat objek Rectangle untuk menentukan area anotasi. Setelah itu, Anda dapat memanggil metode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) untuk menambahkan anotasi FreeText, membuat judul anotasi Anda, dan nomor halaman di mana anotasi tersebut berada.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF adalah format yang lebih baik untuk dokumen modern", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## Menambahkan Anotasi Garis dalam File PDF yang Ada (fasad)

Kami juga menentukan Persegi Panjang, koordinat awal dan akhir garis, nomor halaman, ketebalan, gaya dan warna bingkai anotasi, jenis garis putus-putus, jenis awal dan akhir garis.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Buat Anotasi Garis
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```