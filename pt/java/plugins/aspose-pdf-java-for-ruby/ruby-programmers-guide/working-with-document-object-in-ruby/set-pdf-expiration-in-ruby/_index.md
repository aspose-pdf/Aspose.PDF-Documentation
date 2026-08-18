---
title: Definir expiração de PDF em Ruby
linktitle: Definir expiração de PDF em Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: Implemente datas de expiração em PDFs usando Aspose.PDF for Ruby para documentos urgentes.
lastmod: "2026-06-09"
---
## Aspose.PDF - Definir expiração do PDF

Para definir a expiração do documento PDF usando **Aspose.PDF Java for Ruby**, basta invocar o módulo **SetExpiration**.

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

## Baixar código em execução

Baixe **Definir expiração de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
