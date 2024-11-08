---
title: Convertir un PDF en Classeur Excel en Ruby
type: docs
weight: 40
url: /fr/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir un PDF en Classeur Excel

Pour convertir un document PDF en Classeur Excel en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'appeler le module **PdfToExcel**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instancier l'objet ExcelSave Option

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Sauvegarder la sortie au format XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Le document a été converti avec succès"
```

## Télécharger le Code Exécuté

Téléchargez **Convertir PDF en DOC ou DOCX (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)