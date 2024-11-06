---
title: 将XML转换为FDF格式
type: docs
weight: 20
url: zh/net/converting-an-xml-to-fdf-format/
description: 本节说明如何使用FormDataConverter将XML转换为FDF格式。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 命名空间在 [Aspose.PDF for .NET](/pdf/net/) 中对AcroForms的支持非常好。它还支持将表单数据导入和导出到不同的文件格式，如FDF、XFDF和XML。然而，有时开发人员需要将一种格式转换为另一种格式。在本文中，我们将研究允许我们将FDF格式转换为XML的功能。

{{% /alert %}}

## 详情

FDF代表表单数据格式，FDF文件以键/值对的形式包含表单值。 我们也知道，XML 文件将值包含在标签中。通常，键表示为标签名称，值表示为该标签内的值。现在，[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 提供了将 XML 文件格式转换为 FDF 格式的灵活性。

为此，请使用 [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) 类。此类提供了将一种数据格式转换为另一种格式的不同方法。本文展示了如何使用其中一种方法 ConvertXmlToFdf(..)，该方法以 FDF 文件作为输入或源流，并保存为 XML 格式。以下代码片段显示了如何将 FDF 文件转换为 XML 文件。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}