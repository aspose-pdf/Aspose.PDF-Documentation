---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
weight: 60
url: /pt/net/complex-pdf-example/
description: Aspose.PDF para .NET permite que você crie documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O exemplo [Olá, Mundo](/pdf/pt/net/hello-world-example/) mostrou passos simples para criar um documento PDF usando C# e Aspose.PDF. Neste artigo, vamos examinar a criação de um documento mais complexo com C# e Aspose.PDF para .NET. Como exemplo, pegaremos um documento de uma empresa fictícia que opera serviços de balsa para passageiros.
Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela. Para construir tal documento, usaremos a abordagem baseada em DOM. Você pode ler mais na seção [Fundamentos da API DOM](/pdf/pt/net/basics-of-dom-api/).

Se criarmos um documento do zero, precisamos seguir certos passos:

1.
1. Adicione uma [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) ao objeto do documento. Assim, agora nosso documento terá uma página.
1. Adicione uma [Imagem](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) à Página.
1. Crie um [Fragmento de Texto](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento central.
1. Adicione o cabeçalho às [Parágrafos](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Crie um [Fragmento de Texto](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento central.
1. Adicione (descrição) aos Parágrafos da página.
1. Crie uma tabela, adicione propriedades à tabela.
1. Adicione (tabela) aos [Parágrafos](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Salve o documento "Complex.pdf".

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // Inicializar o objeto do documento
            Document document = new Document();
            // Adicionar página
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // Adicionar imagem
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Adicionar cabeçalho
            var header = new TextFragment("Novas rotas de ferry no Outono de 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Adicionar descrição
            var descriptionText = "Os visitantes devem comprar bilhetes online e os bilhetes são limitados a 5.000 por dia. O serviço de ferry está operando com metade da capacidade e em um horário reduzido. Espere filas.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Adicionar tabela
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("Partida da Cidade");
            headerRow.Cells.Add("Partida da Ilha");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

