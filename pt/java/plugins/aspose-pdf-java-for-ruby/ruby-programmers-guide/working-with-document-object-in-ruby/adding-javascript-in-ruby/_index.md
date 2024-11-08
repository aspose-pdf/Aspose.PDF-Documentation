---
title: Adicionando JavaScript em Ruby
type: docs
weight: 10
url: /pt/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionando JavaScript

Para adicionar JavaScript em um documento PDF usando **Aspose.PDF Java para Ruby**, simplesmente invoque o módulo **AddJavaScript**.

Código Ruby

```java
# O caminho para o diretório de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abra um documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adicionando JavaScript no Nível do Documento

# Instanciar JavascriptAction com a declaração JavaScript desejada

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Atribuir objeto JavascriptAction à ação desejada do Documento

doc.setOpenAction(javaScript)

# Adicionando JavaScript no Nível da Página

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('página 2 foi aberta')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('página 2 foi fechada')"))

# Salvar Documento PDF

doc.save(data_dir + "JavaScript-Added.pdf")

puts "JavaScript adicionado com sucesso, por favor verifique o arquivo de saída."
```


## Download Running Code

Baixar **Adicionando JavaScript (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)