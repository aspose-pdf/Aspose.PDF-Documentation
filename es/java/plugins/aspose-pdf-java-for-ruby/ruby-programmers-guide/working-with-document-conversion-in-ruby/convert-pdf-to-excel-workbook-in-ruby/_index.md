---
title: Convertir PDF a libro de Excel en Ruby
linktitle: Convertir PDF a libro de Excel en Ruby
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
description: Comprenda cómo convertir datos PDF en libros de Excel usando Ruby con Aspose.PDF, simplificando la extracción y el análisis de datos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir PDF a libro de Excel



Para convertir un documento PDF a un libro de Excel usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **PdfToExcel**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Convierta PDF a DOC o DOCX (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
