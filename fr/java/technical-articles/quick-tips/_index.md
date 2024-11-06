---
title: Conseils Rapides
type: docs
weight: 50
url: fr/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page contient quelques conseils rapides liés à Aspose.PDF pour l'API Java

{{% /alert %}}

## Ajouter JavaScript au PDF

Le code suivant peut être utilisé pour définir/ajouter du JavaScript au fichier PDF.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //Ajout de JavaScript au niveau du Document
    //Instancier JavascriptAction avec l'instruction JavaScript désirée
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //Assigner l'objet JavascriptAction à l'action désirée du Document
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //Ajout de JavaScript au niveau de la Page
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**Quelques exemples supplémentaires**

```java

// après impression
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('Le fichier a été imprimé')"));

// après enregistrement
document.getActions().setAfterSaving(new JavascriptAction("app.alert('Le fichier a été enregistré')"));

```

## Libérer la mémoire utilisée

Si vous avez terminé le travail avec Aspose.PDF pour Java et que vous souhaitez libérer la mémoire des différentes instances statiques, pour maximiser la mémoire pour d'autres processus, vous devez exécuter la ligne de code suivante :

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## Charger un PDF depuis ByteArrayInputStream

Le code suivant montre les étapes pour charger un fichier PDF dans un ByteArray puis instancier un objet Document avec ByteArrayInputStream.

```java

 // fichier PDF source

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //aucun doute ici est 0

        //Écrit len octets du tableau d'octets spécifié en commençant à l'offset off dans ce flux de sortie de tableau d'octets.

        System.out.println("lu " + readNum + " octets,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// instancier l'objet Document avec ByteArrayInputStream tout en passant le tableau d'octets comme argument

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// obtenir le nombre de pages du fichier PDF

 System.out.println(doc.getPages().size());

```


## Enregistrer le PDF dans ByteArrayOutputStream

Le fragment de code suivant montre les étapes pour enregistrer le fichier PDF résultant dans ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```