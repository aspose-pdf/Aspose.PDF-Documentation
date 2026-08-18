---
title: Adicionando JavaScript em PHP
linktitle: Adicionando JavaScript em PHP
type: docs
weight: 10
url: /java/adding-javascript-in-php/
description: Aprenda como adicionar JavaScript a arquivos PDF usando PHP e Aspose.PDF para melhorar a interatividade do documento.
lastmod: "2026-06-09"
---
## Aspose.PDF - Adicionando JavaScript

Para adicionar JavaScript em um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **AddJavaScript**.

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

**Baixar código em execução**

Baixe **Adicionando JavaScript (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
