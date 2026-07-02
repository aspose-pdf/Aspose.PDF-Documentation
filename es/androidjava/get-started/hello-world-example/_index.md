---
title: Ejemplo Hello World Java
linktitle: Ejemplo Hello World
type: docs
weight: 20
url: /es/androidjava/hello-world-example/
description: Esta página muestra cómo usar programación simple para crear un documento PDF que contenga texto - Hello World usando Aspose.PDF para Android.
lastmod: "2026-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ejemplo Hello World

Un ejemplo \"Hello World\" se utiliza tradicionalmente para introducir las características de un lenguaje de programación o software con un caso de uso sencillo.

Aspose.PDF for Android via Java API permite a los desarrolladores de aplicaciones Java crear, leer, editar y manipular archivos PDF en sus aplicaciones. Le permite leer y convertir varios tipos de archivos diferentes a y desde el formato de archivo PDF. Este artículo Hello World muestra cómo crear un archivo PDF en Java usando Aspose.PDF for Android via Java API.
Después [instalando Aspose.PDF para Android mediante Java](/pdf/es/androidjava/installation/) en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El fragmento de código siguiente sigue estos pasos:

1. Instanciar un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) objeto
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) al objeto de documento
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) objeto
1. Agregar TextFragment a [Párrafo](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) colección de la página
1. Guardar el documento PDF resultante

El siguiente fragmento de código muestra los pasos básicos del funcionamiento de Aspose.PDF para Android API.

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

