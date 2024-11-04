---
title: Manipular Documento PDF 
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: /java/manipulate-pdf-document/
description: Este artigo contém informações sobre como validar Documento PDF para o Padrão PDF A, como trabalhar com TOC, como definir a data de expiração do PDF e como determinar o Progresso da geração do arquivo PDF.
lastmod: "2021-06-05"
---

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade com PDF/A-1a ou PDF/A-1b, use o método [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este método permite que você especifique o nome do arquivo em que o resultado deve ser salvo e o tipo de validação necessário, utilizando a enumeração [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A ou PDF_A_1B.

O formato XML de saída é um formato Aspose personalizado.
 O XML contém uma coleção de tags com o nome Problem; cada tag contém os detalhes de um problema específico. O atributo ObjectID da tag Problem representa o ID do objeto específico ao qual este problema está relacionado. O atributo Clause representa uma regra correspondente na especificação do PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Validar PDF para PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Salvar arquivo PDF atualizado
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Trabalhando com TOC

### Adicionar TOC a um PDF Existente

A classe ListSection no pacote aspose.pdf permite que você crie um índice ao criar um documento PDF do zero. Para adicionar cabeçalhos, que são elementos do TOC, use a classe [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

Para adicionar um TOC a um arquivo PDF existente, use a classe [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) no pacote com.aspose.pdf. O pacote com.aspose.pdf pode tanto criar novos arquivos PDF quanto manipular arquivos PDF existentes. Para adicionar um índice a um PDF existente, use o pacote com.aspose.pdf.

O trecho de código a seguir mostra como criar um índice dentro de um arquivo PDF existente.

```java
public static void AddTOCtoExistingPDF() {
    // Carregar um arquivo PDF existente
    Document document = new Document(_dataDir + "sample.pdf");

    // Obter acesso à primeira página do arquivo PDF
    Page tocPage = document.getPages().insert(1);

    // Criar objeto para representar as informações do índice
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Índice");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Definir o título para o índice
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Criar objetos string que serão usados como elementos do índice
    String[] titles = new String[4];
    titles[0] = "Primeira página";
    titles[1] = "Segunda página";
    titles[2] = "Terceira página";
    titles[3] = "Quarta página";
    for (int i = 0; i < 4; i++) {
      // Criar objeto Heading
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Especificar a página de destino para o objeto Heading
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Página de destino
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Coordenada de destino
      segment2.setText(titles[i]);

      // Adicionar heading à página contendo o índice
      tocPage.getParagraphs().add(heading2);
    }
    // Salvar o documento atualizado
    document.save("TOC_Output_Java.pdf");
  }
```
### Definir diferentes TabLeaderType para diferentes Níveis de TOC

Aspose.PDF também permite definir diferentes TabLeaderType para diferentes níveis de TOC. Você precisa definir a propriedade LineDash do FormatArray com o valor apropriado do enum TabLeaderType como a seguir.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // definir LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Índice");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Adicionar a seção de lista à coleção de seções do documento Pdf

    tocPage.setTocInfo(tocInfo);

    // Definir o formato da lista de quatro níveis configurando as margens esquerdas e
    // configurações de formato de texto de cada nível

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Criar uma seção no documento Pdf
    Page page = document.getPages().add();

    // Adicionar quatro cabeçalhos na seção
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Cabeçalho de Exemplo" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Adicionar o cabeçalho no Índice.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // salvar o PDF
    document.save(outFile);
  }
```

### Ocultar Números de Página no TOC

Caso você não queira exibir números de página junto com os títulos no TOC, você pode usar a propriedade [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) da Classe [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) como falso. Por favor, verifique o seguinte trecho de código para ocultar números de página no índice:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Adicionar a seção de lista à coleção de seções do documento Pdf
    tocPage.setTocInfo(tocInfo);

    // Definir o formato da lista de quatro níveis configurando as margens esquerdas e
    // configurações de formato de texto de cada nível

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Adicionar quatro títulos na seção
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("this is heading of level " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### Personalizar Números de Página ao adicionar TOC

É comum personalizar a numeração de páginas no TOC ao adicionar TOC em um documento PDF. Por exemplo, pode ser necessário adicionar algum prefixo antes do número da página, como P1, P2, P3 e assim por diante. Nesse caso, o Aspose.PDF para Java fornece a propriedade PageNumbersPrefix da classe TocInfo que pode ser usada para personalizar os números de página, como mostrado no exemplo de código a seguir.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Carregar um arquivo PDF existente
    Document doc = new Document(inFile);
    // Obter acesso à primeira página do arquivo PDF
    Page tocPage = doc.getPages().insert(1);
    // Criar objeto para representar informações do TOC
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Índice");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Definir o título para o TOC
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Criar objeto Heading
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Especificar a página de destino para o objeto heading
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Página de destino
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Coordenada de destino
      segment2.setText("Página " + i);
      // Adicionar heading à página que contém o TOC
      tocPage.getParagraphs().add(heading2);
    }

    // Salvar o documento atualizado
    doc.save(outFile);
  }
```


## Adicionar Camadas ao Arquivo PDF

Camadas podem ser usadas em documentos PDF de várias maneiras. Você pode ter um arquivo multilíngue que deseja distribuir e quer que o texto em cada idioma apareça em camadas diferentes, com o design de fundo aparecendo em uma camada separada. Você também pode criar documentos com animação que aparece em uma camada separada. Um exemplo poderia ser adicionar um contrato de licença ao seu arquivo, e você não quer que um usuário visualize o conteúdo até que concorde com os termos do contrato.

Aspose.PDF para Java suporta a adição de camadas a arquivos PDF.

Para trabalhar com camadas em arquivos PDF, use os seguintes membros da API.

A classe [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) representa uma camada e contém as seguintes propriedades:

- **Name** – o nome da camada.
- **Id** – o ID da camada.
- **Contents** – uma lista de operadores da camada.

Uma vez que os objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) tenham sido definidos, adicione-os à coleção Layers do objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 O código abaixo mostra como adicionar camadas a um documento PDF.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Linha Vermelha");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Linha Verde");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Linha Azul");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Definir Expiração do PDF

O recurso de expiração do PDF define por quanto tempo um arquivo PDF é válido. Em uma data específica, se alguém tentar acessá-lo, um pop-up é exibido, explicando que o arquivo expirou e que é necessário um novo.

O Aspose.PDF permite definir a expiração ao criar e editar arquivos PDF.

O trecho de código abaixo mostra como definir a data de expiração para um arquivo PDF. Você precisa usar JavaScript, pois arquivos salvos por componentes de terceiros (por exemplo, OwnerGuard) não podem ser visualizados em outras estações de trabalho sem essa utilidade.

O arquivo PDF pode ser criado usando o PDF OwnerGuard com um arquivo existente com uma data de expiração. Mas o novo arquivo pode ser aberto apenas em uma estação de trabalho que tenha o PDF OwnerGuard instalado. Estações de trabalho sem o PDF OwnerGuard darão um erro ExpirationFeatureError. Por exemplo, o PDF Reader abre o arquivo se o OwnerGuard estiver instalado, mas o Adobe Acrobat retorna um erro.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('O arquivo está expirado. Você precisa de um novo.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```