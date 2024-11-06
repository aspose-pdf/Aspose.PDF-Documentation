---
title: Converter PDF para formato DOC ou DOCX em PHP
type: docs
weight: 10
url: pt/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para DOC ou DOCX

Para converter um documento PDF para o formato DOC ou DOCX usando **Aspose.PDF Java for PHP**, basta invocar o módulo **PdfToDoc**.

Código PHP

```php

# Abra o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# Salve o arquivo de saída concatenado (o documento alvo)
$pdf->save($dataDir . "output.doc");

print "Documento foi convertido com sucesso";

```

**Baixar Código em Execução**

Baixar **Converter PDF para DOC ou DOCX (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)