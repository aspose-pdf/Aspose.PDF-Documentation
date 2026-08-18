---
title: Integre tabelas PDF com fontes de dados em Java
linktitle: Integrar Tabela
type: docs
weight: 30
url: /java/integrate-table/
description: Aprenda como integrar tabelas PDF com fontes de dados estruturados, como arquivos CSV em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie tabelas PDF a partir de dados estruturados com Java
Abstract: Este artigo explica como integrar tabelas PDF com dados externos usando Aspose.PDF para Java. Abrange a leitura de dados CSV, a seleção de colunas específicas, a construção de um objeto Table estilizado a partir das linhas analisadas e a renderização do resultado em um documento PDF.
---
O exemplo Java cria tabelas PDF a partir de dados CSV sem depender de bibliotecas externas de dataframe.

## Construir uma tabela a partir de linhas CSV

Use este exemplo quando colunas CSV selecionadas devem ser transformadas em uma tabela PDF estilizada.

1. Crie uma [Tabela](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) e configure suas bordas.
1. Detecte os índices de coluna necessários na linha do cabeçalho CSV.
1. Adicione a linha do cabeçalho e o número solicitado de linhas de dados e retorne a tabela.

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

## Crie um PDF a partir de dados CSV

Use este exemplo quando a entrada CSV precisar ser renderizada como um documento de tabela PDF.

1. Leia as linhas CSV do arquivo de entrada.
1. Visualize um subconjunto das linhas analisadas no console.
1. Crie um [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), adicione a tabela gerada e salve o arquivo de saída.

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

## Encontre índices de colunas CSV por nome

Use este auxiliar quando colunas nomeadas específicas precisarem estar localizadas na linha do cabeçalho CSV.

1. Itere pelos nomes das colunas solicitadas.
1. Pesquise na linha do cabeçalho os índices correspondentes.
1. Retorne as posições das colunas coletadas.

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

## Ler linhas CSV de um arquivo

Use este auxiliar quando a fonte CSV precisar ser carregada na memória antes da geração da tabela.

1. Leia todas as linhas do arquivo de entrada.
1. Divida cada linha com o auxiliar do analisador CSV.
1. Retorne os valores das linhas coletadas.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Divida uma linha CSV em valores

Use este auxiliar quando uma linha CSV puder conter valores entre aspas e caracteres de aspas com escape.

1. Itere pelos caracteres da linha.
1. Acompanhe se o analisador está atualmente dentro do texto citado.
1. Construa a lista de valores finais e retorne-a como um array.

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
