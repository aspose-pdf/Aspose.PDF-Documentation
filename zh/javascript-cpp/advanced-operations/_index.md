---
title: 高级操作使用JavaScript通过C++
linktitle: 高级操作
type: docs
weight: 60
url: zh/javascript-cpp/advanced-operations/
description: Aspose.PDF for JavaScript通过C++不仅可以执行简单和容易的任务，还可以应对更复杂的目标。查看下一节以获取高级用户和开发人员的信息。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**高级操作** 是一个关于如何以编程方式处理现有PDF文件的章节，无论是使用Aspose.PDF创建的文档（如[基本操作](/pdf/javascript-cpp/basic-operations/)中讨论的），还是使用Adobe Acrobat、Google Docs、Microsoft Office、Open Office或其他任何PDF生成器创建的PDF。

## 使用Web Workers

版本23.6增加了使用Web Workers的功能：

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

通过C++从JavaScript使用Web Workers，允许您在一个单独的工作线程中执行操作，而不会阻塞界面。

Web Workers 是一种用于在后台运行脚本的简单工具。这使您能够在不干扰用户界面的情况下，在一个独立的工作线程中执行任务。

您将学习不同的方法来：

- [处理文档](/pdf/javascript-cpp/working-with-documents/) - 压缩、拆分和合并文档，并对整个文档进行其他操作。
- [处理页面](/pdf/javascript-cpp/working-with-pages/) - 添加、移动或删除、裁剪页面、添加印章。
- [PDF中的元数据](/pdf/javascript-cpp/pdf-file-metadata/) - 获取或设置文档中的元数据。
- [处理图像](/pdf/javascript-cpp/working-with-images/) - 在文档中插入、删除、提取图像。
- [导航和交互](/pdf/javascript-cpp/navigation-and-interaction/) - 处理动作、书签、页面导航。
- [注释](/pdf/javascript-cpp/annotations/) - 注释允许用户在PDF页面上添加自定义内容。您可以添加、删除和修改PDF文档中的注释。

- [安全和签名](/pdf/javascript-cpp/securing-and-signing/) - 以编程方式保护和签署您的PDF文档。
- [Attachments](/pdf/javascript-cpp/attachments/) - PDF 文档可能包含文件附件。这些附件可以是其他 PDF 文档，或任何类型的文件，如音频文件、Microsoft Office 文档等。您将学习如何向 PDF 添加附件，获取附件的信息，并将其保存为文件，用 JavaScript 从 PDF 中以编程方式删除附件。