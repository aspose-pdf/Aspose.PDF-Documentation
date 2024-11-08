---
title: Converter arquivo PDF para formato HTML
linktitle: Converter arquivo PDF para formato HTML
type: docs
weight: 50
url: /pt/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter arquivo PDF para formato HTML com a biblioteca Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF para Java oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em formato HTML e salvar as imagens do arquivo PDF em uma pasta específica.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF para Java apresenta a você a aplicação online gratuita ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode experimentar a funcionalidade e a qualidade com que trabalha.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Quando se converte um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Pode acabar sendo muito longa. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML.

## Converter páginas de PDF para HTML

Aspose.PDF para Java oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em formato HTML e salvar as imagens do arquivo PDF em uma pasta específica.

O trecho de código a seguir mostra todas as opções possíveis que você pode usar ao converter PDF para HTML.

```java
// Abrir o documento PDF de origem
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// Salvar o arquivo no formato de documento MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## Converter PDF para HTML - Dividindo a Saída em HTML de Múltiplas Páginas

Aspose.PDF para Java suporta o recurso de converter documentos PDF para vários formatos de saída, incluindo HTML.
 No entanto, ao converter arquivos PDF grandes (compostos por várias páginas), pode haver a necessidade de salvar cada página PDF individual em um arquivo HTML separado.

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Pode acabar ficando muito longa. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML. Tente usar o seguinte trecho de código.

```java
// Abra o documento PDF de origem
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// Instanciar objeto HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar para dividir a saída em várias páginas
htmlOptions.setSplitIntoPages(true);

// Salvar o documento
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## Converter PDF para HTML - Evitar Salvar Imagens no Formato SVG

O formato de saída padrão para salvar imagens ao converter de PDF para HTML é SVG. Durante a conversão, algumas imagens de PDF são transformadas em imagens vetoriais SVG. Isso pode ser lento. Em vez disso, as imagens podem ser transformadas em PNG. Para permitir isso, o Aspose.PDF tem a opção de usar SVG para vetores ou criar PNGs.

Para remover completamente a renderização de imagens no formato SVG ao converter arquivos PDF para o formato HTML, tente usar o seguinte trecho de código.

```java
 // Carregar o arquivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instanciar objeto de opções de salvamento HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Especificar a pasta onde as imagens SVG são salvas durante a conversão de PDF para HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// Salvar o arquivo de saída
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## Comprimindo Imagens SVG Durante a Conversão

Para comprimir imagens SVG durante a conversão de PDF para HTML, tente usar o seguinte código:

```java
// Carregar o arquivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Criar HtmlSaveOption com o recurso testado
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Comprimir as imagens SVG, se houver
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Converter PDF para HTML - Especificar Pasta de Imagens

Por padrão, ao converter um arquivo PDF para HTML, as imagens no PDF são salvas em uma pasta separada criada no mesmo diretório onde o HTML de saída é criado. Mas às vezes, é necessário especificar uma pasta diferente para salvar as imagens ao gerar arquivos HTML. Para realizar isso, introduzimos o [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions). O método [SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) é usado para especificar a pasta de destino para armazenar imagens.

```java
// Carregar o arquivo PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Especificar a pasta separada para salvar imagens
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Criar Arquivos Subsequentes com Apenas Conteúdo do Corpo

Com o seguinte trecho de código simples, você pode dividir o HTML de saída em páginas. Nas páginas de saída, todos os objetos HTML devem ir exatamente onde estão agora (processamento e saída de fontes, criação e saída de CSS, criação e saída de imagens), exceto que o HTML de saída conterá conteúdos atualmente colocados dentro das tags (agora as tags "body" serão omitidas).

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## Renderização de Texto Transparente

Caso o arquivo PDF de origem/entrada contenha textos transparentes sombreado por imagens de primeiro plano, então pode haver problemas de renderização de texto. Assim, para atender a tais cenários, os métodos `setSaveShadowedTextsAsTransparentTexts` e `setSaveTransparentTexts` podem ser usados.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Instanciar objeto HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// Salvar o documento
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## Renderização de camadas de documentos PDF

Podemos renderizar camadas de documentos PDF em elementos de tipo de camada separados durante a conversão de PDF para HTML:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// Instanciar objeto HTML SaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Especificar para renderizar camadas de documentos PDF separadamente no HTML de saída
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// Salvar o documento
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

A conversão de PDF para HTML é um dos recursos mais populares do Aspose.PDF porque possibilita visualizar o conteúdo de arquivos PDF em várias plataformas sem usar um visualizador de documentos PDF. O HTML de saída está de acordo com os padrões da WWW e pode ser exibido facilmente em todos os navegadores da web. Usando esse recurso, os arquivos PDF podem ser visualizados em dispositivos portáteis porque não é necessário instalar nenhum aplicativo de visualização de PDF, mas pode-se usar um simples navegador da web.

## PDF para HTML - Excluir recursos de fonte

If you intend to exclude all or some font resources during the conversion of PDF to HTML, Aspose.PDF for Java API lets you achieve this with the help of HtmlSaveOptions class. The API offers two options for this purpose.

Se você pretende excluir todos ou alguns recursos de fonte durante a conversão de PDF para HTML, a API do Aspose.PDF para Java permite que você alcance isso com a ajuda da classe HtmlSaveOptions. A API oferece duas opções para este propósito.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - para prevenir a exportação de todas as fontes
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - é para prevenir a exportação de fontes específicas (nomes de fontes a serem especificados sem hash)

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - para prevenir a exportação de todas as fontes
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - é para prevenir a exportação de fontes específicas (nomes de fontes a serem especificados sem hash)

In order to convert PDF to HTML excluding font resources, use the following steps:

Para converter PDF para HTML excluindo recursos de fonte, use os seguintes passos:

1. Define a new object of HtmlSaveOptions class
1. Defina um novo objeto da classe HtmlSaveOptions
2. Define and set the font names to be prevented from exporting in HtmlSaveOptions.ExcludeFontNameList
2. Defina e configure os nomes das fontes a serem prevenidas de exportação em HtmlSaveOptions.ExcludeFontNameList
3. Conver the PDF to HTML using the save method
3. Converta o PDF para HTML usando o método save

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```