---
title: Converter PDF para Pasta de Trabalho Excel em Ruby
linktitle: Converter PDF para Pasta de Trabalho Excel em Ruby
type: docs
weight: 40
url: /pt/java/convert-pdf-to-excel-workbook-in-ruby/
description: Entenda como converter dados de PDF em pastas de trabalho Excel usando Ruby com Aspose.PDF, simplificando a extração e análise de dados.
lastmod: "2026-10-06"
---
## Aspose.PDF - Converter PDF para Pasta de Trabalho Excel

Para converter documento PDF para Pasta de Trabalho Excel usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **PdfToExcel**.

Código Ruby

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

## Baixar Código em Execução

BaixarВ **Converter PDF para DOC ou DOCX (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
