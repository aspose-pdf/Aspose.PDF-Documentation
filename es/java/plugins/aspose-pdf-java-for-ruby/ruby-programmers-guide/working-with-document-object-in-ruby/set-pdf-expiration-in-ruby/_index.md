---
title: Establecer expiración de PDF en Ruby
linktitle: Establecer expiración de PDF en Ruby
type: docs
weight: 110
url: /es/java/set-pdf-expiration-in-ruby/
description: Implementar fechas de expiración en PDFs usando Aspose.PDF para Ruby en documentos sensibles al tiempo.
lastmod: "2026-09-03"
---
## Aspose.PDF - Establecer expiración de PDF

Para establecer la expiración deВ  documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **SetExpiration**.

Código Ruby

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

## Descargar código en ejecución

DescargarВ **Set PDF Expiration (Aspose.PDF)**В de В cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
