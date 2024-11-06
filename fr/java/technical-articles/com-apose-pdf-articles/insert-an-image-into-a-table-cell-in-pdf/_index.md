---

title: Insérer une Image dans une Cellule de Tableau en PDF  
type: docs  
weight: 20  
url: fr/java/insert-an-image-into-a-table-cell-in-pdf/  
lastmod: "2022-01-27"  

---

{{% alert color="primary" %}}

Les tableaux sont des éléments importants pour afficher des données. Ils fournissent un format présentable pour la représentation des données. Les tableaux sont souvent utilisés pour afficher des informations numériques. L'API Aspose.PDF fournit une classe, Table, qui vous offre la possibilité de créer des tableaux dans un fichier PDF.

Plutôt que de créer un tableau simple, vous pouvez définir différentes options de formatage, par exemple le style de bordure du tableau, les informations sur les marges, l'alignement, la couleur de fond, la largeur des colonnes, les informations sur le titre, la valeur des lignes à répéter sur chaque page et bien plus encore.

{{% /alert %}}

## Approche Aspose.PDF

Selon notre DOM (Document Object Model) un document est composé de Pages.
 Une page contient un ou plusieurs paragraphes, et un paragraphe peut être une image, du texte, un champ de formulaire, un titre, une boîte flottante, un graphique, une pièce jointe ou un tableau. Un tableau, à son tour, comporte une collection de lignes et chaque ligne comporte une collection de cellules. Une cellule est une collection de paragraphes.

Ainsi, selon notre DOM, une cellule de tableau peut contenir n'importe lequel des éléments de paragraphe spécifiés ci-dessus, y compris des images.

## Comprendre la Largeur des Cellules

Il est essentiel de bien comprendre la largeur des cellules, surtout lorsqu'on affiche une image dans une cellule de tableau, afin que la largeur de l'image soit fixée à la largeur d'une cellule pour qu'elle s'affiche correctement. La largeur d'une image peut être définie en utilisant la méthode setFixedWidth() de la classe Image.

## Exemple de Code

```java

 String dataDir = "C:\\temp\\";

//Instancier un objet Document en appelant son constructeur vide

Document pdfDocument = new Document();

//Créer une page dans l'objet Document

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//Instancier un objet table

Table table = new Table();

//Ajouter le tableau dans la collection de paragraphes de la page souhaitée

page.getParagraphs().add(table);

//Définir la largeur des colonnes du tableau

table.setColumnWidths("100 100 120");



//Définir la bordure du tableau en utilisant un autre objet BorderInfo personnalisé

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//Créer un objet image dans la page

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//Définir le chemin du fichier image

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//Créer des lignes dans le tableau, puis des cellules dans les lignes

Row row1 = table.getRows().add();

row1.getCells().add("Texte d'exemple dans la cellule");

// Ajouter la cellule qui contient l'image

Cell cell2 = row1.getCells().add();

//Ajouter l'image à la cellule du tableau

cell2.getParagraphs().add(img1);



row1.getCells().add("Cellule précédente avec image");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//Enregistrer le document

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```