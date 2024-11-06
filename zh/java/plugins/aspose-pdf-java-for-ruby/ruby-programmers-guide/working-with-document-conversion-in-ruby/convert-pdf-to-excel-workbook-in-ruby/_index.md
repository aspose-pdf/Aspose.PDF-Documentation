---
title: 将 PDF 转换为 Excel 工作簿在 Ruby 中
type: docs
weight: 40
url: zh/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将 PDF 转换为 Excel 工作簿

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 实例化 ExcelSave 选项对象

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# 保存输出为 XLS 格式

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "文档已成功转换"
```

## 下载运行代码

从以下任一社交编码网站下载 **Convert PDF to DOC or DOCX (Aspose.PDF)**:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)