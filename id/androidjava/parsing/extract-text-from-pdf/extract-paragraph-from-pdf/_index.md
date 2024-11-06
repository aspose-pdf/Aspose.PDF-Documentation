---
title: Ekstrak Paragraf dari PDF 
linktitle: Ekstrak Paragraf
type: docs
weight: 20
url: id/androidjava/extract-paragraph-from-pdf/
description: Artikel ini menjelaskan cara menggunakan ParagraphAbsorber - alat khusus di Aspose.PDF untuk mengekstrak teks dari dokumen PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks dari dokumen PDF dalam bentuk Paragraf

Kita dapat mengambil teks dari dokumen PDF dengan mencari teks tertentu (menggunakan "teks biasa" atau "ekspresi reguler") dari satu halaman atau seluruh dokumen, atau kita bisa mendapatkan teks lengkap dari satu halaman, rentang halaman, atau seluruh dokumen.
 Namun, dalam beberapa kasus, Anda perlu mengekstrak paragraf dari dokumen PDF atau teks dalam bentuk Paragraf. Kami telah mengimplementasikan fungsionalitas untuk mencari bagian dan paragraf dalam teks halaman dokumen PDF. Kami telah memperkenalkan Kelas ParagraphAbsorber (seperti TextFragmentAbsorber dan TextAbsorber), yang dapat digunakan untuk mengekstrak paragraf dari dokumen PDF. Ada dua cara berikut di mana Anda dapat menggunakan ParagraphAbsorber:

**1- Dengan menggambar batas bagian dan paragraf teks pada halaman PDF:**

```java
public static void ExtractParagraph() {
        // Jalur ke direktori dokumen.
        Document doc = new Document(_dataDir + "input.pdf");
        Page page = doc.getPages().get_Item(2);

        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(page);

        PageMarkup markup = absorber.getPageMarkups().get(0);

        for (MarkupSection section : markup.getSections()) {
            DrawRectangleOnPage(section.getRectangle(), page);
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                DrawPolygonOnPage(paragraph.getPoints(), page);
            }
        }

        doc.save(_dataDir + "output_out.pdf");
    }

    private static void DrawRectangleOnPage(Rectangle rectangle, Page page) {
        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
        page.getContents().add(new SetRGBColorStroke(0, 1, 0));
        page.getContents().add(new SetLineWidth(2));
        page.getContents()
                .add(new Re(rectangle.getLLX(), rectangle.getLLY(), rectangle.getWidth(), rectangle.getHeight()));
        page.getContents().add(new ClosePathStroke());
        page.getContents().add(new GRestore());
    }

    private static void DrawPolygonOnPage(Point[] polygon, Page page) {
        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
        page.getContents().add(new SetRGBColorStroke(0, 0, 1));
        page.getContents().add(new SetLineWidth(1));
        page.getContents().add(new MoveTo(polygon[0].getX(), polygon[0].getY()));
        for (int i = 1; i < polygon.length; i++) {
            page.getContents().add(new LineTo(polygon[i].getX(), polygon[i].getY()));
        }
        page.getContents().add(new LineTo(polygon[0].getX(), polygon[0].getY()));
        page.getContents().add(new ClosePathStroke());
        page.getContents().add(new GRestore());
    }
```

**2- Dengan mengiterasi melalui koleksi paragraf dan mendapatkan teks dari mereka:**

```java
 public static void ExtractParagraph02() {
        // Buka file PDF yang sudah ada
        Document doc = new Document(_dataDir + "input.pdf");
        // Instansiasi ParagraphAbsorber
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(doc);

        for (PageMarkup markup : absorber.getPageMarkups()) {
            int i = 1;
            for (MarkupSection section : markup.getSections()) {
                int j = 1;

                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();

                    for (java.util.List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    paragraphText.append("\r\n");

                    System.out.println("Paragraf " + j + " dari bagian " + i + " pada halaman" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```