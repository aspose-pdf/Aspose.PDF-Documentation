---
title: Ejemplo de Hola Mundo en Java
linktitle: Ejemplo de Hola Mundo
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: Esta página muestra cómo usar programación simple para crear un documento PDF que contiene texto: Hola Mundo utilizando Aspose.PDF para Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ejemplo de Hola Mundo

Un ejemplo de "Hola Mundo" se utiliza tradicionalmente para presentar las características de un lenguaje de programación o software con un caso de uso simple.

Aspose.PDF para Android a través de la API de Java permite a los desarrolladores de aplicaciones Java crear, leer, editar y manipular archivos PDF en sus aplicaciones. Le permite leer y convertir varios tipos diferentes de archivos hacia y desde el formato de archivo PDF. Este artículo de Hola Mundo muestra cómo crear un archivo PDF en Java utilizando Aspose.PDF para Android a través de la API de Java.
Después de [instalar Aspose.PDF para Android a través de Java](/pdf/androidjava/installation/) en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Añadir una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) al objeto documento
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Añadir TextFragment a la colección de [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la página
1. Guardar el documento PDF resultante

El siguiente fragmento de código muestra los pasos básicos del funcionamiento de Aspose.PDF para la API de Android.

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
                // Inicializar objeto documento
                Document document = new Document();

                //Añadir página
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "¡Hola, mundo!";
                }

                // Añadir texto a la nueva página
                page.getParagraphs().add(new TextFragment(myData));

                // Guardar PDF actualizado
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
                // Inicializar objeto documento
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "El documento contiene "+document.getPages().size()+" página(s).";
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