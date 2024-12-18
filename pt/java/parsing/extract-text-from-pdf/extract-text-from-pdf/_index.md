---
title: Extraindo texto bruto de arquivo PDF 
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: /pt/java/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando o Aspose.PDF para Java. De páginas inteiras, de uma parte específica, com base em colunas, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é um requisito comum. Neste exemplo, você verá como o Aspose.PDF para Java permite extrair texto de todas as páginas de um documento PDF.
Para extrair texto de todas as páginas do PDF:

1. Crie um objeto da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abra o PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e chame o método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. A classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorve o texto do documento e retorna na propriedade **Text**.

O trecho de código a seguir mostra como extrair texto de todas as páginas de um documento PDF.

```java
public static void ExtractFromAllPages(){
    // O caminho para o diretório dos documentos.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Abrir documento
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Criar objeto TextAbsorber para extrair texto
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // Aceitar o absorvedor para todas as páginas
    pdfDocument.getPages().accept(textAbsorber);
    
    // Obter o texto extraído
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // Escrever uma linha de texto no arquivo
        writer.write(extractedText);            
        // Fechar o fluxo
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## Extrair Texto de Páginas usando Text Device

Você pode usar a classe **TextDevice** para extrair texto de um arquivo PDF. TextDevice usa [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) em sua implementação, portanto, na verdade, eles fazem a mesma coisa, mas TextDevice foi implementado apenas para unificar a abordagem "Device" para extrair qualquer coisa da página, como ImageDevice, PageDevice, etc. TextAbsorber pode extrair texto de Página, PDF inteiro ou XForm, este TextAbsorber é mais universal.

### Extrair texto de todas as páginas

Os seguintes passos e trecho de código mostram como extrair texto de um PDF usando o dispositivo de texto.

1. Crie um objeto da classe Document com o arquivo PDF de entrada especificado.
1. Crie um objeto da classe TextDevice.
1. Use o objeto da classe TextExtractOptions para especificar as opções de extração.
1. Use o método Process da classe TextDevice para converter o conteúdo em texto.
1. Salve o texto no arquivo de saída.

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // abrir documento
    Document pdfDocument = new Document("input.pdf");
    // arquivo de texto no qual o texto extraído será salvo
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // iterar através de todas as páginas do arquivo PDF
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // criar dispositivo de texto
        TextDevice textDevice = new TextDevice();
        // definir opções de extração de texto - definir modo de extração de texto (Raw ou
        // Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // obter o texto das páginas do PDF e salvá-lo no objeto OutputStream
        textDevice.process(page, text_stream);
    }
    // fechar objeto stream
    text_stream.close();
}
```


## Extrair Texto de uma região específica da página

A classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) fornece a capacidade de extrair texto de uma página específica ou de todas as páginas de um documento PDF. Esta classe retorna o texto extraído na propriedade **Text**. No entanto, se tivermos a necessidade de extrair texto de uma região específica da página, podemos usar a propriedade **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). A propriedade Rectangle aceita um objeto Rectangle como valor e, usando esta propriedade, podemos especificar a região da página da qual precisamos extrair o texto.

O método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de uma página é chamado para extrair o texto.
 Crie objetos das classes [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Chame o método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) na página individual, como **Page** Index, do objeto **Document**. O **Index** é o número específico da página de onde o texto precisa ser extraído. Você pode obter o texto da propriedade **Text** da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). O trecho de código a seguir mostra como extrair texto de uma página individual.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // abrir documento
    Document doc = new Document("page_0001.pdf");
    // criar objeto TextAbsorber para extrair texto
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // aceitar o absorvedor para a primeira página
    doc.getPages().get_Item(1).accept(absorber);
    // obter o texto extraído
    String extractedText = absorber.getText();
    // criar um escritor e abrir o arquivo
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // escrever conteúdo extraído
    writer.write(extractedText);
    // fechar escritor
    writer.close();
}
```

## Extrair texto com base em colunas

Um arquivo PDF pode ser composto de elementos como Texto, Imagem, Anotações, Anexos, Gráficos, etc., e o Aspose.PDF para .NET oferece a funcionalidade de adicionar e manipular todos esses elementos. Esta API é notável quando se trata de adição e extração de texto de um documento PDF, e podemos nos deparar com um cenário em que um documento PDF é composto por mais de uma coluna (documento PDF de várias colunas) e precisamos extrair o conteúdo da página mantendo o mesmo layout, então o Aspose.PDF para .NET é a escolha certa para atender a essa necessidade. Uma abordagem é reduzir o tamanho da fonte do conteúdo dentro do documento PDF e, em seguida, realizar a extração de texto. O trecho de código a seguir mostra as etapas para reduzir o tamanho do texto e, em seguida, tentar extrair texto do documento PDF.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // abrir documento
    Document doc = new Document("page_0001.pdf");
    // criar objeto TextAbsorber para extrair texto
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // aceitar o absorvedor para a primeira página
    doc.getPages().get_Item(1).accept(absorber);
    // obter o texto extraído
    String extractedText = absorber.getText();
    // criar um escritor e abrir o arquivo
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // escrever conteúdo extraído
    writer.write(extractedText);
    // fechar escritor
    writer.close();
}
```


### Segunda abordagem - Usando ScaleFactor

Nesta nova versão, também introduzimos várias melhorias no TextAbsorber e no mecanismo interno de formatação de texto. Então, agora durante a extração de texto usando o modo ‘Pure’, você pode especificar a opção ScaleFactor e pode ser outra abordagem para extrair texto de um documento PDF de várias colunas além da abordagem mencionada acima. Este fator de escala pode ser ajustado para ajustar a grade que é usada para o mecanismo interno de formatação de texto durante a extração de texto. Especificar os valores de ScaleFactor entre 1 e 0.1 (incluindo 0.1) tem o mesmo efeito que a redução de fonte.

Especificar os valores de ScaleFactor entre 0.1 e -0.1 é tratado como valor zero, mas isso faz com que o algoritmo calcule automaticamente o fator de escala necessário durante a extração de texto. O cálculo é baseado na largura média dos glifos da fonte mais popular na página, mas não podemos garantir que, no texto extraído, nenhuma string de coluna alcance o início da próxima coluna. Observe que, se o valor de ScaleFactor não for especificado, o valor padrão de 1.0 será usado. Isso significa que nenhum redimensionamento será realizado. Se o valor especificado de ScaleFactor for mais do que 10 ou menos do que -0.1, o valor padrão de 1.0 será usado.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width (about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Definir o fator de escala para 0.5 é suficiente para dividir colunas na maioria dos documentos
    // A definição de zero permite que o algoritmo escolha o fator de escala automaticamente
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

Observe que não há correspondência direta entre o novo ScaleFactor e o antigo coeficiente de redução manual de fonte. No entanto, por padrão, o algoritmo leva em consideração o valor do tamanho da fonte que já foi reduzido por algumas razões internas. Por exemplo, reduzir o tamanho da fonte de 10 para 7 tem o mesmo efeito que definir um fator de escala para 5/8 (= 0.625).

{{% /alert %}}

## Extrair Texto Destacado de Documento PDF

Em vários cenários de extração de texto de um documento PDF, você pode ter a necessidade de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair texto destacado de um documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O seguinte trecho de código mostra como você pode extrair texto destacado de um documento PDF.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Loop através de todas as anotações
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Filtrar TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Recuperar fragmentos de texto destacados
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Exibir texto destacado
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## Acessar Elementos de Fragmento de Texto e Segmento de XML

Às vezes, precisamos acessar itens de TextFragment ou TextSegment ao processar documentos PDF gerados a partir de XML. O Aspose.PDF para .NET fornece acesso a esses itens pelo nome. O trecho de código abaixo mostra como usar essa funcionalidade.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```