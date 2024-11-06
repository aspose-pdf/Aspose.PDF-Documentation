---
title: Travailler avec un Portfolio dans des documents PDF
linktitle: Portfolio
type: docs
weight: 40
url: fr/java/portfolio/
description: Comment créer un Portfolio PDF avec Java. Vous devriez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

D'abord, essayons de comprendre **Quel est le format de fichier d'un Portfolio PDF ?**

Par exemple, prenez un fichier Portfolio PDF qui contient des présentations Word, Excel, PowerPoint, etc., comme pièces jointes. Ici, chacun des fichiers joints conserve son format de document d'origine, mais est intégré ou assemblé dans un seul fichier Portfolio PDF. Vous pouvez bien sûr ouvrir, lire ou éditer chacun des fichiers individuels du Portfolio PDF comme s'il était sur un lecteur ou un dossier. De plus, tout comme un document PDF normal, vous pouvez également appliquer un filigrane, définir des mots de passe et des autorisations de sécurité telles que la capacité de visualiser, imprimer ou apporter des modifications aux pièces jointes du Portfolio PDF.

Nous pouvons placer ou assembler des fichiers natifs, dans leur type ou format d'origine en tant que pièces jointes, dans un fichier Portfolio PDF.

## Comment créer un portfolio PDF

Aspose.PDF permet de créer des documents de portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Ajoutez un fichier dans un objet Document.Collection après l'avoir obtenu avec la classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Lorsque les fichiers ont été ajoutés, utilisez la méthode Save de la classe Document pour enregistrer le document de portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.

Le code ci-dessous donne le portfolio suivant.

### Un portfolio PDF créé avec Aspose.PDF

![Un portfolio PDF créé avec Aspose.PDF pour Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Instancier l'objet Document
        Document pdfDocument = new Document();

        // Instancier l'objet Collection de document
        pdfDocument.setCollection(new Collection());

        // Obtenir les fichiers à ajouter au portfolio
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // Fournir une description des fichiers
        excel.setDescription ("Fichier Excel");
        word.setDescription ("Fichier Word");
        image.setDescription ("Fichier Image");

        // Ajouter des fichiers à la collection de documents
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // Enregistrer le document de portfolio
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## Extraire des fichiers d'un portfolio PDF

Les portefeuilles PDF vous permettent de rassembler du contenu provenant de diverses sources (par exemple, des fichiers PDF, Word, Excel, JPEG) dans un conteneur unifié. Les fichiers originaux conservent leurs identités individuelles mais sont assemblés dans un fichier de portefeuille PDF. Les utilisateurs peuvent ouvrir, lire, éditer et formater chaque fichier composant indépendamment des autres fichiers composants.

Aspose.PDF permet la création de documents de portefeuille PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Il offre également la possibilité d'extraire des fichiers du portefeuille PDF.

Le code suivant vous montre les étapes pour extraire des fichiers d'un portefeuille PDF.

![Extraire des fichiers d'un portefeuille PDF](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // Ouvrir un document
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // Obtenir la collection de fichiers intégrés
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // Itérer à travers chaque fichier du portefeuille
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## Supprimer des fichiers du portfolio PDF

Afin de supprimer/enlever des fichiers du portfolio PDF, essayez d'utiliser les lignes de code suivantes.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // Charger le portfolio PDF source
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```