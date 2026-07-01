---
title: PDFから段落を抽出
linktitle: 段落を抽出
type: docs
weight: 20
url: /ja/androidjava/extract-paragraph-from-pdf/
description: Aspose.PDF を使用したコンテンツ抽出で、Android/Java で PDF ドキュメントから特定の段落を抽出する方法を学びます。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントからテキストを段落形式で抽出

単一ページまたはドキュメント全体から特定のテキスト（「プレーンテキスト」または「正規表現」を使用）を検索してテキストを取得したり、単一ページ、ページ範囲、またはドキュメント全体の完全なテキストを取得したりできます。しかし、場合によっては PDF ドキュメントから段落や段落形式のテキストを抽出する必要があります。PDF ドキュメントページのテキスト内でセクションや段落を検索する機能を実装しました。TextFragmentAbsorber や TextAbsorber と同様の ParagraphAbsorber クラスを導入し、PDF ドキュメントから段落を抽出できるようにしました。ParagraphAbsorber を使用する方法は以下の 2 つがあります。

**1- PDF ページ上でテキストのセクションと段落の境界を描画することによって:**

```java
public static void ExtractParagraph() {
        // The path to the documents directory.
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

**2- 段落コレクションを反復処理し、それらのテキストを取得する方法:**

```java
 public static void ExtractParagraph02() {
        // Open an existing PDF file
        Document doc = new Document(_dataDir + "input.pdf");
        // Instantiate ParagraphAbsorber
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

                    System.out.println("Paragraph " + j + " of section " + i + " on page" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```

