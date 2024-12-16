---
title: Converter arquivo SVG para formato PDF em PHP
type: docs
weight: 40
url: /pt/java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter SVG para PDF

Para converter arquivo SVG para formato PDF usando **Aspose.PDF Java para PHP**, basta invocar o módulo **SvgToPdf**.

Código PHP

```php
# Instanciar objeto LoadOption usando opção de carga SVG
$options = new SvgLoadOptions();

# Criar objeto de documento
$pdf = new Document($dataDir . 'Example.svg', $options);

# Salvar a saída no formato XLS
$pdf->save($dataDir . "SVG.pdf");

print "Documento foi convertido com sucesso";

```

**Baixar Código em Execução**

Baixe **Converter SVG para PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)