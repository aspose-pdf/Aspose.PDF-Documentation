---
title: Establecer la caducidad de PDF en Ruby
linktitle: Establecer la caducidad de PDF en Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: Implemente fechas de vencimiento en archivos PDF utilizando Aspose.PDF para Ruby para documentos urgentes.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Establecer la caducidad del PDF



Para establecer la caducidad de un documento PDF utilizando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SetExpiration**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## 
Descargar código de ejecución



Descargue **Establecer caducidad de PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
