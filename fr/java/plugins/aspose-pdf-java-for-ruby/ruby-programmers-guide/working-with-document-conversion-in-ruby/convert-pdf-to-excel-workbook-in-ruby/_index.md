---
title: Convertir un PDF en classeur Excel dans Ruby
linktitle: Convertir un PDF en classeur Excel dans Ruby
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
description: Comprenez comment convertir des données PDF en classeurs Excel à l'aide de Ruby avec Aspose.PDF, simplifiant ainsi l'extraction et l'analyse des données.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir un PDF en classeur Excel



Pour convertir un document PDF en classeur Excel à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **PdfToExcel**.

Code Rubis


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
Télécharger le code d'exécution



Téléchargez** Convertir un PDF en DOC ou DOCX (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
