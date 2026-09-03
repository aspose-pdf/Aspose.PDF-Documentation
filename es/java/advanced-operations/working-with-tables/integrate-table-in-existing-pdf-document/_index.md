---
title: Integrar tablas PDF con fuentes de datos en Java
linktitle: Integrar tabla
type: docs
weight: 30
url: /es/java/integrate-table/
description: Aprenda cómo integrar tablas PDF con fuentes de datos estructuradas como archivos CSV en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear tablas PDF a partir de datos estructurados con Java
Abstract: Este artículo explica cómo integrar tablas PDF con datos externos utilizando Aspose.PDF for Java. Cubre la lectura de datos CSV, la selección de columnas específicas, la creación de un objeto Table con estilo a partir de las filas analizadas y la renderización del resultado en un documento PDF.
---
El ejemplo en Java crea tablas PDF a partir de datos CSV sin depender de bibliotecas externas de dataframes.

## Crear una tabla a partir de filas CSV

Utilice este ejemplo cuando las columnas CSV seleccionadas deban transformarse en una tabla PDF con estilo.

1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure sus bordes.
1. Detecte los índices de columna necesarios de la fila de encabezado del CSV.
1. Agrega la fila de encabezado y el número solicitado de filas de datos, luego devuelve la tabla.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## Crear un PDF a partir de datos CSV

Utilice este ejemplo cuando la entrada CSV debe renderizarse como un documento de tabla PDF.

1. Lea las filas CSV del archivo de entrada.
1. Vista previa de un subconjunto de las filas analizadas en la consola.
1. Crear un PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), agrega la tabla generada y guarda el archivo de salida.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## Encontrar índices de columna CSV por nombre

Utilice este asistente cuando sea necesario localizar columnas con nombres específicos en la fila de encabezado del CSV.

1. Itere a través de los nombres de columnas solicitados.
1. Busque en la fila de encabezado los índices coincidentes.
1. Devuelva las posiciones de columna recopiladas.

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## Leer filas CSV de un archivo

Utilice este asistente cuando la fuente CSV debe cargarse en memoria antes de la generación de la tabla.

1. Leer todas las líneas del archivo de entrada.
1. Divide cada línea con el asistente del analizador CSV.
1. Devuelve los valores de fila recopilados.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Dividir una línea CSV en valores

Utilice este asistente cuando una fila CSV pueda contener valores entre comillas y caracteres de comilla escapados.

1. Itere a través de los caracteres en la línea.
1. Rastree si el analizador está actualmente dentro de texto entre comillas.
1. Construya la lista de valores final y devuélvala como una matriz.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
