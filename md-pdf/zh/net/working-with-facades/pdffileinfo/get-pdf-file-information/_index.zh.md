---
title: 获取PDF文件信息
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: 本节解释如何使用Aspose.PDF Facades获取PDF文件信息。
lastmod: "2021-06-05"
draft: false
---

为了获取PDF文件的特定信息，需要创建一个[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)类的对象。之后，可以获取诸如主题、标题、关键字和创建者等各个属性的值。

以下代码片段展示了如何获取PDF文件信息。

```csharp
 public static void GetPdfInfo()
        {
            // 打开文档
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // 获取PDF信息
            Console.WriteLine("Subject: {0}", fileInfo.Subject);
            Console.WriteLine("Title: {0}", fileInfo.Title);
            Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
            Console.WriteLine("Creator: {0}", fileInfo.Creator);
            Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
            Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
            // 判断是否为有效的PDF且是否加密
            Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Page width:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Page height:{0}", fileInfo.GetPageHeight(1));
        }
```

## 获取元信息

为了获取信息，我们使用[Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header)属性。通过'Hashtable'我们获取所有可能的值。

```csharp
public static void GetMetaInfo()
        {
            // 创建PdfFileInfo对象的实例
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // 检索所有现有的自定义属性
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // 检索一个自定义属性
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```