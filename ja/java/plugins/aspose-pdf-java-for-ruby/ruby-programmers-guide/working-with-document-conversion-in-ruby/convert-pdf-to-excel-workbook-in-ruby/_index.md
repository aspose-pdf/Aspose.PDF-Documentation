---
title: "Ruby での PDF の Excel ワークブックへの変換"
linktitle: "Ruby での PDF の Excel ワークブックへの変換"
type: docs
weight: 40
url: /ja/java/convert-pdf-to-excel-workbook-in-ruby/
description: "Aspose.PDF を使用して Ruby で PDF データを Excel ワークブックに変換する方法を理解し、データ抽出と分析を簡素化してください。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF から Excel ワークブックへの変換

PDF ドキュメントを Excel ワークブックに変換するには、**Aspose.PDF Java for Ruby** を使用して、**PdfToExcel** モジュールを呼び出してください。

Ruby コード

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

## 実行コードのダウンロード

**Convert PDF to DOC or DOCX (Aspose.PDF)** を、以下に記載されたいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
