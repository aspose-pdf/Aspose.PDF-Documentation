---
title: Adicionando JavaScript no PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionando JavaScript

Para adicionar JavaScript em um documento Pdf usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **AddJavaScript**.

Código PHP

```php
# Abra um documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Adicionando JavaScript no Nível do Documento
# Instanciar JavascriptAction com a declaração JavaScript desejada
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Atribuir o objeto JavascriptAction à ação desejada do Documento
$doc->setOpenAction($javaScript);

# Adicionando JavaScript no Nível da Página
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Salvar Documento PDF
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScript adicionado com sucesso, por favor verifique o arquivo de saída.";
```


**Baixar Código em Execução**

Baixe **Adicionando JavaScript (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)