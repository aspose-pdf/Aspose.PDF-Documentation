---
title: 在 Ruby 中将 PDF 转换为 Excel 工作簿
linktitle: 在 Ruby 中将 PDF 转换为 Excel 工作簿
type: docs
weight: 40
url: /zh/java/convert-pdf-to-excel-workbook-in-ruby/
description: 了解如何使用 Ruby 与 Aspose.PDF 将 PDF 数据转换为 Excel 工作簿，从而简化数据提取和分析。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 PDF 转换为 Excel 工作簿

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instantiate ExcelSave Option object

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Save the output to XLS format

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Document has been converted successfully"
```

## 下载运行代码

下载В **Convert PDF to DOC or DOCX (Aspose.PDF)**В 来自В 以下提到的任何社交代码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
