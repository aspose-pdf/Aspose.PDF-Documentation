---
title: Mengganti Teks dalam File PDF
type: docs
weight: 40
url: /id/java/replace-text/
description: Bagian ini menjelaskan cara mengganti teks dengan Aspose.PDF Facades - seperangkat alat untuk operasi populer dengan PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mengganti Teks dalam File PDF yang Ada (facades)

Untuk mengganti teks dalam file PDF yang ada, Anda perlu membuat objek dari kelas [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), dan mengikat file PDF input menggunakan metode bindPdf. Setelah itu, Anda perlu memanggil metode [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-).
Anda perlu menyimpan file PDF yang diperbarui menggunakan metode save dari kelas [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Cuplikan kode berikut menunjukkan cara mengganti teks dalam file PDF yang ada.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.TextState;
import com.aspose.pdf.facades.PdfContentEditor;
import com.aspose.pdf.facades.ReplaceTextStrategy;

public class PdfContentEditorText {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ReplaceText01(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label");

        // simpan file keluaran
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


Periksa bagaimana tampilannya dalam dokumen asli:

![Ganti Teks](replace_text1.png)

Dan periksa hasil setelah mengganti teks:

![Hasil Mengganti Teks](replace_text2.png)

Dalam contoh kedua, Anda akan melihat bagaimana, selain mengganti teks, Anda juga dapat memperbesar atau memperkecil ukuran font:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // simpan file output
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

Untuk kemungkinan yang lebih canggih dalam bekerja dengan teks kami, kami akan menggunakan metode [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). Dengan metode ini, kita dapat membuat teks menjadi tebal, miring, berwarna, dan sebagainya.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // simpan file output
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


Jika Anda perlu mengganti semua teks yang ditentukan dalam dokumen, gunakan cuplikan kode berikut. Artinya, penggantian teks akan terjadi di mana pun teks yang ditentukan untuk penggantian akan ditemukan, dan juga akan menghitung jumlah penggantian tersebut.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" kejadian telah diganti.");

        // simpan file output
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Ganti semua Teks](replace_text3.png)

Cuplikan kode berikut menunjukkan cara melakukan semua penggantian teks tetapi pada halaman tertentu dari dokumen Anda.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" kejadian telah diganti.");

        // simpan file output
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


Dalam cuplikan kode berikut, kami akan menunjukkan cara mengganti, misalnya, angka tertentu dengan huruf yang kami butuhkan.

```java
    public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor();
        ReplaceTextStrategy replaceTextStrategy = new ReplaceTextStrategy();
        replaceTextStrategy.setRegularExpressionUsed(true);
        replaceTextStrategy.setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.setReplaceTextStrategy(replaceTextStrategy);
        
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.replaceText("\\d{4}", "ABCDE");

        // simpan file keluaran
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```