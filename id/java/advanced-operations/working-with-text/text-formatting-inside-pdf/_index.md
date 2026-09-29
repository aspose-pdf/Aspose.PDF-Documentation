---
title: Memformat Teks PDF di Java
linktitle: Pemformatan Teks di dalam PDF
type: docs
weight: 70
url: /id/java/text-formatting-inside-pdf/
description: Pelajari cara memformat teks dalam dokumen PDF di Java menggunakan spasi, catatan, daftar, tata letak multi‑kolom, dan opsi penataan.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format dan gaya teks di dalam file PDF dengan Java
Abstract: Artikel ini menjelaskan cara memformat teks dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup jarak baris, jarak karakter, daftar bullet dan bernomor, catatan kaki dan catatan akhir, konten paragraf sebaris, tata letak multi‑kolom, pemecahan halaman paksa, dan hentian tab khusus.
---
Aspose.PDF for Java menawarkan kontrol pemformatan teks untuk spasi, daftar, catatan, tata letak inline, dan komposisi multi-kolom.

## Atur jarak baris sederhana

Gunakan contoh ini ketika teks paragraf harus menggunakan nilai spasi baris tetap.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Muat atau siapkan teks sumber dan buat sebuah `TextFragment`.
1. Atur jarak baris, tambahkan fragmen ke halaman, dan simpan dokumen.

```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## Bandingkan mode spasi baris dengan font khusus

Gunakan contoh ini ketika jarak baris harus diuji dengan mode pemformatan yang berbeda untuk font yang sama.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Muat font khusus dan siapkan dua fragmen dengan mode spasi baris yang berbeda.
1. Tambahkan kedua fragmen ke halaman dan simpan PDF.

```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## Atur jarak karakter dengan fragmen teks

Gunakan contoh ini ketika teks yang sama harus ditampilkan dengan nilai spasi karakter yang berbeda.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun fragmen teks dengan metode pembantu untuk beberapa nilai spasi.
1. Tambahkan fragmen ke halaman dan simpan dokumen.

```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## Atur jarak karakter di dalam paragraf teks

Gunakan contoh ini ketika jarak karakter harus diterapkan di dalam paragraf teks yang terbatas.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat `TextParagraph` dengan persegi panjang target dan opsi pembungkus.
1. Tambahkan fragmen teks bergaya dan simpan PDF-nya.

```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bullet dengan HTML

Gunakan contoh ini ketika pemformatan daftar tidak berurutan harus dihasilkan dari markup HTML.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat string daftar HTML.
1. Tambahkan itu sebagai `HtmlFragment` dan simpan dokumen.

```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bernomor dengan HTML

Gunakan contoh ini ketika format daftar terurut harus diproduksi dari markup HTML.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun string daftar HTML berurutan.
1. Tambahkan itu sebagai `HtmlFragment` dan simpan dokumen.

```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bullet dengan LaTeX

Gunakan contoh ini ketika format daftar tidak berurutan harus di-render dari markup TeX.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan string daftar TeX dengan `itemize` lingkungan.
1. Tambahkan sebagai `TeXFragment` dan simpan PDF.

```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bernomor dengan LaTeX

Gunakan contoh ini ketika format daftar berurutan harus dihasilkan dari penanda TeX.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan string daftar TeX dengan `enumerate` lingkungan.
1. Tambahkan sebagai `TeXFragment` dan simpan PDF.

```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bullet dengan paragraf teks

Gunakan contoh ini ketika daftar bullet manual harus dibangun dari fragmen teks biasa.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun sebuah `TextParagraph` dan tambahkan fragmen yang diawali titik peluru.
1. Tambahkan paragraf ke halaman dan simpan dokumen.

```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## Buat daftar bernomor dengan paragraf teks

Gunakan contoh ini ketika daftar bernomor manual harus dibangun dari fragmen teks biasa.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun sebuah `TextParagraph` dan tambahkan fragmen yang diberi nomor.
1. Tambahkan paragraf ke halaman dan simpan dokumen.

```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan catatan kaki dasar

Gunakan contoh ini ketika fragmen teks harus merujuk ke catatan kaki sederhana.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks utama dan tetapkan a `Note` sebagai catatan kaki.
1. Tambahkan teks lanjutan sebaris apa pun dan simpan dokumen.

```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## Tambahkan catatan kaki dengan gaya teks khusus

Gunakan contoh ini ketika konten catatan kaki harus menggunakan pengaturan font, ukuran, dan warna sendiri.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks utama dan konfigurasikan catatan kaki yang bergaya.
1. Lampirkan catatan dan simpan PDF.

```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan catatan kaki dengan teks penanda khusus

Gunakan contoh ini ketika penanda catatan kaki yang terlihat harus diganti dengan teks khusus.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tetapkan catatan kaki ke fragmen teks utama dan timpa teks penanda-nya.
1. Tambahkan konten yang tersisa dan simpan dokumen.

```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## Sesuaikan garis pemisah catatan kaki

Gunakan contoh ini ketika garis yang memisahkan catatan kaki dari konten halaman harus diberi gaya secara eksplisit.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Konfigurasikan gaya garis catatan halaman melalui `GraphInfo`.
1. Tambahkan fragmen teks dengan catatan kaki dan simpan dokumen.

```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## Tambahkan catatan kaki dengan gambar dan konten tabel

Gunakan contoh ini ketika catatan kaki itu sendiri harus berisi konten kaya seperti gambar, teks, dan tabel.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun sebuah `Note` objek dengan gambar, teks sebaris, dan tabel.
1. Lampirkan ke fragmen teks utama dan simpan dokumen.

```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan catatan akhir

Gunakan contoh ini ketika fragmen teks harus merujuk ke konten catatan akhir alih-alih catatan kaki halaman.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tetapkan catatan akhir pada fragmen teks utama dan tambahkan teks badan pendukung.
1. Simpan dokumen dengan konten catatan akhir yang dihasilkan.

```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## Tambahkan catatan akhir dengan teks penanda khusus

Gunakan contoh ini ketika penanda catatan akhir harus menggunakan label tampilan khusus.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tetapkan catatan akhir ke fragmen teks utama dan timpa teks penanda-nya.
1. Tambahkan teks dokumen yang tersisa dan simpan PDF.

```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## Paksa konten tabel ke halaman baru

Gunakan contoh ini ketika konten yang diformat harus secara eksplisit dimulai pada halaman baru.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun tabel dan isi barisnya.
1. Atur tabel agar mulai pada halaman baru dan simpan dokumen.

```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Campur konten inline dalam satu alur paragraf

Gunakan contoh ini ketika teks dan gambar harus berlanjut dalam alur paragraf yang sama.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan fragmen teks pertama, lalu gambar sebaris, lalu fragmen teks sebaris lainnya.
1. Tambahkan paragraf berdiri sendiri berikutnya dan simpan dokumen.

```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## Buat tata letak teks multi-kolom

Gunakan contoh ini ketika teks bergaya artikel harus mengalir melalui beberapa kolom.

1. Buat dokumen PDF baru dan atur margin halaman.
1. Tambahkan konten heading dan buat multi-kolom `FloatingBox`.
1. Isi dengan teks dan simpan PDF akhir.

```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## Buat teks yang sejajar dengan penghentian tab khusus

Gunakan contoh ini ketika teks harus disejajarkan seperti tabel sederhana dengan menggunakan posisi henti tab.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Konfigurasikan stop tab dengan pengaturan perataan dan pemimpin.
1. Buat fragmen teks yang menggunakan tab stop tersebut dan simpan dokumen.

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
