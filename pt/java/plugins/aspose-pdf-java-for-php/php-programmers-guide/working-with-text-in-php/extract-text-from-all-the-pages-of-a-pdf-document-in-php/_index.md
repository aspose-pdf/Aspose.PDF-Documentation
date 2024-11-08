---
title: Extrair Texto de Todas as Páginas de um Documento PDF em PHP
type: docs
weight: 30
url: /pt/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extrair Texto de Todas as Páginas

Para extrair texto de todas as páginas de um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar o módulo **ExtractTextFromAllPages**.
Código PHP

```php

# Abra o documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# criar objeto TextAbsorber para extrair texto
$text_absorber = new TextAbsorber();

# aceitar o absorvedor para todas as páginas
$pdf->getPages()->accept($text_absorber);

# Para extrair texto de uma página específica do documento, precisamos especificar a página em particular usando seu índice contra o método accept(..).
# aceitar o absorvedor para uma determinada página PDF
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obter o texto extraído
$extracted_text = $text_absorber->getText();

# criar um escritor e abrir o arquivo
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# escrever uma linha de texto no arquivo
# tw.WriteLine(extractedText);
# fechar o fluxo
$writer->close();

print "Texto extraído com sucesso. Verifique o arquivo de saída." . PHP_EOL;

```


**Baixar Código em Execução**

Baixar **Extrair Texto de Todas as Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)