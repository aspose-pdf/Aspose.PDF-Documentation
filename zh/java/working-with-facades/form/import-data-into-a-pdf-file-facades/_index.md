---
title: 将数据导入到PDF文件 - 外观
type: docs
weight: 10
url: zh/java/import-data-into-a-pdf-file-facades/
description: 本节解释了如何使用Aspose.PDF外观和Form类从PDF文件导入数据到XML。
lastmod: "2021-06-05"
---

## 从XML导入数据到PDF文件（外观）

[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类允许您使用 importXml 方法从XML文件导入数据到PDF文件。为了从XML导入数据，您需要创建一个Form类的对象，然后使用FileInputStream对象调用importXml方法。最后，您可以使用Form类的save方法保存PDF文件。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromXmlInToPdf.java" >}}

## 从FDF导入数据到PDF文件（外观）

Form类允许您使用importFdf方法从FDF文件导入数据到PDF文件。
 为了从FDF导入数据，你需要创建一个Form类的对象，然后使用FileInputStream对象调用importFdf方法。最后，你可以使用Form类的save方法保存PDF文件。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromFDFIntoPDF.java" >}}

## 从XFDF导入数据到PDF文件（外观）

Form类允许你使用importXfdf方法从XFDF文件导入数据到PDF文件。为了从XFDF导入数据，你需要创建一个Form类的对象，然后使用FileInputStream对象调用importXfdf方法。最后，你可以使用Form类的save方法保存PDF文件。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromXFDFInToPDF.java" >}}