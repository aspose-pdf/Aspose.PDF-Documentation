---
title: Formatação de Texto dentro do PDF 
linktitle: Formatação de Texto dentro do PDF
type: docs
weight: 30
url: pt/java/text-formatting-inside-pdf/
description: Esta página explica como formatar texto dentro do seu arquivo PDF. Há adição de recuo de linha, adição de borda de texto, adição de sublinhado, adição de uma borda ao redor do texto adicionado, alinhamento de texto para conteúdos de caixa flutuante, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como adicionar Recuo de Linha ao PDF

Aspose.PDF para Java oferece a propriedade SubsequentLinesIndent na classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). Que pode ser usada para especificar o recuo de linha em cenários de geração de PDF com TextFragment e coleção de Parágrafos.

Por favor, use o seguinte trecho de código para usar a propriedade:

```java
public static void AddLineIndentToPDF() {
        // Criar novo objeto de documento
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // Inicializar TextFormattingOptions para o fragmento de texto e especificar
        // valor SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Linha2");
        page.getParagraphs().add(text);

        text = new TextFragment("Linha3");
        page.getParagraphs().add(text);

        text = new TextFragment("Linha4");
        page.getParagraphs().add(text);

        text = new TextFragment("Linha5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## Como adicionar borda ao texto

O trecho de código a seguir mostra como adicionar uma borda a um texto usando TextBuilder e configurando o método DrawTextRectangleBorder de TextState:

```java
public static void AddTextBorder() {
    // Criar novo objeto de documento
    Document pdfDocument = new Document();
    // Obter página específica
    Page pdfPage = pdfDocument.getPages().add();
    // Criar fragmento de texto
    TextFragment textFragment = new TextFragment("texto principal");
    textFragment.setPosition(new Position(100, 600));
    // Definir propriedades do texto
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Usar setStrokingColor para desenhar borda ao redor do retângulo de texto
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Usar o método setDrawTextRectangleBorder para definir o valor como verdadeiro
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Salvar o documento
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## Como adicionar Texto Sublinhado

O trecho de código a seguir mostra como adicionar texto sublinhado ao criar um novo arquivo PDF.

```java
public static void AddUnderlineText(){
    // Criar objeto de documentação
    Document pdfDocument = new Document();
    // Adicionar página ao documento PDF
    Page page = pdfDocument.getPages().add();
    // Criar TextBuilder para a primeira página
    TextBuilder tb = new TextBuilder(page);
    // TextFragment com texto de exemplo
    TextFragment fragment = new TextFragment("Texto com decoração sublinhada");
    // Definir a fonte para TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Definir o formato do texto como Sublinhado
    fragment.getTextState().setUnderline(true);
    // Especificar a posição onde o TextFragment precisa ser colocado
    fragment.setPosition (new Position(10, 800));
    // Anexar TextFragment ao arquivo PDF
    tb.appendText(fragment);

    // Salvar o documento PDF resultante.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## Como adicionar borda ao redor do texto adicionado

Você tem controle sobre a aparência do texto que adiciona. O exemplo abaixo mostra como adicionar uma borda ao redor de um trecho de texto que você adicionou desenhando um retângulo ao seu redor. Saiba mais sobre a classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Salvar o documento PDF resultante.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## Como adicionar quebra de linha

TextFragment não suporta quebra de linha dentro do texto.
 No entanto, para adicionar texto com quebra de linha, use TextFragment com TextParagraph:

- use "\r\n" ou Environment.NewLine em TextFragment em vez de um único “\n”;
- crie um objeto TextParagraph. Ele adicionará texto com divisão de linha;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.
Por favor, use o trecho de código abaixo.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Inicialize um novo TextFragment com texto que contém os marcadores de nova linha necessários
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Defina as propriedades do fragmento de texto, se necessário
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Crie um objeto TextParagraph
    TextParagraph par = new TextParagraph();

    // Adicione o novo TextFragment ao parágrafo
    par.appendLine(textFragment);

    // Defina a posição do parágrafo
    par.setPosition (new Position(100, 600));

    // Crie um objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Adicione o TextParagraph usando o TextBuilder
    textBuilder.appendParagraph(par);

    // Salve o documento PDF resultante.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## Como adicionar Texto Tachado

A classe TextState fornece as capacidades para definir formatação para TextFragments sendo colocados dentro de um documento PDF. Você pode usar esta classe para definir formatação de texto como Negrito, Itálico, Sublinhado e, a partir desta versão, a API forneceu as capacidades para marcar a formatação de texto como Tachado. Por favor, tente usar o seguinte trecho de código para adicionar TextFragment com formatação Tachada.

Por favor, use o trecho de código completo:

```java
public static void AddStrikeOutText(){
    // Abrir documento
    Document pdfDocument = new Document();
    // Obter página específica
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Criar fragmento de texto
    TextFragment textFragment = new TextFragment("texto principal");
    textFragment.setPosition (new Position(100, 600));

    // Definir propriedades do texto
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // usar método setStrikeOut para habilitar Texto Tachado
    textFragment.getTextState().setStrikeOut(true);
    // Marcar texto como Negrito
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Criar objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Anexar o fragmento de texto à página PDF
    textBuilder.appendText(textFragment);

    // Salvar documento PDF resultante.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## Aplicar Sombreamento Gradiente ao Texto

A formatação de texto foi ainda mais aprimorada na API para cenários de edição de texto e agora você pode adicionar texto com espaço de cor de padrão dentro do documento PDF. A classe com.aspose.pdf.Color foi ainda mais aprimorada com a introdução do novo método `setPatternColorSpace`, que pode ser usado para especificar cores de sombreamento para o texto. Este novo método adiciona diferentes Sombreamentos de Gradiente ao texto, por exemplo, Sombreamento Axial, Sombreamento Radial (Tipo 3), conforme mostrado no trecho de código a seguir:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("sempre imprima corretamente");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Criar nova cor com espaço de cor de padrão
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


Para aplicar um Gradiente Radial, você pode usar o método `setPatternColorSpace` igual a `GradientRadialShading(startingColor, endingColor)` no trecho de código acima.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("sempre imprimir corretamente");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Criar nova cor com espaço de cor de padrão
    textFragment.getTextState().setForegroundColor(foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## Como alinhar texto ao conteúdo flutuante

O Aspose.PDF suporta a configuração do alinhamento de texto para conteúdos dentro de um elemento Floating Box.
 As propriedades de alinhamento da instância Aspose.Pdf.FloatingBox podem ser usadas para alcançar isso, como mostrado no exemplo de código a seguir.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom); // Configura o alinhamento vertical para baixo
    floatBox.setHorizontalAlignment(HorizontalAlignment.Right); // Configura o alinhamento horizontal para a direita
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue())); // Configura a borda para todas as laterais com a cor azul
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center); // Configura o alinhamento vertical para o centro
    floatBox1.setHorizontalAlignment(HorizontalAlignment.Right); // Configura o alinhamento horizontal para a direita
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder(new BorderInfo(BorderSide.All, Color.getBlue())); // Configura a borda para todas as laterais com a cor azul
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top); // Configura o alinhamento vertical para o topo
    floatBox2.setHorizontalAlignment(HorizontalAlignment.Right); // Configura o alinhamento horizontal para a direita
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue())); // Configura a borda para todas as laterais com a cor azul
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```