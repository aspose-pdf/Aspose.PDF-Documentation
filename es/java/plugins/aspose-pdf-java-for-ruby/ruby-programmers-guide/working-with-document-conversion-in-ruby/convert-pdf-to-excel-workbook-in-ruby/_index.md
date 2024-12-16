---
title: Convertir PDF a Libro de Excel en Ruby
type: docs
weight: 40
url: /es/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a Libro de Excel

Para convertir un documento PDF a un Libro de Excel usando **Aspose.PDF Java para Ruby**, simplemente invoca el módulo **PdfToExcel**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abre el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instanciar objeto de opción de guardado de Excel

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Guardar la salida en formato XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "El documento ha sido convertido exitosamente"
```

## Descargar Código en Ejecución

Descargar **Convertir PDF a DOC o DOCX (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)