---
title: Crear un PDF complejo
linktitle: Crear un PDF complejo
type: docs
weight: 30
url: /es/java/complex-pdf-example/
description: Aspose.PDF for Java permite crear documentos PDF más complejos que contienen imágenes, fragmentos de texto y tablas en un solo archivo.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un PDF complejo usando Java
Abstract: Este artículo muestra cómo crear un PDF más complejo en Java usando Aspose.PDF. El ejemplo agrega una imagen, un encabezado formateado, un bloque de texto descriptivo y una tabla con celdas de encabezado con estilo y filas de agenda generadas, luego guarda el resultado como un documento PDF.
---
El [Hola Mundo](/pdf/es/java/hello-world-example/) el ejemplo cubre la ruta de creación de PDF más simple. Este ejemplo se basa en ese flujo de trabajo y crea un documento más rico que combina gráficos, texto y contenido tabular.

Para crear un documento PDF más complejo en Java:

1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Agregue una imagen al [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) con `page.addImage(...)` y un objetivo [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Cree un encabezado [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y establezca su fuente, tamaño, alineación y [`Position`](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. Cree un segundo [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) para el párrafo de descripción.
1. Construya un [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) con bordes, relleno y estilo de encabezado.
1. Agregue filas de horario generadas al [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. Agregue al [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) al [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) párrafos.
1. Guarde el PDF de salida [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

El siguiente código Java se basa en `GetStartedExamples.java`.

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

El mismo ejemplo usa un método auxiliar para preparar la tabla de horarios con formato de encabezado y tiempos de salida generados:

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
