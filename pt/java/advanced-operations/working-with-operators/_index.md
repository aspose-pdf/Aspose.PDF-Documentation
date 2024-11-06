---
title: Trabalhando com Operadores
linktitle: Trabalhando com Operadores
type: docs
weight: 170
url: pt/java/operators/
description: Este tópico explica como usar operadores com Aspose.PDF. As classes de operadores fornecem ótimos recursos para manipulação de PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introdução aos Operadores PDF e Seu Uso

Um operador é uma palavra-chave PDF que especifica alguma ação a ser realizada, como pintar uma forma gráfica na página. Uma palavra-chave de operador é diferenciada de um objeto nomeado pela ausência de um caractere de barra inicial (2Fh). Os operadores são significativos apenas dentro do fluxo de conteúdo.

Um fluxo de conteúdo é um objeto de fluxo PDF cujos dados consistem em instruções que descrevem os elementos gráficos a serem pintados em uma página. Mais detalhes sobre os operadores PDF podem ser encontrados na [especificação PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Detalhes da Implementação

Este tópico explica como usar operadores com Aspose.PDF.
 O exemplo selecionado adiciona uma imagem em um arquivo PDF para ilustrar o conceito. Para adicionar uma imagem em um arquivo PDF, diferentes operadores são necessários. Este exemplo usa [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) e [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- O operador [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) salva o estado gráfico atual do PDF.
- Este tópico explica como usar operadores com Aspose.PDF. O exemplo selecionado adiciona uma imagem em um arquivo PDF para ilustrar o conceito. Para adicionar uma imagem em um arquivo PDF, diferentes operadores são necessários. Este exemplo usa [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) e [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore). 
O operador (concatenate matrix) é usado para definir como uma imagem deve ser posicionada na página do PDF.
- O operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) desenha a imagem na página.
- O operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) restaura o estado gráfico.

Para adicionar uma imagem em um arquivo PDF:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abra o documento PDF de entrada.
1. Obtenha a página específica na qual a imagem será adicionada.
1. Adicione a imagem à coleção de Recursos da página.
1. Use os operadores para colocar a imagem na página:
   - Primeiro, use o operador [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) para salvar o estado gráfico atual.
   - Em seguida, use o operador [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) para especificar onde a imagem deve ser colocada.
   - Use o operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) para desenhar a imagem na página.
1. Finalmente, use o operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) para salvar o estado gráfico atualizado.

O trecho de código a seguir mostra como usar os operadores de PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-exemplos/Exemplos/Operadores/";

    public static void AddImageUsingOpeartors() {

        // Cria um novo documento PDF
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Obtenha a página onde a imagem precisa ser adicionada
        Page page = pdfDocument.getPages().get_Item(1);

        // Defina as coordenadas
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Carregar imagem em fluxo
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Bloco de captura gerado automaticamente
            e.printStackTrace();
        }

        // Adicionar imagem à coleção de Imagens dos Recursos da Página
        page.getResources().getImages().add(imageStream);

        // Usando o operador GSave: este operador salva o estado gráfico atual
        page.getContents().add(new GSave());
        // Criar objetos Rectangle e Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem
        // deve ser colocada
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Usando o operador Do: este operador desenha a imagem
        page.getContents().add(new Do(ximage.getName()));
        // Usando o operador GRestore: este operador restaura o estado gráfico
        page.getContents().add(new GRestore());

        // Salvar documento atualizado
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## Desenhar XForm na Página usando Operadores

Este tópico demonstra como usar os operadores GSave/GRestore, o operador ConcatenateMatrix para posicionar um xForm e o operador Do para desenhar um xForm em uma página.

O código abaixo envolve o conteúdo existente de um arquivo PDF com o par de operadores GSave/GRestore. Esta abordagem ajuda a obter o estado gráfico inicial no final dos conteúdos existentes. Sem essa abordagem, transformações indesejáveis podem permanecer no final da cadeia de operadores existente.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // O exemplo demonstra
        // uso dos operadores GSave/GRestore
        // uso do operador ConcatenateMatrix para posicionar xForm
        // uso do operador Do para desenhar xForm na página

        // Envolver conteúdos existentes com o par de operadores GSave/GRestore
        // isso é para obter o estado gráfico inicial no final dos conteúdos existentes
        // caso contrário, podem permanecer algumas transformações indesejáveis no final da
        // cadeia de operadores existente
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Adicionar operador de estado gráfico de salvamento para limpar adequadamente o estado gráfico após
        // novos comandos
        pageContents.add(new GSave());

        // Criar xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Definir largura e altura da imagem
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Carregar imagem no fluxo
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Adicionar imagem à coleção de Imagens dos Recursos XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Usando o operador Do: este operador desenha a imagem
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Colocar o formulário nas coordenadas x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Desenhar formulário com o operador Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Colocar o formulário nas coordenadas x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Desenhar formulário com o operador Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // Restaurar estado gráfico com GRestore após o GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## Remover Objetos Gráficos usando Classes de Operadores

As classes de operadores oferecem grandes recursos para manipulação de PDFs. Quando um arquivo PDF contém gráficos que não podem ser removidos usando o método [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) da classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), as classes de operadores podem ser usadas para removê-los.

O seguinte trecho de código mostra como remover gráficos. Por favor, note que se o arquivo PDF contiver rótulos de texto para os gráficos, eles podem persistir no arquivo PDF, usando esta abordagem. Portanto, pesquise os operadores gráficos para um método alternativo para excluir tais imagens.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // Operadores de pintura de caminho usados
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## Mudando o Espaço de Cor de um Documento PDF

{{% alert color="primary" %}}

Aspose.PDF para Java 9.0.0 suporta a mudança do espaço de cor de um documento PDF. É possível mudar a cor RGB para CMYK e vice-versa.

{{% /alert %}}

Os seguintes métodos foram implementados na classe [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) para permitir que você altere o espaço de cor. Use-o para mudar algumas cores RGB/CMYK específicas para o espaço de cor CMYK/RGB, mantendo o restante do documento PDF como está.

{{% alert color="primary" %}}
**Mudanças na API Pública**
Os seguintes métodos são implementados:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}


O seguinte trecho de código demonstra como mudar o espaço de cor usando Aspose.PDF para Java.

```java
Documento doc = new Documento("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("Valores dos operadores de cor RGB no documento pdf");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // Convertendo cor RGB para CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("Comando não suportado");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// Testando o resultado
System.out.println("Valores dos operadores de cor CMYK convertidos no documento pdf resultante");
doc = new Documento("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```