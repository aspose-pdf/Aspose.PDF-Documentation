---
title: 使用操作
linktitle: 操作
type: docs
weight: 20
url: /zh/java/actions/
description: 本节解释了如何使用 Java 以编程方式向文档和表单字段添加操作。了解如何在 PDF 文件中添加、创建和获取超链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文件可以包含嵌入的文件附件，通常需要链接到这些文档。您可以通过在主文档中创建指向附件的链接，将读者从主 PDF 文档引导到 PDF 附件。

## 在 PDF 文件中添加超链接

可以在 PDF 文件中添加超链接，以便读者导航到 PDF 的另一部分或外部内容。

为了向 PDF 文档添加网页超链接：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。

1. 获取你想添加链接的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类。
1. 使用 Page 和 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 对象。Rectangle 对象用于指定页面上要添加链接的位置。
1. 将 getAction 方法设置为 [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) 对象，该对象指定远程 URI 的位置。
1. 为了显示超链接文本，在与 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 对象放置位置相似的位置添加一个文本字符串。
1. 要添加自由文本：

- 实例化一个 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 对象。
 它也接受 Page 和 Rectangle 对象作为参数，因此可以提供与 LinkAnnotation 构造函数中指定的相同值。
- 使用 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 对象的 Contents 属性，指定应在输出 PDF 中显示的字符串。
- 可选地，将 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 和 FreeTextAnnotation 对象的边框宽度设置为 0，以便它们不会出现在 PDF 文档中。
- 一旦定义了 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 和 [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) 对象，将这些链接添加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的 Annotations 集合中。

- 最后，使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Save 方法保存更新后的 PDF。
以下代码片段展示了如何向 PDF 文件添加超链接。

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // 打开文档
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // 创建链接
        Page page = document.getPages().get_Item(1);
        // 创建链接注释对象
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // 为链接注释创建边框对象
        Border border = new Border(link);
        // 将边框宽度值设置为0
        border.setWidth(0);
        // 设置链接注释的边框
        link.setBorder(border);
        // 指定链接类型为远程 URI
        link.setAction(new GoToURIAction("www.aspose.com"));
        // 将链接注释添加到 PDF 文件第一页的注释集合中
        page.getAnnotations().add(link);

        // 创建自由文本注释
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // 要添加为自由文本的字符串
        textAnnotation.setContents("Link to Aspose website");
        // 设置自由文本注释的边框
        textAnnotation.setBorder(border);
        // 将自由文本注释添加到文档第一页的注释集合中
        page.getAnnotations().add(textAnnotation);

        // 保存更新后的文档
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## 创建指向同一 PDF 中页面的超链接

Aspose.PDF for Java 提供了出色的 PDF 创建和操作功能。它还提供了向 PDF 页面添加链接的功能，链接可以直接指向另一个 PDF 文件中的页面、网页 URL、启动应用程序的链接甚至是同一 PDF 文件中的页面。

为了添加本地超链接，我们需要创建一个 TextFragment，以便将链接与 TextFragment 关联。[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 类有一个名为 [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) 的方法，用于关联 LocalHyperlink 实例。以下代码片段显示了实现此要求的步骤。

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // 创建 Document 实例
        Document document = new Document();

        // 向 PDF 文件的页面集合中添加页面
        Page page = document.getPages().add();

        // 创建 TextFragment 实例
        TextFragment text = new TextFragment("链接页面编号测试到第 2 页");

        // 创建本地超链接实例
        LocalHyperlink link = new LocalHyperlink();

        // 设置链接实例的目标页面
        link.setTargetPageNumber(2);

        // 设置 TextFragment 的超链接
        text.setHyperlink(link);

        // 将文本添加到 Page 的段落集合中
        page.getParagraphs().add(text);

        // 创建新的 TextFragment 实例
        text = new TextFragment("链接页面编号测试到第 1 页");

        // TextFragment 应该添加到新页面上
        text.setInNewPage(true);

        // 创建另一个本地超链接实例
        link = new LocalHyperlink();

        // 为第二个超链接设置目标页面
        link.setTargetPageNumber(1);

        // 为第二个 TextFragment 设置链接
        text.setHyperlink(link);

        // 将文本添加到页面对象的段落集合中
        page.getParagraphs().add(text);

        // 保存更新后的文档
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## 获取 PDF 超链接目标 (URL)

链接在 PDF 文件中表示为注释，可以添加、更新或删除。Aspose.PDF for Java 还支持获取 PDF 文件中超链接的目标 (URL)。

要获取链接的 URL：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象。
1. 获取您想要提取链接的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 类从指定页面中提取所有 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) 对象。
1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 对象传递给 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的 Accept 方法。

1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) 对象的 Selected 属性，将所有选定的链接注释获取到一个 IList 对象中。
1. 最后，将 LinkAnnotation Action 提取为 GoToURIAction。

以下代码片段显示了如何从 PDF 文件中获取超链接目标（URL）。

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // 提取操作
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // 迭代列表中的各个项目
        if (list.size() == 0)
            System.out.println("未找到超链接..");
        else {
            // 遍历所有书签
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // 打印目标 URL
                    System.out.println("目标: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // 结束 else
    }
```


## 获取超链接文本

一个超链接有两个部分：在文档中显示的文本和目标 URL。在某些情况下，我们需要的是文本而不是 URL。

PDF 文件中的文本和注释/操作由不同的实体表示。页面上的文本只是一些单词和字符，而注释带来了一些交互性，例如超链接固有的交互性。

要找到 URL 内容，您需要同时处理注释和文本。[Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) 对象本身没有文本，但位于页面上的文本下。因此，要获取文本，Annotation 提供了 URL 的边界，而 Text 对象提供了 URL 内容。请参阅以下代码片段。

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // 提取操作
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // 打印每个链接注释的 URL
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // 打印与超链接关联的文本
                System.out.println(extractedText);
            }
        }
    }
```


## 从 PDF 文件中移除文档打开操作

[如何在查看文档时指定 PDF 页面](#how-to-specify-pdf-page-when-viewing-document) 解释了如何设置文档在不同于第一页的页面上打开。当连接多个文档时，如果其中一个或多个设置了 GoTo 操作，你可能需要移除它们。例如，如果合并两个文档，而第二个文档有一个 GoTo 操作将你带到第二页，则输出文档将打开在第二个文档的第二页，而不是合并文档的第一页。为了避免这种行为，需要移除打开操作命令。

要移除打开操作：

1. 将 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) 方法设置为 null。
2. 使用 Document 对象的 Save 方法保存更新的 PDF。

以下代码片段展示了如何从 PDF 文件中移除文档打开操作。

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // 打开文档
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // 移除文档打开操作
        document.setOpenAction(null);
        
        // 保存更新后的文档
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## 如何指定查看文档时的 PDF 页面 {#how-to-specify-pdf-page-when-viewing-document}

在 PDF 查看器（例如 Adobe Reader）中查看 PDF 文件时，文件通常会在第一页打开。然而，可以设置文件在其他页面打开。

[XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) 类允许您指定要在 PDF 文件中打开的页面。当将 GoToAction 对象值传递给 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 getOpenAction 方法时，文档将在与 XYZExplicitDestination 对象指定的页面打开。以下代码片段显示了如何指定页面作为文档打开操作。

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // 加载 PDF 文件
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // 获取文档的第二页实例
        Page page2 = document.getPages().get_Item(2);
        // 创建变量以设置目标页面的缩放因子
        double zoom = 1;
        // 创建 GoToAction 实例
        GoToAction action = new GoToAction(page2);
        // 跳转到第 2 页
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // 设置文档打开动作
        document.setOpenAction (action);
        // 保存更新后的文档
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```