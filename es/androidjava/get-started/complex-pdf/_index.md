---
title: Creando un PDF complejo usando Aspose.PDF
linktitle: Creando un PDF complejo
type: docs
weight: 30
url: /es/androidjava/complex-pdf-example/
description: Aspose.PDF para Android a través de Java te permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El ejemplo de [Hola, Mundo](/pdf/es/java/hello-world-example/) mostró pasos simples para crear un documento PDF usando Java y Aspose.PDF. En este artículo, echaremos un vistazo a la creación de un documento más complejo con Java y Aspose.PDF para Java. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry de pasajeros. Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo) y una tabla. Para construir dicho documento, utilizaremos un enfoque basado en DOM. Puedes leer más en la sección [Fundamentos de la API DOM](/pdf/es/java/basics-of-dom-api/).

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Añadir una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) al objeto del documento. Así, ahora nuestro documento tendrá una página.
1. Para añadir una imagen, creamos FileInputStream, indicamos la ruta al archivo que necesitamos. Luego añadimos la imagen al rectángulo con las coordenadas dadas.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Añadir el encabezado a los [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) de la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.

1. Añadir (descripción) a los párrafos de la página. Usamos las fuentes "Helvetica" y "Times Roman" en nuestro ejemplo, pero ten en cuenta que solo hay tres fuentes del sistema en Android:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Crear una tabla, añadir propiedades a la tabla.
1. Añadir (tabla) a la página [Párrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Guardar un documento "Complex.pdf".

Al final, se muestra un mensaje emergente con el mensaje "¡Se ha generado el documento PDF!".

![Ejemplo Complejo de Aspose.PDF para Android a través de Java](complex_example.png)

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
        // Inicializar objeto de documento
        Document document = new Document();

        // Añadir página
        Page page = document.getPages().add();

        // Añadir imagen
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Añadir imagen a la página
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // Añadir encabezado
        TextFragment header = new TextFragment("Nuevas rutas de ferry en otoño 2020");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Añadir descripción
        String descriptionText = "Los visitantes deben comprar boletos en línea y los boletos están " +
                "limitados a 5,000 por día. El servicio de ferry está operando a media capacidad y" +
                " en un horario reducido. Espere filas.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Añadir tabla
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Sale de la ciudad");
        headerRow.getCells().add("Sale de la isla");


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
                "¡Se ha generado el documento PDF!", Toast.LENGTH_LONG);
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