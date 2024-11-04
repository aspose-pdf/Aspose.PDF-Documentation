---
title: Pemformatan Teks di dalam PDF 
linktitle: Pemformatan Teks di dalam PDF
type: docs
weight: 30
url: /java/pemformatan-teks-di-dalam-pdf/
description: Halaman ini menjelaskan cara memformat teks di dalam file PDF Anda. Ada penambahan garis Indent, penambahan batas teks, penambahan teks bergaris bawah, penambahan batas di sekitar teks yang ditambahkan, perataan teks untuk isi kotak mengambang dan lain-lain.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cara menambahkan Garis Indent ke PDF

Aspose.PDF untuk Java menawarkan properti SubsequentLinesIndent ke dalam kelas [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). Yang dapat digunakan untuk menentukan indent garis dalam skenario pembuatan PDF dengan koleksi TextFragment dan Paragraf.

Silakan gunakan cuplikan kode berikut untuk menggunakan properti tersebut:

```java
public static void AddLineIndentToPDF() {
        // Buat objek dokumen baru
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas.");

        // Inisialisasi TextFormattingOptions untuk fragmen teks dan tentukan
        // nilai SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Baris2");
        page.getParagraphs().add(text);

        text = new TextFragment("Baris3");
        page.getParagraphs().add(text);

        text = new TextFragment("Baris4");
        page.getParagraphs().add(text);

        text = new TextFragment("Baris5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## Cara Menambahkan Garis Tepi Teks

Cuplikan kode berikut menunjukkan, cara menambahkan garis tepi ke teks menggunakan TextBuilder dan mengatur metode DrawTextRectangleBorder dari TextState:

```java
public static void AddTextBorder() {
    // Buat objek dokumen baru
    Document pdfDocument = new Document();
    // Dapatkan halaman tertentu
    Page pdfPage = pdfDocument.getPages().add();
    // Buat fragmen teks
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition(new Position(100, 600));
    // Atur properti teks
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Gunakan setStrokingColor untuk menggambar garis tepi (stroking) di sekitar kotak teks
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Gunakan metode setDrawTextRectangleBorder untuk mengatur nilai menjadi true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Simpan dokumen
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## Cara Menambahkan Teks Bergaris Bawah

Cuplikan kode berikut menunjukkan cara menambahkan teks bergaris bawah saat membuat file PDF baru.

```java
public static void AddUnderlineText(){
    // Buat objek dokumentasi
    Document pdfDocument = new Document();
    // Tambahkan halaman ke dokumen PDF
    Page page = pdfDocument.getPages().add();
    // Buat TextBuilder untuk halaman pertama
    TextBuilder tb = new TextBuilder(page);
    // TextFragment dengan teks contoh
    TextFragment fragment = new TextFragment("Teks dengan dekorasi garis bawah");
    // Atur font untuk TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Atur pemformatan teks sebagai garis bawah
    fragment.getTextState().setUnderline(true);
    // Tentukan posisi di mana TextFragment perlu ditempatkan
    fragment.setPosition (new Position(10, 800));
    // Tambahkan TextFragment ke file PDF
    tb.appendText(fragment);

    // Simpan dokumen PDF yang dihasilkan.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## Cara Menambahkan Border di Sekitar Teks yang Ditambahkan

Anda memiliki kontrol atas tampilan dan nuansa teks yang Anda tambahkan. Contoh di bawah ini menunjukkan cara menambahkan border di sekitar sepotong teks yang telah Anda tambahkan dengan menggambar persegi panjang di sekelilingnya. Cari tahu lebih lanjut tentang kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Simpan dokumen PDF yang dihasilkan.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## Cara Menambahkan NewLine feed

TextFragment tidak mendukung line feed di dalam teks.
 Namun, untuk menambahkan teks dengan pemisah baris, silakan gunakan TextFragment dengan TextParagraph:

- gunakan "\r\n" atau Environment.NewLine dalam TextFragment sebagai pengganti satu “\n”;
- buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris;
- tambahkan TextFragment dengan TextParagraph.AppendLine;
- tambahkan TextParagraph dengan TextBuilder.AppendParagraph.
Silakan gunakan cuplikan kode di bawah ini.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Inisialisasi TextFragment baru dengan teks yang mengandung penanda newline yang diperlukan
    TextFragment textFragment = new TextFragment("Nama Pemohon: " + System.lineSeparator() + " Joe Smoe");

    // Atur properti text fragment jika diperlukan
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Buat objek TextParagraph
    TextParagraph par = new TextParagraph();

    // Tambahkan TextFragment baru ke paragraf
    par.appendLine(textFragment);

    // Atur posisi paragraf
    par.setPosition (new Position(100, 600));

    // Buat objek TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Tambahkan TextParagraph menggunakan TextBuilder
    textBuilder.appendParagraph(par);

    // Simpan dokumen PDF yang dihasilkan.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## Cara Menambahkan Teks Coret

Kelas TextState menyediakan kemampuan untuk mengatur pemformatan untuk TextFragment yang ditempatkan di dalam dokumen PDF. Anda dapat menggunakan kelas ini untuk mengatur pemformatan teks sebagai Bold, Italic, Underline dan mulai rilis ini, API telah menyediakan kemampuan untuk menandai pemformatan teks sebagai Coret. Silakan coba gunakan cuplikan kode berikut untuk menambahkan TextFragment dengan pemformatan Coret.

Silakan gunakan cuplikan kode lengkap:

```java
public static void AddStrikeOutText(){
    // Buka dokumen
    Document pdfDocument = new Document();
    // Dapatkan halaman tertentu
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Buat text fragment
    TextFragment textFragment = new TextFragment("teks utama");
    textFragment.setPosition (new Position(100, 600));

    // Atur properti teks
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // gunakan metode setStrikeOut untuk mengaktifkan Teks Coret
    textFragment.getTextState().setStrikeOut(true);
    // Tandai teks sebagai Bold
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Buat objek TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Tambahkan text fragment ke halaman PDF
    textBuilder.appendText(textFragment);

    // Simpan dokumen PDF yang dihasilkan.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## Terapkan Pewarnaan Gradien pada Teks

Pemformatan teks telah lebih ditingkatkan dalam API untuk skenario penyuntingan teks dan sekarang Anda dapat menambahkan teks dengan pola ruang warna di dalam dokumen PDF. Kelas com.aspose.pdf.Color telah lebih ditingkatkan dengan memperkenalkan metode baru `setPatternColorSpace`, yang dapat digunakan untuk menentukan warna pewarnaan untuk teks. Metode baru ini menambahkan berbagai Pewarnaan Gradien ke teks misalnya, Axial Shading, Radial (Type 3) Shading seperti yang ditunjukkan dalam cuplikan kode berikut:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("selalu mencetak dengan benar");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Buat warna baru dengan pola ruang warna
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


Dalam rangka menerapkan Gradien Radial, Anda dapat menggunakan metode `setPatternColorSpace` sama dengan `GradientRadialShading(startingColor, endingColor)` dalam cuplikan kode di atas.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Buat warna baru dengan ruang warna pola
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## Cara menyelaraskan teks ke konten mengambang

Aspose.PDF mendukung pengaturan perataan teks untuk konten di dalam elemen Kotak Mengambang.
 Properti penyelarasan dari instance Aspose.Pdf.FloatingBox dapat digunakan untuk mencapai hal ini seperti yang ditunjukkan dalam contoh kode berikut.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```