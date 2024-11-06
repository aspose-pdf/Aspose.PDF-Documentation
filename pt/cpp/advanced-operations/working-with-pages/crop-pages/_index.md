---
title: Recortar Páginas de PDF programaticamente C++
linktitle: Recortar Páginas
type: docs
weight: 80
url: pt/cpp/crop-pages/
description: Você pode obter propriedades da página, como largura, altura, bleed-, crop- e trimbox usando Aspose.PDF para C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Propriedades da Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. O Aspose.PDF permite que você acesse essas propriedades.

- **Caixa de mídia**: A caixa de mídia é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento tiver sangria, o PDF também terá uma caixa de sangria. Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho ("aparado"), a tinta vá até a borda da página. Mesmo que a página seja mal aparada - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.

- **Caixa de corte**: A caixa de corte indica o tamanho final de um documento após a impressão e o corte.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outros aplicativos.
- **Caixa de recorte**: A caixa de recorte é o tamanho da "página" em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de recorte é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Page Boundaries.
- **Page.Rect**: a interseção (retângulo comumente visível) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.  
Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

O trecho abaixo mostra como cortar a página:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Abrir documento de origem
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Criar novo Retângulo de Caixa
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

Após a alteração, a página ficará como a Figura 2.  
![Figure 2. Cropped Page](crop_page2.png)