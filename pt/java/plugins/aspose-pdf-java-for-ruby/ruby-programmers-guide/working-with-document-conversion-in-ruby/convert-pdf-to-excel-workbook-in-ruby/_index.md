---
title: Converter PDF para Planilha Excel em Ruby
type: docs
weight: 40
url: pt/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para Planilha Excel

Para converter um documento PDF para uma Planilha Excel usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **PdfToExcel**.

Código Ruby

```java

# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra o documento de destino

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instanciar objeto ExcelSave Option

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Salvar a saída no formato XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Documento foi convertido com sucesso"
```

## Baixar Código em Execução

Baixe **Converter PDF para DOC ou DOCX (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)