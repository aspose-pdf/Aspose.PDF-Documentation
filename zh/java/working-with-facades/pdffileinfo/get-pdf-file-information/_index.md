---
title: 获取 PDF 文件信息 - 外观
type: docs
weight: 10
url: zh/java/get-pdf-information/
description: 本节说明如何使用 PdfFileInfo 类通过 Aspose.PDF Facades 获取 PDF 文件信息。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

为了获取特定于 PDF 文件的信息，您需要创建一个 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 类的对象。之后，您可以获取各个属性的值，比如主题、标题、关键词和创建者等。

以下代码片段展示了如何获取 PDF 文件信息。

```java
public static void GetPdfInfo()
    {
        // 打开文档
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // 获取 PDF 信息
        System.out.println("主题: " + fileInfo.getSubject());
        System.out.println("标题: " + fileInfo.getTitle());
        System.out.println("关键词: " + fileInfo.getKeywords());
        System.out.println("创建者: " + fileInfo.getCreator());
        System.out.println("创建日期: " + fileInfo.getCreationDate());
        System.out.println("修改日期: " + fileInfo.getModDate());
        // 检查是否为有效 PDF 以及是否已加密
        System.out.println("是否为有效 PDF: " + fileInfo.isPdfFile());
        System.out.println("是否已加密: " + fileInfo.isEncrypted());

        System.out.println("页面宽度:" + fileInfo.getPageWidth(1));
    }
```


## 获取元信息

为了获取信息，我们使用[getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--)方法。通过'Hashtable'我们可以获取所有可能的值。

```java
public static void GetMetaInfo()
    {        
        // 创建PdffileInfo对象的实例
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // 检索所有现有的自定义属性
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // 获取键
            String key = enumerator.nextElement();  
            // 打印键和值
            System.out.println(key + ": " + hTable.get(key));
        }

        // 检索一个自定义属性
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```