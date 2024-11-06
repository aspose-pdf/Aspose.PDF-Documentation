---
title: Obtenir des informations sur le fichier PDF
type: docs
weight: 50
url: fr/net/get-pdf-file-information/
description: Cette section explique comment obtenir des informations sur le fichier PDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Pour obtenir des informations spécifiques sur un fichier PDF, vous devez créer un objet de la classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Après cela, vous pouvez obtenir les valeurs des propriétés individuelles telles que Sujet, Titre, Mots-clés et Créateur, etc.

L'extrait de code suivant vous montre comment obtenir des informations sur le fichier PDF.

```csharp
 public static void GetPdfInfo()
        {
            // Ouvrir le document
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // Obtenir des informations sur le PDF
            Console.WriteLine("Sujet: {0}", fileInfo.Subject);
            Console.WriteLine("Titre: {0}", fileInfo.Title);
            Console.WriteLine("Mots-clés: {0}", fileInfo.Keywords);
            Console.WriteLine("Créateur: {0}", fileInfo.Creator);
            Console.WriteLine("Date de création: {0}", fileInfo.CreationDate);
            Console.WriteLine("Date de modification: {0}", fileInfo.ModDate);
            // Vérifier si c'est un PDF valide et s'il est également chiffré
            Console.WriteLine("Est un PDF valide: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Est chiffré: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Largeur de la page:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Hauteur de la page:{0}", fileInfo.GetPageHeight(1));
        }
```

## Obtenir des informations méta

Afin d'obtenir des informations, nous utilisons la propriété [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). Avec 'Hashtable', nous obtenons toutes les valeurs possibles.

```csharp
public static void GetMetaInfo()
        {
            // Créer une instance de l'objet PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // Récupérer tous les attributs personnalisés existants
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // Récupérer un attribut personnalisé
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```