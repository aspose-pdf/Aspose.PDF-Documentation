---
title: Establecer Expiración de PDF en Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Establecer Expiración de PDF

Para establecer la expiración de un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque el módulo **SetExpiration**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('El archivo está caducado. Necesitas uno nuevo.');")

doc.setOpenAction(javascript)

# guardar documento actualizado con nueva información

doc.save(data_dir + "set_expiration.pdf")

puts "Información del documento actualizada, por favor revise el archivo de salida."
```


## Descargar Código en Ejecución

Descargue **Establecer Expiración de PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)