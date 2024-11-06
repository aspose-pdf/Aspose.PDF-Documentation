---
title: Recortar Páginas PDF usando PHP
linktitle: Recortar Páginas
type: docs
weight: 80
url: pt/php-java/crop-pages/
description: Você pode obter propriedades da página, como largura, altura, bleed-, crop- e trimbox usando Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Propriedades da Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. O Aspose.PDF para PHP via Java permite que você acesse essas propriedades.

- **Caixa de mídia**: A caixa de mídia é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionada quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento tiver sangria, o PDF também terá uma caixa de sangria.
 Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho ("refilado"), a tinta vá até a borda da página. Mesmo se a página for mal cortada - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.

- **Caixa de corte**: A caixa de corte indica o tamanho final de um documento após a impressão e o corte.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Caixa de corte**: A caixa de corte é o tamanho da "página" no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites da Página.
- **Page.Rect**: a interseção (retângulo comumente visível) da MediaBox e DropBox. A imagem abaixo ilustra essas propriedades. Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

O snippet abaixo mostra como cortar a página:

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // Criar novo Retângulo de Caixa
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

Neste exemplo, usamos um arquivo de amostra [aqui](crop_page.pdf). Inicialmente, nossa página parece como mostrado na Figura 1.
![Figura 1. Página Recortada](crop_page.png)

Após a mudança, a página ficará como a Figura 2.
![Figura 2. Página Recortada](crop_page2.png)