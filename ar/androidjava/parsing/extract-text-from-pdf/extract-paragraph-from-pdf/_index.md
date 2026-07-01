---
title: استخراج الفقرة من PDF
linktitle: استخراج الفقرة
type: docs
weight: 20
url: /ar/androidjava/extract-paragraph-from-pdf/
description: تعلم كيفية استخراج فقرات محددة من مستند PDF في Android/Java باستخدام Aspose.PDF لاستخراج المحتوى.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من مستند PDF بصيغة فقرات

يمكننا الحصول على النص من مستند PDF عن طريق البحث عن نص معين (باستخدام "plain text" أو "regular expressions") من صفحة واحدة أو كامل المستند، أو يمكننا الحصول على النص الكامل لصفحة واحدة، أو نطاق من الصفحات، أو المستند بالكامل. ومع ذلك، في بعض الحالات، تحتاج إلى استخراج الفقرات من مستند PDF أو النص بصيغة فقرات. لقد نفذنا وظيفة للبحث عن الأقسام والفقرات في نص صفحات مستند PDF. قدمنا فئة ParagraphAbsorber (مثل TextFragmentAbsorber و TextAbsorber)، والتي يمكن استخدامها لاستخراج الفقرات من مستندات PDF. هناك طريقتان التاليان يمكنك من خلالهما استخدام ParagraphAbsorber:

**1- عن طريق رسم حدود الأقسام والفقرات النصية على صفحة PDF:**

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

**2- عبر التكرار عبر مجموعة الفقرات والحصول على النص الخاص بها:**

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

