---
title: Adicionar TOC a um PDF Existente em PHP
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar TOC

Para adicionar TOC em um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **AddToc**.

Código PHP

```php

# Abrir um documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obter acesso à primeira página do arquivo PDF
$toc_page = $doc->getPages()->insert(1);

# Criar objeto para representar as informações do TOC
$toc_info = new TocInfo();
$title = new TextFragment("Índice");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Definir o título para o TOC
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Criar objetos string que serão usados como elementos do TOC
$titles = array("Primeira página", "Segunda página");

$i = 0;
while ($i < 2){

    # Criar objeto Heading
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Especificar a página de destino para o objeto de cabeçalho
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Página de destino
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Coordenada de destino
    $segment2->setText($titles[$i]);

    # Adicionar cabeçalho à página que contém o TOC
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Salvar documento PDF
$doc->save($dataDir . "TOC.pdf");

print "TOC adicionado com sucesso, por favor verifique o arquivo de saída.";

```


**Download Running Code**

Baixar **Adicionar TOC (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)