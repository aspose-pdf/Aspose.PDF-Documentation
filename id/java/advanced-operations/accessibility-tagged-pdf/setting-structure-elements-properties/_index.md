---
title: Atur Properti Elemen Struktur Tagged PDF di Java
linktitle: Mengatur Properti Elemen Struktur
type: docs
weight: 30
url: /id/java/setting-structure-elements-properties/
description: Pelajari cara mengatur properti elemen struktur PDF ber-tag dalam Java dengan Aspose.PDF, termasuk judul, bahasa, teks aktual, teks alternatif, teks ekspansi, tautan, catatan, dan nama tag.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Halaman ini mencakup pola pengaturan properti umum untuk elemen struktur PDF ber-tag dalam Java.

## Atur properti elemen struktur umum

Gunakan contoh ini ketika elemen struktur yang ditandai harus menampilkan metadata aksesibilitas seperti judul, bahasa, teks aktual, dan teks alternatif.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan inisialisasi metadata konten yang ditandai.
1. Buat elemen seksi dan header dalam pohon struktur.
1. Atur properti header dan simpan dokumen.

```java
public static void setProperties(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        StructureElement rootElement = taggedContent.getRootElement();
        SectElement sectionElement = taggedContent.createSectElement();
        rootElement.appendChild(sectionElement, true);

        HeaderElement headerElement = taggedContent.createHeaderElement(1);
        sectionElement.appendChild(headerElement, true);
        headerElement.setText("The Header");

        headerElement.setTitle("Title");
        headerElement.setLanguage("en-US");
        headerElement.setAlternativeText("Alternative Text");
        headerElement.setExpansionText("Expansion Text");
        headerElement.setActualText("Actual Text");

        document.save(outputFile.toString());
    }
}
```

## Setel elemen teks

Gunakan contoh ini ketika Anda perlu menambahkan elemen paragraf sederhana ke pohon struktur bertanda.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) dan atur teksnya.
1. Tambahkan paragraf ke elemen root dan simpan dokumen.

```java
public static void setTextElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Paragraph.");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        document.save(outputFile.toString());
    }
}
```

## Atur elemen blok teks

Contoh ini membuat beberapa elemen struktur tingkat blok, termasuk judul dengan beberapa tingkat dan sebuah paragraf.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan elemen header untuk level yang diperlukan dan kemudian buat elemen paragraf.
1. Tambahkan elemen blok ke struktur root dan simpan dokumen.

```java
public static void setTextBlockElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            header.setText("H" + level + ". Header of Level " + level);
            taggedContent.getRootElement().appendChild(header, true);
        }

        ParagraphElement p = taggedContent.createParagraphElement();
        p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet.");
        taggedContent.getRootElement().appendChild(p, true);

        document.save(outputFile.toString());
    }
}
```

## Atur elemen inline

Gunakan contoh ini ketika elemen struktur blok harus berisi span inline bersarang.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Bangun elemen header dan tambahkan anak span ke dalamnya.
1. Buat paragraf dengan beberapa span dan simpan dokumen.

```java
public static void setInlineElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            taggedContent.getRootElement().appendChild(header, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("H" + level + ". ");
            header.appendChild(span1, true);

            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText("Level " + level + " Header");
            header.appendChild(span2, true);
        }

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("P. ");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        for (int index = 1; index <= 10; index++) {
            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + index + ". ");
            paragraphElement.appendChild(span, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Atur nama tag khusus

Contoh ini menetapkan nama tag khusus pada elemen paragraf dan span dalam struktur bertanda.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan elemen section.
1. Buat paragraf dan span, lalu tetapkan nama tag khusus untuk setiap elemen.
1. Tambahkan elemen ke bagian dan simpan dokumen.

```java
public static void setTagName(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        SectElement sectionElement = taggedContent.createSectElement();
        taggedContent.getRootElement().appendChild(sectionElement, true);

        String[] paragraphTags = {"P1", "Para", "Para", "Paragraph"};
        String[] spanTags = {"SPAN", "Sp", "Sp", "TheSpan"};

        for (int index = 0; index < 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            paragraph.setText("P" + (index + 1) + ". ");
            paragraph.setTag(paragraphTags[index]);

            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + (index + 1) + ".");
            span.setTag(spanTags[index]);

            paragraph.appendChild(span, true);
            sectionElement.appendChild(paragraph, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Atur elemen tautan dan gambar

Gunakan contoh ini ketika elemen tautan yang ditandai harus mencakup deskripsi alternatif, hyperlink, dan konten gambar dengan atribut tata letak.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan elemen tautan di dalam paragraf.
1. Konfigurasikan target hyperlink, deskripsi alternatif, dan elemen figure yang ditautkan.
1. Atur atribut layout yang diperlukan dan simpan dokumen.

```java
public static void setElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Link Elements Example");
        taggedContent.setLanguage("en-US");

        for (int index = 1; index <= 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            LinkElement link = taggedContent.createLinkElement();
            paragraph.appendChild(link, true);
            link.setHyperlink(new WebHyperlink("http://google.com"));
            link.setText(index == 4 ? "The multiline link: Google Google Google Google" : "Google");
            link.setAlternateDescriptions("Link to Google");
        }

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        LinkElement link = taggedContent.createLinkElement();
        paragraph.appendChild(link, true);
        link.setHyperlink(new WebHyperlink("http://google.com"));

        FigureElement figure = taggedContent.createFigureElement();
        figure.setImage(imageFile.toString(), 1200);
        figure.setAlternativeText("Google icon");

        StructureAttributes linkLayoutAttributes = link.getAttributes().getAttributes(AttributeOwnerStandard.Layout);
        StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
        placementAttribute.setNameValue(AttributeName.Placement_Block);
        linkLayoutAttributes.setAttribute(placementAttribute);

        link.appendChild(figure, true);
        link.setAlternateDescriptions("Link to Google");

        document.save(outputFile.toString());
    }
}
```

## Tambahkan paragraf dengan konten tautan sebaris

Contoh ini membuat elemen paragraf yang menggabungkan teks biasa dan elemen span bersarang.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat elemen paragraf dan tambahkan anak span dengan teks khusus.
1. Tambahkan paragraf ke elemen akar dan simpan dokumen.

```java
public static void addLinkElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Text Elements Example");
        taggedContent.setLanguage("en-US");

        for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("Span_" + paragraphIndex + "1");
            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText(" and Span_" + paragraphIndex + "2.");

            paragraph.setText("Paragraph with ");
            paragraph.appendChild(span1, true);
            paragraph.appendChild(span2, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Atur elemen catatan

Gunakan contoh ini ketika elemen struktur catatan harus dibuat dengan ID otomatis atau eksplisit.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan elemen paragraf.
1. Buat elemen catatan dan atur teks serta ID-nya sesuai kebutuhan.
1. Tambahkan catatan ke paragraf dan simpan dokumen.

```java
public static void setNoteElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Sample of Note Elements");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        NoteElement note1 = taggedContent.createNoteElement();
        paragraph.appendChild(note1, true);
        note1.setText("Note with auto generate ID. ");

        NoteElement note2 = taggedContent.createNoteElement();
        paragraph.appendChild(note2, true);
        note2.setText("Note with ID = 'note_002'. ");
        note2.setId("note_002");

        NoteElement note3 = taggedContent.createNoteElement();
        paragraph.appendChild(note3, true);
        note3.setText("Note with ID = 'note_003'. ");
        note3.setId("note_003");

        document.save(outputFile.toString());
    }
}
```

## Atur bahasa dan judul untuk konten multibahasa

Contoh ini menetapkan metadata tingkat dokumen dan kemudian membuat paragraf dengan nilai bahasa yang berbeda.

1. Buat PDF ber-tag baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan atur judul dokumen dan bahasa.
1. Tambahkan elemen header dan buat paragraf untuk setiap frasa yang dilokalisasi.
1. Simpan dokumen bertanda multibahasa.

```java
public static void setLanguageAndTitle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example Tagged Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header = taggedContent.createHeaderElement(1);
        header.setText("Phrase on different languages");
        taggedContent.getRootElement().appendChild(header, true);

        addParagraph(taggedContent, "Hello, World!", "en-US");
        addParagraph(taggedContent, "Hallo Welt!", "de-DE");
        addParagraph(taggedContent, "Bonjour le monde!", "fr-FR");
        addParagraph(taggedContent, "Hola Mundo!", "es-ES");

        document.save(outputFile.toString());
    }
}
```

## Tambahkan pembantu paragraf untuk konten ber‑tag

Metode pembantu ini membuat sebuah paragraf, menetapkan bahasanya, dan menambahkannya ke struktur root.

1. Buat sebuah [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Atur teks dan bahasa untuk elemen tersebut.
1. Tambahkan paragraf ke elemen akar konten yang ditandai.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
