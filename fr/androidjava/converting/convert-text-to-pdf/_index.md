---
title: Convertir du texte en PDF
linktitle: Convertir du texte en PDF
type: docs
weight: 300
url: fr/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF pour Android via Java vous permet de convertir un fichier texte brut en PDF ou de convertir un fichier texte préformaté en PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF pour Android via Java** offre la possibilité de convertir des fichiers texte au format PDF. Dans cet article, nous démontrons à quel point il est facile et efficace de convertir un fichier texte en PDF en utilisant Aspose.PDF.

Lorsque vous devez convertir un fichier texte en PDF, commencez par lire le fichier texte source avec un lecteur.
 Nous avons utilisé StringBuilder pour lire le contenu du fichier texte. Instancier un objet Document et ajouter une nouvelle page dans la collection Pages. Créer un nouvel objet TextFragment et passer l'objet StringBuilder à son constructeur. Ajouter un nouveau paragraphe dans la collection Paragraphs en utilisant l'objet TextFragment et enregistrer le fichier PDF résultant en utilisant la méthode Save de la classe Document.

## Convertir un fichier texte brut en PDF

```java
public void convertTXTtoPDF_Simple () {
        // Initialiser l'objet document

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instancier un objet Document en appelant son constructeur vide
        document=new Document();

        // Ajouter une nouvelle page dans la collection Pages du Document
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Créer une instance de TextFragment et passer le texte de l'objet reader à son
        // constructeur en tant qu'argument
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer
        // l'objet TextFragment
        page.getParagraphs().add(text);

        // Enregistrer le fichier PDF résultant
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Convertir un fichier texte préformaté en PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Lire le fichier texte comme un tableau de chaînes
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier un objet Document en appelant son constructeur vide
        document=new Document();

        // Ajouter une nouvelle page à la collection Pages du Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Définir les marges gauche et droite pour une meilleure présentation
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // vérifier si la ligne contient le caractère "saut de page"
            // voir https://fr.wikipedia.org/wiki/Saut_de_page
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Créer une instance de TextFragment et
                // passer la ligne à son
                // constructeur comme argument
                TextFragment text=new TextFragment(line);

                // Ajouter un nouveau paragraphe de texte à la collection de paragraphes et passer l'objet TextFragment
                page.getParagraphs().add(text);
            }
        }
        // Enregistrer le fichier PDF résultant
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```