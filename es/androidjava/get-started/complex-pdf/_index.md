---
title: Crear un PDF complejo usando Aspose.PDF
linktitle: Crear un PDF complejo
type: docs
weight: 30
url: /es/androidjava/complex-pdf-example/
description: Aspose.PDF for Android via Java permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El [Hola, Mundo](/pdf/es/java/hello-world-example/) El ejemplo mostró pasos simples para crear un documento PDF usando Java y Aspose.PDF. En este artículo, analizaremos la creación de un documento más complejo con Java y Aspose.PDF for Java. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferris de pasajeros.
Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo) y una tabla. Para construir dicho documento, utilizaremos un enfoque basado en DOM. Puede leer más en la sección [Conceptos básicos de la API DOM](/pdf/es/java/basics-of-dom-api/).

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) objeto. En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) al objeto documento. Entonces, ahora nuestro documento tendrá una página.
1. Para añadir una Imagen, creamos FileInputStream, indicamos la ruta al archivo que necesitamos. Luego añadimos la imagen al rectángulo con las coordenadas dadas.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Agregar el encabezado a la página [Párrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Agregar (descripción) a la página Párrafos. Usamos las fuentes "Helvetica" y "Times Roman" en nuestro ejemplo, pero tenga en cuenta que solo hay tres fuentes a nivel de sistema en Android:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Crea una tabla, agrega propiedades de tabla.
1. Agregar (tabla) a la página [Párrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Guardar un documento "Complex.pdf".

Al final, se muestra una ventana emergente con el mensaje "PDF document has been generated!".

![Ejemplo complejo de Aspose.PDF para Android vía Java](complex_example.png)

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
        // Initialize document object
        Document document = new Document();

        // Add page
        Page page = document.getPages().add();

        // Add image
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Add image to the page
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // Add Header
        TextFragment header = new TextFragment("New ferry routes in Fall 2020");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Add description
        String descriptionText = "Visitors must buy tickets online and tickets are " +
                "limited to 5,000 per day. Ferry service is operating at half capacity and" +
                " on a reduced schedule. Expect lineups.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Add table
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Departs City");
        headerRow.getCells().add("Departs Island");


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
                "PDF document has been generated!", Toast.LENGTH_LONG);
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
