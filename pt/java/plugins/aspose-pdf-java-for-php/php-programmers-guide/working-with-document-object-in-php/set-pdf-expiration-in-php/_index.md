---
title: Definir Expiração de PDF em PHP
type: docs
weight: 80
url: /pt/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Definir Expiração de PDF

Para definir a expiração de um documento PDF usando **Aspose.PDF Java for PHP**, simplesmente invoque a classe **SetExpiration**.

Código PHP

```php

# Abra um documento PDF.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('O arquivo está expirado. Você precisa de um novo.');");
$doc->setOpenAction($javascript);

# salvar documento atualizado com novas informações
$doc->save($dataDir . "set_expiration.pdf");

print "Informações do documento atualizadas, por favor, verifique o arquivo de saída." . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Definir Expiração de PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)