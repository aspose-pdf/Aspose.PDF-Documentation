---
title: Concaténer des documents PDF
type: docs
weight: 10
url: /fr/java/concatenate-pdf-documents/
description: Cette section explique comment concaténer des documents PDF avec com.aspose.pdf.facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Concaténer des fichiers PDF en utilisant les chemins de fichiers (Facades)

La méthode concatenate de la classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) peut être utilisée pour concaténer deux fichiers PDF. La méthode concatenate vous permet de passer trois paramètres : le premier PDF d'entrée, le second PDF d'entrée et le PDF de sortie. Le PDF de sortie final contient les deux fichiers PDF d'entrée.

Le snippet de code suivant vous montre comment concaténer des fichiers PDF en utilisant les chemins de fichiers.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concaténer les fichiers
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


Dans certains cas, lorsque de nombreux contours sont présents, les utilisateurs peuvent les désactiver en définissant **CopyOutlines** sur false et améliorer ainsi les performances de la concaténation.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concaténer les fichiers
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Concaténer plusieurs fichiers PDF en utilisant des MemoryStreams

La méthode [Concatenate](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) prend en paramètres les fichiers PDF source et le fichier PDF de destination.
 Ces paramètres peuvent être soit des chemins vers les fichiers PDF sur le disque, soit des MemoryStreams. Maintenant, pour cet exemple, nous allons d'abord créer deux flux de fichiers pour lire les fichiers PDF depuis le disque. Ensuite, nous convertirons ces fichiers en tableaux d'octets. Ces tableaux d'octets des fichiers PDF seront convertis en MemoryStreams. Une fois que nous aurons extrait les MemoryStreams des fichiers PDF, nous pourrons les passer à la méthode de concaténation et les fusionner en un seul fichier de sortie.

Le code suivant vous montre comment concaténer plusieurs fichiers PDF en utilisant des MemoryStreams :

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Créer deux flux de fichiers pour lire les fichiers PDF
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Créer des tableaux d'octets pour conserver le contenu des fichiers PDF
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Lire le contenu des fichiers PDF dans des tableaux d'octets
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Maintenant, convertir d'abord les tableaux d'octets en MemoryStreams puis concaténer ces flux
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Créer une instance de la classe PdfFileEditor pour concaténer les flux
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Concaténer les deux MemoryStreams d'entrée et enregistrer dans le MemoryStream de sortie
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convertir le MemoryStream en tableau d'octets
                        byte[] data = pdfStream.ToArray();
                        // Créer un FileStream pour enregistrer le fichier PDF de sortie
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Écrire le contenu du tableau d'octets dans le flux de fichiers de sortie
                        output.Write(data, 0, data.Length);
                        // Fermer le fichier de sortie
                        output.Close();
                    }
                }
            }
            // Fermer les fichiers d'entrée
            fs1.Close();
            fs2.Close();
        }
```

## Concaténer un tableau de fichiers PDF en utilisant les chemins de fichiers (Facades)

Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge de la méthode de concaténation, qui vous permet de passer un tableau de chemins de fichiers PDF. Le résultat final est enregistré sous forme de fichier fusionné créé à partir de tous les fichiers du tableau.

Le snippet de code suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant des chemins de fichiers.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Tableau de fichiers
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Concaténer les fichiers
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Concaténer un tableau de fichiers PDF en utilisant des flux (Facades)

Concaténer un tableau de fichiers PDF n'est pas limité uniquement aux fichiers résidant sur le disque.
 Vous pouvez également concaténer un tableau de fichiers PDF à partir de flux. Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge appropriée de la méthode Concatenate. Tout d'abord, vous devez créer un tableau de flux d'entrée et un flux pour le PDF de sortie, puis appeler la méthode Concatenate. Le résultat sera enregistré dans le flux de sortie.

Le code suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant des flux.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Tableau de flux
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Flux de sortie
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Concaténer le fichier
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Concatenatez les formulaires PDF et gardez les noms des champs uniques

La classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) dans l'espace de noms [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) offre la capacité de concaténer les fichiers PDF.
 Maintenant, si les fichiers Pdf à concaténer ont des champs de formulaire avec des noms similaires, Aspose.PDF offre la fonctionnalité de garder les champs dans le fichier Pdf résultant comme uniques et vous pouvez également spécifier le suffixe pour rendre les noms de champ uniques. La méthode [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) de PdfFileEditor en tant que true rendra les noms de champ uniques lorsque les formulaires Pdf sont concaténés. De plus, la méthode [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) de PdfFileEditor peut être utilisée pour spécifier le format défini par l'utilisateur du suffixe qui est ajouté au nom de champ pour le rendre unique lorsque les formulaires sont concaténés. Cette chaîne doit contenir la sous-chaîne %NUM% qui sera remplacée par des nombres dans le fichier résultant.

Veuillez voir l'extrait de code simple suivant pour réaliser cette fonctionnalité.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Définir les chemins des fichiers d'entrée et de sortie

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Instancier l'objet PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // Pour garder un Id de champ unique pour tous les champs
                KeepFieldsUnique = true,
                // Format du suffixe qui est ajouté au nom de champ pour le rendre unique lorsque les formulaires sont concaténés.
                UniqueSuffix = "_%NUM%"
            };

            // Concaténer les fichiers en un fichier Pdf résultant
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Concatenate Insérer une page blanche

Une fois que les fichiers PDF ont été fusionnés, nous pouvons insérer une page blanche au début du document sur laquelle nous pouvons créer une table des matières. Pour accomplir cette exigence, nous pouvons charger le fichier fusionné dans l'objet Document et nous devons appeler la méthode Page.Insert(…) pour insérer une page blanche.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Concaténer les fichiers
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```