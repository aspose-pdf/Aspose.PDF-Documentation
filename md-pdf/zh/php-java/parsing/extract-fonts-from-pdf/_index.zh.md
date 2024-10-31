---
title: 从PDF提取字体
linktitle: 提取字体
type: docs
weight: 30
url: /php-java/extract-fonts-from-pdf/
description: 如何使用Aspose.PDF for PHP从PDF中提取字体
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

如果您想从PDF文档中获取所有字体，可以使用Document类中提供的[Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--)方法。
请查看以下代码片段，以便从现有PDF文档中获取所有字体：

```php

    // 创建License类的新实例并设置许可证文件。
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // 设置包含PDF文档的目录路径和提取字体的输出目录。
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // 初始化响应数据变量。
    $responseData = "";

    try {
        // 加载PDF文档。
        $document = new Document($inputFile);

        // 获取PDF文档中使用的所有字体。
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // 遍历每个字体并将其保存为TrueType字体文件。
        foreach ($fonts as $font) {
            // 为字体文件设置输出文件路径。
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // 创建一个FileOutputStream对象以写入字体文件。
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // 将字体保存为TrueType字体文件。
            $font->save($fontStream);

            // 关闭字体流。
            $fontStream->close();

            // 将字体名称附加到响应数据。
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // 关闭PDF文档。
        $document->close();
    }
```