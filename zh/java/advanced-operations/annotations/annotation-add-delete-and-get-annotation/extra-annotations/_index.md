---
title: 使用额外类型的PDF注释
linktitle: 额外注释
type: docs
weight: 60
url: zh/java/extra-annotations/
description: 本节介绍如何添加、获取和删除PDF文档中的额外类型的注释。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何在现有PDF文件中添加插入符号注释

插入符号注释是一个指示文本编辑的符号。插入符号注释也是标记注释，因此插入符号类继承自标记类，并提供函数来获取或设置插入符号注释的属性以及重置插入符号注释外观的流程。

创建插入符号注释的步骤：

1. 加载PDF文件 - 新的[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)。

1. 创建新的 [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) 并设置 Caret 参数（新的 Rectangle、title、Subject、Flags、color、width、StartingStyle 和 EndingStyle）。此注释用于指示文本插入。
1. 创建新的 [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) 并设置参数（新的 Rectangle、title、color、新的 QuadPoints 和新的 points、Subject、InReplyTo、ReplyType）。
1. 然后我们可以将注释添加到页面。

以下代码片段显示了如何向 PDF 文件添加 Caret Annotation：

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample.pdf");
        // 此注释用于指示文本插入
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // 此注释用于指示文本替换
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## 获取插入符号注释

请尝试使用以下代码片段在 PDF 文档中获取插入符号注释

```java
    public static void GetCaretAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## 删除插入符号注释

以下代码片段展示了如何从 PDF 文件中删除插入符号注释。

```java
public static void DeleteCaretAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 删除注释
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 是一个超文本链接，指向文档中的其他位置或要执行的操作。

## 添加链接注释

链接是一个可以放置在页面任意位置的矩形区域。每个链接都有一个与之关联的对应 PDF 操作。当用户点击该链接区域时，将执行此操作。

以下代码片段展示了如何使用电话号码示例向 PDF 文件添加链接注释：

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // 文档目录的路径。

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // 加载 PDF 文件
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // 创建 TextFragmentAbsorber 对象以查找电话号码
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // 仅接受第一页的吸收器
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // 创建链接注释并设置操作以拨打电话号码
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // 将注释添加到页面
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 获取链接注释

请尝试使用以下代码片段从 PDF 文档中获取链接注释。

```java
    public static void GetLinkAnnotations() {

        // 加载 PDF 文件
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // 打印每个链接注释的 URL
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // 打印与超链接关联的文本
            System.out.println(extractedText);
        }
    }
```


## 删除链接注释

以下代码片段显示如何从 PDF 文件中删除链接注释。为此，我们需要找到并删除第一页上的所有链接注释。之后，我们将保存删除了注释的文档。

```java
    public static void DeleteLinkAnnotations() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // 保存删除了注释的文档
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## 使用 Aspose.PDF for Java 对特定页面区域进行 Redaction 注释

Aspose.PDF for Java 支持在现有 PDF 文件中添加和操作注释的功能。最近，一些客户提出了一个需求，即在 PDF 文档的某个页面区域进行涂黑（移除文本、图片等元素）。为了满足这一需求，提供了一个名为 RedactionAnnotation 的类，可以用来涂黑某些页面区域，也可以用来操作现有的 RedactionAnnotations 并将其涂黑（即展平注释并移除其下的文本）。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // 打开文档
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 为特定页面区域创建 RedactionAnnotation 实例
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // 要在涂黑注释上打印的文本
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // 在涂黑注释上重复覆盖文本
        annot.setRepeat(true);

        // 将注释添加到第一页的注释集合中
        page.getAnnotations().add(annot);

        // 展平注释并涂黑页面内容（即移除文本和图像
        // 在涂黑的注释下）
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## 门面方法

Aspose.PDF.Facades 命名空间中还有一个名为 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 的类，该类提供了操作 PDF 文件中现有注释的功能。此类包含一个名为 [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) 的方法，该方法提供了删除某些页面区域的功能。

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // 涂抹特定页面区域
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```