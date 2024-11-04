---

title: Création d'un PDF complexe à l'aide de Aspose.PDF  
linktitle: Création d'un PDF complexe  
type: docs  
weight: 30  
url: /androidjava/complex-pdf-example/  
description: Aspose.PDF pour Android via Java vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

L'exemple [Hello, World](/pdf/java/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant Java et Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec Java et Aspose.PDF pour Java. Comme exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers.  
Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe), et un tableau. Pour construire un tel document, nous utiliserons une approche basée sur le DOM. Vous pouvez en lire plus dans la section [Notions de base de l'API DOM](/pdf/java/basics-of-dom-api/).

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Dans cette étape, nous allons créer un document PDF vide avec des métadonnées mais sans pages.
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) à l'objet document. Ainsi, notre document aura maintenant une page.
1. Pour ajouter une image, nous créons un FileInputStream, indiquons le chemin vers le fichier dont nous avons besoin. Ensuite, nous ajoutons l'image au rectangle avec les coordonnées données.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter l'en-tête aux [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) de la page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.

1. Ajouter (description) au paragraphe de la page. Nous avons utilisé les polices "Helvetica" et "Times Roman" dans notre exemple, mais gardez à l'esprit qu'il n'y a que trois polices système sous Android :

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Créer un tableau, ajouter des propriétés au tableau.
1. Ajouter (table) au [Paragraphes](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) de la page.
1. Enregistrer un document "Complex.pdf".

À la fin, une fenêtre contextuelle s'affiche avec le message "Le document PDF a été généré !".

![Exemple Complexe de Aspose.PDF pour Android via Java](complex_example.png)

```java
package com.aspose.pdf.examplecomplex;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.Toast;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Cell;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.Page;
import com.aspose.pdf.Position;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.Row;
import com.aspose.pdf.Table;
import com.aspose.pdf.TextFragment;

import java.io.File;
import java.io.FileInputStream;
import java.time.Duration;
import java.time.LocalTime;

public class MainActivity extends AppCompatActivity {

    Button generate_button;
    File myExternalFile;
    String filepath;
    String filename;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        generate_button = (Button) findViewById(R.id.button);
        generate_button.setOnClickListener(v->RunComplexExample());

        if(!isExternalStorageAvailable()||isExternalStorageReadOnly()){
            generate_button.setEnabled(false);
        }
        else{
            filepath = "MyFileStorage";
            filename = "SampleFile.pdf";
            myExternalFile=new File(getExternalFilesDir(filepath), filename);
        }

    }

    private void RunComplexExample() {
        // Initialiser l'objet document
        Document document = new Document();

        // Ajouter une page
        Page page = document.getPages().add();

        // Ajouter une image
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Ajouter l'image à la page
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // Ajouter un en-tête
        TextFragment header = new TextFragment("Nouvelles routes de ferry à l'automne 2020");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Ajouter une description
        String descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont " +
                "limités à 5 000 par jour. Le service de ferry fonctionne à demi-capacité et" +
                " sur un horaire réduit. Attendez-vous à des files d'attente.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Ajouter un tableau
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Départs Ville");
        headerRow.getCells().add("Départs Île");


        for (Cell headerRowCell : (Iterable<? extends Cell>) headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState()
                    .setForegroundColor(Color.getWhiteSmoke().toRgb());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/sample.pdf");

        Toast toast = Toast.makeText(MainActivity.this,
                "Le document PDF a été généré !", Toast.LENGTH_LONG);
        toast.show();
    }

    private static boolean isExternalStorageReadOnly(){
        String extStorageState= Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable(){
        String extStorageState=Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }

}
```


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/title"
        android:textSize="24sp"
        android:visibility="visible"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/generate_btn" />

</LinearLayout>
```