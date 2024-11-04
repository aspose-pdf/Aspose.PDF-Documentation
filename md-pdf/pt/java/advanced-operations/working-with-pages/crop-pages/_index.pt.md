---
title: Cortar Páginas de PDF programaticamente
linktitle: Cortar Páginas
type: docs
weight: 80
url: /java/crop-pages/
description: Você pode obter propriedades da página, como largura, altura, bleed-, crop- e trimbox usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Propriedades da Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF para Java permite que você acesse essas propriedades.

- **Caixa de mídia**: A caixa de mídia é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento tiver sangria, o PDF também terá uma caixa de sangria.
 Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho ("refilado"), a tinta vá até a borda da página. Mesmo se a página for cortada incorretamente - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Trim box**: A caixa de corte indica o tamanho final de um documento após impressão e corte.
- **Art box**: A caixa de arte é a caixa desenhada em torno do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A caixa de corte é o tamanho da "página" em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites de Página.
- **Page.Rect**: a interseção (retângulo comumente visível) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades. Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

O trecho abaixo mostra como cortar a página:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // Criar um novo Box Retângulo
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Inicialmente, nossa página se parece com a mostrada na Figura 1.
![Figure 1. Página Recortada](crop_page.png)

Após a alteração, a página se parecerá com a Figura 2.
![Figure 2. Página Recortada](crop_page2.png)