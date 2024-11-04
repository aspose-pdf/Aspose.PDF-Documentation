---
title: Exportar dados do Excel para preencher formulário PDF
type: docs
weight: 10
url: /net/export-excel-worksheet-data-to-fill-pdf-form/
description: Esta seção explica como você pode exportar dados da planilha do Excel para preencher formulário PDF usando a classe AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

O [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no [Aspose.PDF para .NET](/pdf/net/) oferece várias maneiras de preencher os formulários Pdf. Você pode importar dados de arquivo XML, DFD, XFDF, usar API e até mesmo usar os dados da planilha do Excel. Estaríamos utilizando o método [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) da classe [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) do [Aspose.Cells](https://docs.aspose.com//cells/net) para exportar os dados da planilha do Excel para o objeto DataTable. Então, precisamos importar esses dados para o formulário Pdf usando o método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) da classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Certifique-se de que o nome da coluna do DataTable seja o mesmo que o nome do campo no formulário PDF.
{{% /alert %}}

## Detalhes da Implementação

No cenário a seguir, vamos usar um formulário PDF, que contém três campos de formulário chamados ID, Nome e Gênero.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

No formulário especificado acima, há uma página, com três campos nomeados como "ID", "Nome" e "Gênero", respectivamente. Estaremos extraindo os dados da planilha do excel a seguir para o objeto DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Precisamos criar um objeto da classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) e vincular o formulário Pdf presente nas imagens acima e usar o método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) para preencher os campos do formulário usando os dados presentes no objeto DataTable.Uma vez que o método é chamado, um novo arquivo de formulário Pdf é gerado, que contém cinco páginas com o formulário preenchido com base nos dados da planilha Excel. O formulário Pdf de entrada era de uma única página e o resultante tem cinco páginas, porque o número de linhas de dados na planilha Excel é 5. A classe DataTable oferece a capacidade de usar a primeira linha da planilha como ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// Criando um fluxo de arquivo contendo o arquivo Excel a ser aberto
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Abrindo o arquivo Excel através do fluxo de arquivo
workbook.Open(fstream);
// Acessando a primeira planilha no arquivo Excel
Worksheet worksheet = workbook.Worksheets[0];
// Exportando o conteúdo de 7 linhas e 2 colunas começando da 1ª célula para o DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Fechando o fluxo de arquivo para liberar todos os recursos
fstream.Close();
// Criar um objeto da classe AutoFiller
AutoFiller autoFiller = new AutoFiller();
// O arquivo pdf de entrada que contém campos de formulário
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// O pdf resultante, que conterá os campos de formulário preenchidos com informações do DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Chamar o método para importar os dados do objeto DataTable para os campos do formulário Pdf.
autoFiller.ImportDataTable(dataTable);
// Chamar o método de salvar para gerar o arquivo pdf
autoFiller.Save();
```

Para preenchimento a partir de XLSX, por favor, use o próximo trecho de código:

```csharp
internal static void FillFromXLSX()
        {
            // Cria um objeto da classe AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // O arquivo pdf de entrada que contém campos de formulário
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // Chama o método para importar os dados do objeto DataTable para os campos do formulário PDF.
            autoFiller.ImportDataTable(dataTable);


            // O pdf resultante, que conterá os campos do formulário preenchidos com informações do DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF para .NET permite gerar Tabela de Dados em documento PDF:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // Cria uma nova DataTable.
            System.Data.DataTable table = new DataTable("Students");
            // Declara variáveis para os objetos DataColumn e DataRow.
            DataColumn column;
            DataRow row;

            // Cria uma nova DataColumn, define o DataType,
            // ColumnName e adiciona ao DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // Adiciona a Coluna à DataColumnCollection.
            table.Columns.Add(column);

            // Cria a segunda coluna.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // Adiciona a coluna à tabela.
            table.Columns.Add(column);

            // Torna a coluna ID a coluna de chave primária.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // Cria três novos objetos DataRow e os adiciona
            // ao DataTable
            var rand = new Random();
            for (int i = 1; i <= 4; i++)
            {
                row = table.NewRow();
                row["id"] = i;
                row["First Name"] = names[rand.Next(names.Length)];
                table.Rows.Add(row);
            }
            return table;
        }
```

## Conclusão

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) também oferece a capacidade de preencher formulários PDF usando dados de um banco de dados, mas esse recurso é atualmente suportado na versão .Net.
{{% /alert %}}