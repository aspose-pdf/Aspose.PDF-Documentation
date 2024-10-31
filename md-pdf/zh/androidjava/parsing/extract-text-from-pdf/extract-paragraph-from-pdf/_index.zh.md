---
title: 从PDF中提取段落
linktitle: 提取段落
type: docs
weight: 20
url: /androidjava/extract-paragraph-from-pdf/
description: 本文介绍如何使用ParagraphAbsorber——Aspose.PDF中的一个特殊工具，从PDF文档中提取文本。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 以段落形式从PDF文档中提取文本

我们可以通过从单个页面或整个文档中搜索特定文本（使用“纯文本”或“正则表达式”）来从PDF文档中获取文本，或者我们可以获取单个页面、页面范围或完整文档的完整文本。
 然而，在某些情况下，您需要从 PDF 文档中提取段落或以段落形式的文本。我们实现了在 PDF 文档页面的文本中搜索章节和段落的功能。我们引入了 ParagraphAbsorber 类（类似于 TextFragmentAbsorber 和 TextAbsorber），可以用于从 PDF 文档中提取段落。您可以通过以下两种方式使用 ParagraphAbsorber：

**1- 通过在 PDF 页面上绘制文本章节和段落的边框：**

```java
public static void ExtractParagraph() {
        // 文档目录的路径。
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

**2- 通过遍历段落集合并获取它们的文本：**

```java
 public static void ExtractParagraph02() {
        // 打开一个现有的 PDF 文件
        Document doc = new Document(_dataDir + "input.pdf");
        // 实例化 ParagraphAbsorber
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

                    System.out.println("第 " + j + " 段, 第 " + i + " 节在页面" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```