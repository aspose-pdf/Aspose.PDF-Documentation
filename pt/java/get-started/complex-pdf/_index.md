---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
weight: 30
url: /java/complex-pdf-example/
description: Aspose.PDF para Java permite criar documentos PDF mais complexos que contêm imagens, fragmentos de texto e tabelas em um arquivo.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie um PDF complexo usando Java
Abstract: Este artigo mostra como criar um PDF mais complexo em Java usando Aspose.PDF. O exemplo adiciona uma imagem, um título formatado, um bloco de texto descritivo e uma tabela com células de cabeçalho estilizadas e linhas de tabela geradas e, em seguida, salva o resultado como um documento PDF.
---
O [Olá mundo](/pdf/pt/java/hello-world-example/) exemplo cobre o caminho mais simples de criação de PDF. Este exemplo baseia-se nesse fluxo de trabalho e cria um documento mais rico que combina gráficos, texto e conteúdo tabular.

Para criar um documento PDF mais complexo em Java:

1. Crie um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Adicione uma imagem ao [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) com `page.addImage(...)` e um alvo [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Crie um cabeçalho [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e defina sua fonte, tamanho, alinhamento e [Posição](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. Crie um segundo [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) para o parágrafo de descrição.
1. Construa um [Mesa](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) com bordas, preenchimento e estilo de cabeçalho.
1. Adicione linhas de agendamento geradas ao [Mesa](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. Anexe o [Mesa](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) para o [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) parágrafos.
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

O seguinte código Java é baseado em `GetStartedExamples.java`.

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

O mesmo exemplo usa um método auxiliar para preparar a tabela de horários com formatação de cabeçalho e horários de partida gerados:

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
