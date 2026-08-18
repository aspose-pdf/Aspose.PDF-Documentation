---
title: Trabalhe com operadores PDF em Java
linktitle: Trabalhando com Operadores
type: docs
weight: 90
url: /java/working-with-operators/
description: Aprenda como usar operadores PDF de baixo nível em Java para manipulação de fluxo de conteúdo, posicionamento de imagens, reutilização de XForm e limpeza de gráficos.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use operadores PDF de baixo nível para controle de fluxo de conteúdo em Java
Abstract: Este artigo explica como trabalhar com operadores PDF de baixo nível em Aspose.PDF para Java. Aprenda como posicionar imagens com precisão, desenhar conteúdo XForm reutilizável e remover operadores gráficos de páginas PDF.
---
## Introdução aos operadores PDF e seu uso

Um operador é uma palavra-chave PDF que especifica alguma ação que deve ser executada, como pintar uma forma gráfica na página. Uma palavra-chave de operador se distingue de um objeto nomeado pela ausência de um caractere solidus inicial (2Fh). Os operadores são significativos apenas dentro do fluxo de conteúdo.

Um fluxo de conteúdo é um objeto de fluxo PDF cujos dados consistem em instruções que descrevem os elementos gráficos a serem pintados em uma página. Mais detalhes sobre operadores PDF podem ser encontrados em [especificação PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Use esta página quando precisar de controle direto sobre um fluxo de conteúdo PDF em Java, como colocar uma imagem com matemática de matriz explícita, reutilizar o mesmo gráfico diversas vezes por meio de um XForm ou excluir instruções de desenho de baixo nível de uma página.

## Adicione uma imagem com operadores PDF

Use operadores de baixo nível quando o posicionamento da imagem precisar ser controlado precisamente no nível do fluxo de conteúdo, em vez de por meio de APIs de layout de nível superior.

1. Abra o PDF de origem com [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e obtenha a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Adicione o fluxo de imagem de entrada aos recursos da página e mantenha o nome do recurso retornado.
1. Crie um [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) que defina a área alvo e construa uma [Matriz](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) a partir de seus limites.
1. Use [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) para preservar o estado gráfico atual, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) para posicionar a imagem, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) para pintá-la e [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) para restaurar o estado anterior.
1. Salve o documento PDF atualizado.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## Desenhe conteúdo XForm reutilizável em uma página

Use esta abordagem quando a mesma imagem ou gráfico precisar ser renderizado mais de uma vez sem duplicar o recurso no arquivo PDF.

1. Abra o PDF de origem com [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), obtenha a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino e acesse seu [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Envolva o conteúdo da página existente com [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) e [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) para que transformações posteriores não vazem para o fluxo de conteúdo original.
1. Crie um recurso [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/), adicione a imagem aos recursos do formulário e use [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) mais [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) para desenhar a imagem dentro do formulário.
1. Coloque o mesmo formulário em coordenadas de múltiplas páginas adicionando uma matriz de tradução e executando o nome do formulário com o operador `Do`.
1. Restaure o estado dos gráficos e salve o PDF de saída.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## Remover operadores gráficos de uma página

Use este exemplo quando uma página contém operadores de desenho vetorial que devem ser removidos diretamente do fluxo de conteúdo.

1. Abra o PDF de origem com [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e obtenha a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Itere pelos operadores de conteúdo da página e colete instâncias de [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) e [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Exclua os operadores coletados do conteúdo da página e salve o PDF atualizado.

Esta técnica remove apenas as instruções de desenho direcionadas. Se a página também contiver rótulos de texto relacionados ou outros operadores não gráficos, esses itens permanecerão no fluxo de conteúdo e poderão precisar de uma etapa de limpeza separada.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## Tópicos Relacionados

- [Operações avançadas de PDF em Java](/pdf/java/advanced-operations/)
- [Trabalhar com imagens em PDF usando Java](/pdf/java/working-with-images/)
- [Trabalhar com páginas PDF em Java](/pdf/java/working-with-pages/)
- [Trabalhar com gráficos vetoriais em Java](/pdf/java/working-with-vector-graphics/)
