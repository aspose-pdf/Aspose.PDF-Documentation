---
title: Atualizar Dimensões da Página em PHP
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Atualizar Dimensões da Página

Para atualizar as dimensões da página usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **UpdatePageDimensions**.

Código PHP

```php

# Abra o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# obter coleção de páginas
$page_collection = $pdf->getPages();

# obter página específica
$pdf_page = $page_collection->get_Item(1);

# defina o tamanho da página como A4 (11,7 x 8,3 pol.) e no Aspose.PDF, 1 polegada = 72 pontos
# então as dimensões A4 em pontos serão (842,4, 597,6)
$pdf_page->setPageSize(597.6,842.4);

# salvar o arquivo PDF recém-gerado
$pdf->save($dataDir . "output.pdf");

print "Dimensões atualizadas com sucesso!" . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Atualizar Dimensões da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)