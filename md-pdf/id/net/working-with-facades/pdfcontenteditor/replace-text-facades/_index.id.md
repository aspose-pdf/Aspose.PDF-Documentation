---
title: Replace Text - Facades
type: docs
weight: 40
url: /net/replace-text-facades/
description: Bagian ini menjelaskan cara bekerja dengan Teks - Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## Mengganti Teks dalam File PDF yang Ada

Untuk mengganti teks dalam file PDF yang ada, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF masukan menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, Anda perlu memanggil metode [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Anda perlu menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Potongan kode berikut menunjukkan kepada Anda cara mengganti teks dalam file PDF yang ada.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

Periksa bagaimana tampilannya dalam dokumen asli:

![Replace Text](replace_text1.png)

Dan periksa hasil setelah mengganti teks:

![Result of replacing Text](replace_text2.png)

Dalam contoh kedua, Anda akan melihat bagaimana, selain mengganti teks, Anda juga dapat memperbesar atau memperkecil ukuran font:
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

Untuk kemungkinan yang lebih canggih dalam bekerja dengan teks kita, kita akan menggunakan metode [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Dengan metode ini, kita dapat membuat teks menjadi tebal, miring, berwarna, dan sebagainya.

```csharp
    public static void ReplaceText03()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        TextState textState = new TextState
        {
            ForegroundColor = Color.Red,
            FontSize = 12,
        };
        editor.ReplaceText("Value", "Label", textState);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

Jika Anda perlu mengganti semua teks yang ditentukan dalam dokumen, gunakan cuplikan kode berikut. Yaitu, penggantian teks akan terjadi di mana pun teks yang ditentukan untuk penggantian ditemukan, dan juga akan menghitung jumlah penggantian tersebut.

```csharp
public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("Value", "Label")) count++;

        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Ganti semua Teks](replace_text3.png)

Cuplikan kode berikut menunjukkan cara melakukan semua penggantian teks tetapi pada halaman tertentu dari dokumen Anda.

```csharp
public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("9999", 2, "ABCDE")) count++;
        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```
Dalam cuplikan kode berikut, kami akan menunjukkan cara mengganti, misalnya, angka yang diberikan dengan huruf yang kami butuhkan.

```csharp
   public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor
        {
            ReplaceTextStrategy = new ReplaceTextStrategy
            {
                IsRegularExpressionUsed = true,
                ReplaceScope = ReplaceTextStrategy.Scope.ReplaceAll
            }
        };
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");
        // simpan file output
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```