---
title: Integrar tabelas PDF com fontes de dados em Java
linktitle: Integrar tabela
type: docs
weight: 30
url: /pt/java/integrate-table/
description: Aprenda como integrar tabelas PDF com fontes de dados estruturadas, como arquivos CSV, em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar tabelas PDF a partir de dados estruturados com Java
Abstract: Este artigo explica como integrar tabelas PDF com dados externos usando Aspose.PDF for Java. Ele cobre a leitura de dados CSV, a seleção de colunas específicas, a construção de um objeto Table estilizado a partir das linhas analisadas e a renderização do resultado em um documento PDF.
---
O exemplo em Java cria tabelas PDF a partir de dados CSV sem depender de bibliotecas externas de dataframes.

## Criar uma tabela a partir de linhas CSV

Use este exemplo quando colunas CSV selecionadas devem ser transformadas em uma tabela PDF estilizada.

1. Crie um [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) e configure suas bordas.
1. Detecte os índices de coluna necessários a partir da linha de cabeçalho CSV.
1. Adicione a linha de cabeçalho e o número solicitado de linhas de dados, então retorne a tabela.

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

## Criar um PDF a partir de dados CSV

Use este exemplo quando a entrada CSV deve ser renderizada como um documento de tabela PDF.

1. Leia as linhas CSV do arquivo de entrada.
1. Visualize um subconjunto das linhas analisadas no console.
1. Crie um PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), adicione a tabela gerada, e salve o arquivo de saída.

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

## Encontrar índices de colunas CSV por nome

Use este auxiliar quando colunas nomeadas específicas precisam ser localizadas na linha de cabeçalho do CSV.

1. Itere pelos nomes de coluna solicitados.
1. Pesquise a linha de cabeçalho em busca de índices correspondentes.
1. Retorne as posições de coluna coletadas.

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

Use este auxiliar quando a fonte CSV deve ser carregada na memória antes da geração da tabela.

1. Leia todas as linhas do arquivo de entrada.
1. Divida cada linha com o auxiliar de analisador CSV.
1. Retorne os valores de linha coletados.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Dividir uma linha CSV em valores

Use este helper quando uma linha CSV pode conter valores entre aspas e caracteres de aspas escapados.

1. Itere pelos caracteres na linha.
1. Acompanhe se o analisador está atualmente dentro de texto entre aspas.
1. Construa a lista final de valores e retorne-a como um array.

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
