---
title: Exemplo Java Hello World
linktitle: Exemplo Hello World
type: docs
weight: 20
url: /pt/androidjava/hello-world-example/
description: Esta página mostra como usar programação simples para criar um documento PDF contendo texto - Hello World usando Aspose.PDF para Android.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Exemplo Hello World

Um exemplo "Hello World" é tradicionalmente usado para apresentar recursos de uma linguagem de programação ou software com um caso de uso simples.

Aspose.PDF for Android via Java API capacita desenvolvedores de aplicações Java a criar, ler, editar e manipular arquivos PDF em suas aplicações. Ele permite ler e converter vários tipos de arquivos diferentes para e a partir do formato de arquivo PDF. Este artigo Hello World mostra como criar um arquivo PDF em Java usando Aspose.PDF for Android via Java  API.
Depois [instalando Aspose.PDF para Android via Java](/pdf/pt/androidjava/installation/) no seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1. Instanciar um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) objeto
1. Adicionar um [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) para objeto de documento
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) objeto
1. Adicionar TextFragment a [Parágrafo](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) coleção da página
1. Salvar o documento PDF resultante

O trecho de código a seguir mostra as etapas básicas do funcionamento da API Aspose.PDF para Android.

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
                // Initialize document object
                Document document = new Document();

                //Add page
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // Add text to new page
                page.getParagraphs().add(new TextFragment(myData));

                // Save updated PDF
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
                // Initialize document object
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Document contain "+document.getPages().size()+" page(s).";
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

