---
title: Remover Metadados de PDF em PHP
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Remover Metadados

Para remover Metadados de um documento Pdf usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **RemoveMetadata**.

Código PHP

```php

# Abrir um documento pdf.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# salvar documento atualizado com novas informações
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Metadados removidos com sucesso, por favor verifique o arquivo de saída." . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Remover Metadados (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)