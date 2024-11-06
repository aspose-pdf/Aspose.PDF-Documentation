---
title: PDF文本注释
Texttitle: 文本注释
type: docs
weight: 10
url: zh/java/text-annotation/
description: Aspose.PDF for Java 允许您添加、获取和删除PDF文档中的文本注释。
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

添加、删除和获取注释对于不同种类的注释是相似的。让我们以文本注释为例。

## 如何在现有PDF文件中添加文本注释

在本教程中，您将学习如何在现有PDF文档中添加文本。文本工具允许您在文档的任何地方添加文本。文本注释是附加到PDF文档中特定位置的注释。关闭时，注释显示为一个图标；打开时，它应显示一个弹出窗口，其中包含读者选择的字体和大小的笔记文本。

注释由特定页面的[Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection)集合包含。
 这份集合仅包含该特定页面的注释；每个页面都有其自己的注释集合。

要向特定页面添加注释，请使用 Add 方法将其添加到该页面的注释集合中。

1. 首先，创建一个要添加到 PDF 的注释。
1. 然后打开输入 PDF。
1. 将注释添加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的注释集合中。

以下代码片段向您展示了如何在 PDF 页面中添加注释。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Sample contents for the annotation");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## 添加新的（或创建）自由文本注释

自由文本注释直接在页面上显示文本。PdfContentEditor.CreateFreeText 方法允许创建这种类型的注释。在以下代码片段中，我们在字符串首次出现的位置上方添加自由文本注释。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("自由文本演示");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## 获取自由文本注释

Aspose.PDF for Java 允许您从 PDF 文档中获取自由文本注释。

请查看以下代码片段以解决此任务：

```java
public static void GetFreeTextAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## 删除自由文本注释

Aspose.PDF for Java 允许您从 PDF 文档中删除自由文本注释。

请查看以下代码片段以解决此任务：

```java
  public static void DeleteFreeTextAnnotation() {
         // 加载PDF文件
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // 使用AnnotationSelector过滤注释
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // 删除注释
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## 从PDF文件的页面删除所有注释

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的 [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) 集合包含该特定页面的所有注释。
 要删除页面中的所有注释，请调用AnnotationCollection集合的*Delete*方法。

以下代码片段展示了如何删除特定页面的所有注释。

```java
    public static void DeleteTextAnnotation() {
         // 加载PDF文件
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // 使用AnnotationSelector过滤注释
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // 删除注释
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## 从PDF文档的页面获取所有注释

Aspose.PDF允许您从整个文档或给定页面获取注释。 要从 PDF 文档中的页面获取所有注释，请遍历所需页面资源的 [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) 集合。下面的代码片段展示了如何获取页面的所有注释。

```java
  public static void GetTextAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```