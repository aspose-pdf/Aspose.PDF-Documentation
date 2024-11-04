---
title: 将 PDF 文件转换为其他格式
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF 文件转换为其他文件格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF 转换为 EPUB

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for PHP 为您提供了一个免费的在线应用程序 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 EPUB 免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="电子出版物">EPUB</abbr>**（电子出版物的缩写）是国际数字出版论坛（IDPF）发布的一个免费的开放电子书标准。
 文件的扩展名为.epub。EPUB专为可重排内容而设计，这意味着EPUB阅读器可以为特定显示设备优化文本。EPUB也支持固定布局内容。该格式旨在成为出版商和转换公司可以内部使用的单一格式，并用于分发和销售。它取代了Open eBook标准。

Aspose.PDF for PHP支持将PDF文档转换为EPUB格式的功能。Aspose.PDF for PHP有一个名为[EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions)的类，可以用作[Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-)方法的第二个参数，以生成EPUB文件。请尝试使用以下代码片段来实现此需求。

```php
// 创建Document类的新实例并加载输入PDF文件
$document = new Document($inputFile);

// 创建EpubSaveOptions类的新实例
$saveOption = new EpubSaveOptions();

// 使用指定的保存选项将文档保存为EPUB格式
$document->save($outputFile, $saveOption);
```

## Convert PDF to LaTeX/TeX

**Aspose.PDF for PHP** 支持将 PDF 转换为 LaTeX/TeX。  
LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统，以实现高质量的排版。

为了将 PDF 文件转换为 TeX，Aspose.PDF 提供了 [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) 类，该类提供了 `setOutDirectoryPath` 方法，用于在转换过程中保存临时图像。

下面的代码片段展示了使用 Java 将 PDF 文件转换为 TEX 格式的过程。

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 LaTeXSaveOptions 对象
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// 将文档保存为 LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for PHP 为您提供了免费的在线应用 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 LaTeX/TeX 使用免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为文本

**Aspose.PDF for PHP** 支持将整个 PDF 文档和单个页面转换为文本文件。

### 将整个 PDF 文档转换为文本文件

您可以使用 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 类的 Visit 方法将 PDF 文档转换为 TXT 文件。

以下代码片段解释了如何从所有页面提取文本。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个 TextAbsorber 对象以从文档中提取文本
$textAbsorber = new TextAbsorber();

// 从文档中提取文本
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// 将提取的文本保存到输出文件
file_put_contents($outputFile, $content);

// 获取输出文件的文件大小
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**

Aspose.PDF for PHP 为您提供了一个免费的在线应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为文本的免费应用程序](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### 将 PDF 页面转换为文本文件

您可以使用 Aspose.PDF for PHP 将 PDF 文档转换为 TXT 文件。您应该使用 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 类的 Visit 方法来解决此任务。

以下代码片段解释了如何从特定页面提取文本。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个 TextAbsorber 对象以从文档中提取文本
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // 将提取的文本保存到输出文件
    file_put_contents($outputFile, $content);
}
```


## 将 PDF 转换为 XPS

**Aspose.PDF for PHP** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的功能。让我们尝试使用提供的代码片段将 PDF 文件转换为 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for PHP 为您提供了在线免费应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 XPS 免费应用程序](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与微软公司开发的 XML Paper Specification 相关联。XML Paper Specification（XPS），曾用代号为 Metro，并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看整合到 Windows 操作系统中的一项倡议。

为了将 PDF 文件转换为 XPS，Aspose.PDF 提供了 [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) 类，该类用作 Document.save(..) 构造函数的第二个参数以生成 XPS 文件。
 以下代码片段显示了将 PDF 文件转换为 XPS 格式的过程。

```php
// 创建一个新的 Document 对象并加载输入的 PDF 文件
$document = new Document($inputFile);

// 创建一个新的 XpsSaveOptions 对象
$saveOption = new XpsSaveOptions();

// 使用指定的保存选项将文档保存为 XPS
$document->save($outputFile, $saveOption);
```