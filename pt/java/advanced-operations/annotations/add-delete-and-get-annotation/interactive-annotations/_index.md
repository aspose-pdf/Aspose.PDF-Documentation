---
title: Anotações interativas usando Java
linktitle: Anotações interativas
type: docs
weight: 60
url: /java/interactive-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de links em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhe com anotações interativas de PDF em Java.
Abstract: Este artigo explica como trabalhar com anotações de links interativos em arquivos PDF usando Aspose.PDF para Java. Abrange a localização de texto, a criação de uma anotação de link na área de texto correspondente, a leitura de anotações de link existentes e a exclusão delas.
---
As anotações interativas nesta seção concentram-se em fluxos de trabalho baseados em links e botões que respondem às ações do usuário dentro de um visualizador de PDF.

## Adicionar uma anotação de link

Use este exemplo quando precisar colocar um link clicável sobre o texto encontrado na página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Localize o fragmento de texto de destino e crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) sobre seu retângulo.
1. Atribua um [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) e salve o documento atualizado.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Obtenha anotações de link

Este exemplo verifica a coleção de anotações de página e relata a localização de cada anotação de link.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações na página de destino.
1. Filtre as anotações por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` e imprima seus retângulos.

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Excluir anotações de link

Use esta abordagem quando as anotações de link existentes precisarem ser removidas da página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Colete anotações cujo tipo seja [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Exclua as anotações coletadas e salve o arquivo de saída.

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma anotação de linha

Este exemplo cria uma anotação de linha interativa com estilos de seta, configurações de borda e uma nota pop-up.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie uma [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) com pontos inicial e final.
1. Configure sua aparência e anotação pop-up e salve o documento.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Adicionar botões de navegação

Use este exemplo quando o PDF incluir botões de página anterior e próxima página para navegação interativa.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e certifique-se de que o documento tenha as páginas necessárias.
1. Crie controles [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) com ações de navegação predefinidas.
1. Adicione os botões à coleção de formulários e salve o documento atualizado.

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione um botão de impressão

Este exemplo cria um botão que aciona o comando de impressão quando o usuário clica nele.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) e atribua a ação predefinida de impressão.
1. Configure a borda e o fundo do botão, adicione-o ao formulário e salve o documento.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
