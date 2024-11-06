---
title: PDFをExcelワークブックに変換するRuby
type: docs
weight: 40
url: ja/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをExcelワークブックに変換

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントをExcelワークブックに変換するには、単に**PdfToExcel**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 変換対象のドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# ExcelSave Optionオブジェクトをインスタンス化

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# 出力をXLS形式で保存

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "ドキュメントが正常に変換されました"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Convert PDF to DOC or DOCX (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)