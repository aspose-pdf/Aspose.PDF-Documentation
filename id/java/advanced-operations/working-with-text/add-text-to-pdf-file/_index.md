---
title: "Menambahkan teks ke PDF di Java"
linktitle: "Menambahkan teks ke PDF"
type: docs
weight: 10
url: /id/java/add-text-to-pdf-file/
description: Pelajari cara menambahkan teks, fragmen HTML, daftar, tautan, dan font khusus ke dokumen PDF dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan teks, tautan, HTML, dan font ke file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan dan menata teks dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup penyisipan teks sederhana, tata letak paragraf, hyperlink, teks kanan-ke-kiri, penataan font, transparansi, border, fragmen HTML dan LaTeX, teks gradien, serta font khusus yang dimuat dari file atau aliran.
---
Aspose.PDF for Java mendukung penyisipan teks biasa, tata letak lanjutan, penataan, gradien, HTML, LaTeX, dan font khusus.

## Menambahkan fragmen teks sederhana

Gunakan contoh ini ketika sebuah string teks pendek harus ditempatkan pada koordinat halaman yang tetap.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `TextFragment` dan atur posisinya.
1. Tambahkan ke halaman dan simpan dokumen.

```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## Menambahkan paragraf di dalam persegi panjang

Gunakan contoh ini ketika blok teks yang lebih besar harus mengalir di dalam area yang dibatasi.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Muat teks sumber dan konfigurasikan sebuah `TextParagraph` persegi panjang dan mode pembungkus.
1. Tambahkan fragmen melalui `TextBuilder` dan simpan PDF.

```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## Menambahkan paragraf dengan pengaturan indentasi yang berbeda

Gunakan contoh ini ketika baris pertama dan baris-baris berikutnya harus menggunakan aturan indentasi yang berbeda.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan fragmen teks bersama dan buat beberapa objek `TextParagraph`.
1. Konfigurasikan indentasi untuk setiap paragraf, tambahkan mereka, dan simpan dokumen.

```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## Memasukkan teks dengan pemutusan baris manual

Gunakan contoh ini ketika satu fragmen teks harus berisi baris baru yang eksplisit.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `TextFragment` berisi pemisah baris dan mengonfigurasi gayanya.
1. Tambahkan itu melalui a `TextParagraph` dan simpan PDF.

```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## Memeriksa jeda baris yang terdeteksi

Gunakan contoh ini ketika Anda perlu meninjau output notifikasi yang terkait dengan tata letak teks dan pembungkus baris.

1. Buat dokumen PDF baru dan aktifkan pencatatan notifikasi.
1. Tambahkan beberapa fragmen teks panjang ke halaman.
1. Periksa notifikasi dan simpan dokumen.

```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## Mengukur lebar teks secara dinamis

Gunakan contoh ini ketika lebar karakter dan string harus diukur sebelum keputusan tata letak dibuat.

1. Tentukan font target dan buat sebuah `TextState`.
1. Ukur karakter dan bandingkan hasilnya dari API font dan status teks.
1. Keluarkan setiap ketidaksesuaian untuk validasi.

```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## Menambahkan teks dengan segmen hyperlink

Gunakan contoh ini ketika satu bagian dari fragmen teks harus berperilaku sebagai tautan web.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun sebuah `TextFragment` dengan beberapa objek `TextSegment`.
1. Tetapkan hyperlink dan gaya pada segmen target, lalu simpan dokumen.

```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks kanan-ke-kiri

Gunakan contoh ini ketika dokumen harus menampilkan konten skrip dari kanan ke kiri dengan perataan yang tepat.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `TextFragment` dengan teks RTL target dan mengonfigurasi font serta perataannya.
1. Tambahkan ke halaman dan simpan PDF.

```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks bergaya dan segmen mirip formula

Gunakan contoh ini ketika teks biasa dan segmen seperti subskrip harus menggunakan keadaan teks yang berbeda dalam satu output.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun fragmen bergaya utama dan susun rumus dengan segmen pembantu.
1. Tambahkan kedua fragmen ke halaman dan simpan dokumen.

```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## Menambahkan teks bergaris bawah

Gunakan contoh ini ketika fragmen teks harus secara terlihat menggunakan gaya garis bawah.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks, konfigurasikan font dan keadaan garis bawahnya, dan atur posisinya.
1. Tambahkan dengan `TextBuilder` dan simpan hasilnya.

```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks transparan di atas bentuk berwarna

Gunakan contoh ini ketika teks harus muncul dengan transparansi di atas grafik latar belakang.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Gambar bentuk latar belakang dan buat fragmen teks semi-transparan.
1. Tambahkan kedua elemen ke halaman dan simpan dokumen.

```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks tak terlihat

Gunakan contoh ini ketika teks yang dapat dicari atau tersembunyi harus ada tanpa rendering yang terlihat.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan fragmen teks yang terlihat dan fragmen kedua dengan flag tak terlihat diaktifkan.
1. Simpan dokumen.

```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks dengan batas persegi panjang

Gunakan contoh ini ketika teks harus digambar bersama dengan persegi panjang pembatasnya.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat bergaya `TextFragment` dan aktifkan menggambar batas persegi panjang teks.
1. Tambahkan dengan `TextBuilder` dan simpan PDF.

```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks coret

Gunakan contoh ini ketika teks harus menggunakan format coret.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks bergaya dengan garis coret diaktifkan.
1. Tambahkan ke halaman dan simpan dokumen.

```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## Menerapkan bayangan gradien aksial pada teks

Gunakan contoh ini ketika teks harus menggunakan isian gradien linear alih-alih warna padat.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks dan tetapkan gradien aksial ke warna latar depannya.
1. Tambahkan ke halaman dan simpan PDF.

```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Menerapkan gradasi radial pada teks

Gunakan contoh ini ketika teks harus menggunakan isian gradien radial.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks dan tetapkan gradien radial ke warna latar depan.
1. Tambahkan ke halaman dan simpan dokumen.

```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan teks berformat gaya HTML secara inline

Gunakan contoh ini ketika format superskrip dan subskrip harus dimasukkan melalui markup HTML.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `HtmlFragment` dengan markup inline yang diperlukan.
1. Tambahkan ke halaman dan simpan PDF.

```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan fragmen teks LaTeX

Gunakan contoh ini ketika konten matematika atau yang diformat dengan TeX harus ditampilkan di dalam PDF.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `TeXFragment` dengan ekspresi yang diperlukan.
1. Tambahkan ke halaman dan simpan dokumen.

```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan fragmen HTML kaya

Gunakan contoh ini ketika halaman harus merender konten HTML terstruktur seperti judul, paragraf, dan tautan.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan string konten HTML dan buat sebuah `HtmlFragment`.
1. Tambahkan ke halaman dan simpan PDF.

```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan fragmen HTML dengan status teks yang di-override

Gunakan contoh ini ketika konten HTML yang diimpor harus mewarisi pengaturan font dan warna yang dikontrol.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan konten HTML dan buat `HtmlFragment`.
1. Tetapkan kustom `TextState`, tambahkan fragmen, dan simpan dokumen.

```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## Menggunakan font khusus yang dimuat dari file

Gunakan contoh ini ketika teks harus menggunakan font yang dimuat langsung dari jalur file font.

1. Temukan jalur file font khusus.
1. Buat fragmen teks dan muat font melalui `FontRepository.openFont`.
1. Terapkan pengaturan font dan simpan dokumen.

```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## Menggunakan font khusus yang dimuat dari aliran

Gunakan contoh ini ketika font khusus harus dibuka dari aliran dan disisipkan ke dalam PDF.

1. Buka file font sebagai aliran dan muat dengan `FontRepository`.
1. Buat TextFragment dan tetapkan Font yang tertanam.
1. Tambahkan fragmen ke halaman dan simpan dokumen.

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
