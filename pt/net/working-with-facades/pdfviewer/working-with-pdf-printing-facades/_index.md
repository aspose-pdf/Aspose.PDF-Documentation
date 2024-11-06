---
title: Trabalhando com Impressão de PDF - Facades
type: docs
weight: 10
url: pt/net/working-with-pdf-printing-facades/
description: Esta seção explica como imprimir arquivos PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Imprimindo Arquivo PDF na Impressora Padrão usando Configurações de Impressora e Página

Primeiramente, o documento é convertido em imagem e depois impresso na impressora.
Criamos uma instância da classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) que permite imprimir um arquivo PDF na impressora padrão, usando o método BindPdf para o documento, e fazer certas configurações. Em nosso exemplo, estamos usando o formato A4, orientação retrato. Nas printerSettings, primeiramente, indicamos o nome da impressora para a qual estamos imprimindo. Caso contrário, ele será impresso na impressora padrão. Em seguida, colocamos o número de cópias que precisamos.

```csharp
 public static void PrintingPDFFile()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada
            viewer.PrintPageDialog = false;   // Não produzir o diálogo de número de página ao imprimir

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Definir nome da impressora
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

Para exibir uma caixa de diálogo de impressão, tente usar o seguinte trecho de código:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada

            // Criar objetos para configurações de impressora e página e PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Definir PageSize (se necessário)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Definir PageMargins (se necessário)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Código de impressão do documento vai aqui
                // Imprimir documento usando configurações de impressora e página
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

## Imprimir PDF para Impressora Virtual

Existem impressoras que imprimem em um arquivo. Definimos o nome da impressora virtual e, por analogia com o exemplo anterior, fazemos as configurações.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada
            viewer.PrintPageDialog = false;   // Não produzir o diálogo de número de página ao imprimir

            viewer.PrintAsImage = false;

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Definir nome da impressora
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Ou definir a impressora PDF
            //ps.PrinterName = "Adobe PDF";

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

## Ocultando o Diálogo de Impressão

Aspose.PDF para .NET permite que você oculte o diálogo de impressão. Para isso, use o método [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

O trecho de código a seguir mostra como ocultar o diálogo de impressão.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada

            viewer.PrintPageDialog = false;   // Não produzir o diálogo de número de página ao imprimir

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Definir nome da impressora XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

## Imprimindo PDF Colorido para Arquivo XPS como Escala de Cinza

Um documento PDF colorido pode ser impresso em uma impressora XPS como escala de cinza, usando [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Para isso, você precisa usar a propriedade PdfViewer.PrintAsGrayscale e defini-la como *true*. O trecho de código a seguir demonstra a implementação da propriedade PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada

            viewer.PrintPageDialog = false;   // Não produzir o diálogo de número de página ao imprimir
            viewer.PrintAsGrayscale = false;

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Definir o nome da impressora XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

## Conversão de PDF para PostScript

A classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) fornece a capacidade de imprimir documentos PDF e, com a ajuda dessa classe, podemos também converter arquivos PDF para o formato PostScript. Para converter um arquivo PDF em PostScript, primeiro instale qualquer impressora PS e apenas imprima para arquivo com a ajuda do PdfViewer.

O trecho de código a seguir mostra como imprimir e converter um PDF para o formato PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada
            viewer.PrintPageDialog = false;   // Não produzir a caixa de diálogo de número de página ao imprimir

            viewer.PrintAsImage = false;

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Definir nome da impressora XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Definir nome do arquivo de saída e atributo PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }
```

## Verificando o Status da Tarefa de Impressão

Um arquivo PDF pode ser impresso em uma impressora física, bem como no Microsoft XPS Document Writer, sem exibir uma caixa de diálogo de impressão, usando a classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Ao imprimir arquivos PDF grandes, o processo pode demorar muito, então o usuário pode não ter certeza se o processo de impressão foi concluído ou encontrou um problema. Para determinar o status de uma tarefa de impressão, use a propriedade PrintStatus. O trecho de código a seguir mostra como imprimir o arquivo PDF para um arquivo XPS e obter o status da impressão.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Criar objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir arquivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Definir atributos para impressão
            viewer.AutoResize = true;         // Imprimir o arquivo com tamanho ajustado
            viewer.AutoRotate = true;         // Imprimir o arquivo com rotação ajustada
            viewer.PrintPageDialog = false;   // Não produzir a caixa de diálogo de número da página ao imprimir

            viewer.PrintAsImage = false;

            // Criar objetos para configurações de impressora e página e PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Definir nome da impressora XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Definir nome do arquivo de saída e atributo PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Definir PageSize (se necessário)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Definir PageMargins (se necessário)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configurações de impressora e página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Verificar o status da impressão
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // Nenhum erro foi encontrado. A tarefa de impressão foi concluída com sucesso
                Console.WriteLine("Impressão concluída sem nenhum problema..");
            }

            // Fechar o arquivo PDF após a impressão
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Imprimindo páginas nos modos Simplex e Duplex

Em um determinado trabalho de impressão, as páginas de um documento PDF podem ser impressas no modo Duplex ou no modo Simplex, mas você não pode imprimir algumas páginas como simplex e outras como duplex em um único trabalho de impressão. No entanto, para atender a esse requisito, diferentes intervalos de páginas e o objeto PrintingJobSettings podem ser usados. O trecho de código a seguir mostra como imprimir algumas páginas de um arquivo PDF no modo Simplex e algumas páginas no modo Duplex.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```