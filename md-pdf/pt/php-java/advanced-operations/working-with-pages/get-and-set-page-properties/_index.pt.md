---
title: Obter e Definir Propriedades da Página
type: docs
weight: 30
url: /php-java/get-and-set-page-properties/
description: Este tópico explica como obter números em um arquivo PDF, obter propriedades de página e determinar a cor da página usando Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
---

Aspose.PDF para PHP via Java permite que você leia e defina propriedades das páginas em um arquivo PDF em suas aplicações Java. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página do PDF, como cor, e definir propriedades de página.

## Obter Número de Páginas no Arquivo PDF

Ao trabalhar com documentos, muitas vezes você deseja saber quantas páginas eles contêm. Com Aspose.PDF isso não leva mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Em seguida, as páginas do documento são recuperadas. É feita uma tentativa de obter a contagem de páginas das páginas recuperadas.

O snippet de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Obter contagem de páginas
    $responseData = $responseData . "Contagem de Páginas : " + $pages->size();
```

### Obter contagem de páginas sem salvar o documento

A menos que o arquivo PDF seja salvo e todos os elementos sejam realmente colocados dentro do arquivo PDF, não podemos obter a contagem de páginas para o documento específico (porque não podemos ter certeza sobre o número de páginas em que todos os elementos serão acomodados). No entanto, a partir do lançamento do Aspose.PDF para PHP via Java, introduzimos um método chamado [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) que fornece a funcionalidade para obter a contagem de páginas para o documento PDF, sem salvar o arquivo. Assim, podemos obter informações de contagem de páginas em tempo real. Tente usar o seguinte trecho de código para realizar essa exigência.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    // adicionar página à coleção de páginas do arquivo PDF
    $page = $document->getPages()->add();
    
    // criar um loop para adicionar 300 instâncias de TextFragment
    for ($i=0; $i < 300; $i++) { 
       // adicionar TextFragment à coleção de parágrafos da primeira página do PDF
       $page->getParagraphs()->add(new TextFragment("Teste de contagem de páginas"));
    }
    
    // processar parágrafos para obter informações de contagem de páginas
    $document->processParagraphs();

    $pages = $document->getPages();

    // Obter contagem de páginas
    $responseData = $responseData . "Contagem de Páginas : " + $pages->size();
```


## Obter Propriedades da Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. O Aspose.PDF permite acessar essas propriedades.

### **Entendendo as Propriedades da Página: a Diferença entre Artbox, BleedBox, CropBox, MediaBox, TrimBox e propriedade Rect**

- **Caixa de mídia**: A caixa de mídia é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do meio em que o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento tiver sangria, o PDF também terá uma caixa de sangria.
 Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho (“refilado”), a tinta vá até a borda da página. Mesmo que a página seja cortada incorretamente - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Caixa de corte**: A caixa de corte indica o tamanho final de um documento após a impressão e o corte.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Caixa de corte**: A caixa de corte é o tamanho da “página” no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat.
  Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites da Página.
- **Page.Rect**: a interseção (retângulo comumente visível) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Acessando Propriedades da Página

O trecho de código a seguir obtém propriedades como ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Número da Página e Rotação para uma página específica no documento. Em seguida, ele armazena os dados extraídos em variáveis separadas e os concatena em uma string de resposta.

1. Crie um novo objeto Document usando a variável $inputFile.
1. Obtenha a coleção de páginas do documento usando o método getPages().
1. Obtenha uma página específica da coleção de páginas usando o método get_Item().
1. Extraia várias propriedades (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Número da Página, Rotação) do objeto de página específico e as armazene em variáveis separadas.
1. O código concatena os valores das propriedades extraídas em strings de resposta separadas ($responseData1, $responseData2, etc.).
1. Em seguida, ele tenta recuperar a contagem de páginas usando o método size() no objeto $pages, mas a variável $pages não está definida.

O trecho de código a seguir mostra como obter propriedades da página.

```php

   // Abrir documento
    $document = new Document($inputFile);

    // Obter a coleção de páginas
    $pageCollection = $document->getPages();

    // Obter uma página específica
    $page = $pageCollection->get_Item(1);

    // Obter as propriedades da página
    $responseData1 = "ArtBox : Altura = " . $page->getArtBox()->getHeight()
        . ", Largura = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Altura = " . $page->getBleedBox()->getHeight() . ", Largura = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Altura = " . $page->getCropBox()->getHeight() . ", Largura = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Altura = " . $page->getMediaBox()->getHeight() . ", Largura = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Altura = " . $page->getTrimBox()->getHeight() . ", Largura = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Altura = " . $page->getRect()->getHeight() . ", Largura = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Número da Página :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotação :-" . $page->getRotate() . PHP_EOL;

    // Obter contagem de páginas
    $responseData8 = $responseData8 . "Contagem de Páginas : " . $pages->size();
```


## Determinar Cor da Página

A classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo que tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - a página usa.

Todas as páginas dos arquivos PDF são contidas pela coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). A propriedade [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) especifica a cor dos elementos na página. Para obter ou determinar as informações de cor para uma página específica do PDF, use a propriedade [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) do objeto da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

O trecho de código a seguir mostra como iterar através de páginas individuais de um arquivo PDF para obter informações de cor.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Iterar através de todas as páginas do arquivo PDF
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Obter as informações do tipo de cor para uma página específica do PDF
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Página # -" . $pageCount . " é Preto e branco..";
                break;
            case 1:
                $responseData ="Página # -" . $pageCount . " está em Escala de Cinza...";
                break;
            case 0:
                $responseData ="Página # -" . $pageCount . " é RGB..";
                break;
            case 3:
                $responseData ="Cor da Página # -" . $pageCount . " é indefinida..";
                break;
        }
    }
```