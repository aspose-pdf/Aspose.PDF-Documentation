---
title: Travailler avec les Opérateurs
linktitle: Travailler avec les Opérateurs
type: docs
weight: 170
url: fr/java/operators/
description: Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. Les classes d'opérateurs offrent de grandes fonctionnalités pour la manipulation de PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction aux Opérateurs PDF et Leur Utilisation

Un opérateur est un mot-clé PDF spécifiant une action à effectuer, telle que peindre une forme graphique sur la page. Un mot-clé opérateur se distingue d'un objet nommé par l'absence d'un caractère solidus initial (2Fh). Les opérateurs n'ont de sens qu'à l'intérieur du flux de contenu.

Un flux de contenu est un objet flux PDF dont les données consistent en des instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans la [spécification PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Détails de l'Implémentation

Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF.
 L'exemple sélectionné ajoute une image dans un fichier PDF pour illustrer le concept. Pour ajouter une image dans un fichier PDF, différents opérateurs sont nécessaires. Cet exemple utilise [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), et [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- L'opérateur [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) sauvegarde l'état graphique actuel du PDF.
- Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. L'exemple sélectionné ajoute une image dans un fichier PDF pour illustrer le concept. Pour ajouter une image dans un fichier PDF, différents opérateurs sont nécessaires. Cet exemple utilise [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), et [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

(l'opérateur de concaténation de matrice) est utilisé pour définir comment une image doit être placée sur la page PDF.
- L'opérateur [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) dessine l'image sur la page.
- L'opérateur [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrez le document PDF d'entrée.
1. Obtenez la page particulière sur laquelle l'image va être ajoutée.
1. Ajoutez l'image dans la collection de ressources de la page.
1. Utilisez les opérateurs pour placer l'image sur la page :
   - Tout d'abord, utilisez l'opérateur [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) pour enregistrer l'état graphique actuel.
   - Ensuite, utilisez l'opérateur [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) pour spécifier où l'image doit être placée.
   - Utilisez l'opérateur [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) pour dessiner l'image sur la page.
1. Enfin, utilisez l'opérateur [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) pour enregistrer l'état graphique mis à jour.

Le code suivant montre comment utiliser les opérateurs PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // Créer un nouveau document PDF
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Obtenez la page où l'image doit être ajoutée
        Page page = pdfDocument.getPages().get_Item(1);

        // Définir les coordonnées
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Charger l'image dans le flux
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Bloc catch généré automatiquement
            e.printStackTrace();
        }

        // Ajouter l'image à la collection d'images des ressources de la page
        page.getResources().getImages().add(imageStream);

        // Utilisation de l'opérateur GSave : cet opérateur enregistre l'état graphique actuel
        page.getContents().add(new GSave());
        // Créer des objets Rectangle et Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Utilisation de l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment
        // l'image doit être placée
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Utilisation de l'opérateur Do : cet opérateur dessine l'image
        page.getContents().add(new Do(ximage.getName()));
        // Utilisation de l'opérateur GRestore : cet opérateur restaure l'état graphique
        page.getContents().add(new GRestore());

        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## Dessiner XForm sur la Page en utilisant les Opérateurs

Ce sujet démontre comment utiliser les opérateurs GSave/GRestore, l'opérateur ConcatenateMatrix pour positionner un xForm et l'opérateur Do pour dessiner un xForm sur une page.

Le code ci-dessous enveloppe le contenu existant d'un fichier PDF avec la paire d'opérateurs GSave/GRestore. Cette approche aide à obtenir l'état graphique initial à la fin du contenu existant. Sans cette approche, des transformations indésirables pourraient rester à la fin de la chaîne d'opérateurs existante.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // L'exemple démontre
        // l'utilisation des opérateurs GSave/GRestore
        // l'utilisation de l'opérateur ConcatenateMatrix pour positionner xForm
        // l'utilisation de l'opérateur Do pour dessiner xForm sur la page

        // Envelopper le contenu existant avec une paire d'opérateurs GSave/GRestore
        // ceci est pour obtenir l'état graphique initial à la fin du contenu existant
        // sinon, il pourrait rester quelques transformations indésirables à la fin de
        // la chaîne d'opérateurs existante
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Ajouter un opérateur d'état graphique de sauvegarde pour effacer correctement l'état graphique après
        // de nouvelles commandes
        pageContents.add(new GSave());

        // Créer xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Définir la largeur et la hauteur de l'image
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Charger l'image dans le flux
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Bloc catch généré automatiquement
            e.printStackTrace();
        }

        // Ajouter l'image à la collection Images des ressources XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Utilisation de l'opérateur Do : cet opérateur dessine l'image
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Placer le formulaire aux coordonnées x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Dessiner le formulaire avec l'opérateur Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Placer le formulaire aux coordonnées x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Dessiner le formulaire avec l'opérateur Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // Restaurer l'état graphique avec GRestore après le GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## Supprimer des objets graphiques à l'aide des classes d'opérateurs

Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation des PDF. Lorsqu'un fichier PDF contient des graphiques qui ne peuvent pas être supprimés à l'aide de la méthode [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), les classes d'opérateurs peuvent être utilisées pour les supprimer à la place.

L'extrait de code suivant montre comment supprimer des graphiques. Veuillez noter que si le fichier PDF contient des étiquettes de texte pour les graphiques, elles peuvent persister dans le fichier PDF en utilisant cette approche. Par conséquent, recherchez les opérateurs graphiques pour une méthode alternative afin de supprimer de telles images.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // Opérateurs de peinture de chemin utilisés
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## Changer l'espace colorimétrique d'un document PDF

{{% alert color="primary" %}}

Aspose.PDF pour Java 9.0.0 prend en charge le changement de l'espace colorimétrique d'un document PDF. Il est possible de changer la couleur RGB en CMYK et vice versa.

{{% /alert %}}

Les méthodes suivantes ont été implémentées dans la classe [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) pour vous permettre de changer l'espace colorimétrique. Utilisez-les pour changer certaines couleurs RGB/CMYK spécifiques vers l'espace colorimétrique CMYK/RGB, en gardant le reste du document PDF tel quel.

{{% alert color="primary" %}}
**Changements de l'API publique**
Les méthodes suivantes sont implémentées :

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

Le code suivant montre comment changer l'espace colorimétrique en utilisant Aspose.PDF pour Java.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("Valeurs des opérateurs de couleur RGB dans le document pdf");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // Conversion de la couleur RGB en couleur CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("Commande non prise en charge");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// Test du résultat
System.out.println("Valeurs des opérateurs de couleur CMYK convertis dans le document pdf de résultat");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```