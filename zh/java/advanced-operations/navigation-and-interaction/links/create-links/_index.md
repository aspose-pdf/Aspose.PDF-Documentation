---
title: 在 PDF 文件中创建链接
linktitle: 创建链接
type: docs
weight: 10
url: zh/java/create-links/
description: 本节解释如何使用 Java 在 PDF 文档中创建链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 创建链接

Aspose.PDF for Java 允许您添加链接到外部 PDF 文件，以便您可以将多个文档链接在一起。通过在文档中添加链接到应用程序，可以从文档中链接到应用程序。这在您希望读者在教程的特定点执行某个操作或创建功能丰富的文档时非常有用。要创建应用程序链接：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象。
2. 获取要添加链接的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)。

1. 使用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 和 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 对象。
1. 使用 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 对象设置链接属性。
1. 同样，设置到 [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) 对象并调用 setAction(..) 方法。
1. 创建 [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) 对象时，指定您想启动的应用程序。
1. 将链接添加到 Page 对象的 [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) 集合中。
1. 最后，使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Save 方法保存更新后的 PDF。


以下代码片段展示了如何在 PDF 文件中创建指向应用程序的链接。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // 打开文档
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // 创建链接
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // 保存更新后的文档
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### 在PDF文件中创建PDF文档链接

Aspose.PDF for Java允许您添加指向外部PDF文件的链接，以便您可以将多个文档链接在一起。
 要创建一个 PDF 文档链接：

1. 首先，创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象。
1. 然后，获取要添加链接的特定 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)。
1. 使用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 和 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 对象。
1. 使用 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 对象设置链接属性。
1. 调用 setAction(..) 方法并传递 [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) 对象。
1. 在创建 [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) 对象时，指定应启动的 PDF 文件，以及应该打开的页码。
1. 将链接添加到页面对象的[注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection)集合中。
1. 最后，使用[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的 Save 方法保存更新后的 PDF。

以下代码片段显示了如何在 PDF 文件中创建 PDF 文档链接。

```java
    public static void CreatePDFDocumentLink() {

        // 打开文档
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // 创建链接
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // 保存更新后的文档
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```