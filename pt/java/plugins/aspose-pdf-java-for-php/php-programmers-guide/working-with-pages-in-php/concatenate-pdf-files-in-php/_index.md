---
title: Concatenar Arquivos PDF em PHP
type: docs
weight: 10
url: pt/java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concatenar Arquivos PDF

Para concatenar arquivos PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **ConcatenatePdfFiles**.

Código PHP

```php

# Abra o documento de destino
$pdf1 = new Document($dataDir . 'input1.pdf');

# Abra o documento de origem
$pdf2 = new Document($dataDir . 'input2.pdf');

# Adicione as páginas do documento de origem ao documento de destino
$pdf1->getPages()->add($pdf2->getPages());

# Salve o arquivo de saída concatenado (o documento de destino)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "O novo documento foi salvo, por favor verifique o arquivo de saída" . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Concatenar Arquivos PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)