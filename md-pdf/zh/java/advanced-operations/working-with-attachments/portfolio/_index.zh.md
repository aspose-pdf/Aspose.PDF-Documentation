---
title: 在 PDF 文档中使用组合文件
linktitle: 组合文件
type: docs
weight: 40
url: /java/portfolio/
description: 如何使用 Java 创建 PDF 组合文件。您应该使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 组合文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

首先，让我们弄清楚**什么是 PDF 组合文件格式？**

例如，获取一个包含 Word、Excel、PowerPoint 演示文稿等作为附件的 PDF 组合文件。在这里，每个附件文件都保持其原始文档格式，但被嵌入或组装到一个 PDF 组合文件中。当然，您可以像在驱动器或文件夹中一样打开、阅读或编辑 PDF 组合文件中的每个单独文件。此外，就像普通 PDF 文档一样，您还可以应用水印、设置密码和安全权限，例如查看、打印或对 PDF 组合文件的附件进行更改的能力。

我们可以将本机文件以其原始类型或格式作为附件放置或组装到 PDF 组合文件中。

## 如何创建 PDF 组合

Aspose.PDF 允许使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类创建 PDF 组合文档。在通过 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 类获取文件后，将文件添加到 Document.Collection 对象中。当文件被添加后，使用 Document 类的 Save 方法保存组合文档。

以下示例使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 组合。

下面的代码生成如下组合。

### 使用 Aspose.PDF 创建的 PDF 组合

![使用 Aspose.PDF for Java 创建的 PDF 组合](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // 实例化 Document 对象
        Document pdfDocument = new Document();

        // 实例化文档集合对象
        pdfDocument.setCollection(new Collection());

        // 获取要添加到组合中的文件
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // 提供文件的描述
        excel.setDescription ("Excel 文件");
        word.setDescription ("Word 文件");
        image.setDescription ("图像文件");

        // 将文件添加到文档集合中
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // 保存组合文档
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## 从 PDF Portfolio 提取文件

PDF Portfolio 允许您将来自各种来源的内容（例如，PDF、Word、Excel、JPEG 文件）整合到一个统一的容器中。原始文件保留其各自的身份，但被组装到一个 PDF Portfolio 文件中。用户可以独立于其他组件文件打开、阅读、编辑和格式化每个组件文件。

Aspose.PDF 允许使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类创建 PDF Portfolio 文档。它还提供了从 PDF Portfolio 中提取文件的功能。

下面的代码片段展示了从 PDF Portfolio 中提取文件的步骤。

![从 PDF Portfolio 提取文件](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // 获取嵌入文件的集合
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // 迭代 Portfolio 的每个文件
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## 从 PDF 组合文件中移除文件

为了从 PDF 组合文件中删除/移除文件，请尝试使用以下代码行。

```java
public static void RemoveFilesFromPDFPortfolio() {
    // 加载源 PDF 组合文件
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```