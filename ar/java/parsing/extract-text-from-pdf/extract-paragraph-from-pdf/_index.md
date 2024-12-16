---
title: استخراج فقرة من PDF
linktitle: استخراج فقرة
type: docs
weight: 20
url: /ar/java/extract-paragraph-from-pdf/
description: تصف هذه المقالة كيفية استخدام ParagraphAbsorber - أداة خاصة في Aspose.PDF لاستخراج النص من مستندات PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من مستند PDF في شكل فقرات

يمكننا الحصول على نص من مستند PDF من خلال البحث عن نص معين (باستخدام "النص العادي" أو "التعبيرات العادية") من صفحة واحدة أو المستند بأكمله، أو يمكننا الحصول على النص الكامل لصفحة واحدة، أو نطاق من الصفحات أو المستند بأكمله.
 ومع ذلك، في بعض الحالات، تحتاج إلى استخراج الفقرات من مستند PDF أو النص في شكل فقرات. لقد قمنا بتنفيذ وظيفة للبحث عن الأقسام والفقرات في نص صفحات مستند PDF. لقد قدمنا فئة ParagraphAbsorber (مثل TextFragmentAbsorber وTextAbsorber)، والتي يمكن استخدامها لاستخراج الفقرات من مستندات PDF. هناك طريقتان يمكنك استخدام ParagraphAbsorber بهما:

**1- من خلال رسم حدود الأقسام والفقرات النصية على صفحة PDF:**

```java
public static void ExtractParagraph() {
    // المسار إلى دليل المستندات.
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
    page.getContents().add(new Re(rectangle.getLLX(), rectangle.getLLY(), rectangle.getWidth(), rectangle.getHeight()));
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

**2- من خلال التكرار عبر مجموعة الفقرات والحصول على نصها:**

```java
public static void ExtractParagraph02() {
        // افتح ملف PDF موجود
        Document doc = new Document(_dataDir + "input.pdf");
        // إنشاء كائن ParagraphAbsorber
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

                    System.out.println("فقرة "+j+" من القسم "+ i + " على الصفحة"+ ":"+markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```