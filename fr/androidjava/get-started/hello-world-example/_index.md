---
title: Exemple Hello World Java
linktitle: Exemple Hello World
type: docs
weight: 20
url: /fr/androidjava/hello-world-example/
description: Cette page montre comment utiliser une programmation simple pour créer un document PDF contenant le texte - Hello World en utilisant Aspose.PDF pour Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Exemple Hello World

Un exemple "Hello World" est traditionnellement utilisé pour introduire les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF pour Android via Java API permet aux développeurs d'applications Java de créer, lire, éditer et manipuler des fichiers PDF dans leurs applications. Il vous permet de lire et de convertir plusieurs types de fichiers différents vers et depuis le format de fichier PDF. Cet article Hello World montre comment créer un fichier PDF en Java en utilisant Aspose.PDF pour Android via l'API Java.
Après avoir [installé Aspose.PDF pour Android via Java](/pdf/fr/androidjava/installation/) dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

L'extrait de code ci-dessous suit ces étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Ajouter TextFragment à la collection [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la page
1. Enregistrer le document PDF résultant

Le code suivant montre les étapes de base du fonctionnement de l'API Aspose.PDF pour Android.

```java
package com.aspose.pdf.examplesimple;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.TextFragment;

import java.io.File;


public class MainActivity extends Activity {
    EditText inputText;
    TextView response;
    Button saveButton,readButton;

    File myExternalFile;
    String myData = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputText = (EditText) findViewById(R.id.myInputText);
        response = (TextView) findViewById(R.id.response);


        saveButton =
                (Button) findViewById(R.id.saveExternalStorage);
        saveButton.setOnClickListener(v -> {
            try {
                // Initialiser l'objet document
                Document document = new Document();

                // Ajouter une page
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Bonjour, le monde!";
                }

                // Ajouter du texte à la nouvelle page
                page.getParagraphs().add(new TextFragment(myData));

                // Enregistrer le PDF mis à jour
                document.save(myExternalFile.getAbsolutePath());

            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText("");
            response.setText(R.string.save_message);
        });

        readButton = (Button) findViewById(R.id.getExternalStorage);
        readButton.setOnClickListener(v -> {
            try {
                // Initialiser l'objet document
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Le document contient "+document.getPages().size()+" page(s).";
            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText(myData);
            response.setText(R.string.read_message);
        });

        if (!isExternalStorageAvailable() || isExternalStorageReadOnly()) {
            saveButton.setEnabled(false);
        }
        else {
            String filename = "SampleFile.pdf";
            String filepath = "MyFileStorage";
            myExternalFile = new File(getExternalFilesDir(filepath), filename);
        }
    }
    private static boolean isExternalStorageReadOnly() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }
}
```