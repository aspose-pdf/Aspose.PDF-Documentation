---
title: Adicionar JavaScript em PHP
linktitle: Adicionar JavaScript em PHP
type: docs
weight: 10
url: /pt/java/adding-javascript-in-php/
description: Aprenda como adicionar JavaScript a arquivos PDF usando PHP e Aspose.PDF para melhorar a interatividade do documento.
lastmod: "2026-10-06"
---
## Aspose.PDF - Adicionando JavaScript

Para adicionar JavaScript em Pdf documento usando **Aspose.PDF Java for PHP**, basta invocar a classe **AddJavaScript**.

Código PHP

```php
# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Adding JavaScript at Document Level
# Instantiate JavascriptAction with desried JavaScript statement
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document
$doc->setOpenAction($javaScript);

# Adding JavaScript at Page Level
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Save PDF Document
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Added JavaScript Successfully, please check the output file.";
```

**Baixar Código em Execução**

Baixar **Adicionando JavaScript (Aspose.PDF)** de qualquer um dos sites de colaboração abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
