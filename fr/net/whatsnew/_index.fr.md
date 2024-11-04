---
title: Quoi de neuf
linktitle: Quoi de neuf
type: docs
weight: 10
url: /net/whatsnew/
description: Cette page présente les nouvelles fonctionnalités les plus populaires d'Aspose.PDF pour .NET qui ont été introduites dans les dernières versions.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Quoi de neuf dans Aspose.PDF 24.8

Conversion de documents PDF en format PDF/A-4

Depuis la version 24.8, il est possible de convertir des documents PDF en PDF/A-4. La partie 4 de la norme, basée sur le PDF 2.0, a été publiée fin 2020.

Le code suivant montre comment convertir un document en format PDF/A-4, en supposant que le document d'entrée est un PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // Seuls les documents PDF-2.x peuvent être convertis en PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
Le second extrait de code montre comment convertir un document en format PDF/A-4 lorsque le document d'entrée est une version antérieure.

```cs
    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.Convert(Stream.Null, PdfFormat.v_2_0, ConvertErrorAction.Delete);

        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```

Depuis le 24.8, nous avons introduit une méthode pour aplatir le contenu transparent dans les documents PDF :

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## Quoi de neuf dans Aspose.PDF 24.7

Comparaison de documents PDF avec Aspose.PDF pour .NET

Depuis 24.7, il est possible de comparer le contenu des documents PDF avec des marques d'annotation et une sortie côte à côte :

Le premier extrait de code montre comment comparer les premières pages de deux documents PDF.
Le premier extrait de code montre comment comparer les premières pages de deux documents PDF.

```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Le deuxième extrait de code étend la comparaison au contenu entier de deux documents PDF.

```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```
## Quoi de neuf dans Aspose.PDF 24.4

Cette version prend en charge l'application d'un masque de découpe aux images :

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

Depuis la version 24.4, vous pouvez sélectionner la source du papier par la taille de la page PDF dans le dialogue d'impression en utilisant l'API

À partir d'Aspose.PDF 24.4, cette préférence peut être activée ou désactivée en utilisant la propriété Document.PickTrayByPdfSize ou la facade PdfContentEditor :

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Bonjour le monde !"));

        // Définir le drapeau pour choisir un bac à papier en utilisant la taille de la page PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs
    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // Définir le drapeau pour choisir un bac à papier en fonction de la taille de la page PDF
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

À partir de cette version, le plugin Aspose.PDF Signature pour .NET a été ajouté :

- Exemple avec la création d'un nouveau champ et des options :

```cs

    // créer Signature
    var plugin = new Signature();
    // créer l'objet SignOptions pour définir les instructions
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // ajouter le chemin du fichier d'entrée
    opt.AddInput(new FileDataSource(inputPath));
    // définir le chemin du fichier de sortie
    opt.AddOutput(new FileDataSource(outputPath));
    // définir des options supplémentaires
    opt.Reason = "ma Raison";
    opt.Contact = "mon Contact";
    opt.Location = "mon Emplacement";
    // effectuer le processus
    plugin.Process(opt);
```

- Exemple avec un champ vide existant

```cs

    // créer Signature
    var plugin = new Signature();
    // créer l'objet SignOptions pour définir les instructions
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // ajouter le chemin du fichier d'entrée avec un champ de signature vide
    opt.AddInput(new FileDataSource(inputPath));
    // définir le chemin du fichier de sortie
    opt.AddOutput(new FileDataSource(outputPath));
    // définir le nom du champ de signature existant
    opt.Name = "Signature1";
    // effectuer le processus
    plugin.Process(opt);
```
## Quoi de neuf dans Aspose.PDF 24.3

À partir de cette version, le plugin PDF/A Converter pour .NET a été ajouté :

```cs

    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // Ajouter le fichier source
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // remplacer par votre chemin de fichier réel

    // Ajouter le chemin pour enregistrer le fichier converti
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // Créer une instance du plugin
    var plugin = new PdfAConverter();

    // Exécuter la conversion
    plugin.Process(options);
```

- Implémenter une recherche à travers une liste de phrases dans un TextFragmentAbsorber :

```cs

    var regexes = new Regex[]
    {
    new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:?", RegexOptions.IgnoreCase),
    new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
    new Regex("Vested in:", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };
    var document = new Document(input);
    var absorber = new TextFragmentAbsorber(
    regexes,
    new TextSearchOptions(true)
    );
    document.Pages.Accept(absorber);
    // Obtenir le résultat
    var result = absorber.RegexResults
```
Depuis la version 24.3, il est possible d'ajouter un champ de signature vide sur chaque page du fichier PDF/A

```cs
    static void Main(string[] args)
    {
        try
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense("Aspose.Total.lic");

            string source = "source.pdf";
            string fieldName = "signature_1234";
            string dest = "source_fieldNotInAllPages.pdf";
            addFieldSingle_NewCode(source, dest, fieldName, 1);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
        Console.ReadLine(); 
    }

    private static void addFieldSingle_NewCode(string source, string dest, string fieldName, int page)
    {
        File.Copy(source, dest, true);
        using (var fs = new FileStream(dest, FileMode.Open))
        {
            // Le nouveau code suggéré, utilisant l'objet SignatureField (ce code fonctionne bien)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // Ajouter l'apparence par défaut pour le champ de signature
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // Comment maintenant rendre newAddedField visible dans toutes les pages ?
            Aspose.Pdf.Annotations.Annotation addedField = null;
            foreach (Aspose.Pdf.Annotations.Annotation a in doc.Pages[1].Annotations)
            {
            if (a.FullName == fieldName)
                {
                    addedField = a;
                    break;
                }
            }
            if (addedField != null)
            {
                for (int p = 1; p <= doc.Pages.Count; p++)
                {
                    if (p == page) continue;
                    doc.Pages[p].Annotations.Add(addedField);
                }
            }

            doc.Save();
        }
        System.Diagnostics.Process.Start(dest);
    }
```
## Quoi de neuf dans Aspose.PDF 24.2

Depuis la version 24.2, il est possible d'obtenir les données vectorielles à partir d'un fichier PDF

GraphicsAbsorber a été implémenté pour obtenir les données vectorielles des documents :

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Quoi de neuf dans Aspose.PDF 24.1

Depuis la version 24.1, il est possible d'importer des annotations au format FDF dans un PDF :

```cs
    var fdfPath = Params.InputPath + "50745.fdf";
    var templatePath = Params.InputPath + "Empty.pdf";
    var outputPath = Params.OutputPath + "50745_form.pdf";

    using (var form = new Aspose.Pdf.Facades.Form(templatePath))
    {
        using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }

        form.Save(outputPath);
    }
```

Support également pour l'accès au Dictionnaire de Pages ou au Catalogue de Documents.
Prend également en charge l'accès au Dictionnaire de Page ou au Catalogue de Documents.

Voici des exemples de code pour DictionaryEditor :

- Ajouter de nouvelles valeurs

```cs
    // exemple de noms de clés
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    var outputPath = "page_dictionary_editor.pdf";
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new CosPdfName("données de nom"));
        dictionaryEditor.Add(KEY_STRING, new CosPdfString("données de chaîne"));
        dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

        doc.Save(outputPath);
    }
```

- Ajouter et définir des valeurs au dictionnaire

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Ancien nom"));
        // ou 
        dictionaryEditor[KEY_NAME] = new CosPdfName("Nouveau nom");
    }
```
- Obtenir la valeur à partir du dictionnaire

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // ou
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- Supprimer la valeur du dictionnaire

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Nouveautés dans Aspose.PDF 23.12

Le formulaire peut être trouvé et le texte remplacé en utilisant le code suivant :

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var absorber = new TextFragmentAbsorber();
            absorber.Visit(form);

            foreach (var fragment in absorber.TextFragments)
            {
                fragment.Text = "";
            }
        }
    }

    document.Save(output);
```

Ou, le formulaire peut être complètement supprimé :

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    for (int i = 1; i <= forms.Count; i++)
    {
        if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
        {
            forms.Delete(forms[i].Name);
        }
    }

    document.Save(output);
```

Une autre variante pour supprimer le formulaire:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var name = forms.GetFormName(form);
            forms.Delete(name);
        }
    }

    document.Save(output);
``` 

- Tous les formulaires peuvent être supprimés en utilisant le code suivant :

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- Implémenter la conversion de PDF en Markdown :

```cs
    string markdownOutputFilePath = "output.md"
    string inputPdfPath = "input.pdf"
    utilisant (Document doc = new Document(inputPdfPath))
    {
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    doc.Save(markdownOutputFilePath, saveOptions);
    }
```

- Implémenter la conversion de OFD en PDF :

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

Depuis cette version, ajout du plugin Merger :

```cs
    // Chemin vers le fichier PDF fusionné en sortie.
    var outputPath = "TestMerge.pdf";

    // Créer une nouvelle instance de Merger.
    var merger = new Merger();

    // Créer MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // Traiter la fusion des PDF.
    merger.Process(opt);
```

Aussi, depuis cette version, ajout du plugin ChatGPT :
Aussi, depuis cette version, ajout du plugin ChatGPT :

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Ajoutez le chemin du fichier de sortie.
    options.ApiKey = "Votre clé API."; // Vous devez fournir la clé pour accéder à l'API.
    options.MaxTokens = 1000; // Le nombre maximum de jetons à générer dans la complétion de chat.

    // Ajoutez les messages de la requête.
    options.Messages.Add(new Message
    {
        Content = "Vous êtes un assistant utile.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "Quel est le diamètre de la plus grande pizza jamais réalisée ?",
        Role = Role.User
    });

    // Traitez la requête.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // L'objet de complétion de chat de l'API ChatGPT.
    }
```

## Quoi de neuf dans Aspose.PDF 23.11
## Nouveautés dans Aspose.PDF 23.11

À partir de cette version, il est possible de supprimer le texte caché d'un fichier PDF :

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // Cette option peut être utilisée pour empêcher les autres fragments de texte de se déplacer après le remplacement du texte caché.
        textAbsorber.TextReplaceOptions = new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        document.Save(outputFile);
```

Depuis la version 23.11, le support pour l'interruption de thread est disponible :

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        // ceci est un long texte, utilisé Lorem Ipsum en 8350 caractères pour provoquer une suspension
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // Le délai doit être inférieur au temps nécessaire pour enregistrer le document complet (sans interruption).
            Thread.Sleep(500);

            // Interrompre le processus
            monitor.Interrupt();

            // Attendre l'interruption...
            thread.Join();
        }
        private class RowSpanWorker
        {
            private readonly string outputPath;
            private readonly InterruptMonitor monitor;

            public RowSpanWorker(string outputPath, InterruptMonitor monitor)
            {
                this.outputPath = outputPath;
                this.monitor = monitor;
            }
            public void Work()
            {
                string text = InterruptMonitorTests.LongText;
                using (var doc = new Document())
                {
                    InterruptMonitor.ThreadLocalInstance = this.monitor;
                    var page = doc.Pages.Add();

                    var table = new Aspose.Pdf.Table
                    {
                        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
                    };

                    var row0 = table.Rows.Add();

                    // ajouter une cellule qui s'étend sur deux rangées et contient un texte très long
                    var cell00 = row0.Cells.Add(text);
                    cell00.RowSpan = 2;
                    cell00.IsWordWrapped = true;
                    row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
                    row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

                    var row1 = table.Rows.Add();
                    row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
                    row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

                    page.Paragraphs.Add(table);

                    try
                    {
                        doc.Save(this.outputPath);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
            }
        }
    }
```
## Quoi de neuf dans Aspose.PDF 23.10

La mise à jour actuelle présente trois versions de la suppression de tags des PDF tagués.

- Supprimer certains éléments de nœud d'un documentElement (élément racine de l'arbre) :

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // élément supprimé
        document.Save(outputPath);
    }

    // Vous pouvez également supprimer le structElement lui-même
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- Supprimer tous les tags des éléments marqués du document, mais conserver les éléments de structure :

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var root = structure.Children[0];
    var queue = new Queue<Element>();
    queue.Enqueue(root);
    while(queue.TryDequeue(out var element))
    {
        foreach (var child in element.Children)
        {
            queue.Enqueue(child);
        }

        if (element is TextElement || element is FigureElement)
        {
            element.Remove();
        }
    }
```
- Supprimer toutes les balises :

```cs
    var document = new Document("un pdf taggé");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

Depuis le 23.10, une nouvelle fonctionnalité a été mise en œuvre pour mesurer la hauteur des caractères. Utilisez le code suivant pour mesurer la hauteur d'un caractère.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

Notez que la mesure est basée sur la police intégrée dans le document. Si des informations pour une dimension sont manquantes, cette méthode retourne 0.

De plus, cette version fournit la fonctionnalité de signer un PDF en utilisant un HASH signé :

```cs
    public void PDFNET_54566()
    {
        var inputPdf = "54566.pdf";
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        var outputPdf = "54566_out.pdf";
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(inputPdf);
            var pkcs7 = new PKCS7(inputP12, inputPfxPassword);
            pkcs7.CustomSignHash = CustomSignHash;
            sign.Sign(1, "raison", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
            sign.Save(outputPdf);
        }
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(outputPdf);
            Assert.IsTrue(sign.VerifySignature("Signature1"));
        }
    }

    private byte[] CustomSignHash(byte[] signableHash)
    {
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
```
Une nouvelle fonctionnalité est l'échelonnage de la page des paramètres du dialogue d'impression :

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Nouveautés dans Aspose.PDF 23.9

Depuis la version 23.9, prise en charge pour supprimer une annotation enfant d'un champ remplissable.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Nouveautés dans Aspose.PDF 23.8

Depuis la version 23.8, prise en charge pour ajouter la détection des mises à jour incrémentielles.

La fonction de détection des mises à jour incrémentielles dans un document PDF a été ajoutée. Cette fonction retourne 'true' si un document a été sauvegardé avec des mises à jour incrémentielles ; sinon, elle retourne 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

De plus, 23.8 prend en charge les façons de travailler avec des champs de cases à cocher imbriqués.
La version 23.8 prend en charge les méthodes de travail avec des champs de cases à cocher imbriqués.

- Créer un champ de case à cocher à valeurs multiples :

```cs

    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Définir la première valeur d'option du groupe de cases à cocher
    checkbox.ExportValue = "option 1";

    // Ajouter une nouvelle option juste en dessous des existantes
    checkbox.AddOption("option 2");

    // Ajouter une nouvelle option à l'emplacement spécifié
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Sélectionner la case à cocher ajoutée
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
    }
```

- Obtenir et définir la valeur d'une case à cocher à valeurs multiples :

```cs

    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Les valeurs autorisées peuvent être récupérées de la collection AllowedStates
    // Définir la valeur de la case à cocher en utilisant la propriété Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // la valeur précédemment définie, par exemple "option 1"

    // La valeur doit être un élément de AllowedStates
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // Décocher les cases soit en définissant Value à "Off", soit en mettant Checked à false
    checkbox.Value = "Off";
    // ou, alternativement :
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## Quoi de neuf dans Aspose.PDF 23.7

À partir d'Aspose.PDF 23.7, prise en charge de l'ajout de l'extraction de formes :

```cs

    public void PDFNET_46298()
    {
        var input1 = "46298_1.pdf";
        var input2 = "46298_2.pdf";

        var source = new Document(input1);
        var dest = new Document(input2);

        var graphicAbsorber = new GraphicsAbsorber();
        graphicAbsorber.Visit(source.Pages[1]);
        var area = new Rectangle(90, 250, 300, 400);
        dest.Pages[1].AddGraphics(graphicAbsorber.Elements, area);
    }
```

Prend également en charge la capacité de détecter un débordement lors de l'ajout de texte :

```cs

    var doc = new Document();
    var paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    var rectangle = new Rectangle(100, 600, 500, 700, false);
    var paragraph = new TextParagraph();
    var fragment = new TextFragment(paragraphContent);
    paragraph.VerticalAlignment = VerticalAlignment.Top;
    paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
    paragraph.Rectangle = rectangle;
    var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.TextState.FontSize -= 0.5f;
        isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    }
    paragraph.AppendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.Pages.Add());
    builder.AppendParagraph(paragraph);
    doc.Save(output);
```
## Quoi de neuf dans Aspose.PDF 23.6

Depuis Aspose.PDF 23.6, prise en charge pour ajouter les prochains plugins :

- Aspose PdfConverter Html en PDF
- Aspose PdfOrganizer Redimensionner API
- Aspose PdfOrganizer Compresser API

Mettre à jour l'Aspose.PdfForm
- ajouter la fonctionnalité 'Exporter les "Valeurs" des champs dans le document vers un fichier CSV'
- ajouter la capacité de définir des propriétés pour des champs séparés

Également prendre en charge la capacité de définir le titre de la page HTML, Epub :

```cs

    var document = new Document(Params.InputPath + "53357.pdf");

    var htmlSaveOptions = new HtmlSaveOptions
    {
        ExplicitListOfSavedPages = new[] { 1 },
        SplitIntoPages = false,
        FixedLayout = true,
        CompressSvgGraphicsIfAny = false,
        SaveTransparentTexts = true,
        SaveShadowedTextsAsTransparentTexts = true,
        FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
        RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
        PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
        Title = "Titre pour la page"   // <-- ceci a été ajouté
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```

## Quoi de neuf dans Aspose.PDF 23.5

Depuis la version 23.5, il est possible d'ajouter l'option de taille de police pour RedactionAnnotation. Utilisez le prochain extrait de code pour résoudre cette tâche :

```cs

    Document doc = new Document(dataDir + "test_factuur.pdf");

    // Créer une instance de RedactionAnnotation pour une région spécifique de la page
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // Texte à imprimer sur l'annotation de rédaction
    annot.OverlayText = "(Inconnu)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // Répéter le texte de superposition sur l'annotation de rédaction
    annot.Repeat = false;
    // Nouvelle propriété ici !
    annot.FontSize = 20;
    // Ajouter l'annotation à la collection d'annotations de la première page
    doc.Pages[1].Annotations.Add(annot);
    // Applatis l'annotation et rédige le contenu de la page (c.-à-d. supprime le texte et l'image
    // Sous l'annotation rédigée)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Quoi de neuf dans Aspose.PDF 23.4

Aspose.PDF a annoncé la sortie du SDK .NET 7.

## Quoi de neuf dans Aspose.PDF 23.3.1

À partir d'Aspose.PDF 23.3, prise en charge pour ajouter les plugins suivants :

- Aspose.PdfForm
- Aspose.PdfConverter PDF en HTML
- Aspose.PdfConverter PDF en XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator pour Images

## Quoi de neuf dans Aspose.PDF 23.3

La version 23.3 a introduit la prise en charge pour ajouter une résolution à une image. Deux méthodes peuvent être utilisées pour résoudre ce problème :

```cs
    var table = new Table
            {
                ColumnWidths = "600"
            };

            for(var j = 0; j < 2; j ++)
            {
                var row = table.Rows.Add();
                var cell = row.Cells.Add();
                cell.Paragraphs.Add(new Image()
                {
                    IsApplyResolution = true,
                    File = imageFile
                });
            }

            page.Paragraphs.Add(table);
```

Et la deuxième approche :

```cs
    page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
            page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
```
L'image sera placée avec une résolution échelonnée ou vous pouvez définir les propriétés FixedWidth ou FixedHeight en combinaison avec IsApplyResolution

## Quoi de neuf dans Aspose.PDF 23.1.1

À partir d'Aspose.PDF 23.1.1, prise en charge pour ajouter les plugins suivants :

- Plugin Aspose.PdfOrganizer
- Plugin Aspose.PdfExtractor

## Quoi de neuf dans Aspose.PDF 23.1

Depuis la version 23.1, prise en charge pour créer l'annotation PrinterMark.

Les marques d'imprimeur sont des symboles graphiques ou du texte ajouté à une page pour aider le personnel de production à identifier les composants d'un travail à plusieurs plaques et à maintenir une sortie constante pendant la production. Les exemples couramment utilisés dans l'industrie de l'impression incluent :

- Cibles d'enregistrement pour aligner les plaques
- Rampes grises et barres de couleur pour mesurer les couleurs et les densités d'encre
- Marques de coupe indiquant où le support de sortie doit être rogné

Nous montrerons l'exemple de l'option avec des barres de couleur pour mesurer les couleurs et les densités d'encre.
Nous allons montrer l'exemple de l'option avec des barres de couleur pour mesurer les couleurs et les densités d'encre.

```cs
var outFile = myDir + "ColorBarTest.pdf");

using (var doc = new Document())
{
    Page page = doc.Pages.Add();
    page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);
    AddAnnotations(page);
    doc.Save(outFile);
}

void AddAnnotations(Page page)
{
    var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
    var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
    var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

    var colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    var colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    var colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.ColorOfCMYK = ColorsOfCMYK.Magenta;
    var colorBarYellow = new ColorBarAnnotation(page, new Aspose.Pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.Annotations.Add(colorBarBlack);
    page.Annotations.Add(colorBarCyan);
    page.Annotations.Add(colorBaMagenta);
    page.Annotations.Add(colorBarYellow);
}
```
## Prise en charge de l'extraction des images vectorielles
Essayez d'utiliser le code suivant pour détecter et extraire les graphiques vectoriels :

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Quoi de neuf dans Aspose.PDF 22.12

À partir de cette version, prise en charge de la conversion de PDF en Image DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## Quoi de neuf dans Aspose.PDF 22.09

Depuis 22.09, prise en charge de l'ajout de propriété pour modifier l'ordre des rubriques de sujet (E=, CN=, O=, OU=, ) dans la signature.

```cs
    using (var fileSign = new PdfFileSignature())
    {
        fileSign.BindPdf(inputPdf);
        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new PKCS7Detached(inputPfx, "123456789");
        signature.CustomAppearance = new SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.CN, SubjectNameElements.O }
            //ou
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## Quoi de neuf dans Aspose.PDF 22.6

Depuis 22.5 support pour extraire le texte en SubScript et SuperScript à partir de PDF.

Si le document PDF contient du texte en SubScript et SuperScript comme H2O, alors l'extraction du texte du PDF doit également extraire leurs informations de formatage (dans le texte extrait en clair).
Si le PDF contient du texte en italique, il doit également être inclus dans le contenu extrait.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## Quoi de neuf dans Aspose.PDF 22.4

Cette version inclut des informations pour Aspose.PDF pour .NET :

- PDF en ODS : Reconnaître le texte en indice et en exposant ;

**exemple**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF en XMLSpreadSheet2003 : Reconnaître le texte en indice et en exposant ;

- PDF en Excel : Reconnaître le texte en indice et en exposant ;
- PDF en Excel : Reconnaître le texte en indice et en exposant;

- Supprimer les signatures UR lors de l'enregistrement du document;

- Supprimer le drapeau Suspects dans MarkInfo lors de l'enregistrement du document;

- Supprimer les informations lors de l'enregistrement du document

## Quoi de neuf dans Aspose.PDF 22.3

Cette version inclut les mises à jour suivantes :

- Support pour AFRelationship;

- Validation de l'en-tête PDF;

- Supprimer le sous-filtre adbe.x509.rsa_sha1 lors de l'enregistrement du document;

- Formater le champ en nombre et format de date;

- Interdire l'utilisation du chiffrement RC4 dans FDF 2.0.

## Quoi de neuf dans Aspose.PDF 22.2

À partir de la version 22.2, il est possible de signer un document en utilisant PdfFileSignature avec LTV, et avec la possibilité de changer le hachage de SHA1 à SHA256.

```csharp
Exemple d'utilisation :
var inputPdf = "51168.pdf";
var inputPfx = "51168.pfx";
var inputPfxPassword = "111111";
var outputPdf = "51168.pdf";

using (var doc = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(doc))
    {
        var pkcs = new PKCS7(inputPfx, inputPfxPassword)
        {
            UseLtv = true,
            TimestampSettings = new TimestampSettings("http://freetsa.org/tsr", string.Empty, DigestHashAlgorithm.Sha256)
        };
        signature.Sign(1, false, new System.Drawing.Rectangle(300, 100, 1, 1), pkcs);
        signature.Save(outputPdf);
    }
}
```
## Quoi de neuf dans Aspose.PDF 22.1

Aspose.PDF pour .NET prend désormais en charge le chargement de documents à partir de l'un des formats de documents les plus populaires, le format Portable Document Format (PDF) version 2.0.

## Quoi de neuf dans Aspose.PDF 21.11

### Autoriser les caractères non latins dans le mot de passe

```csharp
Aspose.Pdf.Facades.PdfFileSecurity fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity();
fileSecurity.AllowExceptions = true;
    try
{
 fileSecurity.BindPdf(exportDoc);
 bool res = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
 Console.WriteLine(res);
 fileSecurity.Save(output("encrypted.pdf"));
}
    catch(Exception e)
{
    Console.WriteLn("Exception: " + e.Message);
}
```

## Quoi de neuf dans Aspose.PDF 21.10

### Comment détecter un texte caché ?

Veuillez utiliser TextState.Invisible pour obtenir des informations sur l'invisibilité du texte hors du paramètre de mode de rendu.

Nous avons utilisé le code suivant pour les tests :

```csharp
Document pdf = new Document(dataDir + "TestPage.pdf");
Console.WriteLine(pdf.FileName);
var page = pdf.Pages[1];
var textFragmentAbsorber = new TextFragmentAbsorber();
page.Accept(textFragmentAbsorber);
var textFragmentCollection = textFragmentAbsorber.TextFragments;
for (int i = 1; i <= textFragmentCollection.Count; i++)
{
    TextFragment fragment = textFragmentCollection[i];
    Console.WriteLine("Fragment {0} à {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Texte : {0}", fragment.Text);
    Console.WriteLine("Mode de rendu : {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibilité : {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```
### Comment obtenir des informations sur le nombre de calques dans un document PDF ?

```csharp
Veuillez utiliser le code suivant :
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Quoi de neuf dans Aspose.PDF 21.9

Personnaliser la couleur de fond pour l'apparence de la signature et la couleur de la police des étiquettes dans la zone de signature avec Aspose.PDF pour .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//définir les couleurs
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## Quoi de neuf dans Aspose.PDF 21.8

### Comment changer la couleur du texte dans la Signature Numérique ?

Dans la version 21.8 la propriété ForegroundColor permet de changer la couleur du texte dans la Signature Numérique.

```csharp
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //créer un rectangle pour l'emplacement de la signature
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//définir la couleur du texte
        ForegroundColor = Color.Green
    };
    // signer le fichier PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //enregistrer le fichier PDF de sortie
    pdfSign.Save(outFile);
}
```

## Quoi de neuf dans Aspose.PDF 21.7

### Création de PDF basée sur XML et XLS avec paramètres

Pour ajouter des paramètres XSL, nous devons créer notre propre [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) et le définir comme propriété dans [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). L'extrait suivant montre comment utiliser cette classe avec les fichiers exemples décrits ci-dessus.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Exemple d'utilisation de XsltArgumentList
         XsltArgumentList argsList = new XsltArgumentList();
        argsList.AddParam("isBoldName", "", "yes");
        //---------------------

        var pdfDocument = new Aspose.Pdf.Document(TransformXml(XmlContent, XsltContent, argsList), options);
        pdfDocument.Save(_dataDir + "data_xml.pdf");
    }

 public static MemoryStream TransformXml(string inputXml, string xsltString, XsltArgumentList argsList=null)
    {
            var transform = new XslCompiledTransform();
            using (var reader = XmlReader.Create(new StringReader(xsltString)))
            {
                transform.Load(reader);
            }
            var memoryStream = new MemoryStream();

            var results = new StreamWriter(memoryStream);
            using (var reader = XmlReader.Create(new StringReader(inputXml)))
            {
                transform.Transform(reader, argsList, results);
            }

            memoryStream.Position = 0;
            return memoryStream;
    }
```
## Quoi de neuf dans Aspose.PDF 21.6

Avec Aspose.PDF pour .NET, vous pouvez masquer des images en utilisant ImagePlacementAbsorber depuis le document :

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // Masquer l'image sur la première page
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Quoi de neuf dans Aspose.PDF 21.5

### Comment extraire le nom complet de la police à partir de sa description/ressource dans un PDF ?

Vous pouvez obtenir une police complète avec le préfixe avec la propriété BaseFont pour la classe Font.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"nom de la police : {font.FontName} nom BaseFont : {font.BaseFont}");
}
pdf.Dispose();
```

## Quoi de neuf dans Aspose.PDF 21.4

### Ajouter une API pour fusionner des images

Aspose.PDF 21.4 vous permet de combiner des images.
Aspose.PDF 21.4 vous permet de combiner des images.

```csharp
private static void MergeAsJpeg()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.jpg", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\49616_600.jpg", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream =
                 PdfConverter.MergeImages(inputImagesStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.jpg", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```
```csharp
private static void MergeAsTiff()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.tiff", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\600.tiff", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream = PdfConverter.MergeImagesAsTiff(inputImagesStreams))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.tiff", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```

## Quoi de neuf dans Aspose.PDF 21.3

### Exposition publique de propriété pour détecter la Protection des Informations Azure
### Exposition publique de propriété pour détecter Azure Information Protection

Avec le prochain extrait de code, vous devriez être capable d'accéder au contenu chiffré de vos fichiers PDF, protégés avec Azure Information Protection :

```csharp
 public void Azure_Information_Protection()
 {
     string inputFile = @"c:\pdf.pdf";
     Document document = new Document(inputFile);
     if (document.EmbeddedFiles[1].AFRelationship == AFRelationship.EncryptedPayload)
     {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
              // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
              // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
              // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
     }
}
```

## Quoi de neuf dans Aspose.PDF 21.1

### Ajout de la prise en charge de la récupération de la couleur d'arrière-plan de TextFragment

Dans cette version d'Aspose.PDF, la fonction est devenue disponible pour récupérer la couleur d'arrière-plan.
Dans cette version d'Aspose.PDF, la fonction est devenue disponible pour récupérer la couleur d'arrière-plan.

Veuillez considérer le code suivant :

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Boucler à travers les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texte : '{0}'", textFragment.Text);
    Console.WriteLine("Couleur d'arrière-plan : '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("Couleur de premier plan : '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Couleur d'arrière-plan du segment : '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### Après la conversion en HTML, la police est entièrement intégrée dans le résultat

Aussi, dans Aspose.PDF 21.1, après la conversion d'un PDF en HTML, il est devenu possible d'avoir des polices intégrées dans un document HTML de sortie. Cela est possible avec la nouvelle option booléenne de sauvegarde HtmlSaveParameter.SaveFullFont.

Voici l'extrait de code :

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
