---
title: Exemplo Java Hello World
linktitle: Exemplo Hello World
type: docs
weight: 20
url: /pt/androidjava/hello-world-example/
description: Esta página mostra como usar programação simples para criar um documento PDF contendo o texto - Hello World usando Aspose.PDF para Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Exemplo Hello World

Um exemplo "Hello World" é tradicionalmente usado para introduzir características de uma linguagem de programação ou software com um caso de uso simples.

Aspose.PDF para Android via Java API capacita desenvolvedores de aplicativos Java a criar, ler, editar e manipular arquivos PDF em suas aplicações. Ele permite ler e converter vários tipos diferentes de arquivos para e a partir do formato de arquivo PDF. Este artigo Hello World mostra como criar um arquivo PDF em Java usando Aspose.PDF para Android via Java API.
Após [instalar Aspose.PDF para Android via Java](/pdf/pt/androidjava/installation/) em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Adicionar uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ao objeto documento
1. Criar um objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Adicionar TextFragment à coleção [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) da página
1. Salvar o documento PDF resultante

O seguinte trecho de código mostra as etapas básicas do funcionamento do Aspose.PDF para API Android.

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
                // Inicializar objeto de documento
                Document document = new Document();

                //Adicionar página
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // Adicionar texto à nova página
                page.getParagraphs().add(new TextFragment(myData));

                // Salvar PDF atualizado
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
                // Inicializar objeto de documento
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "O documento contém " + document.getPages().size() + " página(s).";
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