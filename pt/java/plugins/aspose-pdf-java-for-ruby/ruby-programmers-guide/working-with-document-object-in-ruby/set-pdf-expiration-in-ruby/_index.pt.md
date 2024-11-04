---
title: Definir Expiração de PDF em Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Definir Expiração de PDF

Para definir a expiração de um documento PDF usando **Aspose.PDF Java para Ruby**, basta invocar o módulo **SetExpiration**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('O arquivo está expirado. Você precisa de um novo.');")

doc.setOpenAction(javascript)

# salvar documento atualizado com nova informação

doc.save(data_dir + "set_expiration.pdf")

puts "Informações do documento atualizadas, por favor verifique o arquivo de saída."
```


## Download Running Code

Baixe **Definir Expiração do PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)