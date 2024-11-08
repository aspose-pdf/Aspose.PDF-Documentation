---
title: 在现有PDF中分页
type: docs
weight: 30
url: /zh/java/page-break-in-existing-pdf/
description: 本节说明如何使用PdfFileEditor类在现有PDF中分页。
lastmod: "2021-06-05"
draft: false
---

作为默认布局，PDF文件中的内容是从左上到右下的布局添加的。一旦内容超出页面底部边距，就会发生分页。然而，您可能会遇到根据需要插入分页的要求。一个名为AddPageBreak(...)的方法被添加到[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor)类中以完成此要求。

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src 是源文档/文档路径/包含源文档的流
- dest 是目标文档/保存文档的路径/保存文档的流
- PageBreak 是分页符对象的数组。它有两个属性：分页符必须放置的页面索引和页面上分页符的垂直位置。

## 示例 1（添加分页符）

```java
   public static void PageBrakeExample01() {
        // 实例化 Document 实例
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // 实例化空白 Document 实例
        Document dest = new Document();
        // 创建 PdfFileEditor 对象
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // 保存结果文件
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## 示例 2

```java
  public static void PageBrakeExample02() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## 示例 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```