---

title: Créer un document

type: docs

weight: 10

url: /fr/java/create-pdf-document/

description: Aspose.PDF pour Java vous aide à créer un document PDF et un fichier PDF consultable en quelques étapes faciles.

lastmod: "2021-06-05"

---

Dans cet article, nous allons montrer comment utiliser l'API Aspose.PDF pour Java pour générer et lire facilement des fichiers PDF dans des applications Java.

L'API Aspose.PDF pour Java permet aux développeurs d'applications Java d'intégrer une fonctionnalité de traitement de documents PDF dans leurs applications. Elle peut être utilisée pour créer et lire des fichiers PDF sans avoir besoin d'installer d'autres logiciels sur la machine sous-jacente. Aspose.PDF pour Java peut être utilisé dans une variété de types d'applications Java telles que les applications Desktop, JSP et JSF.

## Comment créer un fichier PDF avec Java

Pour créer un fichier PDF avec Java, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) à la collection Pages de l'objet Document
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) à la collection [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de la page
1. Enregistrez le document PDF résultant

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        //Ajouter une page
        Page page = document.getPages().add();
         
        // Ajouter du texte à la nouvelle page
        page.getParagraphs().add(new TextFragment("Bonjour le monde!"));
         
        // Enregistrer le PDF mis à jour
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


Dans ce cas, nous créons un document PDF d'une page avec un format de page A4, orientation portrait. Notre page contiendra un "Hello, World" dans la partie supérieure gauche de la page.

De plus, Aspose.PDF pour Java offre la possibilité de créer un PDF consultable. Apprenons le prochain extrait de code :

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // Créer callBack - logique pour reconnaître le texte pour les images pdf. Utilisez un OCR externe prenant en charge la norme HOCR(http://en.wikipedia.org/wiki/HOCR).
        // Nous avons utilisé l'OCR gratuit google tesseract(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // lecture de out.html dans une chaîne
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // suppression des fichiers temporaires
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // Fin callBack
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```