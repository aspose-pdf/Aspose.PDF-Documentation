---
title:  从AcroForm提取数据
linktitle:  从AcroForm提取数据
type: docs
weight: 50
url: zh/php-java/extract-data-from-acroform/
description: AcroForms存在于许多PDF文档中。本文旨在帮助您了解如何使用PHP和Aspose.PDF从AcroForms中提取数据。
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档中提取表单字段

Aspose.PDF for PHP不仅让您创建和填写表单字段，还使您能够轻松地从PDF文件中提取表单字段数据或表单字段信息。

假设我们事先不知道表单字段的名称。然后我们应该遍历PDF中的每一页，以提取关于PDF中所有AcroForms的信息以及表单字段的值。要访问表单，我们需要使用[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)方法。

```php

    // 创建License类的新实例并设置许可证文件
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // 设置包含PDF文档的目录路径
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // 设置输入PDF文件的路径
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // 设置响应头以指示响应将采用JSON格式
    header('Content-Type: application/json; charset=utf-8');

    // 初始化响应数据变量
    $responseData = "";

    try {
        // 创建Document类的新实例并加载输入PDF文件
        $document = new Document($inputFile);

        // 从文档中获取表单字段并将它们转换为PHP值
        $fields = java_values($document->getForm()->getFields());

        // 遍历每个表单字段并提取字段名称和值
        foreach ($fields as $formField) {
            // 将字段名称和值连接到响应数据
            $responseData = $responseData . "(字段名称: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " 值: " . $formField->getValue() . "),";
        }

        // 关闭文档
        $document->close();
    }
```


如果您知道要从中提取值的表单字段的名称，那么您可以使用Documents.Form集合中的索引器快速检索这些数据。

## 从PDF文件中提取数据到XML

Form类允许您使用ExportXml方法将数据从PDF文件导出到XML文件。为了将数据导出到XML，您需要创建一个Form类的对象，然后使用FileStream对象调用ExportXml方法。最后，您可以关闭FileStream对象并处理Form对象。以下代码片段显示了如何导出数据到XML文件。

```php

    // 打开文档
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 创建一个FileOutputStream对象来写入字体文件。
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // 导出数据
    $form->exportXml($xmlOutputStream);

    // 关闭文件流
    $xmlOutputStream->close();

    // 关闭文档
    $form->close();
```

## 从PDF文件导出数据到FDF

要将PDF表单数据导出到XFDF文件，我们可以使用[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)类中的[exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-)方法。

请注意，这是来自 `com.aspose.pdf.facades` 的一个类。尽管名称相似，但这个类的用途稍有不同。

为了将数据导出到 FDF，您需要创建一个 `Form` 类的对象，然后使用 `OutputStream` 对象调用 `exportXfdf` 方法。以下代码片段展示了如何将数据导出到 XFDF 文件。

```php

    // 打开文档
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 创建一个 FileOutputStream 对象来写入字体文件。
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // 导出数据
    $form->exportFdf($xmlOutputStream);

    // 关闭文件流
    $xmlOutputStream->close();

    // 关闭文档
    $form->close();
```

## 从 PDF 文件导出数据到 XFDF

要将 PDF 表单数据导出到 XFDF 文件，我们可以使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类中的 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 方法。

为了将数据导出到XFDF，您需要创建一个`Form`类的对象，然后使用`OutputStream`对象调用`exportXfdf`方法。
以下代码片段向您展示如何将数据导出到XFDF文件。

```php

    // 打开文档
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 创建一个FileOutputStream对象以写入字体文件。
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // 导出数据
    $form->exportXfdf($xmlOutputStream);

    // 关闭文件流
    $xmlOutputStream->close();

    // 关闭文档
    $form->close();
```