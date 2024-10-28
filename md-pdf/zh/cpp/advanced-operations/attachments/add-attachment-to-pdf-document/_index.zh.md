```
title: 向PDF文档添加附件
linktitle: 向PDF文档添加附件
type: docs
weight: 10
url: /cpp/add-attachment-to-pdf-document/
description: 本页描述如何使用Aspose.PDF for C++库向PDF文件添加附件
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

附件可以包含各种信息，并且可以是多种类型的文件。本文介绍如何向PDF文件添加附件。

1. 创建一个新的C++项目。
1. 添加对Aspose.PDF DLL的引用。
1. 创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. 使用您要添加的文件和文件描述创建一个[FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification)对象。
1.
``` 将[FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification)对象添加到[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection)集合中，使用集合的Add方法。

[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection)集合包含PDF文件中的所有附件。以下代码片段向您展示了如何在PDF文档中添加附件。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// 打开文档

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// 设置要添加为附件的新文件

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"示例文本文件");


// 将附件添加到文档的附件集合中

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// 保存新的输出

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```