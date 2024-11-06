---
title: Dividir Arquivo PDF em Páginas Individuais em PHP
type: docs
weight: 80
url: pt/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dividir Páginas

Para dividir um documento PDF em páginas individuais usando **Aspose.PDF Java for PHP**, simplesmente invoque a classe **SplitAllPages**.

Código PHP

```php

# Abrir o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# loop através de todas as páginas
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # criar um novo objeto Document
    $new_document = new Document();

    # obter a página em um índice particular da Coleção de Páginas
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # salvar o arquivo PDF recém-gerado
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Processo de divisão concluído com sucesso!";

```

**Baixar Código em Execução**

Baixe **Dividir Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)