---
title: Travailler avec l'impression PDF - Facades
type: docs
weight: 10
url: /net/working-with-pdf-printing-facades/
description: Cette section explique comment imprimer des fichiers PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Impression d'un fichier PDF sur l'imprimante par défaut en utilisant les paramètres de l'imprimante et de la page

Tout d'abord, le document est converti en image puis imprimé sur l'imprimante. Nous créons une instance de la classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) qui vous permet d'imprimer un fichier PDF sur l'imprimante par défaut, en utilisant la méthode BindPdf pour lier le document à celle-ci, et d'effectuer certains réglages. Dans notre exemple, nous utilisons le format A4, orientation portrait. Dans les printerSettings, nous indiquons tout d'abord le nom de l'imprimante sur laquelle nous imprimons. Sinon, il imprimera sur l'imprimante par défaut. Ensuite, nous indiquons le nombre de copies dont nous avons besoin.

```csharp
 public static void PrintingPDFFile()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée
            viewer.PrintPageDialog = false;   // Ne pas afficher la boîte de dialogue du numéro de page lors de l'impression

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Définir le nom de l'imprimante
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Définir la PageSize (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir les PageMargins (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

Afin d'afficher une boîte de dialogue d'impression, essayez d'utiliser l'extrait de code suivant :

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Définir la taille de la page (si nécessaire)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Définir les marges de la page (si nécessaire)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Le code d'impression du document va ici
                // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

## Imprimer un PDF sur une Imprimante Virtuelle

Il existe des imprimantes qui impriment sur un fichier. Nous définissons le nom de l'imprimante virtuelle et, par analogie avec l'exemple précédent, nous effectuons les réglages.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec la taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec la rotation ajustée
            viewer.PrintPageDialog = false;   // Ne pas afficher la boîte de dialogue de numéro de page lors de l'impression

            viewer.PrintAsImage = false;

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Définir le nom de l'imprimante
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Ou définir l'imprimante PDF
            //ps.PrinterName = "Adobe PDF";

            // Définir la taille de la page (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir les marges de la page (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

## Masquer le Dialogue d'Impression

Aspose.PDF pour .NET vous permet de masquer le dialogue d'impression. Pour cela, utilisez la méthode [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

L'extrait de code suivant vous montre comment masquer le dialogue d'impression.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée

            viewer.PrintPageDialog = false;   // Ne pas produire le dialogue de numéro de page lors de l'impression

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Définir le nom de l'imprimante XPS/PDF
            ps.PrinterName = "OneNote pour Windows 10";

            // Définir la taille de la page (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir les marges de la page (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

## Impression d'un fichier PDF en couleur au format XPS en niveaux de gris

Un document PDF en couleur peut être imprimé sur une imprimante XPS en niveaux de gris, en utilisant [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Pour cela, vous devez utiliser la propriété PdfViewer.PrintAsGrayscale et la définir sur *true*. Le fragment de code suivant démontre l'implémentation de la propriété PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée


            viewer.PrintPageDialog = false;   // Ne pas produire la boîte de dialogue du numéro de page lors de l'impression
            viewer.PrintAsGrayscale = false;

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Définir le nom de l'imprimante XPS/PDF
            ps.PrinterName = "OneNote pour Windows 10";

            // Définir la taille de la page (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir les marges de la page (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

## Conversion de PDF en PostScript

La classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) offre la possibilité d'imprimer des documents PDF et, avec l'aide de cette classe, nous pouvons également convertir des fichiers PDF au format PostScript. Pour convertir un fichier PDF en PostScript, installez d'abord une imprimante PS et imprimez simplement sur un fichier avec l'aide de PdfViewer.

L'exemple de code suivant vous montre comment imprimer et convertir un PDF au format PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Définir les attributs d'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée
            viewer.PrintPageDialog = false;   // Ne pas produire la boîte de dialogue du numéro de page lors de l'impression

            viewer.PrintAsImage = false;

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Définir le nom de l'imprimante XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Définir le nom du fichier de sortie et l'attribut PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Définir la taille de la page (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir les marges de la page (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Fermer le fichier PDF après l'impression
            viewer.Close();
        }
```

## Vérification du statut du travail d'impression

Un fichier PDF peut être imprimé sur une imprimante physique ainsi que sur le Microsoft XPS Document Writer, sans afficher de boîte de dialogue d'impression, en utilisant la classe [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Lors de l'impression de fichiers PDF volumineux, le processus peut prendre beaucoup de temps, de sorte que l'utilisateur peut ne pas être certain si le processus d'impression est terminé ou si un problème est survenu. Pour déterminer le statut d'un travail d'impression, utilisez la propriété PrintStatus. L'extrait de code suivant vous montre comment imprimer le fichier PDF vers un fichier XPS et obtenir le statut d'impression.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Créer un objet PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Ouvrir le fichier PDF d'entrée
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Définir les attributs pour l'impression
            viewer.AutoResize = true;         // Imprimer le fichier avec une taille ajustée
            viewer.AutoRotate = true;         // Imprimer le fichier avec une rotation ajustée
            viewer.PrintPageDialog = false;   // Ne pas produire la boîte de dialogue de numéro de page lors de l'impression

            viewer.PrintAsImage = false;

            // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Définir le nom de l'imprimante XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Définir le nom de fichier de sortie et l'attribut PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Définir PageSize (si nécessaire)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Définir PageMargins (si nécessaire)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Vérifier le statut de l'impression
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // Aucune erreur n'a été trouvée. Le travail d'impression s'est terminé avec succès
                Console.WriteLine("Impression terminée sans aucun problème..");
            }

            // Fermer le fichier PDF après impression
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

## Impression des pages en mode Simplex et Duplex

Dans un travail d'impression particulier, les pages d'un document PDF peuvent être imprimées soit en mode Duplex, soit en mode Simplex, mais vous ne pouvez pas imprimer certaines pages en simplex et d'autres pages en duplex dans un même travail d'impression. Cependant, pour répondre à cette exigence, différents intervalles de pages et un objet PrintingJobSettings peuvent être utilisés. L'extrait de code suivant montre comment imprimer certaines pages d'un fichier PDF en mode Simplex et d'autres pages en mode Duplex.

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