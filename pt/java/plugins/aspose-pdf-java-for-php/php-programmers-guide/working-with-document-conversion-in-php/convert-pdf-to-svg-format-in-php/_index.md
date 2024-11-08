---
title: Converter PDF para Formato SVG em PHP
type: docs
weight: 30
url: /pt/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para SVG

Para converter PDF para o formato SVG usando **Aspose.PDF Java para PHP**, simplesmente invoque o módulo **PdfToSvg**.

Código PHP

```php

# Abra o documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# instanciar um objeto de SvgSaveOptions
$save_options = new SvgSaveOptions();

# não comprimir a imagem SVG para o arquivo Zip
$save_options->CompressOutputToZipArchive = false;

# Salvar a saída no formato XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "Documento foi convertido com sucesso" . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Converter PDF para Formato SVG (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)