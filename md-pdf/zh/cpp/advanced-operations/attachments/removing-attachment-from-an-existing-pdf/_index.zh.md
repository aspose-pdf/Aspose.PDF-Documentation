---
title: 从PDF中移除附件
linktitle: 从现有PDF中移除附件
type: docs
weight: 30
url: /cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF for C++ 可以从您的PDF文档中移除附件。使用C++ PDF API通过Aspose.PDF库移除PDF文件中的附件。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF可以从PDF文件中移除附件。PDF文档的附件保存在Document对象的EmbeddedFiles集合中。

要删除与PDF文件关联的所有附件：

1. 调用[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection)集合的[Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843)方法。
1. 使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的Save方法保存更新后的文件。

以下代码片段展示了如何从PDF文档中移除附件。

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // 打开文档
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // 删除所有附件
 pdfDocument->get_EmbeddedFiles()->Delete();

 // 保存更新后的文件
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```