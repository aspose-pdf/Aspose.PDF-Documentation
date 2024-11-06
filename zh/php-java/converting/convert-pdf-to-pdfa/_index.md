---
title: 将 PDF 转换为 PDF/A 格式
linktitle: 将 PDF 转换为 PDF/A 格式
type: docs
weight: 100
url: zh/php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for PHP** 允许您将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。在此之前，必须对文件进行验证。本文解释了如何进行操作。

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 的合规性。市场上的所有工具都有自己对 PDF/A 合规性的“表现”。请参考本文关于 [PDF/A 验证工具](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) 的文章。我们选择 Adobe 产品来验证 Aspose.PDF 如何生成 PDF 文件，因为 Adobe 是所有与 PDF 相关的事物的中心。

在将 PDF 转换为符合 PDF/A 标准的文件之前，请使用 validate 方法验证 PDF。
 验证结果存储在一个XML文件中，然后这个结果也传递给convert方法。您还可以使用[ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction)枚举来指定无法转换的元素的操作。

## PDF到PDF/A转换

以下代码片段显示如何将PDF文件转换为符合PDF/A-1b标准的PDF。

```php
// 创建一个新的Document对象并加载输入PDF文件。
$document = new Document($inputFile);

// 将文档转换为PDF/A-1a格式，并指定日志文件和错误操作。
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// 将转换后的文档保存到输出文件。
$document->save($outputFile);
```

若仅执行验证，请使用以下代码行：

```php
// 创建一个新的Document对象并加载输入PDF文件。
$document = new Document($inputFile);

// 将文档转换为PDF/A-1a格式，并指定日志文件和错误操作。
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// 验证PDF是否符合PDF/A-1a标准
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "有效";
}
else
{
    echo "无效";
}
```

{{% alert color="primary" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}